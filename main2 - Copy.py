import streamlit as st

st.title("Aplikasi Perhitungan Normalitas")

bobot = st.number_input('Masukan nilai bobot')
volume = st.number_input('Masukan nilai Volume')
be = st.number_input('Masukan nilai be')

tombol = st.button('Hitung Nilai Normalitas')

if tombol:
    nilai_normalitas = bobot/(be*volume)
    st.success(f'Nilai normalitas adalah {nilai_normalitas}')