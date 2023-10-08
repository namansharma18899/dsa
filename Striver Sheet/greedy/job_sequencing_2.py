import heapq


class Job:
    def __init__(self, profit, deadline, id) -> None:
        self.profit = profit
        self.deadline = deadline
        self.id = id


class Solution:
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs: list, n: int):
        Jobs = sorted(Jobs, key=lambda x: (x.deadline, x.profit))
        prev = Jobs[0]
        hp = [prev.profit]
        heapq.heapify(hp)
        size = 1
        Jobs.pop(0)
        for each in Jobs:
            if size < each.deadline:
                heapq.heappush(hp, each.profit)
                size += 1
            else:
                heapq.heapreplace(hp, each.profit)
        return len(hp), sum(hp)


sol = Solution()

arr = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 1, 15)]

print(sol.JobScheduling(arr, len(arr)))
