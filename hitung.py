import math
menu = input()
if (menu=="1"):
	r = int(input())
	luas1 = math.pi*r*r
	keliling1 = 2*math.pi*r
	print("==========HASIL==========")
	print("Luas Lingkaran = ",luas1)
	print("Keliling Lingkaran = ",keliling1)
elif (menu=="2"):
	s = int(input())
	luas2 = s*s
	keliling2 = 4*s
	print("==========HASIL==========")
	print("Luas Persegi = ",luas2)
	print("Keliling Persegi = ",keliling2)
elif (menu=="3"):
	a = int(input())
	b = int(input())
	c = int(input())
	t = int(input())
	luas3 = 0.5*a*t
	keliling3 = a+b+c
	print("==========HASIL==========")
	print("Luas Segitiga = ",luas3)
	print("Keliling Segitiga = ",keliling3)
else:
	print("selesai")
pilihan=input()
