import streamlit as st
st.header("Ana Sayfa")
import datetime
from functions import *
st.subheader("Günün Randevuları")   #altbaslık
gununrandevu()


#direkt hesap yapıyor.
#tarih=st.date_input("tarih gir")
#kubra=datetime.date(2022,8,28)
#st.write(kubra-tarih)
#sırada randevu tablosu yap.
