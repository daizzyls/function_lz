from sum import total_sum as summ


def minn(numbers: list):
    min = 0
    for i in range(0, len(numbers)):
        if numbers[i] < numbers[min]:
            min = i
    return numbers[min]


def maxx(number: list):
    max = 0
    for i in range(0, len(number)):
        if number[max] < number[i]:
            max = i
    return number[max]


def mid_closed(numbers: list):
    mid = summ(numbers) / len((numbers))
    dif = mid - numbers[0]
    ind = 0
    if dif == 0:
        return numbers[0]

    for i in range(1, len(numbers)):
        if abs(dif) > abs(mid - numbers[i]):
            dif = mid - numbers[i]
            ind = i
    return numbers[ind]


numbers = [
    84, -12, 403, 91, 5, 234, -89, 67, 12, 900,
    45, 78, -3, 567, 123, 8, 99, -450, 312, 64,
    22, 81, 500, -33, 11, 74, 9, 102, 61, -7,
    350, 48, 19, 888, 2, 73, -120, 55, 93, 40,
    31, 600, -1, 15, 83, 27, 410, 6, 95, 100
]
min_val = minn(numbers)
max_val = maxx(numbers)
mid_val = summ(numbers) / len(numbers)
mid_closed = mid_closed(numbers)

print(f"Список: {numbers}")
print(f"Минимум: {min_val}")
print(f"Максимум: {max_val}")
print(f"Среднее значение: {mid_val:.2f}")
print(f"Ближайшее к среднему: {mid_closed}")
