#Maija Ehlinger
#May 22, 2017
#Homework 1 
birthyear = input("What year were you born?")
age = 2017 - int(birthyear)
if int(birthyear) > 2017:
  print ("Please enter a different date")
else:
  print("2. You are " + str(age) + " years old")
  print ("3. number of times your heart has beaten:"), print ((2017 - int(birthyear)) * 42000000)
  print ("4. Approximate number of times a bluewhale's heart has beaten in your lifetime:"), print ("xxx billion")
  print ("5. Approximate number of times a rabbit's heart has beaten in your lifetime:"), print ((2017 - int(birthyear)) * 63000000)
  print ("7. How old you are on Venus:"), print ((2017 - int(birthyear)) / .615)
  print ("8. How old you are on Neptune:"), print ((2017 - int(birthyear)) / 164.8)
  print ("9. Are you older or younger than me?")
  if age == 25 or age < 25:
    print ("You are younger than me")
  else:
    print ("You are older than me")
  print ("10. Our age difference:"), print ((2017 - int(birthyear)) -25)
  print ("11. Were you born in an even or odd year?")
  if (int(birthyear) % 2) == 0:
   print("Even")
  else:
   print("Odd")
  print (" 12. Number of times the Pittsburgh Steelers have won the Superbowl in your lifetime")
  if age < 9:
    print ("They have never won in your lifetime")
  elif age >= 43:
    print ("They have won the Superbowl 6 times")
  elif age >= 42:
    print ("They have won the Superbowl 5 times")
  elif age >= 39:
    print ("They have won the Superbowl 4 times")
  elif age >=38:
    print ("They have won the Superbowl 3 times")
  elif age >=12:
    print ("The have won at least one Superbowl title in your lifetime")
  else:
    print ("They have never won a Superbowl in your lifetime")

  print ("13. Who was President when you were born?")
  if int(birthyear) >= 2008: 
    print ("President Barak Obama")
  elif int(birthyear) >=2001:
    print ("George W. Bush")
  elif int(birthyear) >=1993:
    print ("Bill Clinton")
  elif int(birthyear) >=1989:
    print ("George H. W. Bush")
  elif int(birthyear) >=1981:
    print ("Ronald Reagan")
  elif int(birthyear) >=1977:
    print ("Jimmy Carter")
  elif int(birthyear) >= 1974:
    print ("Gerald Ford")
  elif int(birthyear) >= 1969:
    print ("Richard Nixon")
  elif int(birthyear) >= 1963:
    print ("Lyndon B. Johnson")
  elif int(birthyear) >=1961:
    print ("John F. Kennedy")
  elif int(birthyear) >= 1953:
    print ("Dwight D. Eisenhower")
  elif int(birthyear) >= 1945:
    print ("Harry S. Truman")
  elif int(birthyear) >=1933:
    print ("Franklin D. Roosevelt")
  else:
    print ("Your birthday is outside of the range")