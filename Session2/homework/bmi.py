

height = int(input("chieu cao cua ban la: "))
weight = int(input("can nang cua ban la: "))

bmi = weight/((height*height)*(10**(-4)))

print ("BMI = ", bmi)
from random import randint

bmi = randint(16, 30)

if bmi <16:
    print ("")

elif bmi <18.5:
    print ("ban dang bi suy dinh duong")

elif bmi <25:
    print ("ban rat binh thuong")

elif bmi <30:
    print ("co ve ban hoi mum mim roi")

else:
    print ("ban qua nang can! Giam can di")