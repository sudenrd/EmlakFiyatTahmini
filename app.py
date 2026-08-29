import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


df = pd.read_excel("data.xlsx")
X = df.drop("FIYAT", axis=1)
y = df["FIYAT"]

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X, y)
st.title("Yapay Zeka Ev Fiyatı Tahmini")
st.write("Lütfen fiyatını öğrenmek istediğiniz evin özelliklerini girin:")

m2 = st.number_input("Metrekare (M2)", min_value=10, value=100)
oda = st.number_input("Oda Sayısı", min_value=1, value=3)
yas = st.number_input("Bina Yaşı", min_value=0, value=5)
kat = st.number_input("Bulunduğu Kat", value=2)

col1, col2 = st.columns(2)
with col1:
    site = st.selectbox("Site İçinde mi?", ["Hayır (0)", "Evet (1)"])
    asansor = st.selectbox("Asansör Var mı?", ["Hayır (0)", "Evet (1)"])
with col2:
    esya = st.selectbox("Eşyalı mı?", ["Hayır (0)", "Evet (1)"])
    otopark = st.selectbox("Otopark Var mı?", ["Hayır (0)", "Evet (1)"])

konum = st.slider("Konum Puanı", 0.0, 5.0, 10.0)

if st.button("Fiyatı Tahmin Et 🚀"):
    site_val = 1 if "Evet" in site else 0
    asansor_val = 1 if "Evet" in asansor else 0
    esya_val = 1 if "Evet" in esya else 0
    otopark_val = 1 if "Evet" in otopark else 0
    
    yeni_ev = pd.DataFrame([{
        "M2": m2, "ODA": oda, "YAS": yas, "KAT": kat, 
        "SITE": site_val, "ASANSOR": asansor_val, 
        "ESYA": esya_val, "OTOPARK": otopark_val, "KONUM": konum
    }])
    
    tahmin = model.predict(yeni_ev)
    st.success(f"Tahmini Ev Fiyatı: {tahmin[0]:,.0f} TL")