import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

if __name__ == "__main__":
   

    pos_array = np.genfromtxt('pos_array.out',delimiter=',')
    angle_array = np.genfromtxt('angle_array.out',delimiter=',')


    print('pos_array',pos_array.shape)
    print('angle_array',angle_array.shape)



    #time.sleep(1000)

    fig2D = plt.figure(figsize = (12,12))
    ax1 = fig2D.add_subplot(2,1,1)
    ax2 = fig2D.add_subplot(2,1,2)

    t = np.linspace(0, 6, num=30)
    ax1.plot(pos_array[0,:],pos_array[1,:],color='red')
    ax1.set_title('Position')
    ax1.set_xlim(-2,2)
    ax1.set_ylim(-1,1.5)

    ax2.plot(t,angle_array,color='green')
    ax2.set_title('Angle')

    ax2.set_ylim(0,3.14)
    
    plt.show()
    import random
