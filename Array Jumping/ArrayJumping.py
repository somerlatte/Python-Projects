def ArrayJumping(arr):
    max_num = max(arr)
    max_index = arr.index(max_num)
    n = len(arr)

    left_index = (max_index - arr[max_index]) % n
    right_index = (max_index + arr[max_index]) % n

    left_steps = 0
    right_steps = 0

    while left_index != max_index and right_index != max_index:
        if left_index == right_index:
            return min(left_steps, right_steps)
        left_index = (left_index - arr[left_index]) % n
        right_index = (right_index + arr[right_index]) % n
        left_steps += 1
        right_steps += 1

    if left_index == max_index:
        return left_steps
    elif right_index == max_index:
        return right_steps
    else:
        return -1

# keep this function call here 
print ArrayJumping(raw_input())