em1 = {'name': 'John', 'salary': 60000, 'program': ['Python', 'Java']}
em2 = {'name': 'Mark', 'salary': 70000, 'program': ['C++', 'Java', 'R']}
em3 = {'name': 'Dan', 'salary': 50000, 'program': ['Python']}
emps = [em1, em2, em3]

#求會Python的員工?
language= 'Python'
names = []
for n in emps :
    for p in n['program'] :
        if p == language :
            names.append(n['name'])
print(names)