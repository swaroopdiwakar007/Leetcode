import random

random.seed("ABC")

numbers = [random.randint(0, 1000) for _ in range(100)]

print(numbers)


def merge_sort(numbers_list, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    merge_sort(numbers_list, left, mid)
    merge_sort(numbers_list, mid + 1, right)
    merge(numbers_list, left, right, mid)


def merge(numbers_list, left, right, mid):
    left_copy = numbers_list[left: mid + 1]
    right_copy = numbers_list[mid + 1: right + 1]

    l, r = 0, 0
    sorted = left

    while l < len(left_copy) and r < len(right_copy):
        if left_copy[l] <= right_copy[r]:
            numbers_list[sorted] = left_copy[l]
            l += 1

        else:
            numbers_list[sorted] = right_copy[r]
            r += 1

        sorted += 1

    while l < len(left_copy):
        numbers_list[sorted] = left_copy[l]
        l += 1
        sorted += 1
    while r < len(right_copy):
        numbers_list[sorted] = right_copy[r]
        sorted += 1
        r += 1


merge_sort(numbers, 0, len(numbers) - 1)
print(numbers)
