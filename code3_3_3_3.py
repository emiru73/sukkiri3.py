hello =input('入力してください >>')
if 'こんにちは' in hello:
    print('ようこそ！')
elif '景気は？' in hello:
    print('ぼちぼちです')
elif 'さようなら' in hello:
    print('お元気で！')
    
else:
    print('どうしました？')