import datetime
from utils.utility import TreeNode, insertLevelOrder, swap

def fun(arr):
    root = insertLevelOrder(arr, 0,len(arr))
    return minimum_ops(root)
#
# Inefficient approach...too slow cause of regular searches for element which will take additional time
# def minimum_shifts(arr):
#     # 27 29 17
#     # import pdb; pdb.set_trace()
#     arr = [int(element.val) for element in arr if element.val.isnumeric()]
#     print('arr -> ', arr)
#     sorted_arr = sorted(arr)
#     operations =0
#     for index in range(0, len(arr)):
#         if sorted_arr[index]!=arr[index]:
#             #find(arr[index])
#             original_index = arr.index(sorted_arr[index])
#             swap(arr, index, original_index)
#             operations+=1
#     return operations

def minimum_shifts(arr):
    # 27 29 17
    import pdb; pdb.set_trace()
    value_index_dict = {int(element.val):index for index, element in enumerate(arr) if element.val.isnumeric()}
    arr = [int(x.val) for x in arr if x.val.isnumeric()]
    # value_index_hashmap = {index: int(element.val) for index, element in enumerate(arr) if element.val.isnumeric()}
    # print('arr -> ', arr)
    sorted_arr = sorted(arr)
    operations =0
    for index in range(0, len(arr)):
        # if sorted_arr[index]!=arr[index]:
        original_index = value_index_dict[sorted_arr[index]]
        if sorted_arr[index] not in value_index_dict.keys():
            continue 
        # original_index = arr[sorted_arr[index]]
        # print(original_index, index)
        if original_index!=index:
            #valueindexhashmap remap
            # print('mismatch -> ', arr[index], arr[original_index])
            value_index_dict[sorted_arr[index]]=index
            del value_index_dict[sorted_arr[index]]
            # value_index_dict[arr[original_index]]=original_index
            swap(arr, index, original_index)
            operations+=1
        # print('dict -> ',value_index_dict)
    # print('Arr -> ', arr)
    return operations

def minimum_ops(root: TreeNode):
    #level order
    queue = [root]
    result = 0
    while(len(queue)>0):
        queue_size = len(queue)
        while(queue_size>0):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            queue_size-=1
            # print('q -> ', queue, ' qsize -> ', queue_size)
        result+=minimum_shifts(queue)
    return result

if __name__=='__main__':
    tcs = int(input())
    while(tcs>0):
        start = datetime.datetime.now();
        print('res -> ',fun(input().split(',')))
        timeTaken = datetime.datetime.now() - start;
        print("Total time taken : " ,timeTaken ," milliseconds");
        tcs-=1


# 1,3,2,7,6,5,4