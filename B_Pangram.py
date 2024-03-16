n = int(input())
string = input().lower()

letters = set(string)

if len(letters) == 26:
    print("YES")
else:
    print("NO")