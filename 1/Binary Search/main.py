# We have total two ways to calculate the binaty search 1. Recursive Method 
# 2. Iterative Method
# 
# Here, both of the functions are written.

# 1. Recursive Method

def binary_search_recursive(start,end,sorted_lst,target):

    if start <= end:
        # find the middle position of the sorted list
        mid = (start+end) // 2

        # check if the target is already at middle position
        if sorted_lst[mid] == target:
            return mid + 1

        # if the target is not at middle position, 
        # then chenge the range from start to mid - 1, since less than middle
        elif target < sorted_lst[mid]:
            return binary_search_recursive(start,mid-1,sorted_lst,target)

        # if target is not at middle position,
        # change the range from mid+1 to end, since greater thatn middle
        elif target > -sorted_lst[mid]:
            return binary_search_recursive(mid+1, end, sorted_lst, target)

        # if the target is not in present in sorted list
        else:
            return -1


# Iterative Method

def binary_search_iterative(start, end, sorted_lst,target):
    # set position of targer at -1
    position = -1

    # iterate over all values in sorted list
    while(start <= end):
        middle = (start + end) // 2

        if sorted_lst[middle] == target:
            position = middle
            return position

        elif target < sorted_lst[middle]:
            end = middle - 1

        elif target > sorted_lst[middle]:
            start = middle +1

# take the range of input user wants to input
length = int(input('Enter the length of the list: '))
sorted_lst = []

for i in range(length):
    inp = int(input('Enter the input value: '))
    sorted_lst.append(inp)

print("Before sorting", sorted_lst)
sorted_lst = sorted(sorted_lst)
print("After sorting", sorted_lst)

target = int(input("Enter the target value: "))

choice = int(input("Enter 1 for Recursive Method 2 for Interative Method: "))
if choice == 1:
    position = binary_search_recursive(0,length-1,sorted_lst,target)

else:
    position = binary_search_iterative(0,length-1,sorted_lst,target)

if position == -1:
    print("Value is not in the inputted list")

else:
    print(f"Value is in the inputted list at {position}")