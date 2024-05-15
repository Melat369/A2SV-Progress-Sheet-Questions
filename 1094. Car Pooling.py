class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passenger = [0] * 1001
        for numPass, initial, final in trips:
            passenger[initial] += numPass
            passenger[final] -= numPass
        maxPass = 0

        for numPass in passenger:
            maxPass += numPass
            if maxPass > capacity:
                return False
        return True