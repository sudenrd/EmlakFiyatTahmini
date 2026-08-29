# 🏡 Emlak Fiyat Tahmini Modeli

Bu proje, çeşitli ev özelliklerini baz alarak makine öğrenmesi teknikleriyle ev fiyatlarını tahmin eden interaktif bir web uygulamasıdır. Etkileşimli kullanıcı arayüzü **Streamlit** ile tasarlanmış olup, tahminleme algoritması olarak **Random Forest Regressor** kullanılmıştır.

## 🧠 Model ve Algoritma (Random Forest) Detayları
Projenin temelinde, çok sayıda karar ağacının bir araya gelmesiyle oluşan ensemble tabanlı **Random Forest** algoritması yer almaktadır. Bu algoritmanın seçilme amacı, aşırı öğrenmeyi engellemesi ve doğrusal olmayan emlak verilerinde yüksek başarı oranı sunmasıdır.

* **Model Eğitimi:** `scikit-learn` kütüphanesindeki `RandomForestRegressor` (n_estimators=200) kullanılarak 200 farklı karar ağacı ile model eğitilmiştir.
* **Veri İşleme:** Pandas ile veri setinin okunması, bağımlı (Fiyat) ve bağımsız (M2, Oda, Yaş, Konum vb.) değişkenlerin ayrıştırılması sağlanmıştır.
* **Özellik Önemi (Feature Importance):** Model, evin fiyatını belirlerken hangi özelliklerin (örneğin konum puanı veya metrekare) daha etkili olduğunu matematiksel olarak analiz edebilecek yapıdadır.

## 🚀 Kullanılan Teknolojiler
* **Python**
* **Scikit-Learn** (Makine Öğrenmesi)
* **Pandas** (Veri Manipülasyonu ve Analizi)
* **Streamlit** (Web Arayüzü Geliştirme)

## ⚙️ Kurulum ve Çalıştırma
Projeyi kendi bilgisayarınızda denemek için:
1. Gerekli kütüphaneleri kurun: 
`pip install -r requirements.txt`
2. Uygulamayı başlatın: 
`streamlit run app.py`
