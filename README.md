# profile-pic-optimizer

Bu Python scripti, büyük boyutlu profil fotoğraflarını kaliteden minimum ödün vererek istenen dosya boyutunun (örn: 1MB altı) altına düşürmek için tasarlanmıştır.

## 🚀 Nasıl Çalıştırılır?

1. Projeyi bilgisayarınıza indirin (clone).
2. Python ortamınızda Pillow kütüphanesinin kurulu olduğundan emin olun:
   \`pip install Pillow\`
3. Sıkıştırmak istediğiniz resmi **`images`** klasörünün içine atın ve adını `profile_image.jpg` olarak değiştirin (veya koddaki `input_file` değişkenini resminizin adına göre güncelleyin).
4. Scripti çalıştırın:
   \`python compressor.py\`
5. İşlem tamamlandığında, sıkıştırılmış resminizi **`compress`** klasörünün içinde bulabilirsiniz.