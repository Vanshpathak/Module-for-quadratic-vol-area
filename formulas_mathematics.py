from math import pi
import math
def arearectangle(l,b):
    area=(l*b)
    print (area)
def areasquare(a):
    area=(a*a)
    print(area)
def areacircle(r):
    area1=(pi*r*r)
    area=round(area1)
    print(area)
def areatriangle(a,b):
    area=(0.5*a*b)
    print(area)
def areatrapezoid(a,b,c):
    area=(0.5*(a+b)*c)
    print(area)
def areaellipse(a,b):
    area1=(pi*a*b)
    area=round(area1)
    print(area)
########volume startsss
#
#
#
#
def volcuboid(a,b,c):
    volume=(a*b*c)
    print(volume)
def volcube(a):
    volume=a**3
    print(volume)
def volcylinder(r,h):
    volume=(pi*(r**2)*h)
    print(volume)
def volsphere(r):
    volume=((4/3)*pi*(r**3))
    print(volume)
def volrtcircularcone(r,h):
    vol=((1/3)*pi*(r**2)*h)
    print(vol)
def volhemisphere(a):
    volume=((2/3)*pi*(a**3))
    print(volume)

##quadratic equations_______________________________
def quadraticformula(a,b,c):
    print(''''Enter the values of quadratic equation as a,b,c.
(a for the sq. term coefficient),(b for the coefficient of x) and
(c for the constant term.)
''')
    f=((b**2)-(4*a*c))
    if f>0:
        g=((-b+(math.pow(f,1/2)))/(a*2))
        k=((-b-(math.pow(f,1/2)))/(a*2))
        print('roots are real and different.The roots are: ',g,k)

    elif f<0:
        print('imaginary roots;function not available')
    elif f==0:
         g=((-b+(math.pow(f,1/2)))/(a*2))
         k=((-b-(math.pow(f,1/2)))/(a*2))
         print('real and equal roots. The roots of the equation are ',g,k)

##end
























