"""
    dict has nodes and code
    represented by [ { pro : , code: , children : [ 0=> left, 1=>right] } ]
"""


def sort_prob(e):
    return e["pro"]


def code_gen(temp):
    if len(temp) <= 2:
        temp.sort(key=sort_prob, reverse=True)
        if len(temp) == 2:
            temp[0]["code"] = 0
            temp[1]["code"] = 1
        elif len(temp) == 1:
            temp[0]["code"] = 0
        else:
            pass
        return temp

    temp.sort(key=sort_prob, reverse=True)
    second = temp.pop()
    first = temp.pop()

    first["code"] = 0
    second["code"] = 1

    children = [first, second]

    new_node = {"pro": first["pro"]+second["pro"], "code": -1, "children": children}
    temp.append(new_node)

    return code_gen(temp)


def key_gen(parser, l, prevcode=None):
    parser1 = parser[0]
    parser2 = parser[1]

    if not len(parser1["children"]):
        if prevcode:
            l.append({parser1["pro"]: str(prevcode) + str(parser1["code"])})
        else:
            l.append({parser1["pro"]: str(parser1["code"])})
    else:
        key_gen(parser1["children"], l, str(prevcode)+str(parser1["code"]) if prevcode else str(parser1["code"]))

    if not len(parser2["children"]):
        if prevcode:
            l.append({parser2["pro"]: str(prevcode) + str(parser2["code"])})
        else:
            l.append({parser2["pro"]: str(parser2["code"])})
    else:
        key_gen(parser2["children"], l, str(prevcode)+str(parser2["code"]) if prevcode else str(parser2["code"]))


class HfCode:

    def __init__(self, ps=None):
        self.ps = ps
        if ps:
            self.parser = self.generate_code()
            self.hf = self.generate_keys()
        else:
            self.parser = None

    def generate_code(self):
        temp = self.ps
        return code_gen(temp)

    def generate_keys(self):
        parser = self.parser
        hf_code_list = []
        key_gen(parser, hf_code_list)
        return hf_code_list


def main():
    a = []
    d = [0.4, 0.3, 0.1, 0.1, 0.06, 0.04]
    for i in range(len(d)):
        a.append({"pro": d[i], "code": -1, "children": []})

    x = HfCode(a)
    print(x.hf)


if __name__ == '__main__':
    main()
