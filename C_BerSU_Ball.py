boys = int(input())
boySkill = [int(x) for x in input().split()]
girls = int(input())
girlSkill = [int(x) for x in input().split()]

boySkill.sort()
girlSkill.sort()

g, b = 0,0
maxPair = 0
while b<boys and g<girls:
    if abs(boySkill[b] - girlSkill[g]) <= 1:
            maxPair += 1
            b += 1
            g += 1
    elif boySkill[b] < girlSkill[g]:
            b += 1
    else:
            g += 1

print(maxPair)
    