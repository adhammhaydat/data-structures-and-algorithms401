  
def merge_sort(arr):
    n = len(arr)

    if n > 1:
        mid = n//2
        left = arr[0:mid]
        right = arr[mid:n]
    #   // sort the left side
        print ("left",left)
        merge_sort(left)
    #   // sort the right side
        print("right",right)
        merge_sort(right)
    #   // merge the sorted left and right sides together
        return Merge(left, right, arr)

def Merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        
        k = k + 1
    print("left merge: ", left)
    print("right merge: ", right)
    if i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
  
    elif j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
print(merge_sort([8,4,23,42,16,15]))  