import math
print("Ingrese el primer operando")
a=int(input())
print("Ingrese el segundo operando")
b=int(input())
c=a+b
print(c)
d=a^b
print(d)
e=a**b
print(e)
message = 'And now for something completely different'
n = 20
pi = 3.1415926535897932
casa_dos=30
print(casa_dos)

##degrees = int(input())
##radians = degrees/(180*math.pi)
##math.sin(radians)

def senoDegree(deg):
    rad = math.radians(deg)
    a = "El valor de seno en grados es:"
    b = math.sin(rad)
    return a + str(b)
print(senoDegree(45))
