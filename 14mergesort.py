def mergesort(lst):
    if len(lst) <= 1:
        return lst        # <--- MUST return the list

    mid = len(lst) // 2
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])

    return merge(left, right)    # <--- MUST return merge result


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add leftovers
    result.extend(left[i:])
    result.extend(right[j:])


    return result

