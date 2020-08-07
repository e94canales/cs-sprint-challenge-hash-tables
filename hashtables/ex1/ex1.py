def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    d = {}
    
    for index, num in enumerate(weights):
        if limit - num in d:
           return [index, d[limit - num]]
        d[num] = index

    return None        

# weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# print(get_indices_of_item_weights(weights_4, 9, 7))
