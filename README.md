# mPass

mPass is a Python password security auditor. It analyzes a password using several criteria and gives it a score from 0 to 100.

## Features

- Password length analysis
- Unique character analysis
- Character class detection
- Theoretical entropy calculation
- Repeated character detection
- Sequential pattern detection
- Repeated pattern detection
- Dictionary detection
- Security score from 0 to 100

## How it works

### Password length — /20

- Less than 8 characters: 0 points
- 8–11: 5 points
- 12–15: 10 points
- 16–19: 15 points
- 20 or more: 20 points

### Character diversity — /15

The diversity is calculated as:

D = unique characters / password length

- Less than 0.30: 0 points
- 0.30–0.49: 5 points
- 0.50–0.69: 9 points
- 0.70–0.89: 12 points
- 0.90 or more: 15 points

### Character classes — /15

mPass checks for four classes:

- Lowercase letters: 26 characters
- Uppercase letters: 26 characters
- Digits: 10 characters
- Special characters: 32 characters

The points depend on the number of classes used:

- 1 class: 3 points
- 2 classes: 7 points
- 3 classes: 11 points
- 4 classes: 15 points

### Theoretical entropy — /30

Entropy is calculated with:

H = L × log2(N)

Where L is the password length and N is the size of the character set used.

- Less than 40 bits: 0 points
- 40–59 bits: 10 points
- 60–79 bits: 20 points
- 80–99 bits: 25 points
- 100 bits or more: 30 points

This is theoretical entropy. It assumes characters are selected independently and uniformly, which does not necessarily represent how humans create passwords.

### Repeated characters — /20

mPass finds the character that appears the most and calculates:

R = maximum character frequency / password length

- 20% or less: 20 points
- 21–30%: 14 points
- 31–40%: 8 points
- More than 40%: 0 points

### Sequential patterns — -10 points

mPass detects sequences of at least three consecutive characters, increasing or decreasing.

Examples:

- abc
- 123
- xyz
- cba
- 987

If a sequence is detected, 10 points are removed.

### Repeated patterns — -10 points

mPass detects consecutive repeated blocks such as:

- abcabcabc
- 121212
- testtest

If a repeated pattern is detected, 10 points are removed.

### Dictionary detection — -20 points

mPass checks whether the password:

- Exactly matches an entry in the wordlist
- Contains an entry from the wordlist

If a dictionary match is found, 20 points are removed.

## Score

The five positive criteria can provide a maximum of 100 points:

- Length: 20
- Diversity: 15
- Character classes: 15
- Entropy: 30
- Repeated characters: 20

The penalties are then applied:

- Sequential pattern: -10
- Repeated pattern: -10
- Dictionary match: -20

The final score is always limited to the range 0–100.

## Project structure

mPass/
├── main.py
├── password.py
├── checker.py
├── wordlist.txt
├── .gitignore
└── README.md

## Technologies

- Python 3
- Object-Oriented Programming
- Git / GitHub

## Disclaimer

mPass is an educational project. The score is a custom scoring system created for this project and is not an official measure of password security.

The entropy calculation is theoretical and does not account for all real-world password attack techniques.

## AI transparency

The core business logic of mPass was designed and implemented by me, including the password analysis methods, entropy calculation, pattern detection, dictionary detection and scoring system.

I used AI assistance mainly for the CLI interface, development guidance and documentation.

This README.md was written with the assistance of AI.
