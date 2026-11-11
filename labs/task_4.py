def arithmetic_mean(values: list[float]) -> float:
    if not values: return 0.0
    total = 0.0
    for v in values: total += v
    return total / len(values)

def normalize_name(name: str) -> str:
    return " ".join(word.capitalize() for word in name.split())

def build_report(student: str, results: list[int], *, precision: int = 2, prefix: str = "Результат") -> str:
    if not results: return f"{prefix}: {student} | Нет данных"
    return f"{prefix}: {student} | Среднее: {arithmetic_mean(results):.{precision}f}"

def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    seen = set()
    res = []
    for t in tags:
        clean = t.strip().lower() if lowercase else t.strip()
        if clean and clean not in seen:
            seen.add(clean)
            res.append(clean)
    return tuple(res)
-
assert arithmetic_mean([10.0, 20.0]) == 15.0
assert normalize_name("  ivan  ivanovich ") == "Ivan Ivanovich"
assert collect_tags("Py", " py ", "JS", "") == ("py", "js")

args = ["Иван", [80, 90]]
kwargs = {"precision": 1, "prefix": "Оценка"}
print(build_report(*args, **kwargs))

course = "Глобальный Python" # Global
def outer_func():
    scope_var = "Внешний уровень" # Enclosing
    def inner_func():
        nonlocal scope_var
        scope_var = "Изменено внутри" 
        local_var = "Локальный уровень" 
        return f"{course}, {scope_var}, {local_var}"
    return inner_func()

print(outer_func())

def add_result(value, results=None):
    if results is None: results = []
    results.append(value)
    return results

def apply_to_results(operation, values):
    return [operation(v) for v in values]

def make_threshold_checker(threshold):
    return lambda x: x >= threshold

check_50 = make_threshold_checker(50)
check_90 = make_threshold_checker(90)
print(apply_to_results(check_50, [40, 60, 95])) # [False, True, True]
