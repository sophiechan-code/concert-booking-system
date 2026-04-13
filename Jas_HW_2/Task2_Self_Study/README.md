# Self-Study: Max Heap and Heap Sort (Task 2)

## Data Structure: Max Heap
- **Abstract Data Type**: A complete binary tree where each parent node is greater than or equal to its children.
- **Key Methods**:
  - `insert(element)`: O(log n)
  - `extract_max()`: O(log n)
  - `peek()`: O(1)
- **Applications**: Priority queues, scheduling, Dijkstra's algorithm.

## Algorithm: Heap Sort
- **Type**: Comparison-based, in-place sorting
- **Time Complexity**:
  - Best/Average/Worst: O(n log n)
  - Space: O(1)
- **Steps**:
  1. Build a max heap from input array.
  2. Repeatedly swap root with last element, reduce heap size, and heapify.

## Implementation
- `data_structures/heap.py`: MaxHeap class
- `algorithms/heap_sort.py`: heap_sort function

## Video Demonstration
Watch the 5-minute explanation video here:  
[INSERT YOUR VIDEO LINK HERE]

## GitHub Repository
https://github.com/sophiechan-code/concert-booking-system
