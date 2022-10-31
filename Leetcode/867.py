import copy

from pyparsing import col
def fun(matrix):
        tempargs = [[-1 for each in matrix] for each in matrix[0]]
        for index in range(len(matrix)):
            for colr in range(len(matrix[index])):
                tempargs[colr][index] = int(matrix[index][colr])
        return tempargs

if __name__=='__main__':
    print(fun([[1,2,3,11,12],[4,5,6,44,32],[7,8,9,43,12]]))