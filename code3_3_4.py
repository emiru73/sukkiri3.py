month = int(input('今は何月ですか？ (数字を入力してください)>>'))
if month in [1,3,5,7,8,10,12]:
    print('31日までありますね')
else:
    if month != 2:
        print('30日までですね')
    else:
        print('1年で一番寒い月ですね')
    print('年があけてから')
print('{}箇月がすぎました'.format(month))