import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

COLS=10
ROWS=10
#np.random.seed(19680801)

grid=np.random.choice(a=[False, True], size=(ROWS,COLS))

def count_neighbors(arr,x,y):
    tot=0
    for i in range(-1,2):
        for j in range(-1,2):
            posx=(x+i+len(arr[0]))%len(arr[0])
            posy=(y+j+len(arr))%len(arr)
            tot+=arr[posy][posx]
    return tot-arr[y][x]

figure,ax=plt.subplots()

def draw(frame):
    global grid
    plot=plt.imshow(grid)
    next_grid=np.empty((ROWS,COLS),dtype=bool)
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            state=grid[j][i]
            neighbors=count_neighbors(grid,i,j)
            if state and(neighbors<2 or neighbors>3):
                next_grid[j][i]=0
            elif not state and (neighbors==3):
                next_grid[j][i]=1
            else:
                next_grid[j][i]=state

    grid =next_grid
    return plot

animation = FuncAnimation(figure, draw, interval=200)

plt.show()   

