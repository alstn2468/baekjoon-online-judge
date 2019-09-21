
# 문제
# According to Wikipedia, FizzBuzz is a group word game for children to teach them about division.
# This may or may not be true, but this question is generally used to torture screen
# young computer science graduates during programming interviews.
# Basically, this is how it works: you print the integers from 1 to N,
# replacing any of them divisible by X with Fizz or, if they are divisible by Y , with Buzz.
# If the number is divisible by both X and Y , you print FizzBuzz instead.
# Check the samples for further clarification.

# 입력
# Input file will contain a single test case.
# Each test case will contain three integers on a single line, X, Y and N (1 ≤ X < Y ≤ N ≤ 100).

# 출력
# Print integers from 1 to N in order, each on its own line,
# replacing the ones divisible by X with Fizz,
# the ones divisible by Y with Buzz and ones divisible by both X and Y with FizzBuzz.

X, Y, M = map(int, input().split())

for i in range(1, M + 1):
    if i % X == 0 and i % Y == 0:
        print("FizzBuzz")

    elif i % X == 0:
        print("Fizz")

    elif i % Y == 0:
        print("Buzz")

    else:
        print(i)
