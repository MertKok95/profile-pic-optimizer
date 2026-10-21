import os
from PIL import Image

def compress_image(input_path, output_path, max_size_kb=950):
    try:
        img = Image.open(input_path)
        quality = 95
        
        img.save(output_path, optimize=True, quality=quality)
        
        while os.path.getsize(output_path) > max_size_kb * 1024 and quality > 10:
            quality -= 5
            img.save(output_path, optimize=True, quality=quality)
            
        final_size = os.path.getsize(output_path) / 1024
        print(f"✅ Başarılı! Yeni boyut: {final_size:.2f} KB (Kalite: %{quality})")
        
    except Exception as e:
        print(f"❌ Bir hata oluştu: {e}")

if __name__ == "__main__":
    input_file = "images/profile_image.jpg" 
    output_file = "images/compress/resize_profile_image.jpg"
    
    if os.path.exists(input_file):
        compress_image(input_file, output_file)
    else:
        print(f"Resim bulunamadı: {input_file}")