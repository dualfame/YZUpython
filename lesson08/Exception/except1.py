import sys
import traceback

x = 10
y = int(input('Key a #'))
try:
    z = x / y
except Exception as e:
    print("ERROR", e)
    print(e.__class__.__name__)
    print(e.args)
    cl, exc, tb = sys.exc_info()
    lastCallStack = traceback.extract_tb(tb)[-1]    #-1:最新一筆資訊
    print(lastCallStack)
else:
    print(z)
