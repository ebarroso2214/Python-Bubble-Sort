# write your bubble sort algorithm below

def bubble_sort(list):
    swapped = False
    
    for i in range(len(list) - 1):
        print(f'Iteration')
        for num in range(len(list) -1):
            print(f'comparing {list[num], list[num+1]}')
            if list[num] > list[num + 1]:
                list[num], list[num + 1] = list[num + 1], list[num]
                swapped = True

        if not swapped:
            return        
    return list
                
sample_list = [6,5,2,7,1]
print(f'Unsorted list: {sample_list}')
bubble_sort(sample_list)
print(f'Sorted list: {sample_list}')