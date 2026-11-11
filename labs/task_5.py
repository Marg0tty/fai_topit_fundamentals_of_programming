students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}


def mean(values):
    if not values:
        return None
    total = 0
    for value in values:
        total += value
    return total / len(values)


def minimum(values):
    if not values:
        return None
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def maximum(values):
    if not values:
        return None
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


def classify(score):
    if score is None:
        return "нет данных"
    if score >= 90:
        return "отлично"
    if score >= 75:
        return "хорошо"
    if score >= 60:
        return "удовлетворительно"
    return "неудовлетворительно"


def student_summary(name, results):
    avg = mean(results)
    return {
        "name": name, "mean": avg, "min": minimum(results),
        "max": maximum(results), "category": classify(avg),
    }


def group_summary(students):
    categories = {"отлично": 0, "хорошо": 0,
                  "удовлетворительно": 0, "неудовлетворительно": 0,
                  "нет данных": 0}
    all_results = []
    for results in students.values():
        categories[classify(mean(results))] += 1
        all_results.extend(results)
    return {"categories": categories, "mean": mean(all_results),
            "students": len(students)}


def find_top_students(students):
    summaries = [student_summary(name, results)
                 for name, results in students.items()]
    top = None
    names = []
    for item in summaries:
        if item["mean"] is not None:
            if top is None or item["mean"] > top:
                top, names = item["mean"], [item["name"]]
            elif item["mean"] == top:
                names.append(item["name"])
    return names


def format_report(student_data, group_data):
    lines = ["Отчёт по группе"]
    for item in student_data:
        lines.append(
            f'{item["name"]}: среднее={item["mean"]}, '
            f'мин={item["min"]}, макс={item["max"]}, категория={item["category"]}'
        )
    lines.append(f'Среднее по группе: {group_data["mean"]}')
    lines.append(f'Категории: {group_data["categories"]}')
    lines.append(f'Лидер(ы): {", ".join(find_top_students(source_students)) or "нет"}')
    return "\n".join(lines)


source_students = students


def main():
    data = [student_summary(name, results) for name, results in students.items()]
    group = group_summary(students)
    print(format_report(data, group))

    assert mean([2, 4]) == 3
    assert mean([]) is None
    assert minimum([3, 1, 2]) == 1
    assert minimum([]) is None
    assert maximum([3, 1, 2]) == 3
    assert maximum([]) is None
    assert classify(90) == "отлично"
    assert classify(None) == "нет данных"
    assert student_summary("X", [])["category"] == "нет данных"
    assert group_summary({})["mean"] is None
    assert find_top_students({"A": [90], "B": [90]}) == ["A", "B"]
    assert find_top_students({"A": []}) == []
    assert classify(75) == "хорошо"


if __name__ == "__main__":
    main()
