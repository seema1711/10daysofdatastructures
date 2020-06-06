def find(A, low, high):
    if high < low:
        return A[0]
    if high == low:
        return A[low]
    midValue = int((low + high)/2)
    if midValue < high and A[midValue+1] < A[midValue]:
        return A[midValue+1]
    if midValue > low and A[midValue] < A[midValue-1]:
        return A[midValue]
    if A[high] > A[midValue]:
        return find(A, low, midValue-1)
    return find(A, midValue+1, high)
Arr = [5,6,1,2,3,4]
n1 = len(Arr)
print(find(Arr, 0, n1-1))