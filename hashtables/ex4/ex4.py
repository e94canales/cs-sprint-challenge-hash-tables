def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    result = []

    for num in a:
        num = abs(num)
        if num not in d:
            d[num] = 0
        d[num] += 1

    result = [num[0] for num in d.items() if num[1] >= 2]
    

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
