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
    Semangat terus ya kuliahnya! 
    Makasih Yandutt udah selalu nemenin aku ngerjain tugas-tugas Elektromedis. 
    Kamu itu penyemangat paling ampuh buat aku!
    """)
    
    # Menampilkan GIF romantis
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHpueG56Znd6Z3Z6Z3Z6Z3Z6Z3Z6Z3Z6Z3Z6Z3Z6Z3Z6Jm09MSZ0PXNf/KzOey77L_K6Be/giphy.gif")
    
    st.success("I Love You So Much, Yandutt! ✨")
    st.snow() # Efek salju
else:
    st.write("<p style='text-align:center;'>Coba deh klik tombol di atas.</p>", unsafe_allow_html=True)
