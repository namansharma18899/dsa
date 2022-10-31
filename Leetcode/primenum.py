from operator import is_
from pydoc import ispackage


n = 39
is_prime = [True for index in range(0,n+2)]
is_prime[0] ,  is_prime[1] = False, False

#we need to precompute/mark all the elemtns divsible by 2
inner=0
count = 0
for i in range(2, n+1):
    count+=1
    inner = 0
    if is_prime[i]==True and i*i<=n:
        for j in range(i*i, n+1,i):
            inner+=1
            is_prime[j]=False
    print('inner -> ',inner, i)

print('coinnt -> ', count)
print(len([x for x in is_prime  if x == True]))
# for index in range(0, len(is_prime)):
#     print('index ->', index, ' = ', is_prime[index])