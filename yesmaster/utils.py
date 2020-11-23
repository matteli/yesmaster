import random, copy

colors = "ROGBYAPW"  # Red, Orange, Green, Blue, Yellow, grAy, Pink, White


def make_tree(dic, depth, max_depth, end):
    depth += 1
    if depth < max_depth:
        for c in colors:
            dic[c] = {}
            dic[c] = make_tree(dic[c], depth, max_depth, end)
    else:
        for c in colors:
            dic[c] = copy.deepcopy(end)
    return dic


def count_colors(code):
    code_dict = {}
    for c in colors:
        code_dict[c] = code.count(c)
    return code_dict


def random_code():
    code = ""
    for i in range(4):
        code += random.choice(colors)
    return code


def random_code_4_colors(except_colors=""):
    if len(except_colors) > 4:
        raise ValueError("except_colors must not exceed 4 colors.")
    code = ""
    for i in range(4):
        while True:
            c = random.choice(colors)
            if c not in code and c not in except_colors:
                break
        code += c
    return code


def verify(test, code, test_dict={}, code_dict={}):
    if not code_dict:
        code_dict = count_colors(code)

    if not test_dict:
        test_dict = count_colors(test)

    total = 0
    for c in colors:
        total += min(code_dict[c], test_dict[c])

    good = 0
    for c, a in zip(code, test):
        if c == a:
            good += 1

    return good, total - good
