#дискретное преобразование фурье
import numpy as np
import math

n = 10 #количевство значений
N = np.random.randint(0,20,(n))
#n=2
#N=([3,5])
Re = np.zeros(n, dtype=np.float) #массив действительных чисел
Im = np.zeros(n, dtype=np.float) #массив мнимых чисел
st = 1/(math.sqrt(n))
for m in range(n):
    sumRe = 0
    sumIm = 0
    for k in range(n):
        sumRe += N[k]*math.cos(2*math.pi/n*k*m)
        sumIm += N[k]*math.sin(2*math.pi/n*k*m)
        #print(math.sin(((2*math.pi)/n)*k*m),'test')
        #print('m='+str(m)+' k='+str(k)+' sin(((2*math.pi)/n)*k*m)='+str(math.sin(2*math.pi/n*k*m))+' 2*math.pi/n='+str(2*math.pi/n))
    Re[m] = st*sumRe
    Im[m] = -(st*sumIm)
print('Исходные данные')
print(N)
print('Действительные значения')
print(Re)
print('Мнимые значения')
print(Im)
