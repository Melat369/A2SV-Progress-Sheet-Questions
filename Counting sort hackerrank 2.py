import os
import sys

def countingSort(arr):
    # Create a frequency array with 100 elements initialized to 0
    frequency = [0] * 100

    # Count the occurrences of each value in the input array
    for num in arr:
        frequency[num] += 1

    return frequency

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()