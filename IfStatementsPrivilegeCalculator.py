isMale= True
isTall= True

if isMale and isTall:
    print("you are a tall male")
elif isMale and not(isTall):
    print("You are a short male")
elif not(isMale) and isTall:
    print("you are not a male but are still tall")
else:
    print("you are not a male and not tall")
