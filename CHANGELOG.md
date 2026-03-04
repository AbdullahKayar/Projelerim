<div align="center">

# 📝 Changelog | Değişiklik Günlüğü

All notable changes to this project will be documented in this file.

Bu projedeki tüm önemli değişiklikler bu dosyada belgelenecektir.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Format [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)'e dayanmaktadır ve
bu proje [Semantic Versioning](https://semver.org/spec/v2.0.0.html)'e uymaktadır.

</div>

---

## [Unreleased]

### Added | Eklendi
- Initial project setup with core data analysis functionality
- FIFA 2022 World Cup group stage statistics dataset
- Six comprehensive visualizations:
  - Bar chart: Top 10 goal-scoring teams
  - Scatter plot: Expected vs. actual goals
  - Histogram: Goal difference distribution
  - Pie chart: Match results distribution
  - Box plot: Points distribution by rank
  - Subplot comparison: Multi-metric analysis
- Custom efficiency metrics calculation using NumPy
- Group-based and rank-based statistical aggregations
- Bilingual documentation (English/Turkish)
- Comprehensive GitHub repository files:
  - MIT License
  - Contributing guidelines
  - Code of conduct
  - Issue and PR templates
  - Security policy
  - GitHub Actions CI/CD workflow

### Changed | Değiştirildi
- N/A

### Deprecated | Kullanımdan Kaldırıldı
- N/A

### Removed | Kaldırıldı
- N/A

### Fixed | Düzeltildi
- N/A

### Security | Güvenlik
- N/A

---

## [1.0.0] - 2024-01-15

### Added | Eklendi
- **Core Analysis Module** (`fıfa2022.py`)
  - Data loading and cleaning with Pandas
  - Custom efficiency metric calculations using NumPy
  - Normalized scoring for comparative analysis
  - Group-wise and rank-wise statistical aggregations
  - Publication-quality visualization generation

- **Dataset** (`group_stats.csv`)
  - Complete FIFA 2022 World Cup group stage statistics
  - 32 teams across 8 groups
  - 15 statistical attributes per team
  - 100% data completeness (no missing values)

- **Visualizations**
  - `1_en_cok_gol_atanlar.png` - Top scorers bar chart
  - `2_xg_vs_gol_sacilim.png` - xG correlation scatter plot
  - `3_averaj_dagilimi_hist.png` - Goal difference histogram
  - `4_sonuc_oranlari_pie.png` - Results pie chart
  - `5_puan_dagilimi_boxplot.png` - Points distribution box plot
  - `6_subplot_karsilastirma.png` - Comparative subplot analysis

- **Documentation**
  - Comprehensive bilingual README.md
  - Technical architecture documentation
  - API reference documentation
  - Installation and usage guides
  - Contribution guidelines (English/Turkish)
  - Code of conduct (English/Turkish)

- **Development Tools**
  - GitHub Actions CI/CD pipeline
  - Python .gitignore for data science projects
  - requirements.txt with dependency specifications

---

## Release Notes | Sürüm Notları

### Version 1.0.0 - Initial Release

This is the initial release of the FIFA 2022 World Cup Data Analysis project. It provides a complete data analysis pipeline for exploring group stage statistics, with a focus on:

- **Data Processing**: Efficient handling of CSV data using Pandas
- **Statistical Analysis**: Custom metrics using NumPy operations
- **Visualization**: Publication-quality charts using Matplotlib
- **Documentation**: Professional, bilingual documentation suitable for CV inclusion

### Key Features
- 📊 Analyzed 32 teams across 8 groups (256+ data points)
- 📈 Created 6 professional visualizations
- 🧮 Developed 2 custom efficiency metrics
- 🎯 100% data completeness
- 🌍 Full English/Turkish documentation

---

## Future Roadmap | Gelecek Yol Haritası

### Planned for v1.1.0
- [ ] Add Jupyter notebook with interactive analysis
- [ ] Implement additional statistical tests
- [ ] Add support for knockout stage data
- [ ] Create interactive Plotly visualizations
- [ ] Add unit tests with pytest

### Planned for v1.2.0
- [ ] Machine learning models for outcome prediction
- [ ] Player-level analysis integration
- [ ] Historical World Cup comparison
- [ ] Web dashboard for interactive exploration

### Planned for v2.0.0
- [ ] Support for multiple tournament years
- [ ] Real-time data integration
- [ ] API endpoint for data access
- [ ] Docker containerization

---

## How to Update This Changelog | Bu Günlüğü Nasıl Güncellersiniz

When making changes to the project, add entries under the `[Unreleased]` section following these guidelines:

1. **Added** - New features
2. **Changed** - Changes to existing functionality
3. **Deprecated** - Soon-to-be removed features
4. **Removed** - Removed features
5. **Fixed** - Bug fixes
6. **Security** - Security-related changes

When releasing a new version:
1. Move `[Unreleased]` changes to a new version section
2. Add release date
3. Add link to version comparison
4. Create a new empty `[Unreleased]` section

---

<div align="center">

**For more information, see [CONTRIBUTING.md](CONTRIBUTING.md)**

**Daha fazla bilgi için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasına bakın**

</div>
