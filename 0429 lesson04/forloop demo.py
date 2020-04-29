#數組
# list(可重複)、set(不可重複)、dict(關鍵值)
scores = [100, 90, 80]
scores.append(70)
print(scores)
print(scores[0])    #輸出維度(index)=0的內容
print(len(scores))  #輸出數組長度(資料比數)
print(scores.index(70))    #輸出內容=70的index

for x in scores :
    print(scores.index(x), x)

for (i, x) in enumerate(scores) :
    print(i, x)
