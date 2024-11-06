import random
print("hey'Lets Play")
computerNumber=random.randint(1,100)
round=0
userNumber=-1
while(userNumber!=computerNumber):
 userNumber=int(input("Enter the guess number:"))
 if(userNumber>computerNumber):
      print(f"Try Again! Guess Number is less then your   Number {userNumber}")
      round+=1
 elif(computerNumber>userNumber):
      print(f"Try Again! Guess Number is greater then your  Number {userNumber}.")
      round+=1
print(f"You have guessed the correct number {computerNumber} in {round} Attempt")
