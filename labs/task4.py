import gc

print("GC включён:", gc.isenabled())
print("Пороги:", gc.get_threshold())
print("Статистика:", gc.get_stats())

first = []
second = []
first.append(second)
second.append(first)

print("Цикл:", first[0] is second, second[0] is first)
ids = id(first), id(second)

del first, second
print("Собрано объектов:", gc.collect())
print("ID удалённых списков:", ids)

gc.disable()
try:
    a, b, c = {}, {}, {}
    a["next"], b["next"], c["next"] = b, c, a

    independent = {"name": "independent"}
    del a, b, c

    print("Собрано из графа:", gc.collect())
    print("Независимый узел:", independent)
finally:
    gc.enable()

print("GC восстановлен:", gc.isenabled())
