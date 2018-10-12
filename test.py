#дискретное преобразование фурье
import numpy as np
import math
import pylab
import matplotlib.pyplot as plt
#n = 10 #количевство значений
#N = np.random.randint(0,20,(n))
n=2
N=([3,5])
Re = np.zeros(n, dtype=np.float) #массив действительных чисел
Im = np.zeros(n, dtype=np.float) #массив мнимых чисел
st = 1/(math.sqrt(n))

#--------------------прямое преобразрвание------------
for m in range(n):
    sumRe = 0
    sumIm = 0
    for k in range(n):
        sumRe += N[k]*math.cos(2*math.pi/n*k*m)
        sumIm += N[k]*math.sin(2*math.pi/n*k*m)
        #print(math.sin(((2*math.pi)/n)*k*m),'test')
        #print('m='+str(m)+' k='+str(k)+' sin(((2*math.pi)/n)*k*m)='+str(math.sin(2*math.pi/n*k*m))+' 2*math.pi/n='+str(2*math.pi/n))
    Re[m] = st*sumRe
    Im[m] = st*sumIm
    #Re[m] = round(st*sumRe,3)
    #Im[m] = round(-(st*sumIm),3)
#----------------конец------------------------------
print('Исходные данные')
print(N)
print('Действительные значения')
print(Re)
print('Мнимые значения')
print(Im)


Nn = np.zeros(n, dtype=np.float)

#-----------------обратное преобразование--------------
for k in range(n):
    sum = 0
    for m in range(n):
        sum+= Re[m]*math.cos(2*math.pi/n*k*m) - Im[m]*math.sin(2*math.pi/n*k*m)
    Nn[k] = st*sum
#---------------конец------------------------------------
print('Полученные исходные данные')
print(Nn)

#--------------равенство парсиваля--------------
sumK = 0
sumNew = 0

for k in range(n):
    sumK += N[k]**2
    sumNew += Re[k]**2 + Im[k]**2

print(sumK,'    ',sumNew)
e = 0.0001
if (math.fabs(sumK-sumNew)<e):
    print('авенство Парсиваля выполнено с точностью ',e)
    print('сумма квадратов исходных данных=',sumK)
    print('сумма квадратов полученных данных=',sumNew)

#---------------конец---------------------------------------

pylab.plot(N,'-.')
pylab.plot(Nn,'b')
pylab.show()
