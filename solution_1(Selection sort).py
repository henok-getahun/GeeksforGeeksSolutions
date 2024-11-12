class Solution:
    def select(self, arr, i):
        minIdx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIdx]:
                minIdx = j
        return minIdx

    def selectionSort(self, arr, n):
        for i in range(n):
            minIdx = self.select(arr, i)
            arr[i], arr[minIdx] = arr[minIdx], arr[i]
        return arr
