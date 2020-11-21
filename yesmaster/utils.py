import random, copy

colors = "ROGBYAPW"  # Red, Orange, Green, Blue, Yellow, grAy, Pink, White


def make_dict(dic, depth, max_depth, end):
    depth += 1
    if depth < max_depth:
        for c in colors:
            dic[c] = {}
            dic[c] = make_dict(dic[c], depth, max_depth, end)
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
