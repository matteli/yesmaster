from utils import make_tree, random_code, random_code_4_colors, verify

class Algo:

    def __init__(self):
        self.test_tree = make_tree({}, 0, 4, {"done": False, "good": 0, "bad": 0})
        self.test_done = []

    def get(self):
        if len(self.test_done) == 0:
            test = random_code_4_colors()
        else:
            while True:
                test = random_code()
                if self.test_tree[test[0]][test[1]][test[2]][test[3]]["done"] == False:
                    compatible = True
                    for t in self.test_done:
                        good, bad = verify(test, t)
                        if (
                            good != self.test_tree[t[0]][t[1]][t[2]][t[3]]["good"]
                            or bad != self.test_tree[t[0]][t[1]][t[2]][t[3]]["bad"]
                        ):
                            self.test_tree[test[0]][test[1]][test[2]][test[3]]["done"] = True
                            compatible = False
                            break
                    if compatible:
                        break
        return test

    def report(self, test, good, bad):
        self.test_tree[test[0]][test[1]][test[2]][test[3]]["good"] = good
        self.test_tree[test[0]][test[1]][test[2]][test[3]]["bad"] = bad
        self.test_tree[test[0]][test[1]][test[2]][test[3]]["done"] = True
        self.test_done.append(test)
        return
