# Python equivalent of Student-Teacher-Subject-Code facts
records = [
    ("S001", "Arun", "T01", "Dr_Ravi", "CS101", "Python"),
    ("S002", "Meena", "T02", "Dr_Latha", "CS102", "AI"),
    ("S003", "Kavin", "T01", "Dr_Ravi", "CS103", "Networks")
]
print("STUDENT-TEACHER-SUBJECT-CODE DATABASE")
for sid, student, tid, teacher, code, subject in records:
    print(f"{sid} {student} | {tid} {teacher} | {code} {subject}")
print("\\nStudents taught by Dr_Ravi:")
for r in records:
    if r[3] == "Dr_Ravi":
        print(r[1])
