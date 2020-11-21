from utils import random_code, make_dict


def init():
    global test_dict, test_done
    test_dict = make_dict({}, 0, 4, False)
    test_done = []


def get():
    global test_dict, test_done
    while True:
        test = random_code()
        if test_dict[test[0]][test[1]][test[2]][test[3]] == False:
            test_dict[test[0]][test[1]][test[2]][test[3]] = True
            test_done.append(test)
            break
    return test


def report(test, good, bad):
    pass
