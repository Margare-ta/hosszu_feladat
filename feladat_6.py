num=int(input("Kérel egy egész számot!"))

if num==4:
    print("A megadott szám a 4-es.")
if num<10:
    print("A megadott szám kisebb mint 10. ")
if (num%2)==0:
    print("A megadott szám páros. ")
if num>=0 and num<=10:
    print("A megadott szám a [0; 10] intervallumba esik. ")
if (num%3)==0 and (num%5)==0:
    print("A megadott szám osztható 3-mal és 5-tel is.")
if num>10 and num>20:
    print("A megadott szám nem a [10; 20] intervallumba esik.")