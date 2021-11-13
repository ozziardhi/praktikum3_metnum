import numpy as np

n=int(input('masukan jumlah titik data :'))


x=np.zeros((n))
y=np.zeros((n))

print('masukan data x dan y')
for i in range(n):
    x[i]=float(input('x['+str(i)+']='))
    y[i]=float(input('y['+str(i)+']='))

xp=float(input('masukan x yang di inginkan:'))

yp=0

for i in range(n):
    p=1

    for j in range(n):
        if i !=j:
            p=p*(xp-x[j])/(x[i]-x[j])

    yp=yp+p*y[i]
print('nilai interpolasi untuk %.3f adalah %.3f.'%(xp,yp))        

