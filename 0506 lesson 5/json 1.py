import json
score = '{"國文":100, "數學":90}'
student = '[{"name":AAA, "age":18}, \
{"name":BBB, "age"":20}, \
{"name":CCC, "age":25}]'

obj = json.loads(score) #字串轉json物件
print(type(obj))    # dict
print(obj.get('國文'))

obj2 = json.loads(student)
print(type(obj2))
for st in obj2:
    print(st.get('name'), st.get('age'))
