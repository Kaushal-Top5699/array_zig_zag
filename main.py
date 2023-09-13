def zigZag(arr, n):
    def switch(arr, i):
        temp = arr[i + 1]
        arr[i + 1] = arr[i]
        arr[i] = temp

    for i in range(n):
        if i == 0 and i != n - 1:
            if arr[i] > arr[i + 1]:
                switch(arr, i)
        elif i != 0 and i != n - 1:
            if (arr[i + 1] > arr[i] > arr[i - 1]) or (arr[i + 1] < arr[i] < arr[i - 1]):
                switch(arr, i)
            elif (arr[i] < arr[i + 1] and arr[i] < arr[i - 1]) or (arr[i] > arr[i + 1] and arr[i] > arr[i - 1]):
                continue
    return arr


a = [1, 4, 3, 2]
print(zigZag(a, len(a)))
