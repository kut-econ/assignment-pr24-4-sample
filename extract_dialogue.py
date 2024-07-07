# extract_dialogue.py
# 発話部分を抽出し、ファイルに出力するPythonスクリプト
# %%
# ファイル読み込み
with open('./melos.txt','r') as file:
    text = file.read()

# %%
# "「"記号で文字列を部分文字列のリストに分割
# 最初の部分文字列を廃棄

talks_start = text.split('「')[1:]

# %%
# 各部分文字列を"」"記号で分割
# 前の部分が発話部分なので、それをリストに
talks = [s.split('」')[0] for s in talks_start]

# %%
# かぎかっこをつける
talks_brackets = ['「' + s + '」' for s in talks]

# %%
with open('./melos_dialogue_example.txt','w') as file:
    file.write('\n'.join(talks_brackets))
