# txt = ['1','2','1','4','5','1','4']
# text_dict = {}
# word_nums = {k: txt.count(k) for k in txt}
# ln_txt = len(txt)
# for i in range(0, ln_txt - 1):
#     if txt[i] in text_dict.keys():
#         if txt[i + 1] in text_dict[txt[i]]:
#             pass
#         else:
#             text_dict[txt[i]].append(txt[i + 1])
#     else:
#         text_dict[txt[i]] = text_dict.get(txt[i], [])
#         text_dict[txt[i]].append(txt[i + 1])
#
# print(text_dict)
def pp(s1, s2):
    for i in s2:
        if not i in s1:
            s1.append(i)
    return s1


d1 = {'a': ['1', '2', '3'], 'b': ['3', '4', '5']}
d2 = {'a': ['2', '6', '7'], 'c': ['4', '4', '4']}
d_buf = {}
for i in d1.keys():
    if i in d2.keys():
        d_buf[i] = d_buf.get(i, pp(d1[i], d2[i]))
d1.update(d2)
d1.update(d_buf)
print(d1)