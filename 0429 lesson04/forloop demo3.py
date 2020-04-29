import statistics as stat
em1 = {'name': 'John', 'salary': 60000}
em2 = {'name': 'Mark', 'salary': 70000}
em3 = {'name': 'Dan', 'salary': 50000}
emps = [em1, em2, em3]
print(emps)

#薪資總和?
salary = [] #建立數組
for s in emps : #放內容到數組
    salary.append(s['salary'])
print(sum(salary))
print(max(salary))
print(min(salary))
print(stat.mean(salary))