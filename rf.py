import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_excel("data.xlsx")

X = df.drop("FIYAT", axis=1)
y = df["FIYAT"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Başarı Sonuçları")
print("----------------------")
print(f"MAE (Ortalama Hata): {mae:,.2f}")
print(f"R2 Score: {r2:.4f}")

importance_df = pd.DataFrame({
    "Ozellik": X.columns,
    "Onem_Degeri": model.feature_importances_
})

importance_df = importance_df.sort_values(
    by="Onem_Degeri",
    ascending=False
)

print("\nOzellik Onem Siralamasi")
print("----------------------")
print(importance_df)


print("\nYeni Ev Bilgilerini Gir")

m2 = float(input("M2: "))
oda = int(input("ODA sayisi: "))
yas = int(input("Bina yasi: "))
kat = int(input("Kat: "))
site = int(input("Site icinde mi? (1=Evet, 0=Hayir): "))
asansor = int(input("Asansor var mi? (1=Evet, 0=Hayir): "))
esya = int(input("Esya dahil mi? (1=Evet, 0=Hayir): "))
otopark = int(input("Otopark var mi? (1=Evet, 0=Hayir): "))
konum = float(input("Konum puani: "))

yeni_ev = pd.DataFrame([{
    "M2": m2,
    "ODA": oda,
    "YAS": yas,
    "KAT": kat,
    "SITE": site,
    "ASANSOR": asansor,
    "ESYA": esya,
    "OTOPARK": otopark,
    "KONUM": konum
}])

tahmin = model.predict(yeni_ev)

print("\nTahmini Ev Fiyati:")
print(f"{tahmin[0]:,.0f} TL")