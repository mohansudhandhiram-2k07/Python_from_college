# step 1: take 2 variable max_so_far and max_ending_here = 0
# step 2: iterate through the array
# step 3: add the value od the current index to max_ending_here (sum of array)
# step 4: if max_so_far < max_ending_here, update max_so_far
# step 5: if max_ending_here < 0 update it to 0 again (reset to 0)
# step 6: return max_so_far


def max_subarray(arr):
    
    max_sum = float('-inf') 
    current_sum = 0
    
    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0 
            
    return max_sum