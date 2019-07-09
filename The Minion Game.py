def minion_game(str1):
    a=0
    b=0
    vowels='AEIOU'
    for i in range(len(str1)):
        if(str1[i] in vowels):
            a=a+(len(s)-i)
        else:
            b=b+(len(s)-i)
    if(a<b):
        print("Stuart "+str(b))
    elif(a>b):
        print("Kevin "+str(a))
    else:
        print("Draw")
    # your code goes here

