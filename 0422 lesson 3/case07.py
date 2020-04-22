#字串
s = "she sell sea shell on the sea shore"
print(s)
print('有 %d 個s' % s.count('s'))
print('有 sea 這個字嗎 %d' % s.find('sea'))

#檢測都是英文字, 先用replace代替空格
print(s.replace(' ','').isalpha()) #英文字母
print(s.replace(' ','').isalnum()) #英數字串
print(s.swapcase())

text = "半徑=10"
name, r = text.split("=")
r = int(r) # convert str
print(type(name), type(r))
print('%s 為 %d 的圓面積是 %.3f' % (name, r, r ** 2 * 3.14))

str = 'Hello PYTHON'
print(str[6])
print(str[-1])
print(str[1:6])
print(str[:6])

#原始字串
path = r"C:\temp\abc.txt" #加r，不視為跳脫字元
print(path)
