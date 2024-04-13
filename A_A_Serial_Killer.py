# initial_vic = input().split()
# n =int(input())
# potential_vic =initial_vic
# x = ' '.join(potential_vic)
# print(x)
# for i in range(n):
#     murderedV = input().split()
#     for i in range(2):
#         if murderedV[0] == potential_vic[i]:
#             potential_vic[i]=murderedV[1]
#             y = ' '.join(potential_vic)
#             print(y)













# initial_ppl = input().split()
# n =int(input())
# potential_ppl ={0:initial_ppl}

# for day in (1,n+1):
#     tegeday , teteki = input().split()
#     potential_ppl[day] = [1 for tegeday in potential_ppl[day-1] if tegeday != tegeday]
#     potential_ppl[day].append(teteki)

# for day, te





































initial_victims = input().split()
n = int(input())
potential_victims = {0: initial_victims}

for day in range(1, n+1):
    murdered, replacement = input().split()
    potential_victims[day] = [1 for victim in potential_victims[day-1] if victim != murdered]
    potential_victims[day].append(replacement)

for day, victims in potential_victims.items():
    print(f"Day {day}: {' '.join(victims)}")