def count_and_say(n):
    if n == 1: return "1"
    prev = count_and_say(n - 1) # Recursive call
    result = ""
    count = 1
    
    for i in range(len(prev)):
        # If next char is same, increment count. Handle out-of-bounds!
        if i + 1 < len(prev) and prev[i] == prev[i+1]:
            count += 1
        else:
            result += str(count) + prev[i]
            count = 1 # Reset count for the next distinct character
            
    return result