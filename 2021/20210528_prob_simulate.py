import random

score = 0
result_counter = {}
for i in range(1000):
    result_counter[i+1] = 0

# 繰り返し回数
c = 10000000

for i in range(c):
    while True:
        r = random.randrange(1, 7)
        score += r
        if r == 1:
            result_counter[score] += 1
            # if result_counter.get(score):
            #     result_counter[score] += 1
            # else:
            #     result_counter[score] = 1
            score = 0
            break
    print(f"trial(s) {i}/{c}", end="\r")

results = []

for key, value in result_counter.items():
    # print(f"{key},{value}")
    results.append(f"{key},{value}")

s = "\n".join(results)

with open("histdata.csv", mode="w", encoding="utf-8") as hist:
    hist.write(s)