Google Analytics (GA4) snippet for Measurement ID: G-HNJHN77SZF

Stream ID: 15064433202

Add this to the <head> of your site's HTML (recommended spot):

```html
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-HNJHN77SZF"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);} 
  gtag('js', new Date());
  gtag('config', 'G-HNJHN77SZF');
</script>
```

Notes:
- For GitHub Pages using Jekyll, add into `_includes/head.html` or `_layouts/default.html` before the closing `</head>` tag.
- To enable IP anonymization: `gtag('config','G-HNJHN77SZF',{ 'anonymize_ip': true });`
- To use Google Tag Manager instead, provide a `GTM-XXXXX` container ID and I can generate that snippet instead.

If you want, I can commit this change and open a branch. Reply `commit` to proceed.