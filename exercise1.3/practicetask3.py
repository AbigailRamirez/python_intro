'''for Loop'''
for i in range(10,51,10):
    print(i)
    if i<50:
        continue
    print("and we're done!")

'''while Loop'''
num = 10
while num<51:
    print(num)
    if num==50:
        print("and we're done!")
    num+=10
