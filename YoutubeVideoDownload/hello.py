q_list = ["蘋果的英文是？", "10-8 = ?"]
a_list = ["apple", "2"]

score = 0

for q,a in zip(q_list,a_list):
    print(q, end=' ')
    ans = input().lower().strip()

    if ans == a:
        print("Great Job!")
    else:
            print("Never Give Up!")