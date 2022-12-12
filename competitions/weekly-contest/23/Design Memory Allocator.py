# from utils import *
class Allocator:
    def __init__(self, n: int):
        self.space = [-1]*n
        self.mid = {}

    def allocate(self, size: int, mID: int) -> int:
        count = 1 if self.space[0]==-1 else 0
        start_index = 0
        found_space_flag = False
        if size>len(self.space):
            return -1
        for index in range(1, len(self.space)):
            if count==size:
                found_space_flag=True
                start_index=index-1
                break
            if self.space[index]==-1:
                if self.space[index-1]!=-1:
                    count=1
                    start_index=index
                else:
                    count+=1
            if count==size:
                found_space_flag=True
                break
        print(found_space_flag, start_index)
        if found_space_flag:
            for x in range(start_index, start_index+size):
                self.space[x]=1
            if mID not in self.mid.keys():
                self.mid[mID] = [int(x) for x in range(start_index, start_index+size)]
            else:
                self.mid[mID]+=[int(x) for x in range(start_index, start_index+size)]
            return start_index
        return -1

    def free(self, mID: int) -> int:
        if mID not in self.mid.keys():
            return 0
        space_to_free = self.mid[mID]
        self.mid[mID]=[]
        for each in space_to_free:
            self.space[each]=-1
        return len(space_to_free)

def fun(args):
    alc = Allocator(n=args)
    num_actiosn = int(input())
    while(num_actiosn>0):
        mem = int(input())
        if mem==1:
            actions = [int(x) for x in input().split(',')]
            print('allocate res -> ', alc.allocate(actions[0],actions[1]))
        else:
            print('free res -> ', alc.free(int(input())))


if __name__=='__main__':
    print(fun(int(input())))