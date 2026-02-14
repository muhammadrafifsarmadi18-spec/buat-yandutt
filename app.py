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
    Semangat KKNnya yandutt!!!
    Makasih Yandutt udah selalu nemenin aku dalam kondisi susah senang dalam kondisi apapunlah makasih juga udah selalu support aku dalam hal apapun itu sayang banget sama kamu akuuu. 
    Kamu itu penyemangat paling ampuh buat aku!
    """)
    
    # Menampilkan GIF romantis
   # Menampilkan gambar yang lebih stabil
   # Nama file harus sama dengan yang kamu upload tadi (TEST.jpeg)
    st.image("TEST.jpeg", caption="Happy Valentine, Yandutt Sayang! ❤️")
    st.success("I Love You So Much, Yandutt! ✨")
    st.snow() # Efek salju
else:
    st.write("<p style='text-align:center;'>Coba deh klik tombol di atas.</p>", unsafe_allow_html=True)
