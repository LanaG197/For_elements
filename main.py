# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустые списки для простых и не простых чисел
primes = []
not_primes = []

# Перебираем каждый элемент в списке numbers
for number in numbers:
    if number < 2:
        # Числа меньше 2 не являются простыми
        not_primes.append(number)
        continue

    # Переменная для отметки простоты числа
    is_prime = True

    # Проверяем делители от 2 до квадратного корня из числа
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    # Записываем число в соответствующий список
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# Выводим списки простых и не простых чисел
print("Простые числа:", primes)
print("Не простые числа:", not_primes)
