from typing import List

def sort(input: List):
    index_smallest = 0
    for i in range(0, len(input) - 1):
        index_smallest = i
        for j in range(i + 1, len(input)):
            if input[j] < input[index_smallest]:
                index_smallest = j

        tmp = input[i]
        input[i] = input[index_smallest]
        input[index_smallest] = tmp
    return input
