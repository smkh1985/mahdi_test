import pandas as pd 
import numpy as np 

from matplotlib import pyplot as plt 
import os


def main():
    print('This code is written by SMKH1985')
    x = np.arange(0,10,0.1)
    y = np.sin(x)
    plt.plot(x,y)
    plt.title('y = Sin(x)')
	plt.xlable('x')
	plt.ylable('y')
    plt.show()
    
if __name__ == "__main__":
    if os.path.exists('Folder'):
        print('directory is ok')
    main()