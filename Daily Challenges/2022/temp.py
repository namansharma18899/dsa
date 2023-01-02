# class X:
#     def any(self, num):
#         self.temp = 22
#         return self.fun(self.temp)

#     def fun(self, num):
#         self.temp = 44



# r = X()
# r.any(11)
# print(r.temp)

int_val = (1,2,3)
str_val = 'GeeksforGeeks'
flt_val = 24.56
 
# Printing the hash values.
# Notice Integer value doesn't change
# You'll have answer later in article.
print("The integer hash value is : " + str(hash(int_val)))
print("The string hash value is : " + str(hash(str_val)))
print("The float hash value is : " + str(hash(flt_val)))