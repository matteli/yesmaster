Yes Master
==========
Goal
----
Yesmaster is a terminal mastermind game. It's possible to play normally or let's play the computer with algorithm :
- random_idiot : totally random and idiot
- random_no_repeat : random but never the same code twice
- compatible : play random but take in consideration the verification and play only code compatible with it
- compatible_8in2 : play the two first code with 8 colors and after that play compatible
- compatible_4in1 : play like compatible but the first must be 4 differents colors
- one_step_ahead : play the move that has the highest expected elimination

Installation
------------
The program is available on [Pypi](https://pypi.org/project/yesmaster/).
You need at least python 3.6 and you can use pipx to install it.
```
pipx install yesmaster
```

Usage
-----
```
usage: yesmaster.py [-h] [--algo ALGO] [--loop LOOP] {play,auto}

positional arguments:{play,auto}  play yourself or let's computer playing

optional arguments:
  -h, --help   show this help message and exit
  --algo ALGO  Choose an algo present in the algo folder
  --loop LOOP  Number of games
```
Test your algorithm
-------------------
You can add your personnal algorithm with a python file in the algo directory (the name of the python file will be the name of the algo to call in the command line). A template file shows you how your algo must be organized. Two functions are mandatory in a class name Algo :
- get(self) : executed for choosing the code. Must return a 4 letters string with letters among ROGBYAPW
- report(self, test, good, bad) : executed with 3 arguments (test : the code that you pushed with get, good : the number of goods colors at good place, bad : the number of goods colors at wrong place). Return nothing.

