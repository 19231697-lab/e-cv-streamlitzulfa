
import streamlit as st
from pathlib import Path
from io import BytesIO
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors

st.set_page_config(
    page_title="E-CV Zulfa Rizqi Saputri",
    page_icon="🌸",
    layout="centered"
)

# =========================
# DATA CV
# =========================
data = {
    "nama": "Zulfa Rizqi Saputri",
    "posisi": "Data Analyst",
    "email": "zulfasaputri2332@gmail.com",
    "telepon": "+628989024573",
    "alamat": "Sukabumi, Jawa Barat",
    "tentang": (
        "Mahasiswa Sistem Informasi yang tertarik pada analisis data dan "
        "pengolahan informasi. Memiliki ketelitian, kemampuan berpikir analitis, "
        "serta minat dalam mengolah data menjadi informasi yang bermanfaat "
        "untuk mendukung pengambilan keputusan. Berkomitmen untuk terus belajar "
        "dan mengembangkan kemampuan di bidang Data Analyst."
    ),
    "pendidikan": (
        "Universitas Bina Sarana Informatika\n"
        "Sistem Informasi, Fakultas Teknik dan Informatika | 2023–Sekarang\n"
        "IPK: 3,92"
    ),
    "pengalaman": (
        "PENGALAMAN ORGANISASI\n"
        "Himpunan Mahasiswa Sistem Informasi (HIMASI)\n"
        "Anggota Pengurus Divisi Sumber Daya Mahasiswa | Januari–Desember 2024\n"
        "• Berpartisipasi dalam pelaksanaan program kerja divisi.\n\n"
        "Anggota Pengurus Departemen Pendidikan | Januari–Desember 2025\n"
        "• Mengumpulkan dan mengolah data melalui Google Forms sebagai bagian "
        "dari pelaksanaan program kerja departemen.\n\n"
        "KEPANITIAAN\n"
        "• Menjadi Master of Ceremony pada beberapa kegiatan HIMASI.\n"
        "• Berpartisipasi dalam berbagai kegiatan kepanitiaan organisasi.\n\n"
        "PROYEK PERGURUAN TINGGI\n"
        "• Proyek Statistika dan Probabilitas: Penerapan Software Statistik "
        "dalam Menganalisis Pengaruh Kebermanfaatan terhadap Penggunaan Nyata "
        "Aplikasi Telegram.\n"
        "• Publikasi artikel ilmiah: Illegal Deepfake-Based Artificial "
        "Intelligence Content and Efforts to Combat It in Indonesia, Jurnal "
        "Ilmiah Sistem Informasi (JUSI), Vol. 5 No. 1, 2026."
    ),
    "keterampilan": (
        "HARD SKILLS\n"
        "• Microsoft Office (Word, PowerPoint)\n"
        "• Google Workspace (Docs, Forms)\n"
        "• Pengumpulan dan pengolahan data menggunakan Google Forms\n"
        "• Dasar-dasar basis data dan SQL\n\n"
        "SOFT SKILLS\n"
        "• Komunikasi\n"
        "• Kerja sama tim\n"
        "• Adaptasi\n"
        "• Ketelitian dan berpikir analitis"
    ),
    "sertifikat": (
        "• Database Design & Database Programming with SQL — Digital Talent "
        "Scholarship (KOMINFO & Oracle Academy), 2024.\n"
        "• Workshop & Mini Proyek Sistem Basis Data — PT. Zahir Internasional."
    )
}


# =========================
# LOKASI FOTO
# =========================
FOLDER_APP = Path(__file__).resolve().parent
FOTO_PATH = FOLDER_APP / "foto_zulfa.jpeg"


# =========================
# WARNA
# =========================
PINK = "#BD5C91"
BIRU = "#35518A"
TEKS = "#34415C"

# =========================
# CSS TAMPILAN
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg, #fff0f6 0%, #f0f5ff 55%, #fceef5 100%
    );
    color: #26334d;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 2.5rem;
}

/* Header */
.cv-title {
    text-align: center;
    color: #35518a;
    font-size: 32px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 4px;
}

.cv-subtitle {
    text-align: center;
    color: #bd5c91;
    font-size: 15px;
    margin-bottom: 24px;
}

/* Area foto */
[data-testid="stImage"] {
    display: flex;
    justify-content: center;
}

[data-testid="stImage"] img {
    border-radius: 50%;
    border: 5px solid #f3b6d2;
    box-shadow: 0 0 0 4px #b9d9f8;
    object-fit: cover;
}

/* Kartu utama Streamlit */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.97);
    border: 1px solid #f0cfe0;
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 8px 28px rgba(74,86,130,0.10);
}

/* Warna teks */
.stApp h1, .stApp h2, .stApp h3 {
    color: #35518a !important;
}

.stApp p, .stApp li,
.stApp [data-testid="stCaptionContainer"] {
    color: #34415c;
}

/* Tombol unduh PDF */
.stDownloadButton button {
    background: linear-gradient(90deg, #d96ca5, #6888d8);
    color: white !important;
    border: none;
    border-radius: 12px;
    min-height: 48px;
    font-weight: 700;
    width: 100%;
}

.stDownloadButton button:hover {
    background: linear-gradient(90deg, #c65391, #4f70c4);
    color: white !important;
    border: none;
}

hr {
    border-color: #f0cfe0 !important;
}

.footer {
    text-align: center;
    color: #8a7190;
    font-size: 12px;
    margin-top: 22px;
}

@media (max-width: 600px) {
    .block-container {
        padding: 1rem 0.7rem 2rem;
    }
    .cv-title {
        font-size: 26px;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown(
    '<div class="cv-title">CURRICULUM VITAE</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="cv-subtitle">🌸 E-CV · Data Analyst · 2026</div>',
    unsafe_allow_html=True
)

# =========================
# FOTO PROFIL
# =========================
if FOTO_PATH.is_file():
    kolom_kiri, kolom_foto, kolom_kanan = st.columns([1, 2, 1])

    with kolom_foto:
        st.image(
            str(FOTO_PATH),
            width=155,
            caption=None
        )
else:
    st.error("Foto profil belum ditemukan.")
    st.caption(
        "Pastikan file foto_zulfa.jpeg sudah diunggah "
        "ke repository GitHub yang terhubung dengan Streamlit."
    )

# =========================
# ISI CV
# =========================
with st.container(border=True):

    st.markdown(
        f"<h1 style='text-align:center;color:{PINK};"
        f"font-size:30px;font-weight:800;margin-bottom:0;'>"
        f"{escape(data['nama'])}</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='text-align:center;color:{PINK};font-size:18px;"
        f"font-weight:700;margin-top:4px;'>"
        f"{escape(data['posisi'])}</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='text-align:center;color:{TEKS};line-height:1.9;'>"
        f"📧 {escape(data['email'])}<br>"
        f"📱 {escape(data['telepon'])}<br>"
        f"📍 {escape(data['alamat'])}</p>",
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 🌷 Tentang Saya")
    st.write(data["tentang"])

    st.markdown("### 🎓 Pendidikan")
    st.text(data["pendidikan"])

    st.markdown("### 💼 Pengalaman")
    st.text(data["pengalaman"])

    st.markdown("### 💻 Keterampilan")
    st.text(data["keterampilan"])

    st.markdown("### 📜 Sertifikat dan Pelatihan")
    st.text(data["sertifikat"])

# =========================
# MEMBUAT PDF
# =========================
pdf_buffer = BytesIO()

doc = SimpleDocTemplate(
    pdf_buffer,
    pagesize=A4,
    rightMargin=45,
    leftMargin=45,
    topMargin=35,
    bottomMargin=35
)

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name="NamaCV",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=21,
    leading=26,
    textColor=colors.HexColor(BIRU),
    alignment=TA_CENTER,
    spaceAfter=5
))

styles.add(ParagraphStyle(
    name="PosisiCV",
    parent=styles["Normal"],
    fontSize=12,
    leading=16,
    textColor=colors.HexColor(PINK),
    alignment=TA_CENTER,
    spaceAfter=7
))

styles.add(ParagraphStyle(
    name="KontakCV",
    parent=styles["Normal"],
    fontSize=8.5,
    leading=13,
    textColor=colors.HexColor(TEKS),
    alignment=TA_CENTER,
    spaceAfter=8
))

styles.add(ParagraphStyle(
    name="BagianCV",
    parent=styles["Heading2"],
    fontSize=11.5,
    leading=15,
    textColor=colors.HexColor(BIRU),
    spaceBefore=9,
    spaceAfter=5
))

styles.add(ParagraphStyle(
    name="IsiCV",
    parent=styles["BodyText"],
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor("#26334D"),
    spaceAfter=3
))

story = []

# Foto profil di dalam PDF
if FOTO_PATH.is_file():
    foto_pdf = Image(str(FOTO_PATH), width=78, height=78)
    foto_pdf.hAlign = "CENTER"
    story.extend([foto_pdf, Spacer(1, 8)])

story.extend([
    Paragraph(escape(data["nama"]), styles["NamaCV"]),
    Paragraph(escape(data["posisi"]), styles["PosisiCV"]),
    Paragraph(
        escape(" | ".join([
            data["email"],
            data["telepon"],
            data["alamat"]
        ])),
        styles["KontakCV"]
    ),
    HRFlowable(
        width="100%",
        thickness=1,
        color=colors.HexColor("#E9A8CC"),
        spaceBefore=3,
        spaceAfter=5
    )
])

bagian = [
    ("Tentang Saya", "tentang"),
    ("Pendidikan", "pendidikan"),
    ("Pengalaman", "pengalaman"),
    ("Keterampilan", "keterampilan"),
    ("Sertifikat dan Pelatihan", "sertifikat")
]

for judul, kunci in bagian:
    story.append(Paragraph(escape(judul), styles["BagianCV"]))

    paragraf = []
    for baris in data[kunci].splitlines():
        teks = escape(baris)
        if teks.startswith("• "):
            paragraf.append("&bull; " + teks[2:])
        elif teks:
            paragraf.append(teks)
        else:
            paragraf.append("&#160;")

    story.append(
        Paragraph("<br/>".join(paragraf), styles["IsiCV"])
    )

doc.build(story)
pdf_buffer.seek(0)

# =========================
# TOMBOL UNDUH PDF
# =========================
st.download_button(
    label="📥 Unduh CV dalam PDF",
    data=pdf_buffer.getvalue(),
    file_name="CV_Zulfa_Rizqi_Saputri.pdf",
    mime="application/pdf",
    use_container_width=True
)

st.markdown(
    '<div class="footer">E-CV Zulfa Rizqi Saputri · '
    'Sistem Informasi</div>',
    unsafe_allow_html=True
)
