class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def _heapify_down(self, i):
        size = len(self.heap)
        while True:
            left = self.left_child(i)
            right = self.right_child(i)
            largest = i
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != i:
                self.swap(i, largest)
                i = largest
            else:
                break

    def __repr__(self):
        return f"MaxHeap({self.heap})"


def heap_sort_descending(arr):
    heap = MaxHeap()
    for num in arr:
        heap.insert(num)
    sorted_arr = []
    while heap.heap:
        sorted_arr.append(heap.extract_max())
    return sorted_arr


class LimitedMaxHeap(MaxHeap):
    def __init__(self, max_size):
        super().__init__()
        self.max_size = max_size

    def insert(self, key):
        if len(self.heap) < self.max_size:
            super().insert(key)
        else:
            if key < self.heap[0]:
                self.heap[0] = key
                self._heapify_down(0)


if __name__ == "__main__":
    print("=== Testing MaxHeap ===")
    h = MaxHeap()
    for x in [3, 1, 6, 5, 2, 4]:
        h.insert(x)
    print("Heap:", h.heap)
    print("Extract max:", h.extract_max())
    print("Heap after extract:", h.heap)

    print("\n=== Testing heap_sort_descending ===")
    arr = [5, 3, 8, 1, 2]
    print("Input:", arr)
    print("Sorted descending:", heap_sort_descending(arr))

    print("\n=== Testing LimitedMaxHeap ===")
    lm = LimitedMaxHeap(max_size=3)
    for num in [10, 20, 5, 30, 2]:
        lm.insert(num)
        print("Heap:", lm.heap)
