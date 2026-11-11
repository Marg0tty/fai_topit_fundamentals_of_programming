
import copy

original = [["Python", 5], ["Algorithms", 4]]
alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

for name, obj in [
    ("original", original), ("alias", alias),
    ("shallow", shallow), ("deep", deep)
]:
    print(name, obj, "id:", id(obj), "вложенный:", id(obj[0]))

original.append(["Databases", 5])
print("\nПосле append:", original, alias, shallow, deep)

original[0][1] = 3
print("\nПосле изменения оценки:", original, alias, shallow, deep)

wrong = [[0] * 3] * 3
wrong[0][0] = 1

correct = [[0] * 3 for _ in range(3)]
correct[0][0] = 1

print("\nОшибочная матрица:", wrong)
print("Правильная матрица:", correct)
print("Общие строки:", wrong[0] is wrong[1])
