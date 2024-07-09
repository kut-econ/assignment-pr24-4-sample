# %%
with open('./melos.txt','r') as file:
    text = file.read()

# %%
# Unicodeコードポイント順にソートして出力
char_sorted_list = sorted(set(text))
print('Unicode/文字/utf-8/shift-jis/回数')
for c in char_sorted_list:
    print(hex(ord(c)),
          repr(c),
          c.encode().hex(),
          c.encode('shift-jis').hex(),
          text.count(c),sep='/')

# %%
