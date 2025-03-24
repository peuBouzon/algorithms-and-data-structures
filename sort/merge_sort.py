def sort(x, start, end):
    _sort(x, start, end, [n for n in x])
    return x

def _sort(x, start, end, aux):
    if (end <= start):
        return
    middle = start + (end - start) // 2
    _sort(x, start, middle, aux)
    _sort(x, middle + 1, end, aux)
    _merge(x, start, middle, end, aux)

def _merge(x, start, middle, end, aux):
    aux[start:end] = x[start:end]
    i, j = start, middle + 1
    for k in range(start, end + 1):
        if i > middle:
            x[k] = aux[j]
            j += 1
        elif j > end:
            x[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            x[k] = aux[i]
            i += 1
        else:
            x[k] = aux[j]
            j += 1

if __name__ == '__main__':
    x = [3, 0, 1, 5, 7]
    print(sort(x, 0, len(x) - 1))