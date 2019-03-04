class Questionnaire(object):
    """読み取ったアンケートのデータ"""
    text = ""

    data = list()
    sentence = list()

    def __init__(self, *args, **kwargs):
        pass

    def processing_comment(self):

        t = self.text.split("---")
        imp_1 = t[0].split()
        imp_2 = t[1].split()

        #print(len(imp_1))
        imp_1 = [s for s in imp_1 if '作品の感想' not in s]

        for i in range(0, len(imp_1) - 1, 2):
            self.data.append(dict(id=imp_1[i], comment=imp_1[i + 1]))
            

        #print(imp_1)
        #print(imp_2)

        print(self.data)



def mm():
    with open("q.txt", "r", encoding="utf-8") as f:
        contents = f.read()

    q = Questionnaire
    q.text = contents

    q.processing_comment(q)