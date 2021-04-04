# my first game
score = 0

word = input('choose write word from this jumble "rerfpe" - ')
a = "prefer"
if(word == a):
      print('right')
      score += 1
else:
      print('wrong')

word1 = input('choose write word from this jumble "tuensdt" - ')
b = 'student'
if(word1 == b):
    print('right')
    score += 1
else:
    print('wrong')

word2 = input('choose write word from this jumble "seronpes" -' )
c = 'response'
if(word2 == c):
    print('right')
    score += 1
else:
    print('wrong')

word3 = input('choose write word from this jumble "vreiopus" -')
d = 'previous'
if(word3 == d):
    print('right')
    score += 1
else:
    print('wrong')

word4 = input('choose write word from this jumble "socoinus" -')
e = 'consious'
if(word4 == e):
    print('right')
    score += 1
else:
    print('wrong')

print("Your score is " + str(score) + "/5")
