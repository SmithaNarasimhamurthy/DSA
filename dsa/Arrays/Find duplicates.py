def find_duplicates(arr):
    freq = {}
    result = []

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num, count in freq.items():
        if count > 1:
            result.append(num)

    return result if result else [-1]

arr = [1, 6, 6, 2, 3, 3, 2]
print(find_duplicates(arr))
