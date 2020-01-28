import matplotlib.pyplot as plt
import os
xpoints=[]
ypoints=[]
img = plt.imread('complexity-graph.png')

def log(x,y):
    xpoints.append(x)
    ypoints.append(y)

def plot(name):
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[0, 400, 0, 300])
    ax.plot(xpoints,ypoints, '--', linewidth=3, color='firebrick')
    plt.savefig(name)


log(10, 10)
log(20,20)
log(30,30)
log(60,60)
log(100,100)
log(200,200)
plot("test.png")
