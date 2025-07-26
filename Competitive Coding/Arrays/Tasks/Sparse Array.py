def matchingStrings(stringList, queries):
    # Write your code here
    counts = []
    for q in queries:
        counts.append(stringList.count(q))
    return counts