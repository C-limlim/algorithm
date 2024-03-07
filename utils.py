def print_array(arr):
    depth = len(arr)
    width = len(arr[0])
    
    print("===print array===")
    for i in range(depth):
        for j in range(width):
            print(arr[i][j], end =" ")
        print()
    print("=================")
