def total_sum(numbers: list):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum


numbers = [10, 20, 30, 40, 50]
print(f"Список: {numbers}")
print(f"Сумма элементов: {total_sum}")
