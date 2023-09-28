class Train:
    def __init__(self, arr, dep):
        self.arr = arr
        self.dep = dep


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

obj = list()
for index in range(0, 3):
    obj.append(Train(arr[index], dep[index]))

obj.sort(key=lambda x: x.dep)
for each in obj:
    print(each.arr)
