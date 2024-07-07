# %%
with open('./melos.txt','r') as file:
    text = file.read()

# %%
# defaultdictを使わない場合
char_count = dict()
for c in text:
    if c in char_count:
        char_count[c] += 1
    else:
        char_count[c] = 1 

# %%
# defaultdictを使う場合
from collections import defaultdict
char_count = defaultdict(int)
for c in text:
    char_count[c] += 1

# %%
# Unicodeコードポイント順にソートして出力
char_sorted_list = sorted(char_count.keys())
print('Unicode/文字/utf-8/shift-jis/回数')
for c in char_sorted_list:
    print(hex(ord(c)),
          repr(c),
          c.encode().hex(),
          c.encode('shift-jis').hex(),
          char_count[c],sep='/')
