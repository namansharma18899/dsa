import heapq
import heapq
from collections import defaultdict


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def Graph():
  def __init__(self, arr):#letarr beadjacency 
    self.graph = defaultdict(list)
    for each in arr:
      self.graph[each][0].append(each[1])
      self.graph[each[1]].append(each[0])

class MaxHeapObj(object):
  def __init__(self, val): self.val = val
  def __lt__(self, other): return self.val > other.val
  def __eq__(self, other): return self.val == other.val
  def __str__(self): return str(self.val)

class MinHeap(object):
  def __init__(self): self.h = []
  def heappush(self, x): heapq.heappush(self.h, x)
  def heappop(self): return heapq.heappop(self.h)
  def __getitem__(self, i): return self.h[i]
  def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
  def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))
  def heappop(self): return heapq.heappop(self.h).val
  def __getitem__(self, i): return self.h[i].val

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_leaf(root: TreeNode):
        if root==None or root.val=='None':
            return False  
        if (root.left==None and root.right==None):
            return True
        else:
            return False

def insertLevelOrder(array: list,i,n)-> TreeNode:
    root = None
    # i ,n= 0,len(array)
    # Base case for recursion 
    if i < n:
        root = TreeNode(array[i]) 
        # insert left child 
        root.left = insertLevelOrder(array, 2 * i + 1, n)
        # insert right child 
        root.right = insertLevelOrder(array, 2 * i + 2, n)          
    return root