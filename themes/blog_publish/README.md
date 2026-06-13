# Publish package: production CVPR review and architecture essay

Target site: `genawass.github.io`

## Files

- `posts/cvpr2026-production.html` -> site `posts/cvpr2026-production.html`
- `posts/vision-pipeline-inside-model.html` -> site `posts/vision-pipeline-inside-model.html`
- `posts/cvpr2026-production/01_architecture.svg` -> conceptual architecture graphic
- `posts/cvpr2026-production/02_readiness.html` -> interactive readiness chart
- `posts/cvpr2026-production/03_pipeline_collapse.svg` -> shared-model capability graphic
- `posts/cvpr2026-production/shortlisted-papers.md` -> full six-per-theme paper appendix
- `posts/cvpr2026-production/paper-*.svg` -> generated featured-paper concept diagrams
- `posts/cvpr2026-production/share-production.png` -> production-review social preview
- `posts/cvpr2026-production/share.png` -> architecture-essay social preview
- `blog-entry.html` -> insert as the first `<li>` in `blog.html`'s `.posts`
- `index-entry.html` -> insert as the first `<li>` in `index.html`'s `.posts`

Both posts follow the site's existing standalone HTML structure and shared
`../styles.css`. The production review is a sequel to `posts/cvpr2026.html`.

## Rebuild graphics

From the CVPR analysis repository:

```bash
python3 build_production_blog_graphics.py
```

The architecture SVG and share cards are generated from a fixed design. The
readiness chart is generated directly from
`themes/production_assessments/assessments.json`.

Featured-paper concept diagrams are generated from `PAPER_CONCEPTS`. Paper
cards only show arXiv, code, project, and demo actions when those resources
are available.

## Suggested social copy

What can CVPR 2026 contribute to a real computer-vision product?

I reviewed 84 papers across 14 production themes: what can ship now, what is
near, and where research still outruns deployment.

---

Software 2.0 replaced computer-vision algorithms. The next transition is
replacing the interfaces between them.

## Validation

- All CVF paper links match records in `cvpr2026_papers.json`.
- Internal links match the existing site structure.
- No changes are required to `styles.css`.
- Generated assets are reproducible from `build_production_blog_graphics.py`.
