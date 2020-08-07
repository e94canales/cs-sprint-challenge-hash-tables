def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    result = []

    for array in arrays:
        for num in array:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
    
    for num in d.items():
        if num[1] is len(arrays):
            result.append(num[0])


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
