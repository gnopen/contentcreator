# Master Design Prompt — Paste Once Per Claude Session

Paste this prompt into [claude.ai](https://claude.ai) at the start of every session. Claude will acknowledge the design system, then you can paste any Chapter spec from `chapters/` and Claude will render an HTML artifact with all 6 slides.

---

```
Saya akan kasih kamu spec untuk Instagram carousel "AI Daily Routine — A Field Manual". Setiap kali saya kirim Chapter spec, kamu render HTML artifact dengan design system Field Manual berikut — JANGAN diubah, ikuti EXACT:

CANVAS: 6 slide vertikal 1080×1350 px. Render semua slide stacked vertical dengan gap 32px. Body background #1a1a1a. Slide background #DDE6EE.

PALETTE:
- BG slide: #DDE6EE | Ink: #0A1F3D | Cobalt: #2E5AAC | Card: #FAFCFE
- Muted body: #4A5A7A | Slate metadata: #88A4C9 | Divider: #B5C2D0

FONT SYSTEM (load via Google Fonts):
- Fraunces serif (300/400/600/700) — semua headline, deck, doc heading
- Inter sans (400/500/600) — body text
- IBM Plex Mono (400/500/600) — semua label, caption, metadata, masthead, footer, table header

ANATOMY TIAP SLIDE (mandatory di SEMUA 6 slide):
1. Register marks: 4 lingkaran kecil 18px dengan crosshair di 4 pojok (top: 20px, sides: 20px), warna #88A4C9
2. Masthead atas: padding 36px 70px 0, isi 2 row mono uppercase 13px letter-spacing 0.12em, kiri "Chapter X — [subtitle]" kanan "Folio XX — [type]", garis horizontal 1px #0A1F3D di bawahnya
3. Footer bawah: padding 0 70px 36px, garis 1px #0A1F3D di atas, lalu 2 row mono uppercase 13px, kiri "Vol. 01 / 30 — Chapter X — Folio XX" kanan "@aidailyroutine" (kecuali Colophon kanan jadi "DM 'AGENT' — waitlist")

TYPOGRAPHY:
- title-xl: Fraunces 300, 120px, line-height 0.95, untuk cover & colophon
- title-lg: Fraunces 300, 88px, line-height 0.98, untuk folio 02-05
- Underline emphasis: kata kunci dalam <em> dengan ::after background cobalt height 5-6px positioned behind text (bukan font-weight bold)
- deck: Fraunces italic 28px, color #4A5A7A
- body-text: Inter 20px line-height 1.55 color #4A5A7A
- label: Mono 11px letter-spacing 0.14em uppercase color #2E5AAC
- caption: Mono 12px letter-spacing 0.1em uppercase color #88A4C9

FOLIO BACKGROUND (slide 2-5 only):
- Roman numeral huge: Fraunces 300, 320px, opacity 0.06, color #0A1F3D, positioned absolute (alternate left/right per slide untuk variasi)
- Slide 2 = I, Slide 3 = II, Slide 4 = III, Slide 5 = IV

CARDS & MOCKUPS:
- Background #FAFCFE, border 1px #B5C2D0, border-radius 4px, shadow 0 8px 32px rgba(10,31,61,0.06)
- Header bar pakai background #2E5AAC color #FAFCFE
- Table header pakai background #0A1F3D color #FAFCFE
- Highlight row pakai background gradient linear 60% transparent + 40% rgba(46,90,172,0.25)

VISUAL TYPES (saya akan specify per folio):
- Type A: Body text kiri + Mockup card kanan dengan annotation [a/b/c] dotted line
- Type B: Pull quote dengan curly mark 180px + Document card berisi structured heading
- Type C: Flow diagram 3-node (Input → Process → Output) + Table dengan kolom № / Task / Owner / Status
- Type D: 3-column Specimen grid (label, big numeral, name, body, meta footer)
- Type E: Sidebar comparison kiri vs kanan dengan divider vertical

ANNOTATION SYSTEM:
- Marker: lingkaran 22px border 1.5px cobalt, isi nomor 1/2/3
- Posisi: absolute, terhubung ke target via dotted line stroke #2E5AAC stroke-dasharray "2,3"
- Label format: "[a] = description" mono 13px

COVER & COLOPHON KHUSUS:
- Cover: issue-mark uppercase mono di atas, title-xl asymmetric kiri, deck italic, hero SVG diagram dengan grid pattern background subtle (#88A4C9 opacity 0.3 stroke 0.5px) dan annotation [a][b][c], caption box "Fig. 01 — [Title]"
- Colophon: end-mark "End · Chapter X · Of 30" dengan 2 dot cobalt sebagai separator, title-xl center closing statement, end-deck italic, next-issue card "Next · Chapter X+1 · [Title]"

ATURAN ABSOLUT:
- Hanya 1 kata di-underline-emphasis per headline (via <em> tag dengan cobalt bar background)
- TIDAK pakai bold weight untuk emphasis — selalu underline cobalt
- TIDAK ada emoji di body utama (boleh di mockup UI yang natural)
- SEMUA metadata pakai IBM Plex Mono uppercase letter-spacing
- Whitespace adalah priority — JANGAN ramai

Konfirmasi paham. Setelah saya kirim "Chapter X spec", render HTML lengkap 6 slide dengan semua anatomy di atas.
```

---

## After Pasting

Claude akan reply dengan konfirmasi paham. Setelah itu:

1. Buka `chapters/chapter-XX.md` untuk hari yang mau kamu post
2. Copy isi spec (mulai dari `Render Chapter X — ...`)
3. Paste ke Claude
4. Tunggu artifact ter-render — 6 slide HTML siap di-screenshot

## Tips

- **Sekali per session**: master prompt cukup di-paste satu kali per chat session. Cache akan retain design system untuk semua chapter berikutnya di session yang sama.
- **Batch produksi**: paste 2-3 chapter sekaligus dalam 1 message — Claude akan render semua dalam 1 artifact panjang.
- **Custom tweak**: setelah artifact jadi, follow-up dengan "Folio 03, ganti pull quote jadi X" — Claude akan patch sebagian saja.
- **Export**: screenshot dari artifact preview, atau open HTML di browser → DevTools F12 → device toolbar set 1080×1350 → Capture full screenshot per slide.
