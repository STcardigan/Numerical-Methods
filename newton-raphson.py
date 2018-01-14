import matplotlib.pyplot as plt

repeat = 20
number = 13

def guess(x):
    a = 2
    while (x>=(a**2)):
        a+=1
    return a-1

def newton(a,x,i):
    piListY = list()
    piListX = list()

    for i in range(0, i):
        piListY.append(x)
        piListX.append(i)

        x = x - (x**2-a)/(2.0*x)
    return piListX,piListY,x

guessNum = guess(number)
piListX,piListY,pi = newton(number,guessNum,repeat)

print(piListY)
print(piListX)
print(pi)

plt.plot(piListX, piListY)
plt.show()
