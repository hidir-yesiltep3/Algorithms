# Quick Sort implementation in Python

class QuickSort:
    def __init__(self, arr):
        self.arr = arr
    
    def _partition(self, p, r):
        """
        Args:
            arr: Array to be sorted
            p:   Start pointer of the array
            r:   End   pointer of the array 

        Note:
            Indexing is zero-based   
        """

        x = self.arr[r]
        i = p - 1
        for j in range(p, r):
            if self.arr[j] <= x:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i + 1], self.arr[r] = self.arr[r], self.arr[i + 1]

        return i + 1

    def sort(self, p, r):
        """
        Sort method of the QuickSort.
        First partitiones the array into two and sorts left and right part recursiveley.
        Sorts in-place.

        Args:
            p: Left  pointer to the array to be sorted
            r: Right pointer to the array to be sorted
        """
        if p < r:
            q = self._partition(p, r)
            self.sort(p, q - 1)
            self.sort(q + 1, r)
        
        return self.arr

if __name__ == '__main__':
    arr = [2, 8, 7, 1, 3, 5, 6, 4]
    qs = QuickSort(arr)
    print(qs.sort(0, len(arr) - 1))

