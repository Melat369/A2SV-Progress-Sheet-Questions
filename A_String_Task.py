name = str(input())
vowels = 'aeiouAEIOU'
new = ""
for char in name:
    if char not in vowels:
        new += "."+char.lower()
print(new)



