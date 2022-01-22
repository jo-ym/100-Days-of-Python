# 100-Days-of-Python
Record my notes and projects about Udemy Class "100 Days of Code: The Complete Python Pro Bootcamp for 2022"

## Check List
### Beginner
- [x] Day 001 - Print, Variables, Input
- [x] Day 002 - Data Types, Numbers, Operations, Type Conversion, f-Strings
- [x] Day 003 - Conditional Statementsm Logical Operators, Code Blocks and Scope
- [x] Day 004 - Randomisation and Lists
    - Good Video: [Random vs. Pseudorandom Number Generators. Created by Brit Cruise.](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators)
    - Good Tool: [Ask Python](https://www.askpython.com/)
    - Need `import random`
    - Seed & State
        - `random.seed(n)`
        - `random.getrandbits(k)`: returns a Python integer with k random bits. This is useful for methods like randrange() to handle arbitrary large ranges for random number generation.
        - `random.getstate()` & `random.setstate()`
    - Random Integers
        - `random.randrange(start, stop, step)`: selected integer from range(start, stop, step)
        - `random.randint(a, b)`: [a to b]
    - Random floating point numbers
        - `random.random()`: [0.0 to 1.0)
            - `random.random() * N` = 0.0 to N-1.99999
        - `random.uniform(a, b)`: a <= N <= b if a <= b and b <= N <= a if b < a
        - `random.expovariate(lambda)`: corresponding to an exponential distribution
        - `random.gauss(mu, sigma)`: corresponding to a gaussian distribution
        - There are similar functions for other distributions, such as Normal Distribution, Gamma Distribution, etc.
    - Random Sequences
        - `random.shuffle(x)`:  shuffle the sequence **in place**
        - `random.choice(seq)`: randomly pick up an item from a List/sequence
        - `random.sample(population, k)`: Returns a random sample from a sequence of length k.
- [x] Day 005 - For Loops, Range and Code Blocks
    - [Have I Been Pwned?](https://haveibeenpwned.com/)
- [x] Day 006 - Functions, Code Blocks and While Loops
    - Good Web for Learning in Game: [Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json)
    - [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [x] Day 007 - Hangman Project
- [x] Day 008 - Functions with Inputs
    - `math.ceil(x)` vs. `math.floor(x)`
        - the smallest integer greater than or equal to x vs. the largest integer not greater than x
        - returns float
- [x] Day 009 - Dictionaries & Nesting
- [x] Day 010 - Functions with Outputs
- [x] Day 011 - Blackjack Capston Project
- [x] Day 012 - Namespaces - Local vs. Global Scope
    - There is no block scope for `if`, `for`,etc in Python.
- [x] Day 013 - Debugging
    - [Visualized Debugging Tool](https://pythontutor.com/visualize.html#mode=edit)
- [x] Day 014 - Higher or Lower Project

## Intermediate
- [x] Day 015 - Coffee Machine Project
- [x] Day 016 - Object Oriented Programming
    - [Pokemon Database](https://pokemondb.net/pokedex/game/x-y)
    - [Python Package Index, PyPi](https://pypi.org/)
    - [prettytable - Tutorial.wiki](https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki)
- [x] Day 017 - Quiz Project
    - [Open Trivia Database](https://opentdb.com/)
- [x] Day 018 - Turtle & the Graphical User Interface
    - [Turtle](https://docs.python.org/3/library/turtle.html)
    - [Turtle Colors](https://cs111.wellesley.edu/labs/lab01/colors)
    - [Trinket Colors](https://trinket.io/docs/colors)
- [x] Day 019 - More Turtle Graphics, Event Listeners, State and Multiple Instances
    - Turtle Coordinate System
        - E = 0, N = 90, W=180, S = 270
        - All turtle positions are measured from their center.
- [x] Day 020 - Snake Game Part 1_Animation & Coordinates
- [x] Day 021 - Snake Game Part 2_Inheritance & List Slicing
    - `super(ClassName, self).__int__()`
- [x] Day 022 - Pong Game
- [x] Day 023 - The Turtle Crossing Capston Project
- [x] Day 024 - Files, Directories, Paths
    - The root is simply `./`, when writing python code you don't need to specify "C:" ( Windows ) or "Macintosh HD" ( Mac )
- [ ] Day 025
- [ ] Day 026
- [ ] Day 027
- [ ] Day 028
- [ ] Day 029
- [ ] Day 030
- [ ] Day 031
- [ ] Day 032
- [ ] Day 033
- [ ] Day 034
- [ ] Day 035
- [ ] Day 036
- [ ] Day 037
- [ ] Day 038
- [ ] Day 039
- [ ] Day 040
- [ ] Day 041
- [ ] Day 042
- [ ] Day 043
- [ ] Day 044
- [ ] Day 045
- [ ] Day 046
- [ ] Day 047
- [ ] Day 048
- [ ] Day 049
- [ ] Day 050
- [ ] Day 051
- [ ] Day 052
- [ ] Day 053
- [ ] Day 054
- [ ] Day 055
- [ ] Day 056
- [ ] Day 057
- [ ] Day 058
## Advanced
- [ ] Day 059
- [ ] Day 060
- [ ] Day 061
- [ ] Day 062
- [ ] Day 063
- [ ] Day 064
- [ ] Day 065
- [ ] Day 066
- [ ] Day 067
- [ ] Day 068
- [ ] Day 069
- [ ] Day 070
- [ ] Day 071
- [ ] Day 072
- [ ] Day 073
- [ ] Day 074
- [ ] Day 075
- [ ] Day 076
- [ ] Day 077
- [ ] Day 078
- [ ] Day 079
- [ ] Day 080
## Professional
- [ ] Day 081
- [ ] Day 082
- [ ] Day 083
- [ ] Day 084
- [ ] Day 085
- [ ] Day 086
- [ ] Day 087
- [ ] Day 088
- [ ] Day 089
- [ ] Day 090
- [ ] Day 091
- [ ] Day 092
- [ ] Day 093
- [ ] Day 094
- [ ] Day 095
- [ ] Day 096
- [ ] Day 097
- [ ] Day 098
- [ ] Day 099
- [ ] Day 100!!!
