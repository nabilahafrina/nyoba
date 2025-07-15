import streamlit as st

# -------------------------------
# Tambahkan CSS untuk background
# -------------------------------
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1581093448796-8a04b3e1e997");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# ========================
# DATA MSDS
# ========================
msds_dict = {
    "HCl": {
        "nama": "Asam Klorida",
        "bahaya": "Korosif, mengiritasi saluran pernapasan.",
        "penanganan": "Gunakan APD lengkap, hindari kontak langsung.",
        "penyimpanan": "Di tempat berventilasi, jauh dari basa.",
        "p3k": "Bilas air mengalir jika terkena kulit. Segera cari bantuan medis."
    },
    "NaOH": {
        "nama": "Natrium Hidroksida",
        "bahaya": "Sangat korosif, merusak jaringan hidup.",
        "penanganan": "Gunakan sarung tangan dan pelindung mata.",
        "penyimpanan": "Simpan di tempat kering, jauh dari asam.",
        "p3k": "Cuci dengan air mengalir, segera ke fasilitas medis."
    },
    "Etanol": {
        "nama": "Etanol",
        "bahaya": "Mudah terbakar, dapat mengiritasi mata.",
        "penanganan": "Jauhkan dari panas dan api, ventilasi cukup.",
        "penyimpanan": "Wadah tertutup rapat, suhu ruang.",
        "p3k": "Jika terhirup, pindah ke udara segar. Jika kontak mata, bilas air."
    },
    "Aseton": {
        "nama": "Aseton",
        "bahaya": "Sangat mudah terbakar, menyebabkan iritasi.",
        "penanganan": "Gunakan pelindung mata dan ventilasi cukup.",
        "penyimpanan": "Tutup rapat, jauhkan dari panas dan api.",
        "p3k": "Jika terhirup, pindah ke tempat terbuka. Jika tertelan, jangan memaksakan muntah."
    },
    "H2SO4": {
        "nama": "Asam Sulfat",
        "bahaya": "Sangat korosif, merusak jaringan dan pakaian.",
        "penanganan": "Gunakan pelindung lengkap, hindari uap.",
        "penyimpanan": "Di tempat sejuk dan berventilasi.",
        "p3k": "Segera bilas kulit/mata dengan air, cari pertolongan medis."
    },
    "NH3": {
        "nama": "Amonia",
        "bahaya": "Gas beracun dan korosif.",
        "penanganan": "Gunakan pelindung pernapasan, hindari uap.",
        "penyimpanan": "Simpan dalam silinder tertutup di tempat sejuk.",
        "p3k": "Segera pindahkan korban ke udara segar, cari bantuan medis."
    },
    "Cl2": {
        "nama": "Klorin",
        "bahaya": "Gas beracun, mengiritasi saluran napas.",
        "penanganan": "Gunakan pelindung gas dan ventilasi cukup.",
        "penyimpanan": "Silinder tertutup rapat, jauh dari panas.",
        "p3k": "Pindahkan ke udara segar, bantu napas bila perlu."
    },
    "Methanol": {
        "nama": "Metanol",
        "bahaya": "Beracun, mudah terbakar.",
        "penanganan": "Gunakan sarung tangan dan pelindung mata.",
        "penyimpanan": "Simpan di tempat sejuk, jauh dari panas.",
        "p3k": "Jika tertelan, segera cari bantuan medis, jangan muntah."
    }
}

# ========================
# APLIKASI STREAMLIT
# ========================
st.set_page_config(page_title="Aplikasi MSDS", layout="centered")

# Sidebar Menu
menu = st.sidebar.radio("📌 Menu", ["🏠 Beranda", "📄 Lihat MSDS"])

# ========================
# BERANDA
# ========================
if menu == "🏠 Beranda":
    st.title("🧪 Aplikasi MSDS Bahan Kimia")
    st.image("https://cdn.pixabay.com/photo/2021/05/25/19/16/lab-6284844_1280.png", use_column_width=True)
    st.markdown("""
    ### Selamat Datang!
    Aplikasi ini membantu kamu mengetahui informasi dasar penanganan bahan kimia berdasarkan MSDS (Material Safety Data Sheet).

    **Gunakan menu di sebelah kiri** untuk:
    - 📄 Melihat informasi bahan kimia
    - 🛟 Mengetahui bahaya, cara penanganan, penyimpanan, dan pertolongan pertama

    ---  
    🔬 Cocok untuk siswa, mahasiswa, guru, dan laboran!
    """)

# ========================
# MENU LIHAT MSDS
# ========================
elif menu == "📄 Lihat MSDS":
    st.title("📄 Lihat MSDS Bahan Kimia")
    bahan = st.selectbox("Pilih bahan kimia:", list(msds_dict.keys()))

    if bahan:
        data = msds_dict[bahan]
        st.subheader(f"Informasi MSDS untuk {bahan}")
        st.markdown(f"**Nama Bahan:** {data['nama']}")
        st.markdown(f"**Bahaya:** {data['bahaya']}")
        st.markdown(f"**Penanganan:** {data['penanganan']}")
        st.markdown(f"**Penyimpanan:** {data['penyimpanan']}")
        st.markdown(f"**Pertolongan Pertama (P3K):** {data['p3k']}")
