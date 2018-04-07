def solution1(A):
    length = len(A)
    if length == 0:
        return -1
    sum = 0
    for i in range(length):
        sum += A[i]
#    print(sum)
    success = 0
    sum_previous = 0
    for i in range(length):
        sum_previous += A[i]
        sum_back = sum - sum_previous
        sum_new_previous = sum_previous - A[i]
        if (sum_new_previous == sum_back):
            return (i)

    return -1



def solution(A):
    length = len(A)
    if(length == 0):
        return -1
    sum = 0
    for i in range(length):
        sum += A[i]
    success = 0

    for i in range(length):
        sum_previous = 0
        for j in range(i+1):
            sum_previous = sum_previous + A[j]
        sum_back = sum - sum_previous
        sum_previous = sum - sum_back - A[i]
        success += 1

        if(sum_previous == sum_back):
            return i
            success = 1
        return -1


A = [-1, 3, -4, 5, 1, -6, 2, 1]

print(solution(A))
print(solution1(A))