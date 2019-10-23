import random
angka=random.randrange(1,100)
tebakan=0
tebakan_saudara=int(input("Tebak angka yang sudah dibangkitkan antara 1 s.d 100: "))
while tebakan_saudara != angka:
    tebakan += 1
    if tebakan_saudara > angka:
        print(tebakan_saudara, "terlalu tinggi.")
    elif tebakan_saudara < angka:
        print(tebakan_saudara, "terlalu rendah.")
    tebakan_saudara=int(input("Tebak lagi: "))
print("\nBagus! Saudara menebak dalam", tebakan, "tebakan.")