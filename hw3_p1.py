n = int(input("Input the total number of students (n>0) : "))
ln = []
i = 0
while i < n:
	ln = ln + [i+1]
	i = i + 1
while len(ln) > 1:
	i = (i + 2) % len(ln)
	ln.pop(i)
	if i == len(ln):
		i = 0
print("The last ID is :",ln)


#TA ANSWER:

n = input("Input the total number of students: ")
n = int(n)

students = list(range(1, n + 1))

# # method 1
# element_to_start = 1
# while len(students) > 1:
#     # delete the student every 3rd student
#     start_index = students.index(element_to_start)
#     index_to_delete = (start_index + 2) % len(students)
#     element_to_start = students[(index_to_delete + 1) % len(students)]
#     students.pop(index_to_delete)
#     print(students)
# print("The student left is: ", students[0])

students = list(range(1, n + 1))
# method 2
start_index = 0
while len(students) > 1:
    # delete the student every 3rd student
    start_index = (start_index + 2) % len(students)
    students.pop(start_index)
    print(students)

# print("The student left is: ", students[0])

# students = [0, 1, 5, 6, 7, 8, 9, 10]
# print(f"Students: {students}")
# # remove element
# students.remove(5)
# print(f"Students: {students}")

# students = [0, 1, 5, 6, 7, 8, 9, 10]
# print(f"Students: {students}")
# # pop index
# students.pop(5)
# print(f"Students: {students}")