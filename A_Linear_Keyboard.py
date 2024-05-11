from collections import Counter

t = int(input())

for _ in range(t):
    keyboard = input()
    word = input()
    result = 0
    idxMap = {char : index for index, char in enumerate(keyboard)}
   
    if len(word) == 0:
        print(0)
    for i in range(len(word) - 1):
        current_char = word[i]
        next_char = word[i + 1]
        difference = abs(idxMap[current_char] - idxMap[next_char])
        result += difference

    print(result)

        # for loop that iterates through the word value and deducts the value of that char refering from the idxMap from the value of the char next to it and if there is no other char next to it it will stop iteratigng througn the workdand the summation of the values optained from deducting it and getting it out of the absolute value would be tracked by the result variable