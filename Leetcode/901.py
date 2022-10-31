from audioop import reverse


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = []
        if not self.stack:
            self.stack.append(int(price))
            return 1
        # print(self.stack)
        res = []
        # import pdb; pdb.set_trace()
        while(self.stack and (int(self.stack[len(self.stack)-1]) <= price)):
            res.append(self.stack.pop())
        if len(res)!=0:
            self.stack +=res[::-1]
        self.stack.append(price)
        # print(self.stack)
        return len(res)+1

pc = [100,80,60,70,60,75,85]
pc = [29,91,62,76,51]
pc =[28,14,28,35,46,53,66,80,87,88]
obj = StockSpanner()
for each in pc:
    print(obj.next(each))