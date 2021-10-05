import math

num =int(input("Kérek egy háromjegyű pozitív számot!"))
num10 =math.floor(num/100)
num20 =math.floor((num/10)-(num10*10))
num30 =math.floor(num-((num10*100)+(num20*10)))

num1 =math.pow(num10,3)
num2 =math.pow(num20,3)
num3 =math.pow(num30,3)

numadd=num1+num2+num3


if num<100 or num>=1000:
    print("Ez a szám nem háromjegyű és/vagy páros")
elif numadd==num:
    print("Armstrong szám!:)")
else:
    print("Nem Armstrong szám!:(")
    

