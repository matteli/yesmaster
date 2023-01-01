from ..utils import random_code, make_tree


class Algo:
    def __init__(self):
        self.test_tree = make_tree({}, 0, 4, False)
        self.test_done = []

    def get(self):
        while True:
            test = random_code()
            if self.test_tree[test[0]][test[1]][test[2]][test[3]] == False:
                self.test_tree[test[0]][test[1]][test[2]][test[3]] = True
                self.test_done.append(test)
                break
        return test

    def report(self, test, good, bad):
        pass
