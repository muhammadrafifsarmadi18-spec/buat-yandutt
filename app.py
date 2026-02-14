import streamlit as st

# Pengaturan halaman untuk iPhone
st.set_page_config(page_title="Happy Valentine Yandutt ❤️", page_icon="💖")

# Tampilan judul
st.markdown("<h1 style='text-align: center; color: #ff4d6d;'>Haii Yandutt Sayang! ❤️</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Ada pesan spesial buat kamu hari ini...</p>", unsafe_allow_html=True)

# Tombol interaktif
if st.button('Klik di sini, Yandutt!'):
    st.balloons() # Efek balon
    st.header("Happy Valentine's Day! 🌹")
    
    st.info("""
    Yandutku yang lagi berjuang di KKN 🤍

Aku tau sekarang kamu lagi capek-capeknya. Bangun pagi, kegiatan ini itu, adaptasi sama orang baru, belum lagi jauh dari rumah… dan jauh dari aku.

Tapi kamu harus tau satu hal,
sejauh apa pun kamu pergi buat ngejar tanggung jawabmu, hatiku tetap ikut kamu.

Aku bangga banget sama kamu, Yandut.
Liat kamu berusaha, belajar mandiri, ketemu banyak pengalaman baru… itu bikin aku makin yakin kalau aku nggak salah milih kamu.

Kalau nanti kamu capek, cerita ya.
Kalau kamu sedih, jangan dipendem sendiri.
Kalau kamu ngerasa sendirian di sana, inget… ada aku yang selalu nunggu kamu pulang dengan senyum paling tulus.

KKN itu cuma sementara,
tapi rasa sayang aku ke kamu nggak ada tanggal selesainya.

Jaga diri baik-baik ya di sana.
Jangan lupa makan, jangan begadang mulu, dan jangan lupa… kamu punya aku yang selalu doain kamu tiap hari 🤍

Aku kangen, Yandut.
Cepet pulang, biar aku bisa lihat senyum kamu langsung, bukan cuma lewat layar.
    """)
    
    # Menampilkan GIF romantis
   # Menampilkan gambar yang lebih stabil
   # Nama file harus sama dengan yang kamu upload tadi (TEST.jpeg)
    st.image("TEST.jpeg", caption="Happy Valentine, Yandutt Sayang! ❤️")
    st.success("I Love You So Much, Yandutt! ✨")
    st.snow() # Efek salju
else:
    st.write("<p style='text-align:center;'>Coba deh klik tombol di atas.</p>", unsafe_allow_html=True)
