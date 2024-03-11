import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Veri setini yükleyelim ve bir DataFrame'e dönüştürelim:
python
Copy code
df = pd.read_csv('Medical_examination.csv')
#overweight sütununu ekleyelim:
python
Copy code
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)
#cholesterol ve gluc değerlerini normalleştirelim:
python
Copy code
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)
#Verileri temizleyelim:
python
Copy code
df = df[(df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]
#Kategorik özelliklerin değer sayılarını gösteren bir catplot oluşturalım
python
Copy code
catplot = sns.catplot(data=df, kind='count', x='cholesterol', hue='gluc', col='smoke', row='alco', aspect=1.5)
plt.show()
#Korelasyon matrisini oluşturalım ve heatmap ile görselleştirelim:
python
Copy code
corr = df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', mask=mask, square=True, linewidths=0.5)
plt.show()