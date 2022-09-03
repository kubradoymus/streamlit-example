import streamlit as st
st.header("ürünler")
from functions import *
with st.expander("ürün ekle"):
    with st.form("ürünekle",clear_on_submit=True):
        isim=st.text_input("ürün ekle")
        model=st.selectbox("model sec",listele('modeller'))
        model=str(model)
        fiyat=st.number_input("fiyat giriniz")
        submitted=st.form_submit_button("ürün ekle")
        if submitted:
            urunekle(isim,model,fiyat)
tabloyap("urunler", ["isim","model","fiyat"])

