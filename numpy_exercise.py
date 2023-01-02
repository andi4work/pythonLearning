import numpy as np


def play_with_numers():
    arr = np.arange(1, 61)
    i = 0
    for i in arr:
        if i <= 9:
            print('10HN1A040' +str(i))
        else:
            print('10HN1A04' + str(i))



if __name__ == '__main__':
    play_with_numers()
