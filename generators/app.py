def square_numbers (nums):
    
    for i in nums:
        yield (i*i) #this makes it a generator
   

my_nums = square_numbers([1,2,3,4,5])

print(my_nums)
# print next(my_nums)
# print next(my_nums)
# print next(my_nums)
# print next(my_nums)
# print next(my_nums)
#print next(my_nums) will result in error

for num in my_nums:
    print (num)


##Using list comprehension

my_nums1 = [x*x for x in [1,2,3,4,5]]

print(my_nums)

my_num2 = (x*x for in [1,2,3,4,5]) #generator

