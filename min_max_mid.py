from sum import total_sum as summ

numbers = [10, 2, 45, 18, 9, 31, 5]


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


min_val = minn(numbers)
max_val = maxx(numbers)
mid_val = summ(numbers) / len(numbers)
mid_closed = mid_closed(numbers)

print(f"Список: {numbers}")
print(f"Минимум: {min_val}")
print(f"Максимум: {max_val}")
print(f"Среднее значение: {mid_val:.2f}")
print(f"Ближайшее к среднему: {mid_closed}")
