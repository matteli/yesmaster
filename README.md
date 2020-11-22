Yesmaster
=========

Yesmaster is a terminal mastermind game. It's possible to play normally or let's play the computer with algorithm :
- random_idiot : totally random and idiot
- random_no_repeat : random but never the same code twice
- compatible : play random but take in consideration the verification and play only code compatible with it
- compatible_2_colors : play the two first code with 8 colors and after that play compatible

You can add your personnal algorithm with a python file in the algo directory. 3 functions must be present :
- init() : execute at the beginning of each game. Return nothing.
- get() : execute for choosing the code. Must return a 4 letters string with letters among ROGBYAPW
- report(test, good, bad) : execute with 3 arguments (test : the code that you push with get, good : the number of good colors at good place, bad : the number of good colors at wrong place). Return nothing.

```
usage: yesmaster.py [-h] [--algo ALGO] [--loop LOOP] {play,auto}

positional arguments:{play,auto}  play or stat

optional arguments:
  -h, --help   show this help message and exit
  --algo ALGO  Choose an algo present in the algo folder
  --loop LOOP  Number of games
```