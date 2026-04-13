class MaxHeap:

    def __init__(self):
        self._heap = []

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def get_size(self) -> int:
        return len(self._heap)

    def _parent(self, index: int) -> int:
        return (index - 1) // 2

    def _left_child(self, index: int) -> int:
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        return 2 * index + 2

    def _swap(self, i: int, j: int) -> None:
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def insert(self, element) -> None:
        self._heap.append(element)
        self._heapify_up(len(self._heap) - 1)

    def _heapify_up(self, index: int) -> None:
        parent_index = self._parent(index)

        if index > 0 and self._heap[parent_index] < self._heap[index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def extract_max(self):
        if self.is_empty():
            return None
            
        if len(self._heap) == 1:
            return self._heap.pop()

        max_val = self._heap[0]

        self._heap[0] = self._heap.pop()
        self._heapify_down(0)
        
        return max_val

    def _heapify_down(self, index: int) -> None:
        largest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self._heap) and self._heap[largest] < self._heap[left]:
            largest = left

        if right < len(self._heap) and self._heap[largest] < self._heap[right]:
            largest = right

        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)
            
    def peek(self):
        if self.is_empty():
            return None
        
        return self._heap[0]
