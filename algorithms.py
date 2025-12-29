"""
Basic Algorithms for Logic Walkthroughs
"""

def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def count_occurrences(items):
    counts = {}
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts
