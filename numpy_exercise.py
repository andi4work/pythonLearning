import numpy as np


# def play_with_numbers():
#     arr = np.arange(1, 61)
#     i = 0
#     for i in arr:
#         if i <= 9:
#             print('10HN1A040' +str(i))
#         else:
#             print('10HN1A04' + str(i))

def play_with_numbers():
    print(np.zeros(shape=10))
    print(np.ones(shape=10))
    print(np.ones(shape=10) * 5)
    print(np.arange(10, 51))

    # Print Even numbers
    print(np.arange(10, 51, 2))
    # To reshape 3*3 matrix
    print(np.arange(9).reshape(3, 3))
    # To print identical matrix
    print(np.eye(3))
    # To print 5 random number between 0,1
    print(np.random.rand(5))
    # To print an array of 25 positive random numbers between 0,1
    print(np.random.rand(25))
    # To print an array of 25 random numbers
    print(np.random.randn(25))
    # To print a 10*10 matrix with 0.01 as 1st element and 1.0 as the last element
    print(np.arange(1, 101).reshape(10, 10) / 100)
    # To print a 5*5 matrix 1-->25
    print(np.arange(1, 26).reshape(5, 5))

    # Slicing a matrix
    arr = np.arange(1, 26).reshape(5, 5)
    print(arr[2:,1:])
    print(arr[3:,3:])

    # Sum of all values in the matrix
    print(np.sum(arr))

    #


if __name__ == '__main__':
    play_with_numbers()
