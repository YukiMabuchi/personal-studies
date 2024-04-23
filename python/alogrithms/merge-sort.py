from typing import List

# 11:00 debugger
# numbersの参照自体をソートしてる
# merge_sortに再起的に入っていって
# numbersのlenが1になったらそこから関数が実行されていく
def merge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers
    
    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1

    return numbers

if __name__ == '__main__':
    import random

    nums = [random.randint(0, 1000) for _ in range(9)]
    print(merge_sort(nums))
    