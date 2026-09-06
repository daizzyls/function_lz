
digigigt = 12346

def digit_sum(digit:int):
    sum_dig = 0
    while digit != 0 :
        sum_dig += (digit % 10)
        digit = digit // 10
    return sum_dig


print(f"Сумма цифр: {digit_sum(digigigt)}")