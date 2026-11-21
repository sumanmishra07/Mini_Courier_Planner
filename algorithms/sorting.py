
def merge_sort(parcels):
    if len(parcels) <= 1:
        return parcels
    mid = len(parcels) // 2
    left = merge_sort(parcels[:mid])
    right = merge_sort(parcels[mid:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = 0
    j = 0
    priority_rank = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }
    while i < len(left) and j < len(right):
        a = left[i]
        b = right[j]
        if (int(a["Deadline"]) < int(b["Deadline"]) or
            (int(a["Deadline"]) == int(b["Deadline"]) and
             priority_rank[a["Priority"]] >= priority_rank[b["Priority"]])):
            result.append(a)
            i += 1
        else:
            result.append(b)
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
