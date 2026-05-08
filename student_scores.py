scores = [100, 55,45,85,90,]

Largest_score = max(scores)
print(f"largest : {Largest_score}")
Lowest_score = min(scores)
print(f"Lowest : {Lowest_score}")

Average = sum(scores)/len(scores)
print(f"Total Average : {round(Average,1)}")

num = sorted(scores, reverse=True)
for new in num:
    if new >  60:
        print(new)

    
    