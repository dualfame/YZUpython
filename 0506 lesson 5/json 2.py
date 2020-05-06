import json
import requests
url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'

r = requests.get(url)
# print(r.status_code)    # 200:OK, 404:error
# print(r.text)   #輸出資訊


# bad_rices = json.loads(r.text)
# for bad in bad_rices:
#     print(bad.get("品名"), bad.get("廠商名稱"))

bad_rices = json.loads(r.text)
for bad in bad_rices:
    if '縱谷' in bad.get("品名"):
        print(bad.get("品名"), bad.get("廠商名稱"), bad.get("不合格原因"))
