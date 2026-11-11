
import sys
import tracemalloc


def measure(name, factory, count):
    tracemalloc.start()
    obj = factory()
    current, peak = tracemalloc.get_traced_memory()
    size = sys.getsizeof(obj)
    tracemalloc.stop()

    return {
        "name": name,
        "count": count,
        "size": size,
        "current": current,
        "peak": peak,
    }


results = [
    measure("list", lambda: list(range(100_000)), 100_000),
    measure("range", lambda: range(100_000), 100_000),
]

for r in results:
    print(f"\nСценарий: {r['name']}")
    print(f"Элементов: {r['count']}")
    print(f"Размер объекта: {r['size']} байт")
    print(f"Текущая память: {r['current'] / 1024:.2f} КБ")
    print(f"Пиковая память: {r['peak'] / 1024:.2f} КБ")

list_peak = results[0]["peak"]
range_peak = results[1]["peak"]

print("\nОтношение пиков list/range:",
      f"{list_peak / max(range_peak, 1):.2f} раза")
