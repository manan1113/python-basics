# Lists in python 
# what is list: A list in python is an ordered,mutable,and indexed collection that allows duplicates. 
# It is written in square brackets.
# Can store mixed data types.(int,float,string)

# my_list = [10,20,30,40,50,"neeraj"]
# print(my_list)
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
# print(my_list[5])

# # Updating elements
# my_list[5] = "spiderman"
# print(my_list)

# # Adding elements
# my_list.append("ram")
# print(my_list)

# my_list.insert(2,"ram")
# print(my_list)

# # Removig elements
# my_list.remove(40)
# print(my_list)

# del my_list[4]
# print(my_list)

# # finding length of list
# print(len(my_list))

# # sorting 
# nums = [5,6,8,9,10,45]
# nums.sort()
# print("the list in ascending order is",nums)

# nums.sort(reverse=True)
# print("the list in desecnding order is",nums)

# # Slicing in list 
# nums = [5,3,1,9,10,15]
# print(nums[0:6:2])

# # To find second largest number 
# nums = [10,20,4,45,78,99,20,34,78]
# def second_largest(nums):
#     a = list(set(nums))
#     a.sort()
#     if len(a)<2:
#         return None
#     return a[-2]
# print("second largest number is :",second_largest(nums))

# # reversing list using slicing 
# nums = [1,2,3,4,5]
# def reverse_list(ist):
#     return ist[::-1]
# print("Reversed number is :",reverse_list(nums))

# To find pairs that makes a total of target
nums = [1,5,7,-1,5]
target = 6
def findpairs(ist,target):
    pairs = []
    for i in range(len(ist)):
        for j in range(i + 1,len(ist)):
            if ist[i]+ist[j]==target:
                pairs.append((ist[i],ist[j]))
    return pairs
print("pairs with sum ", target ," is ", findpairs(nums,target))


    



