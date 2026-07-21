#!/usr/bin/env bash
set -euo pipefail

# Base URL for Pages — change to your custom domain if needed
BASE_URL="https://athiclairs.github.io"

mkdir -p site site/thumbs
cd site || exit 0

# Remove any leftover aux files (from local runs)
rm -f -- *.aux *.log *.out *.toc *.synctex.gz *.gz *.bbl *.blg *.nav *.snm || true
: > .nojekyll

cat > index.html <<'HTML'
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Document</title>
<!-- Custom favicon from icon/ folder -->
<link rel="icon" type="image/x-icon" href="icon/favicon.ico">
<link rel="icon" type="image/png" href="icon/logo.png">
<style>
  :root{
    --preview-desktop: 70vw;
    --preview-mobile: 90vw;
  }
  body{font-family:system-ui,Segoe UI,Roboto,Helvetica,Arial,sans-serif;max-width:64rem;margin:2rem auto;padding:0 1rem;line-height:1.45}
  header{display:flex;align-items:center;gap:1rem;margin-bottom:.75rem}
  .header-logo{height:2.5rem;width:auto}
  h1{margin:0;font-size:1.6rem}
  .pdf-list{list-style:none;padding:0;margin:0}
  .pdf-item{padding:.5rem 0;border-bottom:1px solid #f0f0f0}
  .pdf-header{margin-bottom:.3rem}
  .pdf-link{
    color:#0b66ff;
    font-weight:600;
    text-decoration:none;
    font-size:1rem;
  }
  .pdf-link:hover{text-decoration:underline}
  .preview-container{
    display:block;
    margin-top:.5rem;
  }
  .preview-wrapper{margin:0 auto;box-sizing:border-box;padding:6px;border:1px solid #ddd;background:#fff;width:var(--preview-desktop)}
  @media (max-width:700px){ .preview-wrapper{width:var(--preview-mobile)} }
  .preview-thumb{width:100%;height:auto;display:block;border:1px solid #eee;background:#fafafa}
  .no-thumb{font-size:.95rem;color:#6b7280;padding:.5rem}
</style>
</head>
<body>
  <header>
    <img class="header-logo" src="icon/logo.png" alt="Logo" onerror="this.style.display='none'">
    <h1>Document</h1>
  </header>

  <section>
    <ul class="pdf-list">
HTML

# List PDF files from the pdfs/ subfolder
if find pdfs/ -maxdepth 1 -type f -name '*.pdf' | grep -q '.' 2>/dev/null; then
  find pdfs/ -maxdepth 1 -type f -name '*.pdf' -printf '%f\n' | sort | while IFS= read -r f; do
    esc=$(printf '%s' "$f" | sed 's/&/\&amp;/g;s/</\&lt;/g;s/>/\&gt;/g')
    href="${BASE_URL}/pdfs/${f}"
    thumb="thumbs/${f%.*}.png"
    cat >> index.html <<EOF
      <li class="pdf-item">
        <div class="pdf-header">
          <a class="pdf-link" href="${href}" target="_blank" rel="noopener">${esc}</a>
        </div>
        <div class="preview-container">
          <div class="preview-wrapper">
            <img class="preview-thumb" src="${thumb}" alt="Thumbnail for ${esc}" />
            <div class="no-thumb" style="display:none">No preview available</div>
          </div>
        </div>
      </li>
EOF
  done
else
  echo '      <li class="pdf-item">No PDFs found.</li>' >> index.html
fi

cat >> index.html <<'HTML'
    </ul>
  </section>
</body>
</html>
HTML

exit 0
