def integer_square_root(k):
    if (k == 0 or k == 1):
        return k
    
    # Binary search
    startPoint = 1
    endPoint = k
    while (startPoint <= endPoint):
        midPoint = (startPoint+endPoint) // 2
        if (midPoint*midPoint == k):
            return midPoint
        if (midPoint*midPoint < k):
            startPoint = midPoint + 1
            ans = midPoint
        else:
            endPoint = midPoint - 1
    return ans
print(integer_square_root(200))
