# %%
with open('./melos.txt','r') as file:
    text = file.read()
# %%
hiragana_ord = range(0x3041,0x3096+1)
katakana_ord = range(0x30A1,0x30F6+1)

trans = dict()
for i,j in zip(hiragana_ord,katakana_ord):
    trans[i] = chr(j)
    trans[j] = chr(i)

# %%
with open('./melos_katakana_example.txt','w') as file:
    file.write(text.translate(trans))

# %%
for i,j in zip(hiragana_ord,katakana_ord):
    print(chr(i),chr(j))
