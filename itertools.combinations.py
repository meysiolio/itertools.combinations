from itertools import combinations

string, r = input().split()

for i in range(1,int(r)+1):
    print(*[''.join(i) for i in list(combinations(sorted(string),i))],sep='\n')