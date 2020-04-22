import random
ans = random.randint(1, 99)
min = 1
max = 100
count = 1

while count <= 7:
    guess = int(input('(第%d次) 請輸入數字 %d ~ %d :' % (count, min, max)))
    count += 1
    #範圍驗證
    if guess <= min or guess >= max:
        print("範圍錯誤")
        continue;

    #開始遊戲比對
    if guess == ans:
        print('恭喜答對了')
        break;
    elif guess < ans:
        min = guess
    else:
        max = guess