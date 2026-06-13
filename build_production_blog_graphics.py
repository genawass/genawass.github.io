#!/usr/bin/env python3
"""Build graphics for the production-CV review and architecture essay.

Outputs:
  01_architecture.svg  Conceptual evolution from pipeline to generalist system
  02_readiness.html    Interactive readiness distribution by production theme
  03_pipeline_collapse.svg  Shared-model view of the emerging vision stack
  shortlisted-papers.md  Full six-per-theme paper appendix
  paper-01.svg ...     Featured-paper concept diagrams
  share.png            Architecture-essay social-preview image
  share-production.png Production-review social-preview image

Usage:
  python3 build_production_blog_graphics.py
  python3 build_production_blog_graphics.py --out /path/to/site/posts/cvpr2026-production
"""

import argparse
import html
import json
import os
from collections import Counter


ROOT = os.path.dirname(os.path.abspath(__file__))
ASSESSMENTS = os.path.join(ROOT, "themes", "production_assessments", "assessments.json")
DEFAULT_OUT = os.path.join(ROOT, "themes", "blog_publish", "posts", "cvpr2026-production")

BG = "#ffffff"
TEXT = "#20242b"
MUTED = "#6a7079"
RULE = "#e7e7e4"
BLUE = "#0b5fb0"
GREEN = "#2f855a"
AMBER = "#b7791f"
PURPLE = "#6b46c1"
SANS = '-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif'

PAPER_CONCEPTS = [
    (
        "Open-vocabulary detection",
        ["image regions", "language classes"],
        ["hierarchical calibration", "unbiased objectness"],
        ["known + unseen objects", "reliable proposals"],
    ),
    (
        "Open-vocabulary defects",
        ["factory images", "defect prompts"],
        ["multimodal defect model", "cross-domain dataset"],
        ["detect + segment", "describe defects"],
    ),
    (
        "Molmo2",
        ["images + video", "points + language"],
        ["open video-language model", "grounded temporal state"],
        ["caption + answer", "point + track"],
    ),
    (
        "DynUAV tracking benchmark",
        ["moving UAV video", "blur + occlusion"],
        ["break smooth-motion assumptions", "deployment-shaped stress test"],
        ["robust MOT evaluation", "identity under motion"],
    ),
    (
        "D4RT",
        ["video", "space-time queries"],
        ["one feed-forward transformer", "shared query interface"],
        ["depth + pose", "correspondence + motion"],
    ),
    (
        "SDGS",
        ["camera frames", "spatial differences"],
        ["sparse Gaussian scene model", "joint pose optimization"],
        ["localization", "3D reconstruction"],
    ),
    (
        "SaPaVe",
        ["language goal", "active camera view"],
        ["vision-language-action model", "geometry-aware control"],
        ["choose what to observe", "manipulate"],
    ),
    (
        "Mobile low-light denoising",
        ["raw UHD frames", "extreme low light"],
        ["efficient temporal raw model", "ISP-aware deployment"],
        ["clean video", "real-time mobile"],
    ),
    (
        "Unified 2D/3D correspondence",
        ["2D images", "3D point clouds"],
        ["one shared-weight transformer", "2D-2D · 2D-3D · 3D-3D"],
        ["matches across modalities", "registration + tracking"],
    ),
]


def svg_text(x, y, text, size=18, weight=400, color=TEXT, anchor="middle"):
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
        f'font-family="Arial, Helvetica, sans-serif" font-size="{size}" '
        f'font-weight="{weight}" fill="{color}">{html.escape(text)}</text>'
    )


def svg_box(x, y, width, height, label, fill, stroke, size=16):
    return "\n".join([
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="9" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>',
        svg_text(x + width / 2, y + height / 2 + 6, label, size=size, weight=600),
    ])


def svg_multiline(x, y, lines, size=18, weight=400, color=TEXT, anchor="middle",
                  line_height=25):
    spans = []
    for index, line in enumerate(lines):
        dy = 0 if index == 0 else line_height
        spans.append(
            f'<tspan x="{x}" dy="{dy}">{html.escape(line)}</tspan>'
        )
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
        f'font-family="Arial, Helvetica, sans-serif" font-size="{size}" '
        f'font-weight="{weight}" fill="{color}">{"".join(spans)}</text>'
    )


def build_architecture(path):
    width, height = 1200, 700
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'role="img" aria-labelledby="title desc">',
        '<title id="title">The production computer-vision stack is consolidating</title>',
        '<desc id="desc">Three architectures: classical rules, specialized learned pipeline, '
        'and Software 3.0 generalist models inside a deterministic shell.</desc>',
        f'<rect width="{width}" height="{height}" fill="{BG}"/>',
        svg_text(50, 54, "The production computer-vision stack is consolidating",
                 size=29, weight=700, anchor="start"),
        svg_text(50, 84, "Capability moves from code, to many learned modules, to a few general models.",
                 size=16, color=MUTED, anchor="start"),
    ]

    columns = [
        (40, "Software 1.0", "Rules and classical vision", BLUE),
        (420, "Software 2.0", "A learned model per task", AMBER),
        (800, "Software 3.0", "Generalists programmed by intent", PURPLE),
    ]
    for x, title, subtitle, color in columns:
        parts += [
            f'<rect x="{x}" y="120" width="350" height="510" rx="14" fill="#fafafa" '
            f'stroke="{RULE}" stroke-width="1.5"/>',
            svg_text(x + 24, 160, title, size=22, weight=700, color=color, anchor="start"),
            svg_text(x + 24, 188, subtitle, size=15, color=MUTED, anchor="start"),
        ]

    # Software 1.0
    for i, label in enumerate(["features", "geometry", "thresholds", "rules"]):
        parts.append(svg_box(92, 235 + i * 78, 246, 52, label, "#ffffff", BLUE))
        if i < 3:
            parts.append(svg_text(215, 305 + i * 78, "↓", size=24, color=MUTED))
    parts.append(svg_text(215, 575, "behavior written in code", size=15, color=MUTED))

    # Software 2.0
    labels = ["detector", "tracker", "pose model", "classifier", "rules + glue"]
    for i, label in enumerate(labels):
        parts.append(svg_box(472, 225 + i * 68, 246, 48, label, "#ffffff", AMBER))
        if i < len(labels) - 1:
            parts.append(svg_text(595, 287 + i * 68, "↓", size=20, color=MUTED))
    parts.append(svg_text(595, 595, "each model has its own data and failures",
                          size=14, color=MUTED))

    # Software 3.0
    parts += [
        svg_box(852, 235, 246, 72, "vision / video generalist", "#f3effb", PURPLE, 16),
        svg_text(975, 345, "+", size=28, color=MUTED),
        svg_box(852, 370, 246, 72, "language-action model", "#f3effb", PURPLE, 16),
        svg_text(975, 480, "inside", size=14, color=MUTED),
        f'<rect x="830" y="500" width="290" height="75" rx="12" fill="#ffffff" '
        f'stroke="{GREEN}" stroke-width="2" stroke-dasharray="7 5"/>',
        svg_text(975, 531, "deterministic shell", size=17, weight=700, color=GREEN),
        svg_text(975, 557, "tools · memory · validators · control", size=13, color=MUTED),
        svg_text(975, 608, "behavior specified by language, examples, and constraints",
                 size=14, color=MUTED),
        svg_text(405, 395, "→", size=35, color=RULE),
        svg_text(785, 395, "→", size=35, color=RULE),
        "</svg>",
    ]
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(parts))


def build_pipeline_collapse(path):
    width, height = 1200, 760
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'role="img" aria-labelledby="title desc">',
        '<title id="title">One shared visual model replaces task pipelines</title>',
        '<desc id="desc">Many sensor inputs flow into a shared correspondence and world '
        'model which exposes detection, tracking, segmentation, registration, localization, '
        'geometry, motion, and forecasting as outputs.</desc>',
        f'<rect width="{width}" height="{height}" fill="{BG}"/>',
        svg_text(50, 58, "The new unit of computer vision is a shared world model",
                 size=29, weight=700, anchor="start"),
        svg_text(50, 90, "Tasks become queries over persistent identity, geometry, semantics, and motion.",
                 size=16, color=MUTED, anchor="start"),
    ]

    inputs = ["RGB", "thermal", "depth", "event", "radar / IMU", "language"]
    outputs = [
        "detect", "segment", "track", "register",
        "localize", "reconstruct", "reason", "forecast",
    ]
    for index, label in enumerate(inputs):
        y = 150 + index * 82
        parts.append(svg_box(55, y, 190, 50, label, "#ffffff", BLUE, 15))
        parts.append(f'<line x1="245" y1="{y + 25}" x2="385" y2="355" '
                     f'stroke="{RULE}" stroke-width="2"/>')

    parts += [
        f'<rect x="385" y="210" width="430" height="300" rx="24" fill="#f3effb" '
        f'stroke="{PURPLE}" stroke-width="3"/>',
        svg_text(600, 265, "shared correspondence", size=24, weight=700, color=PURPLE),
        svg_text(600, 300, "+ persistent world model", size=24, weight=700, color=PURPLE),
        svg_box(455, 345, 290, 48, "identity · geometry · semantics", "#ffffff", PURPLE, 14),
        svg_box(455, 415, 290, 48, "motion · memory · uncertainty", "#ffffff", PURPLE, 14),
        svg_text(600, 555, "language · examples · queries · tools", size=16, color=MUTED),
    ]

    for index, label in enumerate(outputs):
        column = index % 2
        row = index // 2
        x = 870 + column * 150
        y = 175 + row * 110
        parts.append(f'<line x1="815" y1="355" x2="{x}" y2="{y + 25}" '
                     f'stroke="{RULE}" stroke-width="2"/>')
        parts.append(svg_box(x, y, 125, 50, label, "#ffffff", GREEN, 14))

    parts += [
        svg_text(150, 690, "different observations", size=16, weight=600, color=BLUE),
        svg_text(600, 690, "one learned state", size=16, weight=600, color=PURPLE),
        svg_text(1015, 690, "many capabilities", size=16, weight=600, color=GREEN),
        "</svg>",
    ]
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(parts))


def short_name(name):
    replacements = {
        "Detection, segmentation & visual recognition": "Detection & segmentation",
        "Video intelligence & persistent tracking": "Video intelligence",
        "3D perception, reconstruction & digital twins": "3D / digital twins",
        "Robotics, embodied AI & autonomous systems": "Robotics / embodied AI",
        "Human understanding, biometrics & interaction": "Human understanding",
        "Industrial inspection, quality & anomaly detection": "Industrial inspection",
        "Medical, biological & scientific imaging": "Medical / scientific",
        "Geospatial, aerial & remote-sensing analytics": "Geospatial / remote sensing",
        "Computational imaging & visual enhancement": "Computational imaging",
        "Visual search, multimodal understanding & agents": "Visual agents & search",
        "Generative visual media & content production": "Generative media",
        "Data engines, adaptation & continuous learning": "Data engines / adaptation",
        "Efficient, robust & trustworthy deployment": "Robust deployment",
    }
    return replacements.get(name, name)


def build_readiness(path, themes):
    import plotly.graph_objects as go

    names = [short_name(theme["name"]) for theme in themes]
    counts = {
        readiness: [Counter(p["readiness"] for p in theme["papers"])[readiness] for theme in themes]
        for readiness in ("now", "near", "research")
    }
    colors = {"now": GREEN, "near": BLUE, "research": "#b9bdc4"}
    labels = {"now": "Usable now", "near": "Near-term", "research": "Research-stage"}
    fig = go.Figure()
    for readiness in ("now", "near", "research"):
        fig.add_bar(
            name=labels[readiness],
            y=names,
            x=counts[readiness],
            orientation="h",
            marker_color=colors[readiness],
            text=counts[readiness],
            textposition="inside",
            hovertemplate=f"%{{y}}<br>{labels[readiness]}: %{{x}} of 6 papers<extra></extra>",
        )
    fig.update_layout(
        barmode="stack",
        paper_bgcolor=BG,
        plot_bgcolor=BG,
        font=dict(family=SANS, size=13, color=TEXT),
        margin=dict(l=20, r=25, t=65, b=55),
        legend=dict(orientation="h", yanchor="bottom", y=1.025, xanchor="left", x=0),
        xaxis=dict(
            title="Shortlisted papers per theme",
            range=[0, 6],
            dtick=1,
            gridcolor=RULE,
            zeroline=False,
        ),
        yaxis=dict(autorange="reversed", automargin=True),
        hoverlabel=dict(bgcolor="#ffffff", bordercolor=RULE, font=dict(family=SANS, size=13)),
    )
    fig.write_html(path, include_plotlyjs="cdn", full_html=True,
                   config={"responsive": True, "displayModeBar": False},
                   div_id="production-readiness")


def build_paper_concepts(out_dir):
    width, height = 1200, 500
    for index, (title, inputs, model, outputs) in enumerate(PAPER_CONCEPTS, 1):
        parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'role="img" aria-labelledby="title desc">',
            f'<title id="title">{html.escape(title)} concept diagram</title>',
            f'<desc id="desc">Inputs flow through the paper architecture to production capabilities.</desc>',
            f'<rect width="{width}" height="{height}" fill="{BG}"/>',
            f'<rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="18" '
            f'fill="#fafafa" stroke="{RULE}" stroke-width="2"/>',
            svg_text(48, 62, title, size=28, weight=700, anchor="start"),
            svg_text(48, 92, "What this paper collapses into one learned path",
                     size=15, color=MUTED, anchor="start"),
            svg_text(175, 150, "INPUTS", size=14, weight=700, color=BLUE),
            svg_text(600, 150, "ARCHITECTURAL MOVE", size=14, weight=700, color=PURPLE),
            svg_text(1025, 150, "CAPABILITIES", size=14, weight=700, color=GREEN),
            f'<rect x="55" y="185" width="240" height="185" rx="18" fill="#eef6fd" '
            f'stroke="{BLUE}" stroke-width="2"/>',
            f'<rect x="390" y="175" width="420" height="205" rx="24" fill="#f3effb" '
            f'stroke="{PURPLE}" stroke-width="3"/>',
            f'<rect x="905" y="185" width="240" height="185" rx="18" fill="#eff8f2" '
            f'stroke="{GREEN}" stroke-width="2"/>',
            svg_multiline(175, 255, inputs, size=21, weight=600, color=TEXT, line_height=42),
            svg_multiline(600, 250, model, size=22, weight=700, color=PURPLE, line_height=44),
            svg_multiline(1025, 255, outputs, size=21, weight=600, color=TEXT, line_height=42),
            f'<line x1="295" y1="278" x2="390" y2="278" stroke="{AMBER}" stroke-width="4"/>',
            f'<polygon points="390,278 370,266 370,290" fill="{AMBER}"/>',
            f'<line x1="810" y1="278" x2="905" y2="278" stroke="{AMBER}" stroke-width="4"/>',
            f'<polygon points="905,278 885,266 885,290" fill="{AMBER}"/>',
            svg_text(600, 435, "fewer handoffs · shared representation · broader interface",
                     size=16, color=MUTED),
            "</svg>",
        ]
        with open(os.path.join(out_dir, f"paper-{index:02d}.svg"), "w", encoding="utf-8") as handle:
            handle.write("\n".join(parts))


def load_why_it_matters():
    """Curated, abstract-grounded one-liners keyed by exact paper title.

    Falls back to the generated production_value template for any title not
    present, so the appendix still builds if a paper is swapped in.
    """
    path = os.path.join(ROOT, "why_it_matters.json")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def build_shortlisted_papers(path, themes):
    why = load_why_it_matters()
    missing = sorted({
        paper["title"] for theme in themes for paper in theme["papers"]
        if paper["title"] not in why
    })
    if missing:
        print(f"[why_it_matters] {len(missing)} titles fell back to template:")
        for title in missing:
            print(f"  - {title}")
    lines = [
        "# CVPR 2026 production computer-vision shortlist",
        "",
        "The full set behind the readiness chart in "
        "[What CVPR 2026 Says About Production Computer Vision]"
        "(https://genawass.github.io/posts/cvpr2026-production.html).",
        "",
        f"**{len(themes)} themes · {sum(len(theme['papers']) for theme in themes)} papers "
        "· six papers per theme.**",
        "",
        "Grades measure production usefulness, not academic quality. "
        "Readiness is `now`, `near`, or `research`.",
        "",
    ]
    for index, theme in enumerate(themes, 1):
        lines += [
            f"## {index}. {theme['name']}",
            "",
            f"**Production scope:** {theme['market']}",
            "",
        ]
        for paper in theme["papers"]:
            flag = " · must-read" if paper["must_read"] else ""
            lines += [
                f"{paper['rank']}. [{paper['title']}]({paper['link']})",
                f"   - **Grade:** {paper['grade']} · **Novelty:** {paper['novelty']} · "
                f"**Readiness:** {paper['readiness']}{flag}",
                f"   - **Why it matters:** {why.get(paper['title'], paper['production_value'])}",
            ]
        lines.append("")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


def build_share(path, *, label, title, subtitle, boxes):
    from PIL import Image, ImageDraw, ImageFont

    width, height = 1200, 630
    image = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(image)
    regular = "/System/Library/Fonts/SFNS.ttf"
    bold = "/System/Library/Fonts/SFNS.ttf"
    title_font = ImageFont.truetype(bold, 60)
    sub_font = ImageFont.truetype(regular, 28)
    small_font = ImageFont.truetype(regular, 22)
    label_font = ImageFont.truetype(bold, 24)
    arrow_font = ImageFont.truetype(regular, 46)

    draw.rectangle((0, 0, width, 18), fill=BLUE)
    draw.text((64, 52), label, font=small_font, fill=MUTED)
    draw.multiline_text(
        (64, 98),
        title,
        font=title_font,
        fill=TEXT,
        spacing=8,
    )
    draw.multiline_text(
        (64, 252),
        subtitle,
        font=sub_font,
        fill=MUTED,
        spacing=9,
    )
    for x0, y0, x1, y1, label, subtitle, color in boxes:
        draw.rounded_rectangle((x0, y0, x1, y1), radius=18, fill="#fafafa", outline=color, width=4)
        draw.text((x0 + 24, y0 + 34), label, font=label_font, fill=color)
        draw.text((x0 + 24, y0 + 84), subtitle, font=small_font, fill=TEXT)
    draw.text((404, 416), "→", font=arrow_font, fill=RULE)
    draw.text((770, 416), "→", font=arrow_font, fill=RULE)
    draw.text((64, 562), "genawass.github.io", font=small_font, fill=MUTED)
    image.save(path, optimize=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--assessments", default=ASSESSMENTS)
    parser.add_argument("--out", default=DEFAULT_OUT)
    args = parser.parse_args()

    with open(args.assessments, encoding="utf-8") as handle:
        themes = json.load(handle)
    os.makedirs(args.out, exist_ok=True)
    build_architecture(os.path.join(args.out, "01_architecture.svg"))
    build_readiness(os.path.join(args.out, "02_readiness.html"), themes)
    build_pipeline_collapse(os.path.join(args.out, "03_pipeline_collapse.svg"))
    build_shortlisted_papers(os.path.join(args.out, "shortlisted-papers.md"), themes)
    build_paper_concepts(args.out)
    build_share(
        os.path.join(args.out, "share.png"),
        label="COMPUTER VISION · ARCHITECTURE",
        title="The Pipeline Is Moving\nInside the Model",
        subtitle="Software 2.0 replaced vision algorithms. The next transition\n"
        "is replacing the interfaces between them.",
        boxes=[
            (64, 372, 404, 512, "CLASSICAL", "rules + geometry", BLUE),
            (430, 372, 770, 512, "SPECIALISTS", "model per task", AMBER),
            (796, 372, 1136, 512, "FUSED MODEL", "shared objective", PURPLE),
        ],
    )
    build_share(
        os.path.join(args.out, "share-production.png"),
        label="CVPR 2026 · PRODUCTION VISION",
        title="What CVPR 2026 Says About\nProduction Computer Vision",
        subtitle="A practical review of what can ship now, what is near,\n"
        "and where research still outruns deployment.",
        boxes=[
            (64, 372, 404, 512, "38 PAPERS", "usable now", BLUE),
            (430, 372, 770, 512, "18 PAPERS", "near-term", AMBER),
            (796, 372, 1136, 512, "28 PAPERS", "research-stage", PURPLE),
        ],
    )
    print(f"Wrote production blog graphics to {os.path.abspath(args.out)}")


if __name__ == "__main__":
    main()
