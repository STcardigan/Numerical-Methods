import random
import matplotlib.pyplot as plt

total = 1000

def circle(x, y):
    return (x**2 + y**2) < 1

inside = 0
inX = list()
inY = list()
outX = list()
outY = list()

piList = list()
Xlist = list()
for i in range(0,total):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if circle(x, y):
        inside += 1
        inX.append(x)
        inY.append(y)
    else:
        outX.append(x)
        outY.append(y)

    pi = (inside / (i+1)) * 4
    print(pi)
    piList.append(pi)
    Xlist.append(i)

plt.plot(Xlist, piList)
plt.show()
print(pi)
'''
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
circ = plt.Circle((0,0), radius=1, color='g', fill=False)
ax.add_patch(circ)
ax.plot(inX, inY, 'ro', outX, outY, 'bo')
plt.show()
'''