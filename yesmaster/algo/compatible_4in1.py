from utils import make_tree, random_code, random_code_4_colors, verify


def init():
    global test_dict, test_done
    test_dict = make_tree({}, 0, 4, {"done": False, "good": 0, "bad": 0})
    test_done = []


def get():
    global test_dict, test_done
    if len(test_done) == 0:
        test = random_code_4_colors()
    else:
        while True:
            test = random_code()
            if test_dict[test[0]][test[1]][test[2]][test[3]]["done"] == False:
                compatible = True
                for t in test_done:
                    good, bad = verify(test, t)
                    if (
                        good != test_dict[t[0]][t[1]][t[2]][t[3]]["good"]
                        or bad != test_dict[t[0]][t[1]][t[2]][t[3]]["bad"]
                    ):
                        test_dict[test[0]][test[1]][test[2]][test[3]]["done"] = True
                        compatible = False
                        break
                if compatible:
                    break
    return test


def report(test, good, bad):
    global test_dict, test_done
    test_dict[test[0]][test[1]][test[2]][test[3]]["good"] = good
    test_dict[test[0]][test[1]][test[2]][test[3]]["bad"] = bad
    test_dict[test[0]][test[1]][test[2]][test[3]]["done"] = True
    test_done.append(test)
    return
