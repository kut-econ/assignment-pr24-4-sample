# extract_dialogue.py
# 走れメロスの会話部分を抽出し、ファイルに出力するPythonスクリプト
# %%
with open('./melos.txt','r') as file:
    text = file.read()
# %%
# "「"記号で文字列を部分文字列のリストに分割します。
# 最初の部分文字列は発話部分を含まないので廃棄します。

talks_start = text.split('「')[1:]

# %%
# 各部分文字列をさらに"」"記号で二つに分割します。
# 分割した前の部分が発話部分なので、それをリストにします。
# ここでは内包表記を使いますが、内包表記を使わない場合は、
talks = [s.split('」')[0] for s in talks_start]

# %%
# 取り出した発話部分にかぎかっこをつけます。
talks_brackets = ['「' + s + '」' for s in talks]

# %%
with open('./melos_dialogue_example.txt','w') as file:
    file.write('\n'.join(talks_brackets))
