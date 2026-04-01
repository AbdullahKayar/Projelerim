📊 Discord Data Warehouse & Analytics Bot

🇹🇷 Proje Özeti

Bu proje, Discord sunucuları için geliştirilmiş gelişmiş bir Veri Ambarı ve OSINT botudur. Sunucudaki tüm mesaj trafiğini SQLite veritabanına işler, silinen/düzenlenen mesajları "Gölge Kayıt" olarak saklar ve yöneticilere CSV dökümü alma imkanı sunar.

🇬🇧 Project Overview

An advanced Data Warehouse and OSINT bot designed for Discord servers. It logs all message traffic into a local SQLite database, maintains shadow records of deleted/edited messages, and allows administrators to export data as CSV files for analysis.

🚀 Quick Start Guide / Hızlı Başlangıç Rehberi

1. Clone the Project / Projeyi İndirin

git clone [https://github.com/AbdullahKayar/Discord-Data-Bot.git](https://github.com/AbdullahKayar/Discord-Data-Bot.git)
cd Discord-Data-Bot


2. Install Dependencies / Kütüphaneleri Kurun

"Hangi kütüphaneleri kurmalıyım?" diye düşünmenize gerek yok. Tek komutla her şeyi hazırlayabilirsiniz:

pip install -r requirements.txt


(Kurulanlar: discord.py, pandas, aiosqlite, python-dotenv)

3. Configuration / Ayarlar

.env.example dosyasının adını .env olarak değiştirin.

Bot token'ınızı dosyanın içine yapıştırın: DISCORD_TOKEN=your_token_here

4. Run / Çalıştırın

python main.py


🌟 Key Features / Öne Çıkan Özellikler

Shadow Logging: Silinen ve düzenlenen mesajlar asla kaybolmaz, veritabanına yedeklenir.

Autonomous Reporting: Her Pazar gecesi haftalık sunucu aktiflik raporu otomatik oluşturulur.

Data Export: Tüm veriler pandas aracılığıyla profesyonel CSV formatına dönüştürülebilir.

RBAC Security: Admin ve kullanıcı komutları kanal bazlı yetkilendirme ile korunur.

🛡️ Security Warning / Güvenlik Uyarısı

Bu bot verileri yerel (local) olarak saklar. Lütfen .env ve .db dosyalarınızı asla GitHub'da paylaşmayın. Bu proje, .gitignore ile bu dosyaları koruyacak şekilde yapılandırılmıştır.

📫 Connect with me / İletişim

LinkedIn: linkedin.com/in/abdullah-kayar

GitHub: github.com/AbdullahKayar

Email: abdullahkayar@email.com

Developed by Abdullah Kayar with ❤️ and Data Science principles.