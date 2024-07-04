# %%
with open('./melos.txt','r') as file:
    text = file.read()
# %%
text_rm_space = text.replace('　','')
# %%

talks_start = text_rm_space.split('「')[1:]
talks = [s.split('」')[0] for s in talks_start]
talks_brackets = ['「' + s + '」' for s in talks]

# %%
with open('./talks.txt','w') as file:
    file.write('\n'.join(talks_brackets))
# %%
