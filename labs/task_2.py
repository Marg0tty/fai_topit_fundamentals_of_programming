def analyze(values):
    total = values[0]
    low = high = values[0]
    evens = 0

    for value in values:
        total += value if value != values[0] else 0
        if value < low:
            low = value
        if value > high:
            high = value
        if value % 2 == 0:
            evens += 1

    average = total / len(values)
    above = 0
    for value in values:
        if value > average:
            above += 1
    return total, low, high, evens, above


def linear_search(values, target):
    for i, value in enumerate(values):
        if value == target:
            return i
    return -1


def is_prime(n):
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def selection_sort(values):
    result = values.copy()
    for i in range(len(result)):
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j] < result[smallest]:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]
    return result


def binary_search(values, target):
    left, right, comparisons = 0, len(values) - 1, 0
    while left <= right:
        middle = (left + right) // 2
        comparisons += 1
        if values[middle] == target:
            return middle, comparisons
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1, comparisons


def main():
    measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]
    total = 0
    low = high = measurements[0]
    evens = 0
    for value in measurements:
        total += value
        if value < low:
            low = value
        if value > high:
            high = value
        if value % 2 == 0:
            evens += 1
    average = total / len(measurements)
    above = 0
    for value in measurements:
        if value > average:
            above += 1
    print("Сумма, минимум, максимум, чётные, выше среднего:",
          total, low, high, evens, above)

    target = int(input("Число для линейного поиска: "))
    print("Индекс:", linear_search(measurements, target))
    n = int(input("Число для проверки простоты: "))
    print("Простое:", is_prime(n))

    assert linear_search([4, 2, 4], 4) == 0
    assert linear_search([1, 2], 3) == -1
    assert is_prime(2) and is_prime(17) and not is_prime(1) and not is_prime(9)
    assert selection_sort([3, 1, 2]) == [1, 2, 3]
    assert binary_search([1, 3, 5], 3)[0] == 1

    print("n | линейные сравнения | бинарные сравнения")
    for size in (10, 100, 1000):
        values = list(range(size))
        _, comparisons = binary_search(values, size - 1)
        print(size, "|", size, "|", comparisons)


if __name__ == "__main__":
    main()
