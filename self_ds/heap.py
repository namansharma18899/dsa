from Leetcode.utils.utility import timer
import heapq
import random

@timer
def effecient_python_heapq(arr):
    heapq.heapify(arr)

def print_heap(arr, N):
    print("Array representation of Heap is:")
    for i in range(N):
        print(arr[i], end=" ")
    print()


def heapify(arr: list, N: int, ind: int):
    L = 2*ind + 1
    R = 2*ind + 2
    largest = ind
    if L < N and arr[L] > arr[largest]:
        largest = L
    if R < N and arr[R] > arr[largest]:
        largest = R
    if (
        largest != ind
    ):  # Left or Right has greater value, swap and heapify the subtree for upcoming new L/R
        arr[ind], arr[largest] = arr[largest], arr[ind]
        heapify(arr, N, largest)  # largest -> L/R

@timer
def build_heap(arr: list, N: int):
    last_non_leaf_node = (N//2) - 1
    for index in range(last_non_leaf_node, -1, -1):
        heapify(arr, N, index)


if __name__ == "__main__":
    arr = [random.randrange(100000) for x in range(100000)]
    arr1= arr+[]
    arr2 = arr+[]
    build_heap(arr1, len(arr))
    effecient_python_heapq(arr2)
