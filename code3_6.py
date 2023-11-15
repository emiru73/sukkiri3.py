scores = {'network': 60, 'database': 80, 'security': 50}

key = input('追加する科目名を入力してください >>')
if key in scores:
    print('既に登録済みです')
else:
    data = int(input('得点を入力してください >>'))
    scores[key] = data

    print(f'{data,scores[key]}を追加しました')
print(scores)