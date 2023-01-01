#!/usr/bin/python3
from .utils import *
import argparse
import time
import importlib
import sys


__version__ = "3.0.1"


def play():
    code = random_code()
    code_dict = count_colors(code)
    attempt = 0
    while True:
        forbiden = True
        while forbiden:
            print("Test (4 letters among ROGBYAPW):")
            test = input().upper()
            if len(test) != 4:
                print("Test must be 4 letters among ROGBYAPW.\n")
            else:
                forbiden = False
                for l in test:
                    if l not in colors:
                        print(l + " is not in ROGBYAPW.\n")
                        forbiden = True
        attempt += 1

        good, bad = verify(test, code, code_dict=code_dict)

        print(str(good) + " good " + str(bad) + " bad\n")
        if good == 4:
            print("Bravo " + str(attempt) + " attempts")
            break


def auto(algo, loop):
    start = time.time()
    total_attempt = 0
    max_attempt = 0
    min_attempt = 100000000
    history = []
    try:
        algo_module = importlib.import_module(".algo." + algo, package="yesmaster")
    except ModuleNotFoundError:
        print("Algo " + str(algo) + " is not implented.")
        return

    for game in range(loop):
        code = random_code()
        code_dict = count_colors(code)
        attempt = 0
        algo = algo_module.Algo()
        history_test = []
        while True:
            test = algo.get()
            attempt += 1
            good, bad = verify(test=test, code=code, code_dict=code_dict)
            algo.report(test, good, bad)
            report = {"test": test, "good": good, "bad": bad}
            history_test.append(report)
            if good == 4:
                total_attempt += attempt
                if attempt > max_attempt:
                    max_attempt = attempt
                if attempt < min_attempt:
                    min_attempt = attempt
                print(
                    "Bravo Game n°:"
                    + str(game + 1)
                    + "/"
                    + str(loop)
                    + " Number of attempts:"
                    + format(attempt, "05d")
                    + " Average:"
                    + str(total_attempt / (game + 1))
                )
                break
        history.append(history_test)
    end = time.time()
    print(
        "Average:"
        + str(total_attempt / loop)
        + " max:"
        + str(max_attempt)
        + " min:"
        + str(min_attempt)
        + " in "
        + str(end - start)
        + " seconds"
    )
    while True:
        print("Enter number of game for history or (q)uit :")
        key = input()
        if key == "q":
            break
        else:
            try:
                num = int(key)
                for d in history[num - 1]:
                    print(d["test"] + " " + str(d["good"]) + " " + str(d["bad"]))
            except ValueError:
                print("need integer")
            except IndexError:
                print("integer must be between 1 and " + str(len(history)))


def main(what, algo, loop):
    if what == "play":
        play()
    elif what == "auto":
        auto(algo, loop)


def run():
    parser = argparse.ArgumentParser(
        prog="Yesmaster", description="Play or stat Mastermind"
    )
    parser.add_argument(
        "what", choices=["play", "auto"], default="play", help="play or stat"
    )
    parser.add_argument(
        "-a",
        "--algo",
        type=str,
        default="compatible",
        help="Choose an algo present in the algo folder",
    )
    parser.add_argument("-l", "--loop", type=int, default=10, help="Number of games")
    parser.add_argument("-v", "--version", action="version", version=__version__)

    args = parser.parse_args(sys.argv[1:])
    main(what=args.what, algo=args.algo, loop=args.loop)


if __name__ == "__main__":
    run()
