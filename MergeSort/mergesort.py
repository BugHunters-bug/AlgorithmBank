def mergeSort(inp_arr):
    
    # current length of array
    size = len(inp_arr)
    if size > 1:
        middle = size // 2
        left_arr = inp_arr[:middle]     #left half of the array
        right_arr = inp_arr[middle:]    #right half of the array
 
        mergeSort(left_arr)             #recursive call for the left half
        mergeSort(right_arr)            #recursive call for the right half
 
        lp = rp = op = 0                #lp -> pointer for left array, rp -> pointer for right array
                                        #op -> pointer for the original array

        left_size = len(left_arr)       
        right_size = len(right_arr)
        
        # compare elements from both left and right array and insert into original array
        while lp < left_size and rp < right_size:
            if left_arr[lp] < right_arr[rp]:
              inp_arr[op] = left_arr[lp]
              lp += 1
            else:
                inp_arr[op] = right_arr[rp]
                rp += 1
             
            op += 1
 
        # if there are any elements left in left array, this loop will execute
        while lp < left_size:
            inp_arr[op] = left_arr[lp]
            lp += 1
            op += 1
        
        # if there are any elements left in right array, this loop will execute
        while rp < right_size:
            inp_arr[op]=right_arr[rp]
            rp += 1
            op += 1
 
def main():
    inp_arr = [11, 31, 7, 41, 101, 56, 77, 2]
    print("Sample input: ", inp_arr)            #Sample input:  [11, 31, 7, 41, 101, 56, 77, 2]
    mergeSort(inp_arr)
    print("Sample output: ",inp_arr)            #Sample output:  [2, 7, 11, 31, 41, 56, 77, 101]
if __name__ == "__main__":
    main() 
