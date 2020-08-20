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


def logistic_regression(x,y):
    print('Everything is ok')
    print('Results are successfull')

def normalization(x):
    # normalize data
    return x_normal

if __name__ == "__main__":
    if os.path.exists('Folder'):
        print('directory is ok')
    main()