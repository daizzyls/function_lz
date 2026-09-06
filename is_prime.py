num = int(input("Введите число: "))

if num <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"Число {num} — простое")
else:
    print(f"Число {num} — составное (или <= 1)")
