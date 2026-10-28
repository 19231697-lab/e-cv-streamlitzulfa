
import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as PDFImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from io import BytesIO
from xml.sax.saxutils import escape

st.set_page_config(
    page_title="E-CV Zulfa Rizqi Saputri",
    page_icon="📄",
    layout="wide"
)

# Data CV yang langsung ditampilkan saat aplikasi dibuka
DATA_AWAL = {
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
    ),
    "foto": None
}

st.markdown("""
<style>
.stApp {
    background-color: #f4f6fb;
}
.main-title {
    text-align: center;
    color: #243b64;
    font-size: 36px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: #64748b;
    margin-bottom: 30px;
}
.cv-card {
    background-color: white;
    padding: 30px;
    border-radius: 15px;
    border: 1px solid #e2e8f0;
}
h3 {
    color: #243b64;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">E-CV ZULFA RIZQI SAPUTRI</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Curriculum Vitae Digital | Data Analyst</div>',
    unsafe_allow_html=True
)

# Isi data awal agar preview langsung muncul
if "cv_data" not in st.session_state:
    st.session_state["cv_data"] = DATA_AWAL.copy()

kolom_form, kolom_cv = st.columns([1, 1.2])

with kolom_form:
    st.subheader("📝 Edit Data CV")
    st.caption("Data sudah terisi. Kamu bisa mengubahnya lalu klik Buat / Perbarui CV.")

    data_awal = st.session_state["cv_data"]

    with st.form("form_cv"):
        st.markdown("### Data Pribadi")

        nama = st.text_input("Nama Lengkap", value=data_awal["nama"])
        posisi = st.text_input("Posisi atau Bidang yang Diminati", value=data_awal["posisi"])
        email = st.text_input("Email", value=data_awal["email"])
        telepon = st.text_input("Nomor Telepon", value=data_awal["telepon"])
        alamat = st.text_input("Domisili", value=data_awal["alamat"])
        tentang = st.text_area("Tentang Saya", value=data_awal["tentang"], height=120)

        foto = st.file_uploader(
            "Upload Foto Profil",
            type=["png", "jpg", "jpeg"]
        )

        st.markdown("### Pendidikan")
        pendidikan = st.text_area(
            "Riwayat Pendidikan",
            value=data_awal["pendidikan"],
            height=100
        )

        st.markdown("### Pengalaman")
        pengalaman = st.text_area(
            "Pengalaman Kerja, Magang, atau Organisasi",
            value=data_awal["pengalaman"],
            height=220
        )

        st.markdown("### Keterampilan")
        keterampilan = st.text_area(
            "Keterampilan",
            value=data_awal["keterampilan"],
            height=150
        )

        st.markdown("### Sertifikat")
        sertifikat = st.text_area(
            "Sertifikat atau Pelatihan",
            value=data_awal["sertifikat"],
            height=100
        )

        submit = st.form_submit_button(
            "✨ Buat / Perbarui CV",
            use_container_width=True
        )

if submit:
    foto_baru = (
        foto.getvalue()
        if foto
        else st.session_state["cv_data"].get("foto")
    )

    st.session_state["cv_data"] = {
        "nama": nama,
        "posisi": posisi,
        "email": email,
        "telepon": telepon,
        "alamat": alamat,
        "tentang": tentang,
        "pendidikan": pendidikan,
        "pengalaman": pengalaman,
        "keterampilan": keterampilan,
        "sertifikat": sertifikat,
        "foto": foto_baru
    }

with kolom_cv:
    st.subheader("👤 Preview E-CV")
    data = st.session_state["cv_data"]

    st.markdown('<div class="cv-card">', unsafe_allow_html=True)

    if data["foto"]:
        st.image(data["foto"], width=140)

    st.markdown(f"# {data['nama'] or 'Nama Lengkap'}")
    st.markdown(f"**{data['posisi'] or 'Posisi yang Diminati'}**")
    st.caption(f"📧 {data['email']} | 📱 {data['telepon']}")
    st.caption(f"📍 {data['alamat']}")
    st.divider()

    bagian = [
        ("Tentang Saya", "tentang"),
        ("Pendidikan", "pendidikan"),
        ("Pengalaman", "pengalaman"),
        ("Keterampilan", "keterampilan"),
        ("Sertifikat", "sertifikat")
    ]

    for judul, kunci in bagian:
        st.markdown(f"### {judul}")
        st.write(data[kunci] or "-")

    st.markdown('</div>', unsafe_allow_html=True)

    # Membuat CV PDF
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

    story = []

    if data["foto"]:
        try:
            foto_pdf = PDFImage(
                BytesIO(data["foto"]),
                width=80,
                height=80
            )
            foto_pdf.hAlign = "CENTER"
            story.extend([foto_pdf, Spacer(1, 10)])
        except Exception:
            pass

    story.append(Paragraph(
        escape(data["nama"] or "Nama Lengkap"),
        styles["NamaCV"]
    ))

    story.append(Paragraph(
        escape(data["posisi"] or "Posisi yang Diminati"),
        styles["Normal"]
    ))

    kontak = " | ".join(
        x for x in [data["email"], data["telepon"], data["alamat"]] if x
    )

    if kontak:
        story.extend([
            Spacer(1, 8),
            Paragraph(escape(kontak), styles["Normal"])
        ])

    for judul, kunci in bagian:
        isi = data[kunci]
        if isi.strip():
            story.append(Paragraph(escape(judul), styles["BagianCV"]))
            isi_pdf = escape(isi).replace("\n", "<br/>")
            story.append(Paragraph(isi_pdf, styles["Normal"]))

    doc.build(story)
    pdf_buffer.seek(0)

    st.download_button(
        label="📥 Unduh CV dalam PDF",
        data=pdf_buffer.getvalue(),
        file_name="CV_Zulfa_Rizqi_Saputri.pdf",
        mime="application/pdf",
        use_container_width=True
    )
