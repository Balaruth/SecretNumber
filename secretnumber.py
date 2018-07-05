import random

secret = random.randint(1, 50)
guess = 0

while guess != secret:

  guess = int(raw_input("Guess a number between 1 and 50 (type 0 to give up):"))
  if guess > 0:
    if guess < secret:
      print "Too bad, that's not the secret number! Try a higher number..."
    elif guess > secret:
      print "Too bad, that's not the secret number! Try a lower number..."
  else:
    print "That's a shame... Try again another time!"
    break
else:
  print "Congratulations! You guessed the secret number!"