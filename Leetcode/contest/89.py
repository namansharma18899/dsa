def fun(args):
    arg=[]
    # print(args)
    for each in args:
        if not each=='?' and not each==':':
            # print('sss -> ',each, args)
            arg.append(int(each))
        else:
            arg.append(each)
    hours , min = arg[0:2], arg[3:]
    # print(hours,min)
    count = 1
    # import pdb; pdb.set_trace()
    if '?' in hours:
        if '?' in str(hours[0]):
            if '?' in str(hours[1]):
                count=count*24
            else:
                if int(hours[1])<4:
                    count=count*3
                else:
                    count=count*2
        else:
            if '?' in str(hours[0]):
                count=count*24
            else:
                if int(hours[0])==2:
                    count=count*4
                else:
                    count=count*10
    if '?' in str(min[0]):
        if '?' in str(min[1]):
            count=60
        else:
            count = count*6
    return count



if __name__=='__main__':
    file1 = open('./testcase.txt', 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
        print(line.split('|')[0])
        res = fun(line.split('|')[0])
        expected = line.split('|')[1]
        try:
            # print(str(res)==str(expected))
            assert str(res) == str(expected)
        except Exception as e:
            print(type(e))
            print(f'FAILED {res}, expected {expected}')
        print(f'Passed {res}, expected {expected}')
        