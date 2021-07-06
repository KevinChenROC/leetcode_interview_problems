# add val to the range [lo, hi]


def add(arr, N, lo, hi, val):

    arr[lo] += val
    if hi < N - 1:
        arr[hi + 1] -= val


# Utility method to get actual
# array from operation array


def updateArray(arr, N):

    # convert array into prefix sum array
    for i in range(1, N):
        arr[i] += arr[i - 1]


# method to print final updated array


def printArr(arr, N):

    updateArray(arr, N)
    for i in range(N):
        print(arr[i], end=" ")
    print()


# Driver code
N = 5
arr = [0] * N

# Range addition Queries
add(arr, N, 0, 2, 1)
add(arr, N, 1, 3, 1)
add(arr, N, 2, 3, 1)

updateArray(arr, N)
print(arr)
