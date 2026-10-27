import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image as PDFImage
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from io import BytesIO

st.set_page_config(
    page_title="E-CV Generator",
    page_icon="📄",
    layout="wide"
)

# CSS tampilan
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
    '<div class="main-title">E-CV GENERATOR</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Buat CV digital profesional dengan mudah</div>',
    unsafe_allow_html=True
)

# Membagi halaman menjadi dua kolom
kolom_form, kolom_cv = st.columns([1, 1.2])

with kolom_form:
    st.subheader("📝 Isi Data CV")

    with st.form("form_cv"):

        st.markdown("### Data Pribadi")

        nama = st.text_input("Nama Lengkap")
        posisi = st.text_input(
            "Posisi atau Bidang yang Diminati",
            placeholder="Contoh: Web Developer"
        )

        email = st.text_input("Email")
        telepon = st.text_input("Nomor Telepon")
        alamat = st.text_input("Domisili")

        tentang = st.text_area(
            "Tentang Saya",
            placeholder="Tuliskan deskripsi singkat tentang diri kamu..."
        )

        foto = st.file_uploader(
            "Upload Foto Profil",
            type=["png", "jpg", "jpeg"]
        )

        st.markdown("### Pendidikan")

        pendidikan = st.text_area(
            "Riwayat Pendidikan",
            placeholder="Contoh: S1 Sistem Informasi - Universitas XYZ"
        )

        st.markdown("### Pengalaman")

        pengalaman = st.text_area(
            "Pengalaman Kerja, Magang, atau Organisasi",
            placeholder="Tuliskan pengalaman dan tanggung jawab kamu..."
        )

        st.markdown("### Keterampilan")

        keterampilan = st.text_area(
            "Keterampilan",
            placeholder="Contoh: Python, HTML, CSS, Laravel"
        )

        st.markdown("### Sertifikat")

        sertifikat = st.text_area(
            "Sertifikat atau Pelatihan",
            placeholder="Tuliskan sertifikat yang kamu miliki..."
        )

        submit = st.form_submit_button(
            "✨ Buat CV",
            use_container_width=True
        )

# Menampilkan CV setelah tombol ditekan
if submit:
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
        "foto": foto.getvalue() if foto else None
    }

with kolom_cv:
    st.subheader("👤 Preview E-CV")

    if "cv_data" not in st.session_state:
        st.info(
            "Isi formulir di sebelah kiri, "
            "kemudian klik tombol Buat CV."
        )

    else:
        data = st.session_state["cv_data"]

        st.markdown('<div class="cv-card">', unsafe_allow_html=True)

        if data["foto"]:
            st.image(
                data["foto"],
                width=140
            )

        st.markdown(f"# {data['nama'] or 'Nama Lengkap'}")

        st.markdown(
            f"**{data['posisi'] or 'Posisi yang Diminati'}**"
        )

        st.caption(
            f"📧 {data['email']}  |  "
            f"📱 {data['telepon']}"
        )

        st.caption(f"📍 {data['alamat']}")

        st.divider()

        st.markdown("### Tentang Saya")
        st.write(data["tentang"] or "-")

        st.markdown("### Pendidikan")
        st.write(data["pendidikan"] or "-")

        st.markdown("### Pengalaman")
        st.write(data["pengalaman"] or "-")

        st.markdown("### Keterampilan")
        st.write(data["keterampilan"] or "-")

        st.markdown("### Sertifikat")
        st.write(data["sertifikat"] or "-")

        st.markdown('</div>', unsafe_allow_html=True)

        # Membuat PDF
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

        # Foto profil PDF
        if data["foto"]:
            try:
                foto_pdf = PDFImage(
                    BytesIO(data["foto"]),
                    width=80,
                    height=80
                )
                foto_pdf.hAlign = "CENTER"
                story.append(foto_pdf)
                story.append(Spacer(1, 10))
            except Exception:
                pass

        story.append(Paragraph(
            data["nama"] or "Nama Lengkap",
            styles["NamaCV"]
        ))

        story.append(Paragraph(
            data["posisi"] or "Posisi yang Diminati",
            styles["Normal"]
        ))

        kontak = " | ".join(
            x for x in [
                data["email"],
                data["telepon"],
                data["alamat"]
            ] if x
        )

        if kontak:
            story.append(Spacer(1, 8))
            story.append(Paragraph(kontak, styles["Normal"]))

        bagian = [
            ("Tentang Saya", "tentang"),
            ("Pendidikan", "pendidikan"),
            ("Pengalaman", "pengalaman"),
            ("Keterampilan", "keterampilan"),
            ("Sertifikat", "sertifikat")
        ]

        for judul, kunci in bagian:
            isi = data[kunci]

            if isi.strip():
                story.append(
                    Paragraph(judul, styles["BagianCV"])
                )

                isi_pdf = (
                    isi.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace("\n", "<br/>")
                )

                story.append(
                    Paragraph(isi_pdf, styles["Normal"])
                )

        doc.build(story)

        pdf_buffer.seek(0)

        st.download_button(
            label="📥 Unduh CV dalam PDF",
            data=pdf_buffer.getvalue(),
            file_name="CV_Saya.pdf",
            mime="application/pdf",
            use_container_width=True
        )
