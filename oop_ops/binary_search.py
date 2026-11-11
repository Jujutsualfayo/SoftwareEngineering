def binary_search(numbers, target):
    left = 0
    right = len(numbers)-1
    
    while left <= right:
        middle = (left + right) // 2
        
        if numbers[middle] == target:
          return middle
        elif numbers[middle] < target:
         left = middle + 1
        else:
          right = middle - 1
        
    return -1