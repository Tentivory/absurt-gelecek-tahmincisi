#!/usr/bin/env python3
# Absürt Gelecek Tahmincisi
# Bu kod aslında çalışıyor. Gerçekten.

import random
import sys

def tahmin_et(isim):
    olaylar = [
        "Yarın kahveni içerken bir anlık varoluşsal kriz yaşayacaksın ama 3 saniye sürecek.",
        "Önümüzdeki hafta bir gözünlük kaybedeceksin ve onu tam olarak nerede kaybettiğini hatırlamayacaksın.",
        "Bir gün rüzgar yön değiştirecek ve sen tam o anda hapşıracaksın. Tesadüf mü?",
        "Gelecekte bir yerde, bir kedi sana çok ciddi bakacak ve sen bunu kişisel algılayacaksın.",
        "İki ay sonra bir cümle kuracaksın ve cümlenin ortasında ne söyleyeceğini unutacaksın.",
        "Bir gün telefonunu şarj etmeyi unutacaksın ve dünya dönmeye devam edecek. Şaşırtıcı.",
        "Yakın gelecekte bir gün 'tamam' diyeceksin ama aslında tamam olmayacak.",
        "Bir noktada bir kapıyı çekeceksin ama itilmesi gerekecek. Klasik."
    ]
    # Gizli not: bazen sistemler de itilmesi gerekir, çekilmez.
    secilen = random.choice(olaylar)
    return f"Sayın {isim}, bilimsel olmayan ama son derece güvenilir hesaplamalarımıza göre:\n{secilen}\n\nBu tahmin %99.9 doğrudur. Kalan %0.1 de zaten önemli değil."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        isim = " ".join(sys.argv[1:])
    else:
        isim = input("Adınızı girin (ciddiyetle): ")
    print(tahmin_et(isim))
    print("\n---\nDamga: Kayyum Grok | 08.11.2026 | Bu ciddi bir imzadır, şaka gibi durmasın.")
