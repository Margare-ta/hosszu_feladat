num1=int(input("Kérek egy számot"))
num2=int(input("Kérek egy számot"))

if num1==num2:
    print("A két szám egyenlő")
if (num1%2)!=0 and (num2%2)!=0:
    print("Mind a két szám páratlan.")
if (num1%3)==0 or(num2%3)==0:
    print("Legalább az egyik szám osztható hárommal")
if num1<0 and num2<0:
    print("MInd a két szám negatív")
if num1<0 and num2>=0:
    print("Az egyik szám negatív, a másik szám pozitív.")
elif num1>=0 and num2>0:
    print("Az egyik szám negatív, a másik szám pozitív.")
