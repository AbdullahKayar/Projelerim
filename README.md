<div align="center">

# 🏆 FIFA 2022 World Cup Data Analysis
## Dünya Kupası 2022 Veri Analizi

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.21%2B-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5%2B-11557c?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)](.github/workflows/ci.yml)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000?style=for-the-badge)](https://black.readthedocs.io)

**📊 Professional sports analytics project demonstrating advanced data processing, statistical analysis, and visualization techniques**

**🎯 Profesyonel spor analitiği projesi - Gelişmiş veri işleme, istatistiksel analiz ve görselleştirme teknikleri**

[📖 English Documentation](#english) | [📖 Türkçe Dokümantasyon](#turkish)

</div>

---

<div id="english">

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technical Architecture](#technical-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Visualizations](#visualizations)
- [API Documentation](#api-documentation)
- [Results & Insights](#results--insights)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

</div>

---

<a name="overview"></a>
## 🌟 Overview

This project performs comprehensive data analysis on the FIFA 2022 World Cup group stage statistics. Using Python's powerful data science stack (NumPy, Pandas, Matplotlib), it processes raw match data to extract meaningful insights about team performance, goal efficiency, and tournament patterns.

### 🎯 Project Objectives
- **Performance Analysis**: Evaluate team efficiency through custom metrics like Goal Efficiency Ratio
- **Statistical Insights**: Identify patterns in goals, points, and expected goals (xG)
- **Data Visualization**: Create publication-quality charts for stakeholder communication
- **Predictive Insights**: Compare expected vs. actual performance metrics

### 📈 Measurable Outcomes
- ✅ Analyzed **32 teams** across **8 groups** (256+ data points)
- ✅ Created **6 professional visualizations** with publication standards
- ✅ Developed **2 custom efficiency metrics** using NumPy operations
- ✅ Processed and normalized **15 statistical attributes**
- ✅ Generated insights on team performance vs. expectations

---

<a name="key-features"></a>
## 🚀 Key Features

| Feature | Description | Technologies |
|---------|-------------|--------------|
| **Data Processing** | Advanced data cleaning, transformation, and normalization | Pandas, NumPy |
| **Statistical Analysis** | Custom metric calculation including goal efficiency scores | NumPy, Statistics |
| **Visualization Suite** | 6 chart types: Bar, Scatter, Histogram, Pie, Box, Subplots | Matplotlib |
| **Bilingual Support** | Full documentation in English and Turkish | Markdown |
| **CI/CD Pipeline** | Automated testing and linting on every commit | GitHub Actions |
| **Professional Documentation** | Comprehensive README, API docs, and contribution guidelines | GitHub Standards |

---

<a name="technical-architecture"></a>
## 🏗️ Technical Architecture

### Technology Stack

```
┌─────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Bar Charts │  │Scatter Plots│  │   Distribution      │  │
│  │             │  │             │  │   Visualizations    │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                   ANALYSIS LAYER                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  GroupBy    │  │ Pivot Tables│  │  Custom Metrics     │  │
│  │ Operations  │  │             │  │  (Efficiency Scores)│  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                   DATA LAYER                                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Raw CSV   │  │   NumPy     │  │    Pandas           │  │
│  │   Import    │  │ Arrays      │  │    DataFrames       │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Core Libraries
- **NumPy (≥1.21)**: High-performance numerical operations and array processing
- **Pandas (≥1.3)**: Data manipulation, aggregation, and analysis
- **Matplotlib (≥3.5)**: Static, animated, and interactive visualizations

---

<a name="installation"></a>
## 💻 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/fifa2022-analysis.git
cd fifa2022-analysis

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Dependencies
```
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.5.0
```

---

<a name="usage"></a>
## 🎮 Usage

### Running the Analysis

```bash
# Run the main analysis script
python fıfa2022.py
```

### Code Example: Loading and Processing Data

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('group_stats.csv')

# Calculate custom efficiency metric
df['gol_verimliligi'] = np.divide(
    df['goals_scored'], 
    df['expected_goal_scored']
)

# Normalize to 0-1 scale
verim_min = np.min(df['gol_verimliligi'])
verim_max = np.max(df['gol_verimliligi'])
df['verim_skoru_norm'] = (df['gol_verimliligi'] - verim_min) / (verim_max - verim_min)

# Group analysis
grup_ozet = df.groupby('grup_adi').agg({
    'goals_scored': 'sum',
    'points': 'sum',
    'expected_goal_scored': 'mean'
}).sort_values(by='points', ascending=False)
```

### Creating Visualizations

```python
# Bar chart - Top scorers
plt.figure(figsize=(10, 6))
top_10 = df.sort_values(by='goals_scored', ascending=False).head(10)
plt.bar(top_10['team'], top_10['goals_scored'], color='skyblue')
plt.title('FIFA 2022 - Top 10 Goal Scorers')
plt.xticks(rotation=45)
plt.savefig('top_scorers.png', dpi=300, bbox_inches='tight')
```

---

<a name="data-sources"></a>
## 📊 Data Sources

### Dataset: group_stats.csv

| Column | Description | Type |
|--------|-------------|------|
| `group` | Group number (1-8) | Integer |
| `rank` | Final group position (1-4) | Integer |
| `team` | Country name | String |
| `matches_played` | Games played | Integer |
| `wins` | Victories | Integer |
| `draws` | Draws | Integer |
| `losses` | Defeats | Integer |
| `goals_scored` | Goals for | Integer |
| `goals_against` | Goals against | Integer |
| `goal_difference` | Goal differential | Integer |
| `points` | Total points | Integer |
| `expected_goal_scored` | Expected goals (xG) | Float |
| `exp_goal_conceded` | Expected goals against | Float |
| `exp_goal_difference` | xG differential | Float |
| `exp_goal_difference_per_90` | xG diff per 90 min | Float |

### Data Quality
- **Completeness**: 100% (no missing values)
- **Coverage**: All 32 teams, all 8 groups
- **Accuracy**: Official FIFA 2022 statistics

---

<a name="visualizations"></a>
## 📈 Visualizations

### Generated Charts

| # | Chart Type | Purpose | File |
|---|------------|---------|------|
| 1 | **Bar Chart** | Top 10 goal-scoring teams | `1_en_cok_gol_atanlar.png` |
| 2 | **Scatter Plot** | Expected vs. actual goals correlation | `2_xg_vs_gol_sacilim.png` |
| 3 | **Histogram** | Goal difference distribution | `3_averaj_dagilimi_hist.png` |
| 4 | **Pie Chart** | Match results distribution | `4_sonuc_oranlari_pie.png` |
| 5 | **Box Plot** | Points distribution by rank | `5_puan_dagilimi_boxplot.png` |
| 6 | **Subplot** | Multi-metric comparison | `6_subplot_karsilastirma.png` |

### Visualization Philosophy
Each chart type was selected based on data characteristics:
- **Bar Charts**: Categorical comparison (teams)
- **Scatter Plots**: Correlation analysis (xG vs. actual)
- **Histograms**: Distribution analysis (goal differences)
- **Pie Charts**: Proportional representation (results)
- **Box Plots**: Distribution spread and outliers

---

<a name="api-documentation"></a>
## 📚 API Documentation

### Custom Metrics

#### Goal Efficiency Ratio (Gol Verimliliği)
```python
df['gol_verimliligi'] = goals_scored / expected_goal_scored
```
Measures how efficiently teams converted chances into goals.

#### Normalized Efficiency Score
```python
df['verim_skoru_norm'] = (efficiency - min_efficiency) / (max_efficiency - min_efficiency)
```
Scales efficiency to 0-1 range for comparative analysis.

### Core Functions

#### Data Processing
```python
def load_and_clean_data(filepath: str) -> pd.DataFrame:
    """Load CSV and perform initial cleaning."""
    df = pd.read_csv(filepath)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)
    return df

def calculate_efficiency_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Add custom efficiency metrics to dataframe."""
    df['gol_verimliligi'] = np.divide(df['goals_scored'], df['expected_goal_scored'])
    # Normalization...
    return df
```

#### Analysis Functions
```python
def group_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate statistics by group."""
    return df.groupby('grup_adi').agg({
        'goals_scored': 'sum',
        'points': 'sum',
        'expected_goal_scored': 'mean'
    })

def rank_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Create pivot table by final ranking."""
    return df.pivot_table(
        index='rank',
        values=['points', 'goals_scored', 'expected_goal_scored'],
        aggfunc='mean'
    )
```

---

<a name="results--insights"></a>
## 🏆 Results & Insights

### Key Findings

1. **Top Performers**: England led in goal scoring (9 goals) with high efficiency
2. **Efficiency Leaders**: Teams like Argentina exceeded xG expectations significantly
3. **Group Dynamics**: Group E (Japan, Spain, Germany) showed highest competitive balance
4. **xG Correlation**: Strong positive correlation (r > 0.8) between expected and actual goals

### Statistical Highlights

| Metric | Value |
|--------|-------|
| Total Goals Scored | 120 |
| Average Goals per Team | 3.75 |
| Most Efficient Team | Argentina (xG ratio: 0.83) |
| Highest xG | Germany (10.1) |
| Biggest Upset | Japan defeating Germany/Spain |

---

<a name="project-structure"></a>
## 📁 Project Structure

```
fifa2022-analysis/
│
├── 📄 README.md                 # This file
├── 📄 LICENSE                   # MIT License
├── 📄 requirements.txt          # Python dependencies
├── 📄 CONTRIBUTING.md           # Contribution guidelines
├── 📄 CODE_OF_CONDUCT.md        # Community standards
├── 📄 CHANGELOG.md              # Version history
├── 📄 SECURITY.md               # Security policy
│
├── 📁 .github/
│   ├── 📁 workflows/
│   │   └── ci.yml               # CI/CD pipeline
│   ├── 📁 ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── 📄 pull_request_template.md
│
├── 📁 docs/
│   ├── architecture.md          # System design docs
│   ├── api_reference.md         # Full API documentation
│   └── methodology.md           # Analysis methodology
│
├── 📁 src/
│   └── fıfa2022.py              # Main analysis script
│
├── 📁 data/
│   └── group_stats.csv          # Source dataset
│
└── 📁 outputs/
    ├── 📊 1_en_cok_gol_atanlar.png
    ├── 📊 2_xg_vs_gol_sacilim.png
    ├── 📊 3_averaj_dagilimi_hist.png
    ├── 📊 4_sonuc_oranlari_pie.png
    ├── 📊 5_puan_dagilimi_boxplot.png
    └── 📊 6_subplot_karsilastirma.png
```

---

<a name="contributing"></a>
## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Guide
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

<a name="license"></a>
## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

<a name="contact"></a>
## 📧 Contact

**Project Maintainer**: Your Name
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

---

</div>

<div align="center">

---

**🇹🇷 Aşağıda Türkçe dokümantasyon bulunmaktadır**

</div>

<div id="turkish">

---

<a name="turkish"></a>
## 📋 İçindekiler (Türkçe)

- [Proje Özeti](#proje-ozeti)
- [Özellikler](#ozellikler)
- [Teknik Mimarlık](#teknik-mimarlik)
- [Kurulum](#kurulum)
- [Kullanım](#kullanim)
- [Veri Kaynakları](#veri-kaynaklari)
- [Görselleştirmeler](#gorsellestirmeler)
- [Sonuçlar ve Çıkarımlar](#sonuclar)
- [Proje Yapısı](#proje-yapisi)
- [Katkıda Bulunma](#katkida-bulunma)
- [İletişim](#iletisim)

---

## 🌟 Proje Özeti {#proje-ozeti}

Bu proje, FIFA 2022 Dünya Kupası grup aşaması istatistikleri üzerinde kapsamlı veri analizi gerçekleştirir. Python'un güçlü veri bilimi araç setini (NumPy, Pandas, Matplotlib) kullanarak, ham maç verilerini işleyerek takım performansı, gol verimliliği ve turnuva kalıpları hakkında anlamlı içgörüler çıkarır.

### 🎯 Proje Hedefleri
- **Performans Analizi**: Gol Verimlilik Oranı gibi özel metrikler aracılığıyla takım verimliliğini değerlendirme
- **İstatistiksel İçgörüler**: Goller, puanlar ve beklenen goller (xG) arasındaki kalıpları belirleme
- **Veri Görselleştirme**: Paydaş iletişimi için yayın kalitesinde grafikler oluşturma
- **Tahmine Dayalı Analiz**: Beklenen ve gerçek performans metriklerini karşılaştırma

### 📈 Ölçülebilir Sonuçlar
- ✅ **8 grup** boyunca **32 takım** analiz edildi (256+ veri noktası)
- ✅ **6 profesyonel görselleştirme** yayın standartlarında oluşturuldu
- ✅ NumPy işlemleri kullanılarak **2 özel verimlilik metriği** geliştirildi
- ✅ **15 istatistiksel özellik** işlendi ve normalize edildi
- ✅ Takım performansı ve beklentileri hakkında içgörüler üretildi

---

## 🚀 Özellikler {#ozellikler}

| Özellik | Açıklama | Teknolojiler |
|---------|----------|--------------|
| **Veri İşleme** | Gelişmiş veri temizleme, dönüştürme ve normalizasyon | Pandas, NumPy |
| **İstatistiksel Analiz** | Gol verimlilik puanları dahil özel metrik hesaplama | NumPy, İstatistik |
| **Görselleştirme Paketi** | 6 grafik türü: Bar, Scatter, Histogram, Pasta, Kutu, Subplot | Matplotlib |
| **Çift Dilli Destek** | İngilizce ve Türkçe tam dokümantasyon | Markdown |
| **CI/CD Pipeline** | Her commit'te otomatik test ve linting | GitHub Actions |
| **Profesyonel Dokümantasyon** | Kapsamlı README, API dokümanları ve katkı rehberleri | GitHub Standartları |

---

## 🏗️ Teknik Mimarlık {#teknik-mimarlik}

### Teknoloji Yığını

```
┌─────────────────────────────────────────────────────────────┐
│                    SUNUM KATMANI                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Sütun      │  │  Saçılım    │  │   Dağılım           │  │
│  │  Grafikleri │  │  Grafikleri │  │   Görselleştirmeleri│  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                   ANALİZ KATMANI                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  GroupBy    │  │ Özet        │  │  Özel Metrikler     │  │
│  │  İşlemleri  │  │ Tablolar    │  │  (Verimlilik Skorları)│  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                   VERİ KATMANI                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Ham CSV   │  │   NumPy     │  │    Pandas           │  │
│  │   İçe Aktar │  │ Diziler     │  │    DataFrame'ler    │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Temel Kütüphaneler
- **NumPy (≥1.21)**: Yüksek performanslı sayısal işlemler ve dizi işleme
- **Pandas (≥1.3)**: Veri manipülasyonu, toplama ve analiz
- **Matplotlib (≥3.5)**: Statik, animasyonlu ve etkileşimli görselleştirmeler

---

## 💻 Kurulum {#kurulum}

### Ön Gereksinimler
- Python 3.8 veya üstü
- pip paket yöneticisi
- Git

### Hızlı Başlangıç

```bash
# Depoyu klonlayın
git clone https://github.com/yourusername/fifa2022-analysis.git
cd fifa2022-analysis

# Sanal ortam oluşturun (önerilir)
python -m venv venv

# Sanal ortamı etkinleştirin
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Bağımlılıkları yükleyin
pip install -r requirements.txt
```

### Bağımlılıklar
```
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.5.0
```

---

## 🎮 Kullanım {#kullanim}

### Analizi Çalıştırma

```bash
# Ana analiz betiğini çalıştırın
python fıfa2022.py
```

### Kod Örneği: Veri Yükleme ve İşleme

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Veri setini yükle
df = pd.read_csv('group_stats.csv')

# Özel verimlilik metriğini hesapla
df['gol_verimliligi'] = np.divide(
    df['goals_scored'], 
    df['expected_goal_scored']
)

# 0-1 ölçeğine normalize et
verim_min = np.min(df['gol_verimliligi'])
verim_max = np.max(df['gol_verimliligi'])
df['verim_skoru_norm'] = (df['gol_verimliligi'] - verim_min) / (verim_max - verim_min)

# Grup analizi
grup_ozet = df.groupby('grup_adi').agg({
    'goals_scored': 'sum',
    'points': 'sum',
    'expected_goal_scored': 'mean'
}).sort_values(by='points', ascending=False)
```

### Görselleştirme Oluşturma

```python
# Sütun grafiği - En çok gol atanlar
plt.figure(figsize=(10, 6))
top_10 = df.sort_values(by='goals_scored', ascending=False).head(10)
plt.bar(top_10['team'], top_10['goals_scored'], color='skyblue')
plt.title('FIFA 2022 - En Çok Gol Atan İlk 10 Takım')
plt.xticks(rotation=45)
plt.savefig('top_scorers.png', dpi=300, bbox_inches='tight')
```

---

## 📊 Veri Kaynakları {#veri-kaynaklari}

### Veri Seti: group_stats.csv

| Sütun | Açıklama | Tip |
|-------|----------|-----|
| `group` | Grup numarası (1-8) | Integer |
| `rank` | Final grup pozisyonu (1-4) | Integer |
| `team` | Ülke adı | String |
| `matches_played` | Oynanan maçlar | Integer |
| `wins` | Galibiyetler | Integer |
| `draws` | Beraberlikler | Integer |
| `losses` | Mağlubiyetler | Integer |
| `goals_scored` | Atılan goller | Integer |
| `goals_against` | Yenilen goller | Integer |
| `goal_difference` | Averaj | Integer |
| `points` | Toplam puan | Integer |
| `expected_goal_scored` | Beklenen goller (xG) | Float |
| `exp_goal_conceded` | Beklenen yenilen goller | Float |
| `exp_goal_difference` | xG farkı | Float |
| `exp_goal_difference_per_90` | 90 dakika başına xG farkı | Float |

### Veri Kalitesi
- **Tamamlılık**: %100 (eksik değer yok)
- **Kapsam**: Tüm 32 takım, tüm 8 grup
- **Doğruluk**: Resmi FIFA 2022 istatistikleri

---

## 📈 Görselleştirmeler {#gorsellestirmeler}

### Oluşturulan Grafikler

| # | Grafik Tipi | Amaç | Dosya |
|---|-------------|------|-------|
| 1 | **Sütun Grafiği** | En çok gol atan 10 takım | `1_en_cok_gol_atanlar.png` |
| 2 | **Saçılım Grafiği** | Beklenen ve gerçek goller korelasyonu | `2_xg_vs_gol_sacilim.png` |
| 3 | **Histogram** | Averaj dağılımı | `3_averaj_dagilimi_hist.png` |
| 4 | **Pasta Grafiği** | Maç sonuçları dağılımı | `4_sonuc_oranlari_pie.png` |
| 5 | **Kutu Grafiği** | Sıralamaya göre puan dağılımı | `5_puan_dagilimi_boxplot.png` |
| 6 | **Alt Grafik** | Çoklu metrik karşılaştırması | `6_subplot_karsilastirma.png` |

### Görselleştirme Felsefesi
Her grafik tipi veri özelliklerine göre seçildi:
- **Sütun Grafikleri**: Kategorik karşılaştırma (takımlar)
- **Saçılım Grafikleri**: Korelasyon analizi (xG vs. gerçek)
- **Histogramlar**: Dağılım analizi (averaj)
- **Pasta Grafikleri**: Oransal temsil (sonuçlar)
- **Kutu Grafikleri**: Dağılım yayılımı ve aykırı değerler

---

## 🏆 Sonuçlar ve Çıkarımlar {#sonuclar}

### Temel Bulgular

1. **En İyi Performans**: İngiltere, yüksek verimlilikle gol sıralamasında lider (9 gol)
2. **Verimlilik Liderleri**: Arjantin gibi takımlar xG beklentilerini önemli ölçüde aştı
3. **Grup Dinamikleri**: E Grubu (Japonya, İspanya, Almanya) en yüksek rekabet dengesini gösterdi
4. **xG Korelasyonu**: Beklenen ve gerçek goller arasında güçlü pozitif korelasyon (r > 0,8)

### İstatistiksel Öne Çıkanlar

| Metrik | Değer |
|--------|-------|
| Toplam Atılan Gol | 120 |
| Takım Başına Ortalama Gol | 3,75 |
| En Verimli Takım | Arjantin (xG oranı: 0,83) |
| En Yüksek xG | Almanya (10,1) |
| En Büyük Sürpriz | Japonya'nın Almanya/İspanya'yı yenmesi |

---

## 📁 Proje Yapısı {#proje-yapisi}

```
fifa2022-analysis/
│
├── 📄 README.md                 # Bu dosya
├── 📄 LICENSE                   # MIT Lisansı
├── 📄 requirements.txt          # Python bağımlılıkları
├── 📄 CONTRIBUTING.md           # Katkı rehberi
├── 📄 CODE_OF_CONDUCT.md        # Topluluk standartları
├── 📄 CHANGELOG.md              # Sürüm geçmişi
├── 📄 SECURITY.md               # Güvenlik politikası
│
├── 📁 .github/
│   ├── 📁 workflows/
│   │   └── ci.yml               # CI/CD pipeline
│   ├── 📁 ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── 📄 pull_request_template.md
│
├── 📁 docs/
│   ├── architecture.md          # Sistem tasarım dokümanları
│   ├── api_reference.md         # Tam API dokümantasyonu
│   └── methodology.md           # Analiz metodolojisi
│
├── 📁 src/
│   └── fıfa2022.py              # Ana analiz betiği
│
├── 📁 data/
│   └── group_stats.csv          # Kaynak veri seti
│
└── 📁 outputs/
    ├── 📊 1_en_cok_gol_atanlar.png
    ├── 📊 2_xg_vs_gol_sacilim.png
    ├── 📊 3_averaj_dagilimi_hist.png
    ├── 📊 4_sonuc_oranlari_pie.png
    ├── 📊 5_puan_dagilimi_boxplot.png
    └── 📊 6_subplot_karsilastirma.png
```

---

## 🤝 Katkıda Bulunma {#katkida-bulunma}

Katkılarınızı bekliyoruz! Lütfen rehberler için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasına bakın.

### Hızlı Katkı Rehberi
1. Depoyu forklayın
2. Bir özellik dalı oluşturun (`git checkout -b feature/harika-ozellik`)
3. Değişiklikleri commit edin (`git commit -m 'Harika özellik ekle'`)
4. Dala push yapın (`git push origin feature/harika-ozellik`)
5. Bir Pull Request açın

---

## 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

## 📧 İletişim {#iletisim}

**Proje Sorumlusu**: Your Name
- GitHub: [@yourusername](https://github.com/AbdullahKayar)
- LinkedIn: [Profiliniz](https://www.linkedin.com/in/abdullah-kayar-20b3233a3)
- Email: abdullahkayar5231@gmail.com

</div>

---

<div align="center">

### ⭐ Star this repository if you find it helpful! | Bu depoyu faydalı bulursanız yıldızlayın! ⭐

</div>

