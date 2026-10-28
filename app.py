
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
    page_icon="📄",
    layout="centered"
)

# Data CV
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

st.markdown("""
<style>
.stApp {
    background-color: #f4f6fb;
}
.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.cv-card {
    background-color: white;
    padding: 30px;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
}
.cv-title {
    text-align: center;
    color: #243b64;
    font-size: 34px;
    font-weight: bold;
}
.cv-subtitle {
    text-align: center;
    color: #64748b;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="cv-title">CURRICULUM VITAE</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="cv-subtitle">E-CV | Data Analyst</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="cv-card">', unsafe_allow_html=True)

st.title(data["nama"])
st.subheader(data["posisi"])
st.caption(
    f"📧 {data['email']}  |  📱 {data['telepon']}  |  📍 {data['alamat']}"
)

st.divider()

st.markdown("### Tentang Saya")
st.write(data["tentang"])

st.markdown("### Pendidikan")
st.text(data["pendidikan"])

st.markdown("### Pengalaman")
st.text(data["pengalaman"])

st.markdown("### Keterampilan")
st.text(data["keterampilan"])

st.markdown("### Sertifikat dan Pelatihan")
st.text(data["sertifikat"])

st.markdown('</div>', unsafe_allow_html=True)

# Membuat file PDF CV
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
    fontSize=22,
    textColor=colors.HexColor("#243b64"),
    alignment=TA_CENTER,
    spaceAfter=8
))

styles.add(ParagraphStyle(
    name="BagianCV",
    parent=styles["Heading2"],
    fontSize=13,
    textColor=colors.HexColor("#243b64"),
    spaceBefore=12,
    spaceAfter=6
))

styles.add(ParagraphStyle(
    name="IsiCV",
    parent=styles["BodyText"],
    fontSize=9,
    leading=14,
    spaceAfter=3
))

story = [
    Paragraph(escape(data["nama"]), styles["NamaCV"]),
    Paragraph(escape(data["posisi"]), styles["Normal"]),
    Spacer(1, 8),
    Paragraph(
        escape(" | ".join([
            data["email"], data["telepon"], data["alamat"]
        ])),
        styles["Normal"]
    ),
    Spacer(1, 12)
]

bagian = [
    ("Tentang Saya", "tentang"),
    ("Pendidikan", "pendidikan"),
    ("Pengalaman", "pengalaman"),
    ("Keterampilan", "keterampilan"),
    ("Sertifikat dan Pelatihan", "sertifikat")
]

for judul, kunci in bagian:
    story.append(Paragraph(escape(judul), styles["BagianCV"]))
    isi_pdf = escape(data[kunci]).replace("\n", "<br/>")
    story.append(Paragraph(isi_pdf, styles["IsiCV"]))

doc.build(story)
pdf_buffer.seek(0)

st.download_button(
    label="📥 Unduh CV dalam PDF",
    data=pdf_buffer.getvalue(),
    file_name="CV_Zulfa_Rizqi_Saputri.pdf",
    mime="application/pdf",
    use_container_width=True
)
