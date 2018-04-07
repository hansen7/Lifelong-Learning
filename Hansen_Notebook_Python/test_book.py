# Python program to find maximum product subarray
 
# Returns the product of max product subarray.
# Assumes that the given array always has a subarray
# with product more than 1
def maxsubarrayproduct(arr):
 
    n = len(arr)
 
    # max positive product ending at the current position
    max_ending_here = 1
 
    # min positive product ending at the current position
    min_ending_here = 1
 
    # Initialize maximum so far
    max_so_far = 1
 
    # Traverse throughout the array. Following values
    # are maintained after the ith iteration:
    # max_ending_here is always 1 or some positive product
    # ending with arr[i]
    # min_ending_here is always 1 or some negative product
    # ending with arr[i]
    for i in range(0,n):
 
        # If this element is positive, update max_ending_here.
        # Update min_ending_here only if min_ending_here is
        # negative
        if arr[i] > 0:
            max_ending_here = max_ending_here*arr[i]
            min_ending_here = min (min_ending_here * arr[i], 1)
 
        # If this element is 0, then the maximum product cannot
        # end here, make both max_ending_here and min_ending_here 0
        # Assumption: Output is alway greater than or equal to 1.
        elif arr[i] == 0:
            max_ending_here = 1
            min_ending_here = 1
 
        # If element is negative. This is tricky
        # max_ending_here can either be 1 or positive.
        # min_ending_here can either be 1 or negative.
        # next min_ending_here will always be prev.
        # max_ending_here * arr[i]
        # next max_ending_here will be 1 if prev
        # min_ending_here is 1, otherwise
        # next max_ending_here will be prev min_ending_here * arr[i]
        else:
            temp = max_ending_here
            max_ending_here = max (min_ending_here * arr[i], 1)
            min_ending_here = temp * arr[i]
        if (max_so_far <  max_ending_here):
            max_so_far  =  max_ending_here
    return max_so_far
 
# Driver function to test above function
arr = [1.0, 0.1, -1.0, -7.0, 3.0, -5.0, -2.5, 0.0, 1.0] 
print ("Maximum product subarray is",maxsubarrayproduct(arr))
 
# This code is contributed by Devesh Agrawal
