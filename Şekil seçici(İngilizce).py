a = int(input("How many sides does your shape have\n"))
if a == 3:
    print("İt can be a triangle")
    k1 = int(input("Write its first side\n"))
    k2 = int(input("Ok now write its second side\n"))
    k3 = int(input("Finally write its third side\n"))
    if k1 > abs(k2 - k3) and k2 > abs(k1 - k3) and k3 > abs(k2 - k1):
        s = float((k1 + k2 + k3) / 2)
        A = float((s * (s - k1) * (s - k2) * (s - k3)) ** 0.5)
        print("This is a triangle:")
        if k1 == k2 == k3:
            print("Its an equilateral triangle")
        elif k1 == k2 != k3 or k2 == k3 != k1 or k3 == k1 != k2:
            print("Its an isosceles triangle")
        else:
            print("Its a scalene triangle")
    else:
        print("It doesn't meet the requirements to be a triangle")
elif a == 4:
    print("It can be a quadrangle")
