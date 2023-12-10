#define your function here:
def getAttribute(subtrees, attr) -> list:
    results = []
    for subtree in subtrees:
        if subtree.has_attr(attr):
            results.append(subtree[attr])
    return results