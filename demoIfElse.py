# demoIfElse.py 
# if else만 - switch구문 
# 블럭 처리: ctrl + / 
# score = int(input("점수를 입력:"))
# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

#반복구문
value = 5 
while value > 0:
    print(value)
    value -= 1 

#딕셔너리
d = {"apple":100, "kiwi":200}
for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for k,v in d.items():
    print(k, v)

