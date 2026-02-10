#chocolate distribution algorithm
# step1: sort the array
# step2: make the array as groups of number of students
# step3: find the difference between the min and max of the group
# step4: choose the group with the minimum difference

def min_diff(packets,m):
    n = len(packets)
    packets.sort()

    min_diff = float('inf')
    
    for i in range(n-m+1):
        curr_diff = packets[i+m-1] - packets[i]
        if curr_diff < min_diff:
            min_diff = curr_diff
    
    return min_diff



if __name__ == "__main__":
    chocolates = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42]
    children = 7
    
    result = min_diff(chocolates, children)
    print(f"Minimum difference is {result}")