import streamlit as st

st.title("tralala")
st.write(
    "Love X-D."
)
st.image("views/450d080f-b15d-4a3f-afa0-10ca7d0552d8.jpeg", width=200)
st.write("\n")
st.subheader("Angelika")
st.write(
    "Mari kita lihat X-D"
)

#with col1 :
st.header ("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
