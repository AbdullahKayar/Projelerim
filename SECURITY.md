<div align="center">

# 🔒 Security Policy | Güvenlik Politikası

[![Security Policy](https://img.shields.io/badge/Security-Policy-blue?style=for-the-badge)](SECURITY.md)

**Reporting security vulnerabilities in FIFA 2022 World Cup Data Analysis**

**FIFA 2022 Dünya Kupası Veri Analizi'nde güvenlik açıklarının bildirilmesi**

</div>

---

## 📋 Supported Versions | Desteklenen Sürümler

The following versions of this project are currently being supported with security updates.

Bu projenin aşağıdaki sürümleri şu anda güvenlik güncellemeleriyle desteklenmektedir.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

---

## 🚨 Reporting a Vulnerability | Güvenlik Açığı Bildirme

### English

If you believe you have found a security vulnerability in this project, please report it to us through coordinated disclosure.

**Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**

Instead, please send an email to: **security@example.com** (replace with actual security email)

Please include as much of the following information as possible to help us better understand the nature and scope of the possible issue:

- **Type of issue** (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- **Full paths** of source file(s) related to the manifestation of the issue
- **Location** of affected source code (tag/branch/commit or direct URL)
- Any **special configuration** required to reproduce the issue
- **Step-by-step instructions** to reproduce the issue
- **Proof-of-concept or exploit code** (if possible)
- **Impact** of the issue, including how an attacker might exploit it

### Türkçe

Bu projede bir güvenlik açığı bulduğunuzu düşünüyorsanız, lütfen koordineli açıklama yoluyla bize bildirin.

**Lütfen güvenlik açıklarını kamuya açık GitHub sorunları, tartışmalar veya çekme istekleri aracılığıyla bildirmeyin.**

Bunun yerine, lütfen şu adrese bir e-posta gönderin: **security@example.com** (gerçek güvenlik e-postası ile değiştirin)

Lütfen olası sorunun doğası ve kapsamını daha iyi anlamamıza yardımcı olmak için mümkün olduğunca aşağıdaki bilgileri ekleyin:

- **Sorun tipi** (örn. buffer overflow, SQL injection, cross-site scripting, vb.)
- Sorunun tezahürüyle ilgili kaynak dosya(lar)ın **tam yolları**
- Etkilenen kaynak kodun **konumu** (etiket/dal/commit veya doğrudan URL)
- Sorunu yeniden üretmek için gereken **özel yapılandırma**
- Sorunu yeniden üretmek için **adım adım talimatlar**
- **Kanıt kavramı veya exploit kodu** (mümkünse)
- Sorunun **etkisi**, saldırganın bunu nasıl kullanabileceği dahil

---

## ⏱️ Response Timeline | Yanıt Zaman Çizelgesi

| Timeframe | Action | Eylem |
|-----------|--------|-------|
| Within 24 hours | Acknowledgment of your report | Raporunuzun onaylanması |
| Within 72 hours | Initial assessment | İlk değerlendirme |
| Within 7 days | Detailed response and next steps | Detaylı yanıt ve sonraki adımlar |
| Monthly | Progress updates on fixes | Düzeltmeler hakkında ilerleme güncellemeleri |

---

## 🛡️ Security Best Practices | Güvenlik En İyi Uygulamaları

1. **Keep dependencies updated** | **Bağımlılıkları güncel tutun**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

2. **Use virtual environments** | **Sanal ortamlar kullanın**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Don't commit sensitive data** | **Hassas verileri commit etmeyin**
   - API keys
   - Passwords
   - Personal data

4. **Validate input data** | **Girdi verilerini doğrulayın**
   - Check file formats
   - Validate CSV structures
   - Sanitize inputs

---

## 📜 Data Privacy | Veri Gizliliği

This project:
- Uses publicly available FIFA 2022 World Cup statistics
- Does not collect personal information
- Does not store user data
- Processes data locally on your machine

Bu proje:
- Kamuya açık FIFA 2022 Dünya Kupası istatistiklerini kullanır
- Kişisel bilgi toplamaz
- Kullanıcı verisi depolamaz
- Verileri yerel makinenizde işler

---

## 📞 Contact | İletişim

- **Security Email**: security@example.com
- **Project Maintainers**: See [README.md](README.md#contact)

---

<div align="center">

**Thank you for helping keep this project secure!**

**Bu projeyi güvenli tutmaya yardım ettiğiniz için teşekkür ederiz!**

🔐 **Security is everyone's responsibility** | **Güvenlik herkesin sorumluluğundadır** 🔐

</div>
