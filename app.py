
import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from io import BytesIO
from xml.sax.saxutils import escape

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
# TEMA PINK & BIRU
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #fff0f6 0%,
        #f0f5ff 55%,
        #fceef5 100%
    );
    color: #26334d;
}

.block-container {
    max-width: 850px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Header */
.cv-title {
    text-align: center;
    color: #35518a !important;
    font-size: 36px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 5px;
}

.cv-subtitle {
    text-align: center;
    color: #bd5c91 !important;
    font-size: 15px;
    margin-bottom: 28px;
}

/* Kartu utama */
.cv-card {
    background-color: #ffffff;
    color: #26334d;
    padding: 32px;
    border-radius: 20px;
    border: 1px solid #f3d7e6;
    box-shadow: 0 8px 28px rgba(74, 86, 130, 0.10);
}

/* Semua teks dibuat mudah dibaca */
.stApp p,
.stApp li,
.stApp label,
.stApp .stMarkdown,
.stApp [data-testid="stCaptionContainer"] {
    color: #34415c;
}

.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4 {
    color: #35518a !important;
}

/* Nama */
[data-testid="stHeading"] h1 {
    color: #bd5c91 !important;
    font-weight: 800;
}

/* Garis pemisah */
hr {
    border-color: #f0cfe0 !important;
}

/* Tombol unduh */
.stDownloadButton button {
    background: linear-gradient(90deg, #d96ca5, #6888d8);
    color: #ffffff !important;
    border: none;
    border-radius: 12px;
    min-height: 48px;
    font-weight: 700;
    transition: 0.2s ease;
}

.stDownloadButton button:hover {
    background: linear-gradient(90deg, #c65391, #4f70c4);
    color: #ffffff !important;
    border: none;
}

/* Footer */
.footer {
    text-align: center;
    color: #8a7190;
    font-size: 12px;
    margin-top: 24px;
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
# TAMPILAN CV
# =========================
st.markdown('<div class="cv-card">', unsafe_allow_html=True)

st.title(data["nama"])
st.markdown(
    f"<p style='color:#bd5c91;font-size:19px;"
    f"font-weight:700;'>{escape(data['posisi'])}</p>",
    unsafe_allow_html=True
)

st.caption(
    f"📧 {data['email']}  \n"
    f"📱 {data['telepon']}  \n"
    f"📍 {data['alamat']}"
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

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# MEMBUAT PDF
# =========================
pdf_buffer = BytesIO()

doc = SimpleDocTemplate(
    pdf_buffer,
    pagesize=A4,
    rightMargin=45,
    leftMargin=45,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name="NamaCV",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=22,
    leading=28,
    textColor=colors.HexColor("#35518a"),
    alignment=TA_CENTER,
    spaceAfter=8
))

styles.add(ParagraphStyle(
    name="PosisiCV",
    parent=styles["Normal"],
    fontSize=12,
    leading=16,
    textColor=colors.HexColor("#bd5c91"),
    alignment=TA_CENTER,
    spaceAfter=8
))

styles.add(ParagraphStyle(
    name="KontakCV",
    parent=styles["Normal"],
    fontSize=9,
    leading=14,
    textColor=colors.HexColor("#34415c"),
    alignment=TA_CENTER,
    spaceAfter=8
))

styles.add(ParagraphStyle(
    name="BagianCV",
    parent=styles["Heading2"],
    fontSize=12,
    leading=16,
    textColor=colors.HexColor("#35518a"),
    spaceBefore=12,
    spaceAfter=6,
    borderColor=colors.HexColor("#e9a8cc"),
    borderWidth=0,
))

styles.add(ParagraphStyle(
    name="IsiCV",
    parent=styles["BodyText"],
    fontSize=9,
    leading=14,
    textColor=colors.HexColor("#26334d"),
    spaceAfter=3
))

story = [
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
    Spacer(1, 10)
]

bagian = [
    ("Tentang Saya", "tentang"),
    ("Pendidikan", "pendidikan"),
    ("Pengalaman", "pengalaman"),
    ("Keterampilan", "keterampilan"),
    ("Sertifikat dan Pelatihan", "sertifikat")
]

for judul, kunci in bagian:
    story.append(
        Paragraph(escape(judul), styles["BagianCV"])
    )

    isi_pdf = escape(data[kunci]).replace("\n", "<br/>")
    story.append(
        Paragraph(isi_pdf, styles["IsiCV"])
    )

doc.build(story)
pdf_buffer.seek(0)

st.download_button(
    label="📥  Unduh CV dalam PDF",
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
