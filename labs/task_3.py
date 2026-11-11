submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]


def add_submission(record):
    student, lab, score = record
    students.add(student)
    labs.add(lab)
    attempts.setdefault(student, []).append((lab, score))
    key = (student, lab)
    if key not in best or score > best[key]:
        best[key] = score
    counts[key] = counts.get(key, 0) + 1


students, labs, attempts, best, counts = set(), set(), {}, {}, {}
for submission in submissions:
    add_submission(submission)


def command(line):
    parts = line.split()
    if not parts:
        return "Пустая команда"
    match parts:
        case ["student", name]:
            return attempts.get(name, "Студент не найден")
        case ["best", name, lab]:
            return best.get((name, lab), "Результат не найден")
        case ["attempts", name, lab]:
            return counts.get((name, lab), 0)
        case ["completed", lab]:
            return {name for name, work in best if work == lab}
        case _:
            return "Неизвестная команда"


def main():
    print("Студенты:", students)
    print("Лабораторные:", labs)
    print("Попытки:", attempts)
    print("Лучшие результаты:", best)
    print("Количество попыток:", counts)
    for lab in labs:
        completed = {name for name, work in best if work == lab}
        print("Сдали", lab, ":", completed)
    add_submission(("daria", "lab_02", 4))
    print("После добавления:", best, counts)

    assert best[("anna", "lab_01")] == 5
    assert counts[("anna", "lab_01")] == 2
    assert command("best anna lab_01") == 5
    assert command("attempts boris lab_02") == 1
    assert command("best nobody lab_01") == "Результат не найден"
    assert command("unknown") == "Неизвестная команда"


if __name__ == "__main__":
    main()
