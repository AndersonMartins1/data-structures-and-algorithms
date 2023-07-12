def bucket_sort(arr):
    #create the list of buckets
    buckets = [[] for i in arr]
    arr_len = len(arr)

    #put elements in bucket
    for i in arr:
        buckets[int(arr_len*i)].append(i)

    #sort all elements in buckets
    for j in range(len(arr)):
        #change this later on
        buckets[j] = sorted(buckets[j])

    #put sorted elements back in array
    k = 0
    for i in range(len(arr)):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k+=1


arr = [0.32,0.22,0.66,0.25,0.31,0.44,0.37]
bucket_sort(arr)
print(arr)