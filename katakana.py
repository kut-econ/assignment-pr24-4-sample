# %%
with open('./melos.txt','r') as file:
    text = file.read()
# %%
hiragana_ord = range(ord('あ'),ord('ん')+1)
katakana_ord = range(ord('ア'),ord('ン')+1)

trans = dict()
for i,j in zip(hiragana_ord,katakana_ord):
    trans[i] = chr(j)
    trans[j] = chr(i)

# %%
with open('./melos_katakana_example.txt','w') as file:
    file.write(text.translate(trans))
