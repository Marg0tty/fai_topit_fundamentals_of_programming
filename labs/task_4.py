course = "Python"


def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее непустого списка."""
    if not values:
        raise ValueError("Список не должен быть пустым")
    total = 0
    for value in values:
        total += value
    return total / len(values)


def normalize_name(name: str) -> str:
    """Очищает имя и приводит слова к обычному регистру."""
    return " ".join(part.capitalize() for part in name.split())


def build_report(student: str, results: list[int], *,
                 precision: int = 2, prefix: str = "Результат") -> str:
    """Формирует отчет о результатах студента."""
    if not results:
        return f"{prefix}: {student} — нет результатов"
    return f"{prefix}: {student}, среднее = {arithmetic_mean(results):.{precision}f}"


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    result = []
    for tag in tags:
        tag = tag.strip()
        if lowercase:
            tag = tag.lower()
        if tag and tag not in result:
            result.append(tag)
    return tuple(result)


def scope_demo():
    value = "внешнее"

    def inner():
        nonlocal value
        value = "изменённое"
        return value

    return inner(), value


def add_result(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results


def apply_to_results(operation, values):
    return [operation(value) for value in values]


def make_threshold_checker(threshold):
    return lambda value: value >= threshold


def main():
    assert arithmetic_mean([2, 4]) == 3
    assert arithmetic_mean([5]) == 5
    try:
        arithmetic_mean([])
        assert False
    except ValueError:
        pass

    assert normalize_name("  aNNa   ivANOVA ") == "Anna Ivanova"
    assert normalize_name("BORIS") == "Boris"
    assert normalize_name(" ") == ""

    assert "Анна" in build_report("Анна", [4, 5])
    assert build_report("Борис", []) == "Результат: Борис — нет результатов"
    assert build_report("Анна", [3, 4], precision=1, prefix="Итог").startswith("Итог")

    assert collect_tags(" Python ", "python", "", "Code") == ("python", "code")
    assert collect_tags("A", "a", lowercase=False) == ("A", "a")
    assert collect_tags(" ", "x") == ("x",)

    print(build_report("Анна", [78, 91, 84]))
    print(collect_tags("Python", " Code ", "python"))
    print(arithmetic_mean(*[[2, 4, 6]]))
    options = {"student": "Борис", "results": [60, 80], "precision": 1, "prefix": "Итог"}
    print(build_report(**options))
    print("LEGB:", scope_demo(), "глобальный course:", course)
    print(add_result(5), add_result(7))
    print(apply_to_results(abs, [-2, 3]))
    print(apply_to_results(lambda x: x * 2, [1, 2, 3]))
    pass_mark = make_threshold_checker(60)
    high_mark = make_threshold_checker(90)
    print(pass_mark(70), high_mark(70))


if __name__ == "__main__":
    main()
