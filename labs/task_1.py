import copy
a = 10
b = a
a += 1
print("Числа:", a, b, a is b)

first = [10, 20]
second = first
second.append(30)
print("Общие списки:", first, second, first is second)

second = first.copy()
print("Копия:", first == second, first is second)
second.append(40)
print("После изменения:", first, second)

config1 = {
    "name": "Project",
    "users": ["Anna", "Ivan"],
    "params": [["--debug", True]]
}

config2 = config1
config2["params"][0].append("--test")
print("Общие параметры:", config1["params"])

config3 = copy.deepcopy(config1)
config3["params"][0].append("--prod")
assert config1["params"] != config3["params"]
assert config1["users"] is config3["users"] is False

print("Независимая копия:", config1, config3)
