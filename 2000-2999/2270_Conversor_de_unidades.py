d_cm = int(input())
copy = d_cm
km = d_cm//100000
d_cm = d_cm - (km*100000)
mts = d_cm//100
d_cm = d_cm - (mts*100)

print(copy,"centímetros son", km, "km", mts,"m" ,d_cm,"cm")