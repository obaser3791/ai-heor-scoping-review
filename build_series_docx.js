const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, PageBreak,
  Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType, ImageRun,
  Header, Footer, PageNumber, convertInchesToTwip, PageOrientation,
} = require("docx");

const ROOT = "/home/user/workspace";
const OUT = path.join(ROOT, "deliverables/series");
fs.mkdirSync(OUT, { recursive: true });

const SERIF = "Times New Roman";
const SANS = "Arial";
const NONE = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const NOBORDER = { top: NONE, bottom: NONE, left: NONE, right: NONE };
const REPO = "https://github.com/obaser/ai-heor-scoping-review";

function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\^[^\^]+\^)/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const tok = m[0];
    if (tok.startsWith("**")) out.push(new TextRun({ text: tok.slice(2, -2), bold: true, ...base }));
    else out.push(new TextRun({ text: tok.slice(1, -1), superScript: true, ...base }));
    last = re.lastIndex;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  if (out.length === 0) out.push(new TextRun({ text: "", ...base }));
  return out;
}

const h1 = (text) => new Paragraph({
  children: runs(text, { font: SERIF, size: 26, bold: true }),
  spacing: { before: 360, after: 180, line: 360 }, keepNext: true, outlineLevel: 0,
});
const h2 = (text) => new Paragraph({
  children: runs(text, { font: SERIF, size: 24, bold: true }),
  spacing: { before: 300, after: 140, line: 360 }, keepNext: true, outlineLevel: 1,
});
const body = (text) => new Paragraph({
  children: runs(text, { font: SERIF, size: 24 }), spacing: { line: 480, after: 0 },
});

function pngSize(buf) { return { w: buf.readUInt32BE(16), h: buf.readUInt32BE(20) }; }
function imgPara(rel) {
  const buf = fs.readFileSync(path.join(ROOT, rel));
  const dim = pngSize(buf);
  const s = Math.min(600 / dim.w, 700 / dim.h, 1);
  return new Paragraph({
    children: [new ImageRun({ type: "png", data: buf, transformation: { width: Math.round(dim.w * s), height: Math.round(dim.h * s) } })],
    alignment: AlignmentType.CENTER, spacing: { before: 200, after: 120 },
  });
}

// ------------------------------------------------------------------ manuscript
function manuscript(cfg) {
  const src = fs.readFileSync(path.join(ROOT, cfg.src), "utf8");
  const lines = src.split("\n");
  let i = 0; const fm = {};
  if (lines[0].trim() === "---") {
    i = 1;
    while (lines[i].trim() !== "---") {
      const mm = lines[i].match(/^(\w+):\s*"?(.*?)"?\s*$/);
      if (mm) fm[mm[1]] = mm[2];
      i++;
    }
    i++;
  }
  const ms = [];
  ms.push(new Paragraph({ children: runs(fm.title || "", { font: SERIF, size: 32, bold: true }), spacing: { after: 160, line: 360 } }));
  ms.push(new Paragraph({ children: runs(fm.subtitle || "", { font: SERIF, size: 26, italics: true }), spacing: { after: 320, line: 360 } }));
  ms.push(new Paragraph({ children: runs("Article type: " + (fm.type || "Review"), { font: SERIF, size: 22 }), spacing: { after: 320 } }));

  let inRefs = false, inFigs = false, refNo = 0;
  for (; i < lines.length; i++) {
    const line = lines[i].trimEnd();
    if (!line.trim()) continue;
    if (line.startsWith("## ")) {
      const t = line.slice(3).trim();
      inRefs = t === "References"; inFigs = t === "Figures";
      if (["Introduction", "References", "Figures", "Tables"].includes(t)) ms.push(new Paragraph({ children: [new PageBreak()] }));
      ms.push(h1(t));
      if (t === "Tables") ms.push(body(cfg.tablesNote));
      continue;
    }
    if (line.startsWith("### ")) { ms.push(h2(line.slice(4).trim())); continue; }
    if (inFigs) {
      const fm2 = line.match(/^\*\*(Figure \d)\./);
      if (fm2 && cfg.figs[fm2[1]]) ms.push(imgPara(cfg.figs[fm2[1]]));
      ms.push(new Paragraph({ children: runs(line, { font: SERIF, size: 22 }), spacing: { line: 300, after: 320 } }));
      continue;
    }
    if (inRefs) {
      const rm = line.match(/^(\d+)\.\s+(.*)$/);
      if (rm) {
        refNo++;
        ms.push(new Paragraph({
          children: runs(rm[1] + ". " + rm[2], { font: SERIF, size: 21 }),
          spacing: { line: 300, after: 120 },
          indent: { left: convertInchesToTwip(0.35), hanging: convertInchesToTwip(0.35) },
        }));
        continue;
      }
    }
    const tight = /^\*\*(BACKGROUND|METHODS|RESULTS|CONCLUSIONS)\*\*$/.test(line) || /^\^\d\^/.test(line) || /^[¹²]/.test(line);
    ms.push(new Paragraph({ children: runs(line, { font: SERIF, size: 24 }), spacing: { line: tight ? 300 : 480, after: tight ? 60 : 0 } }));
  }
  const doc = new Document({
    creator: "Onur Baser", title: fm.title,
    sections: [{
      properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
      headers: { default: new Header({ children: [new Paragraph({ children: [new TextRun({ text: cfg.head, font: SERIF, size: 18, color: "555555" })], alignment: AlignmentType.RIGHT })] }) },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], font: SERIF, size: 20 })] })] }) },
      children: ms,
    }],
  });
  return { doc, refNo, fm };
}

// ---------------------------------------------------------------- table docs
const spec = JSON.parse(fs.readFileSync(path.join(ROOT, "tables/tables_spec.json"), "utf8"));
const byId = {}; spec.forEach((t) => { byId[t.id] = t; });
const LAND_W = 15840, LAND_H = 12240, MARGIN = 720;
const PRINT = LAND_W - 2 * MARGIN;

function colWidths(headers, rows, fontSize) {
  const n = headers.length;
  const score = headers.map((h, c) => {
    let mx = String(h).length;
    for (const r of rows) mx = Math.max(mx, String(r[c] === undefined ? "" : r[c]).length);
    return Math.min(mx, 70);
  });
  const chDxa = Math.ceil((fontSize / 2) * 0.62 * 20);
  const longestWord = (v) => String(v).split(/\s+/).reduce((a, b) => Math.max(a, b.length), 1);
  const floors = headers.map((h, c) => {
    let L = longestWord(h);
    for (const r of rows) L = Math.max(L, longestWord(r[c] === undefined ? "" : r[c]));
    return Math.min(Math.max(L * chDxa + 200, 460), 3400);
  });
  const total = score.reduce((a, b) => a + b, 0);
  let w = score.map((s, c) => Math.max(Math.round(PRINT * s / total), floors[c]));
  let sum = w.reduce((a, b) => a + b, 0);
  if (sum > PRINT) {
    const excess = sum - PRINT;
    const slack = w.map((x, c) => x - floors[c]);
    const slackSum = slack.reduce((a, b) => a + b, 0);
    if (slackSum > 0) w = w.map((x, c) => x - Math.floor(excess * slack[c] / slackSum));
    else w = w.map((x) => Math.floor(x * PRINT / sum));
  }
  sum = w.reduce((a, b) => a + b, 0);
  const k = PRINT / sum;
  w = w.map((x) => Math.floor(x * k));
  w[n - 1] = PRINT - w.slice(0, n - 1).reduce((a, b) => a + b, 0);
  return w;
}

function cellPara(text, { bold = false, size = 16, align = AlignmentType.LEFT, indent = 0 } = {}) {
  return new Paragraph({
    children: runs(String(text), { font: SANS, size, bold }),
    spacing: { line: 220, before: 20, after: 20 }, alignment: align,
    indent: indent ? { left: indent } : undefined,
  });
}

function buildTable(t, fontSize) {
  const headers = t.headers, rows = t.rows;
  const w = colWidths(headers, rows, fontSize);
  const heavy = { style: BorderStyle.SINGLE, size: 10, color: "333333" };
  const isNum = (v) => /^[\d(][\d.,%() to\u2013-]*$/.test(String(v).trim());
  const rightAligned = headers.map((_, c) => {
    if (c === 0) return false;
    let filled = 0, num = 0;
    for (const r of rows) {
      const v = String(r[c] === undefined ? "" : r[c]).trim();
      if (!v) continue; filled++; if (isNum(v)) num++;
    }
    return filled > 0 && num / filled >= 0.7;
  });
  const headRow = new TableRow({
    tableHeader: true, cantSplit: true,
    children: headers.map((h, c) => new TableCell({
      width: { size: w[c], type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: "E8EDEE", color: "auto" },
      borders: { top: heavy, bottom: heavy, left: NONE, right: NONE },
      margins: { top: 60, bottom: 60, left: 80, right: 80 },
      children: [cellPara(h, { bold: true, size: fontSize, align: rightAligned[c] ? AlignmentType.RIGHT : AlignmentType.LEFT })],
    })),
  });
  const hasIndent = rows.some((r) => String(r[0] === undefined ? "" : r[0]).startsWith("  "));
  const bodyRows = rows.map((r, ri) => {
    const label = String(r[0] === undefined ? "" : r[0]);
    const indented = label.startsWith("  ");
    const isSection = hasIndent && !indented && label.trim() !== "";
    return new TableRow({
      cantSplit: rows.length <= 30,
      children: headers.map((_, c) => {
        const v = String(r[c] === undefined ? "" : r[c]).trim();
        return new TableCell({
          width: { size: w[c], type: WidthType.DXA },
          borders: { top: NONE, bottom: ri === rows.length - 1 ? heavy : { style: BorderStyle.SINGLE, size: 2, color: "DDDDDD" }, left: NONE, right: NONE },
          shading: isSection ? { type: ShadingType.CLEAR, fill: "F4F4F2", color: "auto" } : undefined,
          margins: { top: 50, bottom: 50, left: 80, right: 80 },
          children: [cellPara(c === 0 ? label.trim() : v, {
            bold: isSection, size: fontSize,
            align: rightAligned[c] ? AlignmentType.RIGHT : AlignmentType.LEFT,
            indent: c === 0 && indented ? 140 : 0,
          })],
        });
      }),
    });
  });
  return new Table({ width: { size: PRINT, type: WidthType.DXA }, columnWidths: w, layout: "fixed", borders: NOBORDER, rows: [headRow, ...bodyRows] });
}

function tableDoc(items, docTitle, head, intro) {
  const kids = [];
  kids.push(new Paragraph({ children: runs(docTitle, { font: SANS, size: 28, bold: true }), spacing: { after: 120 } }));
  kids.push(new Paragraph({ children: runs(head, { font: SANS, size: 20, italics: true }), spacing: { after: 80 } }));
  kids.push(new Paragraph({ children: runs("Onur Baser, Ph.D.", { font: SANS, size: 20 }), spacing: { after: 200 } }));
  if (intro) kids.push(new Paragraph({ children: runs(intro, { font: SANS, size: 20 }), spacing: { after: 200, line: 260 } }));
  items.forEach((t, idx) => {
    if (idx > 0) kids.push(new Paragraph({ children: [new PageBreak()] }));
    const wide = t.headers.length;
    const fontSize = wide >= 14 ? 12 : wide >= 9 ? 14 : 16;
    kids.push(new Paragraph({
      children: [new TextRun({ text: t.id + ". ", font: SANS, size: 22, bold: true }), ...runs(t.title, { font: SANS, size: 22, bold: true })],
      spacing: { before: 120, after: 140, line: 280 }, keepNext: true, outlineLevel: 0,
    }));
    kids.push(buildTable(t, fontSize));
    if (t.footnote) kids.push(new Paragraph({ children: runs(t.footnote, { font: SANS, size: 16 }), spacing: { before: 120, line: 240 } }));
  });
  return new Document({
    creator: "Onur Baser", title: docTitle,
    sections: [{
      properties: { page: { size: { width: LAND_H, height: LAND_W, orientation: PageOrientation.LANDSCAPE }, margin: { top: MARGIN, right: MARGIN, bottom: MARGIN, left: MARGIN } } },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], font: SANS, size: 18 })] })] }) },
      children: kids,
    }],
  });
}

// remap: list of [oldId, newId]
function remap(pairs, xrefs) {
  return pairs.map(([oldId, newId]) => {
    const t = JSON.parse(JSON.stringify(byId[oldId]));
    t.id = newId;
    if (t.footnote) {
      for (const [from, to] of xrefs) t.footnote = t.footnote.split(from).join(to);
    }
    return t;
  });
}

const HEAD1 = "Faster but Not Truer, Part 1: AI in Health Economics and Outcomes Research";
const HEAD2 = "Faster but Not Truer, Part 2: The Regulatory Record, the Economics, and TRACE-HEOR";

const P1 = {
  src: "series/part1.md", head: HEAD1,
  figs: {
    "Figure 1": "figures/figure1_prisma.png",
    "Figure 2": "figures/figure2_growth.png",
    "Figure 3": "figures/figure3_evidence_map.png",
    "Figure 4": "figures/figure4_validation.png",
  },
  tablesNote: "Table 1 and Table 2 are provided as a separate document, Tables 1 to 2, formatted in landscape orientation. Legends appear below.",
};
const P2 = {
  src: "series/part2.md", head: HEAD2,
  figs: { "Figure 1": "figures/part2_figure1_timeline.png" },
  tablesNote: "Table 1 through Table 3 are provided as a separate document, Tables 1 to 3, formatted in landscape orientation. Legends appear below.",
};

const p1 = manuscript(P1);
const p2 = manuscript(P2);

const p1Mains = remap([["Table 1", "Table 1"], ["Table 2", "Table 2"]], []);
const p2Mains = remap([["Table 3", "Table 1"], ["Table 4", "Table 2"], ["Table 5", "Table 3"]], []);

const p1Etabs = remap(
  Array.from({ length: 14 }, (_, k) => ["eTable " + (k + 1), "eTable " + (k + 1)]), []);
const p2Xrefs = [["eTable 15", "eTable 1"], ["eTable 16", "eTable 2"], ["eTable 17", "eTable 3"], ["eTable 18", "eTable 4"], ["eTable 19", "eTable 5"]];
const p2Etabs = remap([["eTable 15", "eTable 1"], ["eTable 16", "eTable 2"], ["eTable 17", "eTable 3"], ["eTable 18", "eTable 4"], ["eTable 19", "eTable 5"]], p2Xrefs);

const p1Tables = tableDoc(p1Mains, "Tables 1 to 2", HEAD1,
  "All counts derive from the replication package at " + REPO + ". Reliability statistics come from blinded independent classification of 300 randomly sampled included records.");
const p2Tables = tableDoc(p2Mains, "Tables 1 to 3", HEAD2,
  "All sources are cited in full in the reference list of Part 2. Provenance labels are Peer reviewed, Preprint, Conference abstract, Company communication, and Not available. The replication package is at " + REPO + ".");

const p1Supp = tableDoc(p1Etabs, "Supplementary Appendix, Part 1", HEAD1,
  "eTable 1 through eTable 14 support the Methods and Results of Part 1. Every value is reproducible from the public replication package at " + REPO + ".");
const p2Supp = tableDoc(p2Etabs, "Supplementary Appendix, Part 2", HEAD2,
  "eTable 1 through eTable 5 support the Results of Part 2. Provenance labels are Peer reviewed, Preprint, Conference abstract, Company communication, and Not available. The replication package is at " + REPO + ".");

(async () => {
  const jobs = [
    ["Faster-but-Not-Truer-Part-1-Manuscript.docx", p1.doc],
    ["Faster-but-Not-Truer-Part-1-Tables-1-to-2.docx", p1Tables],
    ["Faster-but-Not-Truer-Part-1-Supplementary-Appendix.docx", p1Supp],
    ["Faster-but-Not-Truer-Part-2-Manuscript.docx", p2.doc],
    ["Faster-but-Not-Truer-Part-2-Tables-1-to-3.docx", p2Tables],
    ["Faster-but-Not-Truer-Part-2-Supplementary-Appendix.docx", p2Supp],
  ];
  for (const [name, doc] of jobs) {
    const buf = await Packer.toBuffer(doc);
    fs.writeFileSync(path.join(OUT, name), buf);
    console.log("wrote", name, (buf.length / 1024).toFixed(0) + " KB");
  }
  console.log("refs part1:", p1.refNo, "part2:", p2.refNo);
})();
