# extract_dialogue.py
# 発話部分を抽出し、ファイルに出力するPythonスクリプト
# %%
# ファイル読み込み

with open('./melos.txt','r') as file:
    text = file.read()

# %%
# 1. 正規表現を使わない場合

talks_start = text.split('「')[1:]
talks = ['「' + s.split('」')[0] + '」' for s in talks_start]
with open('./melos_dialogue_example.txt','w') as file:
    file.write('\n'.join(talks))

# %%
# 2. 正規表現を使う方法

import re
ptn = re.compile(r'「[^」]+」')
talks = [m.group() for m in ptn.finditer(text)]
with open('./melos_dialogue_example2.txt','w') as file:
    file.write('\n'.join(talks))

# %%
