#!/usr/bin/env python3
"""Social-preview card for the INT8 quantization post.

Reuses build_share() from build_production_blog_graphics.py so the card matches
the other posts' share images exactly.

    python3 build_int8_share.py
"""

import os

from build_production_blog_graphics import AMBER, BLUE, PURPLE, build_share

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "posts", "int8-dla", "share.png")


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    build_share(
        OUT,
        label="EDGE DEPLOYMENT · QUANTIZATION",
        title="Quantization Is Three\nProblems, Not One",
        subtitle="PTQ finds the ranges, QAT moves the weights into them,\n"
        "QDQ translation hands them to TensorRT.",
        boxes=[
            (64, 372, 404, 512, "PTQ", "where are the ranges?", BLUE),
            (430, 372, 770, 512, "QAT", "can weights live there?", AMBER),
            (796, 372, 1136, 512, "TRANSLATION", "can the runtime be told?", PURPLE),
        ],
    )
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
