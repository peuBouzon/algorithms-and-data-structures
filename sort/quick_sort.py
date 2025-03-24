# Quicksort
def sort(x):
    _sort(x, 0, len(x) - 1)
    return x

def _sort(x, start, end):
    if end <= start:
        return
    partition_index = _partition(x, start, end)
    _sort(x, start, partition_index)
    _sort(x, partition_index + 1, end)

def _partition(x, start, end):
    i, j = start + 1, end
    partition_element = x[start]
    while True:
        while x[i] <= partition_element:
            if i == end:
                break
            i += 1
        while x[j] >= partition_element:
            if j == start:
                break
            j -= 1

        if i >= j:
            break
        x[i], x[j] = x[j], x[i]
    
    x[start], x[j] = x[j], x[start]
    return j

if __name__ == '__main__':
    x = [3, 0, 1, 5, 7]
    print(sort(x))