import random

def main():
  secret = random.randint(1, 50)

  while True:
    try:
      guess = int(raw_input("Guess a number between 1 and 50 (type 0 to give up):"))

      if guess == secret:
        print "Congratulations, " + str(guess) + " is the secret number!"
        break
      elif guess == 0:
        print "That's a shame... Try again another time!"
        break
      elif guess < secret:
        print "Too bad, that's not the secret number! Try a higher number..."
      elif guess > secret:
        print "Too bad, that's not the secret number! Try a lower number..."
    except:
      print "Please enter a whole number to play!"

main()