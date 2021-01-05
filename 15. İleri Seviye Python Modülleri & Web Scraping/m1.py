
# --- Datatime Modülü ---
"""
import datetime

result = dir(datetime)
print(result)       # datetime modülünün içerisindeki özellikleri görücez
"""

from datetime import datetime

suan  = datetime.now()     # Anlık tarih ve saati alma
print(suan)

print("-----------------------------------------------")

suanYil = suan.year
suanAy = suan.month
suanGun = suan.day
suanSaat = suan.hour
suanDakika = suan.minute
suanSaniye = suan.second

print(suanYil)
print(suanAy)
print(suanGun)
print(suanSaat)
print(suanDakika)
print(suanSaniye)

print("-----------------------------------------------")

bugun = datetime.ctime(suan)    # Ayrıntılı bugün
print("bugun: ", bugun)

print("-----------------------------------------------")

simdi = datetime.today()
print("simdi: ", simdi)

print("-----------------------------------------------")

r = datetime.strftime(simdi, '%Y')      #datetime.today() fonksiyonundaki sadece yili alir.
r2 = datetime.strftime(simdi, '%X')     # sadece saat bilgisi
r3 = datetime.strftime(simdi, '%Y %B %A')
print("r: ", r)
print("r2: ", r2)
print("r3: ", r3)