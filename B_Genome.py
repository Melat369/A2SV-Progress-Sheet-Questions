from collections import Counter

n = int(input())
s = input()
x = n//4
occurance = Counter(s)
max_count = max(occurance[letter] for letter in "ACGT")

missing_counts = {letter: max(0, x - count) for letter, count in occurance.items()}

result = ""
for letter in s:
    if letter == '?':
        for l in "ACGT":
            if missing_counts[l] > 0:
                result += l
                missing_counts[l] -= 1
                break
    else:
        result += letter


is_balanced = all(count == x for count in Counter(result).values())
if n%4!= 0:
    print('===')

if is_balanced:
    print(result)
else:
    print("===")







# each occurence of the letters should be x = n/4 times
# if the maximum occurance of a letter is x times then we will go and replace the "?" characters by the missing letters uptill all the occurences of the letters A, C, G , T are equal to the value of x and print out the resulting string
# number of A == C == G == T
def decode_genome(n, s):
    # Count occurrences of each nucleotide
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0, '?': 0}
    for char in s:
        counts[char] += 1
    
    # Calculate the maximum number of occurrences for each nucleotide
    max_count = max(counts[nuc] for nuc in 'ACGT')
    
    # If the count of any nucleotide exceeds the maximum possible count, it's not possible to decode the genome
    for nuc in 'ACGT':
        if counts[nuc] > max_count + counts['?']:
            return "==="

    # Fill in the question marks with the nucleotide that is needed to balance the counts
    decoded_genome = []
    for char in s:
        if char == '?':
            for nuc in 'ACGT':
                if counts[nuc] < max_count:
                    decoded_genome.append(nuc)
                    counts[nuc] += 1
                    break
            else:
                return "==="  # No nucleotide can balance the counts, return "===".
        else:
            decoded_genome.append(char)
    
    return ''.join(decoded_genome)

# Reading input
n = int(input())
s = input().strip()

# Decode the genome and print the result
result = decode_genome(n, s)
print(result if result != "===" else result)
