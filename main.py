import random
import pickle


class Generator:
    def del_punct(self, txt):
        punct = '!,./;…:"(-–)?'
        txt = txt.lower()
        for i in punct:
            txt = txt.replace(f'{i}', '')
        return txt

    def import_text(self, path='texts\\paust.txt'):
        p = input('Введите путь к тексту или поставьте "-" ')
        if p == '-':
            text = self.del_punct(open(path, 'r', encoding='utf-8').read().replace('\n', ' '))
        else:
            text = self.del_punct(open(p, 'r', encoding='utf-8').read().replace('\n', ' '))
        text = text.split()
        return text

    # -------------------------------------------- #

    def fit(self, model_file='model\\model.pickle'):
        txt = self.import_text()
        text_dict = {}
        ln_txt = len(txt)
        for i in range(0, ln_txt - 1):
            if txt[i] in text_dict.keys():
                if txt[i + 1] in text_dict[txt[i]]:
                    pass
                else:
                    text_dict[txt[i]].append(txt[i + 1])
            else:
                text_dict[txt[i]] = text_dict.get(txt[i], [])
                text_dict[txt[i]].append(txt[i + 1])

        def pp(s1, s2):
            for i in s2:
                if not i in s1:
                    s1.append(i)
            return s1

        try:
            with open(model_file, 'rb') as f:
                model = pickle.load(f)
        except Exception:
            model = {}
        d_buf = {}
        for i in model.keys():
            if i in text_dict.keys():
                d_buf[i] = d_buf.get(i, pp(model[i], text_dict[i]))
        model.update(text_dict)
        model.update(d_buf)

        with open(model_file, 'wb') as f:
            pickle.dump(model, f)

    # --------------------------------------------------------------- #

    def generate(self, model, ln, prefix=None):
        if prefix is None:
            result = [random.choice(list(model.keys()))]
        else:
            result = [prefix]
        for i in range(ln - 1):
            result.append(random.choice(model[result[-1]]))
        return ' '.join(result)


tt = Generator()
tt.fit()
with open('model\\model.pickle', 'rb') as f:
    md = pickle.load(f)
print(tt.generate(md, 20))
