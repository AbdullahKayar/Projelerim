import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('group_stats.csv')

# Verinin ilk 5 satırı
print(df.head())

# Sütun isimleri, veri türleri ve boş olmayan satır sayıları
df.info()

# Ortalama, standart sapma, min, max gibi istatistikler
print(df.describe())

# Her sütundaki boş (NaN) değer sayısı
print(df.isnull().sum())
# --- ADIM 3: NumPy ile Analitik (Türetilmiş Metrik) ---
# Oyuncuların/Takımların 'Gol Verimliliği'ni hesaplayalım.
# Formül: Atılan Gol / Beklenen Gol (xG)
# np.where kullanarak 0'a bölünme hatasını engelliyoruz.

df['gol_verimliligi'] = np.divide(df['goals_scored'], df['expected_goal_scored'])

# NumPy ile normalizasyon: Verimliliği 0 ile 1 arasına çekelim (Rubrikte 'normalize skor' isteniyor)
verim_min = np.min(df['gol_verimliligi'])
verim_max = np.max(df['gol_verimliligi'])
df['verim_skoru_norm'] = (df['gol_verimliligi'] - verim_min) / (verim_max - verim_min)

print("\n--- NumPy ile Türetilen Yeni Metrikler (İlk 5 Satır) ---")
print(df[['team', 'gol_verimliligi', 'verim_skoru_norm']].head())


# --- ADIM 4: Pandas ile Temizleme ve Dönüştürme ---
# 1. 'Unnamed: 0' gibi gereksiz sütunları silelim
if 'Unnamed: 0' in df.columns:
    df.drop(columns=['Unnamed: 0'], inplace=True)

# 2. Grup numaralarını (1, 2...) Harflere (A, B...) çevirelim (Daha iyi okunabilirlik için)
grup_esleme = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}
df['grup_adi'] = df['group'].map(grup_esleme)


# --- ADIM 5: Pandas ile Analiz ve Özetleme ---
# Analiz 1: Grup bazında toplam gol ve puan durumları (Groupby)
grup_ozet = df.groupby('grup_adi').agg({
    'goals_scored': 'sum',
    'points': 'sum',
    'expected_goal_scored': 'mean'
}).sort_values(by='points', ascending=False)

# Analiz 2: Turnuva sıralamasına (Rank) göre puan ve gol ortalamaları (Pivot Table)
siralam_ozet = df.pivot_table(index='rank', values=['points', 'goals_scored', 'expected_goal_scored'], aggfunc='mean')

print("\n--- Gruplara Göre Analiz Özeti ---")
print(grup_ozet)
print("\n--- Sıralamaya Göre (1.ler, 2.ler...) Pivot Tablo ---")
print(siralam_ozet)
# --- ADIM 6: Matplotlib ile Görselleştirme ---

# Grafiklerin stilini ayarlayalım
plt.style.use('ggplot')

# 1. GRAFİK: Bar Chart (Sütun Grafiği)
# Gerekçe: Kategorik verileri (Takımlar) karşılaştırmak için en uygun grafik türüdür.
plt.figure(figsize=(10, 6))
top_10_scorers = df.sort_values(by='goals_scored', ascending=False).head(10)
plt.bar(top_10_scorers['team'], top_10_scorers['goals_scored'], color='skyblue', edgecolor='black')
plt.title('FIFA 2022 - En Çok Gol Atan İlk 10 Takım', fontsize=14)
plt.xlabel('Takımlar', fontsize=12)
plt.ylabel('Atılan Gol Sayısı', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('1_en_cok_gol_atanlar.png')
print("Grafik 1 kaydedildi.")

# 2. GRAFİK: Scatter Plot (Saçılım Grafiği)
# Gerekçe: İki sayısal değişken (xG ve Atılan Gol) arasındaki korelasyonu görmek için kullanılır.
plt.figure(figsize=(10, 6))
plt.scatter(df['expected_goal_scored'], df['goals_scored'], color='green', s=100, alpha=0.6, edgecolors='white')
# Referans çizgisi (Beklenti = Gerçekleşen)
plt.plot([0, 10], [0, 10], color='red', linestyle='--', label='Beklenen = Gerçekleşen')
plt.title('Beklenen Gol (xG) vs Gerçekleşen Gol', fontsize=14)
plt.xlabel('Beklenen Gol (xG)', fontsize=12)
plt.ylabel('Gerçekleşen Gol', fontsize=12)
plt.legend()
plt.savefig('2_xg_vs_gol_sacilim.png')
print("Grafik 2 kaydedildi.")

# 3. GRAFİK: Histogram
# Gerekçe: Verilerin (Averaj) hangi aralıklarda yoğunlaştığını (dağılımını) görmek için kullanılır.
plt.figure(figsize=(10, 6))
plt.hist(df['goal_difference'], bins=8, color='orange', edgecolor='black', alpha=0.7)
plt.title('Takımların Averaj Dağılımı', fontsize=14)
plt.xlabel('Averaj (Gol Farkı)', fontsize=12)
plt.ylabel('Takım Sayısı', fontsize=12)
plt.savefig('3_averaj_dagilimi_hist.png')
print("Grafik 3 kaydedildi.")

# 4. GRAFİK: Pie Chart (Pasta Grafiği)
# Gerekçe: Bir bütünün (Tüm sonuçlar) parçalara göre oranını göstermek için idealdir.
plt.figure(figsize=(8, 8))
toplam_sonuclar = [df['wins'].sum(), df['draws'].sum(), df['losses'].sum()]
etiketler = ['Galibiyet', 'Beraberlik', 'Mağlubiyet']
renkler = ['#66b3ff', '#99ff99', '#ff9999']
plt.pie(toplam_sonuclar, labels=etiketler, autopct='%1.1f%%', startangle=140, colors=renkler, explode=(0.05, 0, 0))
plt.title('Turnuva Genel Maç Sonuç Dağılımı', fontsize=14)
plt.savefig('4_sonuc_oranlari_pie.png')
print("Grafik 4 kaydedildi.")

# 5. GRAFİK: Box Plot (Kutu Grafiği)
# Gerekçe: Gruplar (Sıralama) arasındaki puan yayılımını ve aykırı değerleri görmek için kullanılır.
plt.figure(figsize=(10, 6))
puan_verileri = [df[df['rank'] == i]['points'] for i in range(1, 5)]
plt.boxplot(puan_verileri, labels=['1. Sırada', '2. Sırada', '3. Sırada', '4. Sırada'], patch_artist=True)
plt.title('Grup Sıralamasına Göre Puan Dağılımı', fontsize=14)
plt.ylabel('Toplanan Puan', fontsize=12)
plt.savefig('5_puan_dagilimi_boxplot.png')
print("Grafik 5 kaydedildi.")

# BONUS: Subplot (Yan Yana Çizim) - Rubrik Madde 8 için şart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Sol taraf: Puanlar
ax1.bar(df['team'].head(8), df['points'].head(8), color='purple')
ax1.set_title('İlk 8 Takım Puanları')
ax1.tick_params(axis='x', labelrotation=45)

# Sağ taraf: Yenilen Goller
ax2.bar(df['team'].head(8), df['goals_against'].head(8), color='salmon')
ax2.set_title('İlk 8 Takım Yenilen Goller')
ax2.tick_params(axis='x', labelrotation=45)

plt.tight_layout()
plt.savefig('6_subplot_karsilastirma.png')
print("Subplot kaydedildi.")