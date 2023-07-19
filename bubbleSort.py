# write your bubble sort algorithm below

def bubble_sort(list):
    for i in range(len(list) - 1):
        for num in range(len(list) -1):
            if list[num] > list[num + 1]:
                list[num], list[num + 1] = list[num + 1], list[num]
    return list
                
sample_list = [6,5,2,1,7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")