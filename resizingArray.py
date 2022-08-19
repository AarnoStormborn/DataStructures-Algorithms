from dataclasses import dataclass
import numpy as np

@dataclass
class ResizingArray:
    capacity: int # max size of array

    def __post_init__(self):
        self.myArr = np.zeros(self.capacity, dtype=np.int64)
        self.N = 0

    def isEmpty(self):
        return self.N == 0

    def resizeByDouble(self):
        if self.N + 1 == self.capacity:
            tempArr = np.zeros(self.capacity*2, dtype=np.int64)
            for i in range(self.N):
                tempArr[i] = self.myArr[i]
            self.myArr = tempArr
            self.capacity = self.capacity*2
            print(f"Resized from {self.capacity} to {self.capacity*2}")

    def addToArray(self, num):
        self.myArr[self.N] = num
        self.N += 1
        self.resizeByDouble()
        
    def resizeByHalf(self):
        if self.N - 1 == self.capacity:
            tempArr = np.zeros(self.capacity//2, dtype=np.int64)
            for i in range(self.N):
                tempArr[i] = self.myArr[i]
            self.myArr = tempArr
            self.capacity = self.capacity//2
            print(f"Resized from {self.capacity} to {self.capacity//2}")
        return self.myArr

    def __str__(self) -> str:
        return f"updated array: {self.myArr}"

# Driver code
if __name__=='__main__':
    arr = ResizingArray(10)

    randomList = np.random.randint(1,100,100)
    for i in randomList:
        arr.addToArray(i)