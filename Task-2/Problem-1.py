
if __name__ == '__main__':
 n = int(input())


students = []


for _ in range(n):
    name = input().strip()
    grade = float(input().strip())
    students.append([name, grade])

uniqueGrades = sorted(set(student[1] for student in students))

second_lowest_grade = uniqueGrades[1]

second_lowest_students = sorted([student[0] for student in students if student[1] == second_lowest_grade])

for name in second_lowest_students:
    print(name)
