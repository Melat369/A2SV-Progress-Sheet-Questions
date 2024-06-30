n = int(input())
magic_numbers = set([1, 14, 144])

while True:
    if n in magic_numbers:
        print("YES")
        break
    
    found = False
    for num in [144, 14, 1]:
        if str(num) in str(n):
            n = int(str(n).replace(str(num), ""))
            magic_numbers.add(num)
            found = True
            break
    
    if not found:
        print("NO")
        break