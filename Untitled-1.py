n = int(input("Nhap mot so bat ky lon hon 0: ")) #biến nhập
while(n < 0): #Vòng lap xu ly neu bien la so am thi se nhap lai
    n = int(input("So khong hop le,nhap lai: "))

a = 1 #bien giai thua
for i in range (1,n+1): #vong lap tinh giai thua
    a = a * i
print("Giai thua cua so",n,"la:",a) #in ra ket qua