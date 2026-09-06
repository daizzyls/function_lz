hours = int(input("Часы: "))
minutes = int(input("Минуты: "))
seconds = int(input("Секунды: "))

total_seconds = hours * 3600 + minutes * 60 + seconds
print(f"Общее время в секундах: {total_seconds}")
