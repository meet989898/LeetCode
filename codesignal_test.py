
def solution(arr):
    result = []
    first_number = is_even(arr[0])
    new_arr = [first_number]

    for i in range(1, len(arr)):

        new_number = is_even(arr[i])

        if new_arr:
            last_numer = new_arr[-1]


            if new_number == last_numer:
                result.append(new_arr)
                new_arr = []

        else:
            new_arr.append(new_number)

    if new_arr:
        result.append(new_arr)

    return len(result)

def is_even(num):
    if num % 2 == 0:
        return 1
    else:
        return 0


arr = [1, 3, 5, 7, 9]
print(solution(arr))