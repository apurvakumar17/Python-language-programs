# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     # query_name = input()
#     print(student_marks)
a={'apurva': [1.0, 2.0, 3.0], 'kumar': [7.0, 8.0, 9.0]}
print(a.keys())
l=a.keys()
for x in l:
    print(a[x])
    