n = int(input())

for i in range(n):
    total = 0
    score = 0
    answer = input()
    for x in answer:
        if (x == "O"):
            score += 1
            total += score
        else:
            score = 0
                
    print(total)
