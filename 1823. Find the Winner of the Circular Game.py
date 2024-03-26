class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        array = []
        ind = 0
        for index in range(1,n+1):
            array.append(index)

        while len(array) != 1:
            ind = (ind+k-1)%len(array)
            array.remove(array[ind])

        return array[0]


