total=d=e=f=g=h=j=k=l=m=o=p=q=s=0
z = float(input("Current in hall effect setup(mA): \n"))
t = float(input("Thickness Of the sample: \n"))
x = float(input("Conductivity of the sample: \n"))
y = float(input("Charge of electron or hole(w/o 10^19): \n"))
r = int(input("Number Of Observations: \n"))
for i in range(r):
    a = float(input("Current in the constant current power supply(A): "))
    b = float(input("Magnetic Field(gauss): "))
    c = float(input("Hall Voltage(mV): "))
    total = (c*t*100000000)/(z*b)
    if i == 0:
        print(f"First HC: \n{total}")
        d=total
    elif i==1:
        print(f"Second HC: \n{total}")
        e=total
    elif i==2:
        print(f"Third HC:\n{total}")
        f=total
    elif i==3:
        print(f"Fourth HC:\n{total}")
        g=total
    elif i==4:
        print(f"Fifth HC:\n{total}")
        h=total
    elif i==5:
        print(f"Sixth HC:\n{total}")
        j=total
    elif i==6:
        print(f"Seventh HC:\n{total}")
        k=total
    elif i==7:
        print(f"Eighth HC:\n{total}")
        l=total
    elif i==8:
        print(f"Ninth HC:\n{total}")
        m=total
    elif i==9:
        print(f"Tenth HC:\n{total}")
        n=total
    elif i==10:
        print(f"Eleventh HC:\n{total}")
        o=total
    elif i==11:
        print(f"Twelth HC:\n{total}")
        p=total
    elif i==12:
        print(f"Thirteenth HC:\n{total}")
        q=total
    i += 1

mean = (d+e+f+g+h+j)/r
print(f"Mean HC is {mean}")
n = 1/(mean*y)
print(f" Carrier Density is {n} * 10^19")
u = mean*x
print(f"Carrier Mobility is {u}")

