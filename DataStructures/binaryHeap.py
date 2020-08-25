'''
Max Heap -> Parent nodes are always larger than the child
        -> Left nodes are filled first

For any index n of an array, its left child is at 2n + 1, right child is at 2n + 2,
    parent is at (n - 1) / 2

    NOTE: 1) For MinHeap, just reverse the signs in the below solutiom
          2) For Priority Queue, define a new Node as follows -

                class Node:
                    def __init__(self, val, priority):
                        self.value = val
                        self.priority = priority
                
                and just compare with self.values[idx].priority
'''

class MaxHeap:
    def __init__(self):
        self.values = []
    
    def insert(self, element):
        self.values.append(element)
        self.bubbleUp()
    
    def bubbleUp(self):
        idx = len(self.values) - 1
        element = self.values[idx]

        while idx > 0:
            parentIdx = (idx - 1) // 2
            parent = self.values[parentIdx]

            if parent >= element: # means its a maxheap
                break
            self.values[parentIdx], self.values[idx] = element, parent
            idx = parentIdx
    
    def extractMax(self):
        max = self.values[0]
        element = self.values.pop()

        if len(self.values) > 0:
            self.values[0] = element
            self.sinkDown()
        
        return max
    
    def sinkDown(self):
        idx = 0
        element = self.values[idx]
        length = len(self.values)

        while True:
            leftChildIdx = 2*idx + 1
            rightChildIdx = 2*idx + 2
            swapIdx = None

            if leftChildIdx < length:
                leftChild = self.values[leftChildIdx]
                if leftChild > element:
                    swapIdx = leftChildIdx
            
            if rightChildIdx < length:
                rightChild = self.values[rightChildIdx]
                if (swapIdx is None and rightChild > element) or (swapIdx is not None and rightChild > leftChild):
                    swapIdx = rightChildIdx
            
            if swapIdx is None:
                break

            self.values[idx], self.values[swapIdx] = self.values[swapIdx], element

            idx = swapIdx

        

    def print(self):
        print(self.values)

heap = MaxHeap()
heap.print()
heap.insert(1)
heap.print()
heap.insert(10)
heap.print()
heap.insert(5)
heap.print()
heap.insert(100)
heap.print()
heap.insert(45)
heap.print()
heap.insert(3)
heap.print()
print("======== Extracting now =======\n")
heap.extractMax()
heap.print()
heap.extractMax()
heap.print()
heap.extractMax()
heap.print()
heap.extractMax()
heap.print()
heap.extractMax()
heap.print()



