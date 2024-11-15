def quicksort(data, left, right):
    if left+1 >= right:
        return
    ai, bi, ci = left, (left+right)//2, right-1
    a, b, c = data[ai], data[bi], data[ci]
    if a < b:
        if c < a:
            pos = ai
        elif c < b:
            pos = ci
        else:
            pos = bi
    else:
        if c < b:
            pos = bi
        elif c < a:
            pos = ci
        else:
            pos = ai
    pivot = data[pos]
    data[pos] = data[right-1]
    tail = left
    for i in range(left, right-1):
        if data[i] < pivot:
            data[tail], data[i] = data[i], data[tail]
            tail += 1
    data[right-1], data[tail] = data[tail], pivot
    quicksort(data, left, tail)
    quicksort(data, tail+1, right)

mydict = { 'a': 1, 'b': 4, 'c': 9, 'd': 3, 'e': 1 }
values = [value for key, value in mydict.items()]
quicksort(values, 0, len(values))
print(values)