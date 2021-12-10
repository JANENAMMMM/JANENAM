count=input("몇 개의 정수를 입력하실 건가요?")
given=input("위의 입력한만큼 정수를 입력하시오(space 필요)")
given3=[]
given2=given.split(" ")
for i in given2:
    given3.append(int(i))

print("최댓값은 ",max(given3))
print("최솟값은 ",min(given3))