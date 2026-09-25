#!/usr/bin/env python3
"""Graphics for the Anti-UAV410 tracker post.

    python3 build_antiuav_blog_graphics.py

Reads posts/antiuav410-trackers/data.json -- exported from the benchmark's scored reports by
SVTracker's scripts/export_antiuav_blog_data.py -- so no number in a figure is typed by hand.
Every model is named on its own row, so no chart depends on colour to say which is which.
"""

import json
import os

from build_production_blog_graphics import (
    AMBER, BLUE, GREEN, MUTED, PURPLE, RULE, TEXT, build_share, svg_text,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "posts", "antiuav410-trackers")
DATA = os.path.join(OUT, "data.json")

# One colour per model, the same in every figure.
COLOUR = {"UETrack-B": PURPLE, "EfficientTAM-Ti": AMBER, "SAM 2.1-tiny": BLUE, "UETrack-T": GREEN}
WIDTH = 1200


def _svg(height, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" '
        f'width="{WIDTH}" height="{height}" role="img">\n'
        f'<rect width="{WIDTH}" height="{height}" fill="#ffffff"/>\n' + "\n".join(body) + "\n</svg>\n"
    )


def _line(x0, y0, x1, y1, color=RULE, width=1.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}" stroke="{color}" stroke-width="{width}"{d}/>'


def _write(name, content):
    path = os.path.join(OUT, name)
    with open(path, "w") as f:
        f.write(content)
    print("wrote", path)


def build_forest(data):
    """Difference from UETrack-B with 95% intervals: a tie on the left, a gap on the right."""
    rows = [m for m in data["models"] if "vs_reference" in m]
    panels = [
        ("lost", "Frames lost", "Lost% minus UETrack-B, percentage points", -6, 14),
        ("ends_lost_pts", "Sequences that end lost", "share of the 120 sequences, minus UETrack-B, points", -6, 28),
    ]
    top, row_h = 124, 74
    height = top + row_h * len(rows) + 86
    label_w, gap = 170, 56
    panel_w = (WIDTH - label_w - 40 - gap - 40) / 2
    body = [
        svg_text(40, 44, f"Difference from {data['reference']}, with 95% interval",
                 size=22, weight=700, anchor="start"),
        svg_text(40, 72, f"Paired bootstrap over the {data['sequences']} test sequences "
                 f"({data['resamples']:,} resamples). An interval that crosses zero is a tie.",
                 size=15, color=MUTED, anchor="start"),
    ]
    for p, (key, title, axis, lo, hi) in enumerate(panels):
        x0 = label_w + 40 + p * (panel_w + gap)
        scale = lambda v, x0=x0, lo=lo, hi=hi: x0 + (v - lo) / (hi - lo) * panel_w
        body.append(svg_text(x0, top - 12, title, size=16, weight=700, anchor="start"))
        bottom = top + row_h * len(rows)
        for tick in range(lo, hi + 1, 2 if hi - lo <= 20 else 6):
            body.append(_line(scale(tick), top, scale(tick), bottom, color="#f1f1ee", width=1))
            body.append(svg_text(scale(tick), bottom + 20, f"{tick:+d}" if tick else "0",
                                 size=12, color=MUTED))
        body.append(_line(scale(0), top - 4, scale(0), bottom + 4, color=TEXT, width=1.5))
        body.append(svg_text(x0 + panel_w / 2, bottom + 46, axis, size=13, color=MUTED))
        for r, m in enumerate(rows):
            est, low, high = m["vs_reference"][key]
            y = top + row_h * r + row_h / 2
            col = COLOUR[m["label"]]
            body.append(_line(scale(low), y, scale(high), y, color=col, width=3))
            for x in (scale(low), scale(high)):
                body.append(_line(x, y - 7, x, y + 7, color=col, width=2))
            body.append(f'<circle cx="{scale(est):.1f}" cy="{y:.1f}" r="7" fill="{col}"/>')
            verdict = "tie" if low <= 0 <= high else "worse"
            # Above the point, centred: a label beside the interval runs off the panel edge.
            label = svg_text(scale(est), y - 14, f"{est:+.1f}  [{low:+.1f}, {high:+.1f}]  {verdict}",
                             size=13, weight=600 if verdict == "worse" else 400,
                             color=TEXT if verdict == "worse" else MUTED)
            # A white halo drawn as its own copy underneath, so a label across the zero line
            # stays legible -- paint-order would do it in one element, but not every renderer
            # honours it, and the ones that don't paint the halo over the text.
            body.append(label.replace("<text ", '<text stroke="#ffffff" stroke-width="5" '
                                                'stroke-linejoin="round" ', 1))
            body.append(label)
    for r, m in enumerate(rows):
        y = top + row_h * r + row_h / 2
        body.append(svg_text(label_w + 20, y + 6, m["label"], size=16, weight=600, anchor="end"))
    _write("01_forest.svg", _svg(height, body))


def _grouped_bars(name, title, subtitle, groups, xmax, axis):
    """Horizontal bars, one labelled row per model inside each group -- nothing overlaps."""
    models = list(COLOUR)
    label_w, bar_h, row_gap, group_gap, top, head = 200, 18, 8, 30, 116, 30
    plot_w = WIDTH - label_w - 140
    scale = lambda v: label_w + v / xmax * plot_w
    rows_h = len(models) * (bar_h + row_gap)
    height = top + len(groups) * (head + rows_h + group_gap) + 58
    body = [
        svg_text(40, 44, title, size=22, weight=700, anchor="start"),
        svg_text(40, 72, subtitle, size=15, color=MUTED, anchor="start"),
    ]
    bottom = height - 58
    for tick in range(0, xmax + 1, 10):
        body.append(_line(scale(tick), top - 10, scale(tick), bottom, color="#f1f1ee", width=1))
        body.append(svg_text(scale(tick), bottom + 20, str(tick), size=12, color=MUTED))
    body.append(svg_text(label_w + plot_w / 2, bottom + 44, axis, size=13, color=MUTED))
    y = top
    for group, values in groups:
        # the group's heading gets its own line: beside the first bar it collides with a name
        body.append(svg_text(40, y + 14, group, size=16, weight=700, anchor="start"))
        for i, m in enumerate(models):
            yy = y + head + i * (bar_h + row_gap)
            v = values[m]
            body.append(svg_text(label_w - 14, yy + bar_h - 4, m, size=14, color=TEXT, anchor="end"))
            body.append(f'<rect x="{label_w}" y="{yy}" width="{max(scale(v) - label_w, 1):.1f}" '
                        f'height="{bar_h}" rx="3" fill="{COLOUR[m]}"/>')
            body.append(svg_text(scale(v) + 8, yy + bar_h - 4, f"{v:.1f}", size=13, anchor="start"))
        y += head + rows_h + group_gap
    _write(name, _svg(height, body))


def build_out_of_view(data):
    groups = [(f"{g}  (n={v['n']})", v) for g, v in data["by_absence"].items()]
    _grouped_bars(
        "02_out_of_view.svg",
        "When the drone leaves the frame, every tracker loses it",
        "Lost%, grouped by the longest stretch each test sequence spends with the drone out of view.",
        groups, 70, "Lost%  (frames whose predicted centre is more than one target size from the truth)",
    )


def build_size(data):
    buckets = [b for b, n in data["size_buckets"].items() if n > 1]  # one large target is not a bucket
    groups = [(f"{b}  (n={data['size_buckets'][b]})",
               {m["label"]: m["by_size"][b] for m in data["models"]}) for b in buckets]
    _grouped_bars(
        "03_size.svg",
        "About half the frames on sub-16-pixel drones are lost by every model",
        "Lost%, grouped by each sequence's median target size (square root of box area).",
        groups, 70, "Lost%",
    )


def build_card(data):
    """Same card as the other posts. Their builder names a macOS font; fall back elsewhere."""
    from PIL import ImageFont

    original = ImageFont.truetype

    def truetype(path, size, *a, **k):
        try:
            return original(path, size, *a, **k)
        except OSError:
            return original("DejaVuSans.ttf", size, *a, **k)

    ImageFont.truetype = truetype
    try:
        ref = {m["label"]: m for m in data["models"]}
        build_share(
            os.path.join(OUT, "share.png"),
            label="EDGE TRACKING · MEASURED, NOT REPORTED",
            title="Four Trackers on\nAnti-UAV410",
            subtitle="Same loss rate, very different endings: who gets\nthe drone back after losing it.",
            boxes=[
                (64, 372, 404, 512, "LOSS RATE", "a three-way tie", BLUE),
                (430, 372, 770, 512, "RECOVERY", f"{ref['UETrack-B']['ends_lost']} vs "
                 f"{ref['SAM 2.1-tiny']['ends_lost']} end lost", PURPLE),
                (796, 372, 1136, 512, "OUT OF VIEW", "breaks every model", AMBER),
            ],
        )
    finally:
        ImageFont.truetype = original


def main():
    with open(DATA) as f:
        data = json.load(f)
    build_forest(data)
    build_out_of_view(data)
    build_size(data)
    build_card(data)


if __name__ == "__main__":
    main()
