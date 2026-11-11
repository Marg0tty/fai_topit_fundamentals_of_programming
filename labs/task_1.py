def classify(score, work_type, absences):
    if not 0 <= score <= 100 or not 0 <= absences <= 5:
        return "Некорректные данные"

    if score >= 90:
        level = 3
    elif score >= 75:
        level = 2
    elif score >= 60:
        level = 1
    else:
        level = 0

    if absences > 3:
        if level > 0:
            level -= 1

    levels = ["недостаточный", "удовлетворительный", "хороший", "отличный"]
    match work_type:
        case "exam":
            work = "экзаменационная работа"
        case "project":
            work = "проектная работа"
        case "practice":
            work = "практическая работа"
        case _:
            work = "неизвестный тип работы"

    return f"{work}: {levels[level]} результат ({score}), пропусков: {absences}"


def main():
    records = [
        (0, "exam", 0), (59, "project", 1), (60, "practice", 0),
        (74, "exam", 4), (75, "project", 0), (89, "practice", 1),
        (90, "exam", 0), (100, "project", 5), (82, "exam", 4),
        (67, "practice", 2),
    ]
    counts = {"недостаточный": 0, "удовлетворительный": 0,
              "хороший": 0, "отличный": 0}

    for record in records:
        result = classify(*record)
        print(result)
        for level in counts:
            if level in result:
                counts[level] += 1
    print("Сводка:", counts)

    assert "недостаточный" in classify(59, "exam", 0)
    assert "удовлетворительный" in classify(60, "exam", 0)
    assert "хороший" in classify(75, "project", 0)
    assert "отличный" in classify(90, "practice", 0)
    assert classify(101, "exam", 0) == "Некорректные данные"


if __name__ == "__main__":
    main()
