from operator import le, ge

class Heap:
    def __init__(self, strategy='max') -> None:
        self.heap = []
        self.count = 0
        self.op = le if strategy == 'max' else ge

    @classmethod
    def build(cls, heap, strategy='max'):
        instance = cls(strategy)
        instance.heap = heap
        instance.count = len(heap)

        for non_child_idx in range((instance.count // 2) - 1, -1, -1):
            instance.heapify(non_child_idx)

        return instance

    def insert(self, value):
        self.heap.append(value)
        self.count += 1
        self.heapify_insert(self.count-1)

    def heapify_insert(self, index):
        parent = (index-1) // 2
        if (parent >= 0) and self.op(self.heap[parent], self.heap[index]):
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapify_insert(parent)

    def delete(self):
        self.heap[0], self.heap[self.count-1] = self.heap[self.count-1], self.heap[0]
        self.count -= 1
        self.heapify(0)
        return self.heap.pop()

    def heapify(self, current_root):
        heap_strategy_extreme = current_root
        left_child = 2*current_root + 1
        right_child = left_child + 1
        if (right_child < self.count) and self.op(self.heap[heap_strategy_extreme], self.heap[right_child]):
            heap_strategy_extreme = right_child

        if (left_child < self.count) and self.op(self.heap[heap_strategy_extreme], self.heap[left_child]):
            heap_strategy_extreme = left_child

        if heap_strategy_extreme != current_root:
            self.heap[heap_strategy_extreme], self.heap[current_root] = self.heap[current_root], self.heap[heap_strategy_extreme]
            self.heapify(heap_strategy_extreme)


def heap_sort(array, ascending=True):
    # To remove auxilary space, convert heapify method to a function call
    # Then use for loop from size-1 to 1 and just swap the top with the last
    # This will keep sorting the array, as the top element will be only max or min
    # based on the strategy chosen
    strategy = 'min' if ascending else 'max'
    heap = Heap.build(array, strategy)
    sorted_array = [heap.delete() for _ in range(heap.count)]
    return sorted_array


if __name__ == '__main__':
    arr = [10, 5, 3, 6, 4]
    max_heap = Heap.build(arr)
    print("Built Max heap:", max_heap.heap)

    max_heap.insert(15)
    print("After Insertion of 15:", max_heap.heap)

    max_heap.delete()
    print("After Deletion of 15:", max_heap.heap)

    arr = heap_sort(arr, ascending=True)
    print("After sorting:", arr)
