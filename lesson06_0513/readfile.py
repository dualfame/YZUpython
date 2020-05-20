# file = open('salary.txt', 'r', encoding='UTF-8')
# rows = file.readlines()
# print(rows)
#
# #薪資總和
# employees = []
# for row in rows:
#     data = row.split(',')
#     dict = {'name':data[0], 'salary':int(data[1].strip('\n'))}
#     employees.append(dict)
#
# print(employees)
#
# sum = 0
# for emp in employees:
#     sum = sum + emp['salary']
# print(sum)

f = open('textcsv.csv', 'r')
reader = f.readlines()
print(reader)

data = []
for row in reader:
    sq = row.split(',')
    dict = {'C1':sq[0], 'N':int(sq[1]), 'fac1':int(sq[2]), 'fac2':int(sq[3]), 'multiple':int(sq[4].strip('\n'))}
    data.append(dict)
print(data)

C5 = []
for Col in data:

    sum(C5)
    # sum = sum + Col['multiple']
print(sum)
