# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for string in files:
        words = string[1:].split("/")
        for word in words:
            if word not in cache:
                cache[word] = []
            
            cache[word].append(string)

    result = [paths[1] for paths in cache.items() if paths[0] in queries]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
