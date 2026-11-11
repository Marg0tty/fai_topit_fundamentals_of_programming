
import sys
import tracemalloc

values = list(range(10))

objects = {
    "Пустой список": [],
    "Список из 10 чисел": values,
    "Кортеж из 10 чисел": tuple(values),
    "Строка из 10 символов": "abcdefghij",
    "Целое число": 100,
    "None": None,
}

for name, obj in objects.items():
    print(f"{name}: {sys.getsizeof(obj)} байт")

print("\nРост списка:")
items = []
size = sys.getsizeof(items)

for i in range(100):
    items.append(i)
    new_size = sys.getsizeof(items)
    if new_size != size:
        print(f"Длина: {len(items)}, размер: {new_size} байт")
        size = new_size

def measure(factory):
    tracemalloc.start()
    numbers = factory()
    current, peak = tracemalloc.get_traced_memory()
    result = (sys.getsizeof(numbers), current, peak)
    tracemalloc.stop()
    return result


for name, factory in [
    ("list", lambda: list(range(100_000))),
    ("range", lambda: range(100_000)),
]:
    size, current, peak = measure(factory)
    print(f"\n{name}: объект={size} Б, текущая память={current / 1024:.1f} КБ, пик={peak / 1024:.1f} КБ")
