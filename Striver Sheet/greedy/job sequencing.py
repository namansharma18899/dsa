# class Solution:
#     # Function to find the maximum profit and the number of jobs done.
#     def JobScheduling(self, Jobs, n):
#         """
#         first sort jobs based on profit, assign a time slot from time range( job.ddline -> 1 )
#         """
#         jb = sorted(Jobs, key=lambda x: x.profit, reverse=True)
#         result = list()
#         time_ranges = [False] * (n+1)
#         for each in jb:
#             for time in range(each.deadline, 0, -1):
#                 if time_ranges[time] == False:
#                     result.append(each.profit)
#                     time_ranges[time] = True
#                     break
#         return result

class Solution:
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        Jobs = sorted(Jobs, key=lambda x: x.profit, reverse=True)
        maxi  = Jobs[0].deadline
        for index in range(1, n):
            maxi = max(maxi, Jobs[index].deadline)
        slots = [-1] *(maxi + 1)
        result = 0
        cjs= 0
        for i in range(n):
            dl = Jobs[i].deadline
            for j in range(dl, 0, -1):
                if slots[j]==-1:
                    slots[j] = i
                    cjs+=1 
                    result+=Jobs[i]
                    break
        return cjs, result

class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit


if __name__ == "__main__":
    obj = Solution()
    jobs = {(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)}
    Jobs = []
    for each in jobs:
        Jobs.append(Job(each[0], each[1], each[2]))
    print(obj.JobScheduling(Jobs, len(jobs)))
