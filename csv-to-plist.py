from plistlib import dump
import csv

csv_path='example.csv'
plist_path=csv_path.split('.')[0]+'.plist'

with open(csv_path, newline='') as csvfile:

    result=[]
    key=['phrase','shortcut']
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)

    # 以迴圈輸出每一列
    for row in rows:
        result.append({' '.join(l[0].split()).lower():' '.join(l[1].split()).lower() for l in list(zip(key,row))})

    with open(plist_path, 'wb') as fp:
        dump(result, fp)
