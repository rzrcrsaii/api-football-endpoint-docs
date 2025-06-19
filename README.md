# 🏈 API Football Endpoint Dokümantasyonu

Bu repository, **API Football** servisinin tüm endpoint'lerinin dokümantasyonunu içerir ve bu dokümantasyonları tek bir dosyada birleştiren otomatik Python aracını sunar.

## 📋 İçerik

- **API Endpoint Dosyaları**: Tüm API Football endpoint'lerinin detaylı dokümantasyonu
- **Otomatik Birleştirme Aracı**: Python scripti ile tüm dokümantasyonu tek dosyada toplama
- **Birleştirilmiş Dokümantasyon**: `all-in-one.md` dosyasında tüm endpoint'ler

## 🚀 Hızlı Başlangıç

### Gereksinimler
- Python 3.6+
- Git

### Kullanım

1. **Repository'yi klonlayın:**
```bash
git clone https://github.com/rzrcrsaii/api-football-endpoint-docs.git
cd api-football-endpoint-docs
```

2. **Dokümantasyon birleştirme scriptini çalıştırın:**
```bash
python create_all_in_one_docs.py
```

3. **Birleştirilmiş dokümantasyonu görüntüleyin:**
- `all-in-one.md` dosyası oluşturulacak
- Bu dosya tüm API endpoint'lerini içerir

## 📁 Dosya Yapısı

```
api-football-endpoint-docs/
├── README.md                          # Bu dosya
├── create_all_in_one_docs.py         # Dokümantasyon birleştirme scripti
├── all-in-one.md                     # Birleştirilmiş dokümantasyon
├── countries                         # Countries endpoint dokümantasyonu
├── fixtures                          # Fixtures endpoint dokümantasyonu
├── leagues.txt                       # Leagues endpoint dokümantasyonu
├── Timezone.txt                      # Timezone endpoint dokümantasyonu
├── fixture-events                    # Fixture Events endpoint dokümantasyonu
├── fixture-h2h                       # Head-to-Head endpoint dokümantasyonu
├── fixture-lineups                   # Lineups endpoint dokümantasyonu
├── fixture-playerstatistics          # Player Statistics endpoint dokümantasyonu
├── fixture-statistics                # Fixture Statistics endpoint dokümantasyonu
├── fixtures-round                    # Fixtures Round endpoint dokümantasyonu
├── injures                           # Injuries endpoint dokümantasyonu
├── odds-live                         # Live Odds endpoint dokümantasyonu
├── odds-live-bets                    # Live Bets endpoint dokümantasyonu
├── player-profiles                   # Player Profiles endpoint dokümantasyonu
├── player-squads                     # Player Squads endpoint dokümantasyonu
├── player-statistics                 # Player Statistics endpoint dokümantasyonu
├── prematch-bets                     # Pre-match Bets endpoint dokümantasyonu
├── prematch-bookmakers               # Bookmakers endpoint dokümantasyonu
├── prematch-mapping                  # Mapping endpoint dokümantasyonu
├── prematch-odds                     # Pre-match Odds endpoint dokümantasyonu
├── seasons                           # Seasons endpoint dokümantasyonu
├── standings                         # Standings endpoint dokümantasyonu
├── team-countries                    # Team Countries endpoint dokümantasyonu
├── team-statistics                   # Team Statistics endpoint dokümantasyonu
└── teamsinfo                         # Teams Info endpoint dokümantasyonu
```

## 🔧 Script Özellikleri

`create_all_in_one_docs.py` scripti şu özelliklere sahiptir:

### ✨ Ana Özellikler
- **Kapsamlı Tarama**: Tüm alt klasörleri dahil ederek dosyaları tarar
- **Akıllı Filtreleme**: Binary, gizli ve geçici dosyaları otomatik atlar
- **Self-Exclusion**: Script kendi dosyasını çıktıya dahil etmez
- **Hata Yönetimi**: Okunamayan dosyalar için güvenli hata yakalama
- **Çoklu Encoding**: UTF-8, Latin-1, CP1252 desteği
- **Syntax Highlighting**: Dosya uzantısına göre otomatik kod vurgulama
- **Metadata**: Her dosya için boyut ve değişiklik tarihi
- **İçindekiler**: Otomatik navigasyon linkleri
- **Progress Tracking**: Terminal çıktısında işlem durumu

### 📊 Çıktı Formatı
- **Markdown Format**: GitHub uyumlu Markdown
- **Organize Yapı**: Her dosya için başlık ve metadata
- **Kod Blokları**: Uygun syntax highlighting
- **Navigasyon**: Tıklanabilir içindekiler tablosu

## 📈 İstatistikler

- **Toplam Endpoint**: 26 adet
- **Dokümantasyon Boyutu**: ~200KB
- **Desteklenen Formatlar**: Text, Markdown, JSON örnekleri
- **Otomatik Güncelleme**: Script her çalıştırıldığında yeniden oluşturur

## 🛠️ Geliştirme

### Script Geliştirme
Script'i geliştirmek için:

1. `create_all_in_one_docs.py` dosyasını düzenleyin
2. Test edin: `python create_all_in_one_docs.py`
3. Sonuçları `all-in-one.md` dosyasında kontrol edin

### Yeni Endpoint Ekleme
1. Yeni endpoint dokümantasyon dosyasını ekleyin
2. Script'i çalıştırın - otomatik olarak dahil edilecek

## 📝 API Football Hakkında

Bu dokümantasyon [API Football](https://www.api-football.com/) servisinin endpoint'lerini kapsar. API Football, futbol verilerine erişim sağlayan kapsamlı bir REST API'dir.

### Temel Özellikler
- **Canlı Maç Verileri**: Gerçek zamanlı skor ve etkinlikler
- **Lig Bilgileri**: Dünya çapında 1000+ lig
- **Takım & Oyuncu İstatistikleri**: Detaylı performans verileri
- **Bahis Oranları**: Canlı ve maç öncesi oranlar
- **Tahminler**: AI destekli maç tahminleri

## 🤝 Katkıda Bulunma

1. Repository'yi fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## 📞 İletişim

- **GitHub**: [@rzrcrsaii](https://github.com/rzrcrsaii)
- **Repository**: [api-football-endpoint-docs](https://github.com/rzrcrsaii/api-football-endpoint-docs)

## 🙏 Teşekkürler

- [API Football](https://www.api-football.com/) - Kapsamlı futbol API'si için
- Python Community - Harika araçlar için

---

⭐ Bu repository'yi faydalı bulduysanız yıldızlamayı unutmayın!
