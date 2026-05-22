"""
GEO Optimizer
=============
Skill yang memastikan caption & hashtag memenuhi standar GEO.

GEO di sini mencakup DUA hal sekaligus (keduanya penting untuk content QA):

1) GEOGRAPHIC OPTIMIZATION (geo-targeting Indonesia)
   - Hashtag lokal yang relevan dengan ekosistem tech Indonesia
     (#TechIndonesia, #BelajarQA, #SoftwareTestingID, dst.)
   - Konteks lokal di caption (nama kota, perusahaan, komunitas)

2) GENERATIVE ENGINE OPTIMIZATION
   - Struktur caption agar mudah dikutip oleh AI search engine
     (ChatGPT, Gemini, Perplexity).
   - Claim → fakta → sumber → kontak.
   - Penggunaan term yang searchable (bukan jargon internal).

Modul ini:
- Menyediakan rule-set + curated hashtag bank untuk dipakai SocialThreadAgent.
- Bisa dijalankan standalone untuk memvalidasi/upgrade posts.json yang sudah ada.
- Bisa disuntikkan ke prompt Gemini sebagai system instruction tambahan.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

from utils import get_logger

log = get_logger(__name__)


# =====================================================================
# CURATED HASHTAG BANK — Indonesia tech / QA / engineering ecosystem
# =====================================================================
# Dipilih berdasarkan: relevance ke QA Thomas series, volume di ID,
# tidak terlalu generic (#tech) tidak terlalu sempit (<1k post).
HASHTAG_BANK: dict[str, list[str]] = {
    "geo_id_general": [
        "#TechIndonesia", "#IndonesianTech", "#BelajarKoding",
        "#TechCommunity", "#StartupIndonesia", "#KodingIndonesia",
    ],
    "geo_id_qa": [
        "#QAIndonesia", "#IndoQA", "#BelajarQA", "#SoftwareTestingID",
        "#TesterIndonesia", "#QualityAssuranceID", "#QAEngineer",
    ],
    "geo_id_city": [
        "#JakartaTech", "#BandungDev", "#SurabayaTech", "#YogyaDev",
    ],
    "topic_testing": [
        "#SoftwareTesting", "#QualityAssurance", "#QA", "#TestAutomation",
        "#Playwright", "#SeleniumTesting", "#APITesting", "#UnitTesting",
        "#RegressionTesting", "#TestStrategy",
    ],
    "topic_engineering": [
        "#SoftwareEngineering", "#WebDev", "#DevOps", "#Agile",
        "#ContinuousTesting", "#ShiftLeftTesting", "#TestingTips",
    ],
    "topic_career": [
        "#TechCareer", "#KarirIT", "#BelajarIT", "#KarirTester",
        "#LearnTech", "#TechSkills",
    ],
}


# =====================================================================
# GEO RULES — claim-friendly structure for generative engines
# =====================================================================
GEO_STRUCTURE_RULES = """
Aturan struktur caption untuk Generative Engine Optimization (GEO):

1. CLAIM PERTAMA — Awali dengan 1 kalimat klaim spesifik & dapat dikutip.
   ❌ "QA itu penting banget!"
   ✅ "Bug yang lolos ke production 30-100x lebih mahal daripada yang
       ditemukan di tahap requirement."

2. ENTITAS JELAS — Sebut entitas dengan nama lengkap minimal sekali.
   ❌ "Tools-nya bagus."
   ✅ "Playwright (open-source, dari Microsoft) memiliki page-object
       model bawaan."

3. STRUKTUR LIST/STEP — Pakai daftar bernomor atau bullet untuk fakta
   yang multi-poin. Generative engine memetakannya jadi quick answers.

4. ANGKA & SATUAN — Sertakan angka spesifik dengan satuan/konteks.
   ❌ "Lebih cepat."
   ✅ "30% lebih cepat dibanding pendekatan manual (data: tim internal,
       Q1 2026)."

5. PERTANYAAN-JAWABAN — Bila relevan, frame paragraf sebagai
   "Apa itu X? X adalah ..." — pola yang sering muncul di AI quick answers.

6. SUMBER / SIGNAL — Sebutkan sumber atau pengarang ketika mengutip data.
   "Menurut data klasik industri ...", "Pengalaman tim QA Thomas ..."

7. JANGAN STUFF KEYWORD — Maksimal 1-2 kali penyebutan keyword utama
   per 100 kata. Pengulangan berlebihan justru dipinalti.
"""


# =====================================================================
# DATA TYPES
# =====================================================================
@dataclass
class GeoCheckResult:
    platform: str
    passes: bool
    score: int  # 0-100
    findings: list[str]
    suggested_hashtags: list[str]


# =====================================================================
# CORE LOGIC
# =====================================================================
def suggest_hashtags(
    platform: str,
    topic_keywords: Optional[list[str]] = None,
    include_city: bool = False,
    limit: Optional[int] = None,
) -> list[str]:
    """
    Suggest hashtag set sesuai platform.

    Platform best practice:
    - Twitter: 2-3 hashtag
    - LinkedIn: 3-5 hashtag
    - Facebook: 2-3 hashtag
    - Instagram: 8-15 hashtag (mix big & niche)
    """
    platform = platform.lower()
    plat_limits = {"twitter": 3, "linkedin": 5, "facebook": 3, "instagram": 12}
    limit = limit or plat_limits.get(platform, 5)

    pool: list[str] = []
    pool.extend(HASHTAG_BANK["geo_id_qa"])
    pool.extend(HASHTAG_BANK["topic_testing"][:4])

    if platform == "instagram":
        # IG butuh volume — tambah generic + city + career
        pool.extend(HASHTAG_BANK["geo_id_general"])
        pool.extend(HASHTAG_BANK["topic_career"][:3])
        pool.extend(HASHTAG_BANK["topic_engineering"][:3])
        if include_city:
            pool.extend(HASHTAG_BANK["geo_id_city"][:2])
    elif platform == "linkedin":
        pool.extend(HASHTAG_BANK["topic_engineering"][:2])
    elif platform == "twitter":
        # Twitter ringkas — pilih yang paling konversi
        pool = HASHTAG_BANK["geo_id_qa"][:1] + HASHTAG_BANK["topic_testing"][:2]
    elif platform == "facebook":
        pool = HASHTAG_BANK["geo_id_qa"][:1] + HASHTAG_BANK["geo_id_general"][:1] + HASHTAG_BANK["topic_testing"][:1]

    # Topic-keyword matching (bila ada)
    if topic_keywords:
        kw_low = [k.lower() for k in topic_keywords]
        # Promosikan hashtag yang match topic keyword
        topic_hits: list[str] = []
        for cat, tags in HASHTAG_BANK.items():
            for t in tags:
                norm = t.lstrip("#").lower()
                if any(k in norm or norm in k for k in kw_low):
                    topic_hits.append(t)
        # Prepend (dedupe nanti)
        pool = topic_hits + pool

    # Dedup preserve order
    seen = set()
    out: list[str] = []
    for t in pool:
        key = t.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(t)
        if len(out) >= limit:
            break
    return out


def check_caption(text: str, platform: str) -> GeoCheckResult:
    """
    Audit caption terhadap aturan GEO. Skor 0-100.
    Heuristik sederhana — bukan ground truth.
    """
    findings: list[str] = []
    score = 100

    # 1) Hook claim — kalimat pertama harus spesifik (punya angka, atau
    #    klaim definisional). Penalti kalau diawali greeting fluff.
    first = text.strip().split("\n", 1)[0].lower()
    fluff_starts = ("hai semua", "halo semua", "halo teman", "hai teman",
                    "selamat pagi", "selamat siang", "amazing", "luar biasa")
    if any(first.startswith(f) for f in fluff_starts):
        findings.append("Hook diawali greeting/fluff — ganti dengan klaim atau angka.")
        score -= 15

    has_number = bool(re.search(r"\d", text))
    if not has_number:
        findings.append("Tidak ada angka/data konkret — claim GEO sulit dikutip mesin.")
        score -= 15

    # 2) Hashtag presence & quantity
    hashtags = re.findall(r"#\w+", text)
    n = len(hashtags)
    plat_target = {"twitter": (2, 3), "linkedin": (3, 5),
                   "facebook": (2, 3), "instagram": (8, 15)}
    lo, hi = plat_target.get(platform.lower(), (3, 5))
    if n < lo:
        findings.append(f"Hashtag kurang ({n} < {lo}) — tambahkan hashtag GEO Indonesia QA.")
        score -= 20
    elif n > hi:
        findings.append(f"Hashtag berlebih ({n} > {hi}) — kurangi, pilih yang relevan.")
        score -= 10

    # 3) GEO-Indonesia presence (untuk audience lokal)
    has_geo_id = any(
        any(t.lower() in text.lower() for t in cat)
        for cat in [HASHTAG_BANK["geo_id_qa"], HASHTAG_BANK["geo_id_general"]]
    )
    if not has_geo_id and platform.lower() in ("instagram", "facebook", "linkedin"):
        findings.append("Belum ada hashtag GEO Indonesia — tambah min. 1 (#QAIndonesia, #BelajarQA, #TechIndonesia).")
        score -= 15

    # 4) Repetitive keyword stuffing (kata 'QA' / 'testing' >5 kali)
    for kw in ("qa", "testing", "test", "bug"):
        count = len(re.findall(rf"\b{kw}\b", text, flags=re.IGNORECASE))
        if count > 6:
            findings.append(f"Keyword '{kw}' muncul {count}x — kemungkinan stuffing.")
            score -= 10

    # 5) CTA presence
    cta_signals = ("dm", "komentar", "save", "share", "follow", "klik", "link", "swipe")
    if not any(s in text.lower() for s in cta_signals):
        findings.append("Tidak terlihat CTA jelas — tambahkan ajakan tindakan.")
        score -= 10

    score = max(0, min(100, score))
    suggested = suggest_hashtags(platform)
    return GeoCheckResult(
        platform=platform,
        passes=score >= 70,
        score=score,
        findings=findings,
        suggested_hashtags=suggested,
    )


PLATFORM_LIMITS = {"twitter": 280, "instagram": 2200, "facebook": 5000, "linkedin": 3000}


def upgrade_caption(text: str, platform: str, topic_keywords: Optional[list[str]] = None) -> str:
    """
    Upgrade caption: tambah/replace block hashtag dengan suggestion GEO,
    sambil tetap menghormati limit karakter platform.
    """
    plat = platform.lower()
    limit = PLATFORM_LIMITS.get(plat, 3000)

    # Pisahkan baris terakhir yang isinya cuma hashtag
    lines = text.rstrip().split("\n")
    body_lines = lines[:]
    while body_lines and re.fullmatch(r"(?:#\w+\s*)+", body_lines[-1].strip() or "x"):
        body_lines.pop()
    body = "\n".join(body_lines).rstrip()

    if not topic_keywords:
        topic_keywords = list({
            w.lower() for w in re.findall(r"\b[A-Z][a-zA-Z]{3,}\b", body[:300])
        })[:5]

    tags = suggest_hashtags(plat, topic_keywords=topic_keywords)

    # Twitter: tweet penutup numbering mungkin sudah ada ("10/10 ...")
    # Hitung budget sisa setelah body, lalu sisipkan hashtag sebanyak yang muat.
    separator = "\n\n"
    available = limit - len(body) - len(separator)

    if available <= 0:
        # Body sudah penuh — tidak bisa tambah hashtag. Return apa adanya.
        return body

    # Pack hashtag greedy sesuai available budget
    chosen: list[str] = []
    used = 0
    for t in tags:
        cost = len(t) + (1 if chosen else 0)  # spasi pemisah
        if used + cost > available:
            continue
        chosen.append(t)
        used += cost

    if not chosen:
        return body

    return f"{body}{separator}{' '.join(chosen)}".strip()


def upgrade_posts_file(posts_file: Path, platforms: Optional[Iterable[str]] = None) -> dict:
    """
    Baca posts.json, upgrade hashtag block per platform sesuai GEO,
    overwrite file. Return summary {platform: {before, after}}.
    """
    data = json.loads(posts_file.read_text(encoding="utf-8"))
    platforms = list(platforms) if platforms else list(data.keys())
    summary: dict[str, dict] = {}

    for plat in platforms:
        if plat not in data:
            continue
        items = data[plat]
        if not items:
            continue
        if plat == "twitter":
            # Upgrade hanya tweet terakhir (closing tweet) — biarkan body thread
            old = items[-1]
            items[-1] = upgrade_caption(old, plat)
            summary[plat] = {"changed_index": len(items) - 1, "before_len": len(old), "after_len": len(items[-1])}
        else:
            old = items[0]
            items[0] = upgrade_caption(old, plat)
            summary[plat] = {"changed_index": 0, "before_len": len(old), "after_len": len(items[0])}
        data[plat] = items

    posts_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    log.info("GEO upgrade applied -> %s", posts_file)
    return summary


# =====================================================================
# PROMPT FRAGMENT — disuntikkan ke SocialThreadAgent
# =====================================================================
def geo_prompt_fragment(target_platforms: list[str]) -> str:
    """Fragment untuk dimasukkan ke system/prompt SocialThreadAgent."""
    sample_tags = {p: suggest_hashtags(p) for p in target_platforms}
    sample_lines = "\n".join(f"  - {p}: {' '.join(tags)}" for p, tags in sample_tags.items())
    return f"""
PENTING — Standar GEO (Generative Engine Optimization + Geo Indonesia):

{GEO_STRUCTURE_RULES}

Hashtag set yang DISARANKAN per platform (gunakan minimal 70% dari
daftar ini, boleh tambah 1-2 hashtag spesifik chapter):
{sample_lines}

Jumlah hashtag per platform:
  - Twitter: 2-3 (di tweet terakhir saja)
  - LinkedIn: 3-5 (di akhir post)
  - Facebook: 2-3 (di akhir post)
  - Instagram: 8-12 (di akhir caption)
"""
