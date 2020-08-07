# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for string in files:
        word = string.split("/")[-1]

        if word not in cache and "nofile" not in word:
            cache[word] = [string]
        elif word in cache:
            cache[word].append(string)


    for q in queries:
        if q in cache:
            result.append(cache[q])

    flattenedResults = [finalRes for arr in result for finalRes in arr]
    return flattenedResults


if __name__ == "__main__":
    files = []

    for i in range(500000):
        files.append(f"/dir{i}/file{i}")

    for i in range(500000):
        files.append(f"/dir{i}/dirb{i}/file{i}")

    queries = []

    for i in range(1000000):
        queries.append(f"nofile{i}")

    queries += [
        "file3490",
        "file256",
        "file999999",
        "file8192"
    ]
    print(finder(files, queries))

    # ['/dir256/dirb256/file256',
    #         '/dir256/file256', '/dir3490/dirb3490/file3490',
    #         '/dir3490/file3490', '/dir8192/dirb8192/file8192',
    #         '/dir8192/file8192']
