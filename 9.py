def binary_search(arr, item):
    for i in range(len(arr)):
        if item in arr:
            return arr.index(item)
        else:
            return -1

arr_list = [10,20,30,40,50]
n = int(input("enter the integer to find: "))
print(binary_search(arr_list, n))