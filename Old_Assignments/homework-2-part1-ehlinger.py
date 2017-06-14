#Maija Ehlinger
#May 24, 2017
#Homework 2, Part 1 

#Part One: Lists

numbers = [22,90,0,-10,3,22,48]
#1) Make a list of the following numbers 
print("1.", numbers)
#2) Display the number of elements in the list. This is the len()
print("2.", len(numbers))
#3) Display the 4th element in the list. This is numbers[# you want in the list starting with zero]
print("3.", numbers[3])
#4) Display the sum of the 2nd and 4th element of the list.
print("4.", numbers[1] + numbers[3])
#5) Display the 2nd-largest value in the list.
#for things in sorted(numbers):
  #print (things) 
print("5.", numbers[6])
#6) Display the last element of the original unsorted list
print("6.", numbers[6])

print("7. is long and hard and I will come back to it") 

#8) Display the sum of all of the numbers divided by two 
print("8.", sum(numbers) / 2)

#PART ONE: Dictionaries

movie = {
  'title': 'Spotlight',
  'year': 2015,
  'director': 'Tom McCarthy'
}
print("8. My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

#9) On the lines after that, add entries to the movie dictionary for budget and revenue 
#(you'll use code like movie['budget'] = 1000), and print out the difference between the two.
movie = {
  'title': 'Spotlight',
  'year': 2015,
  'director': 'Tom McCarthy',
  'budget': 20000000,
  'revenue': 92000000
}
print("9. It made $", movie['revenue'] - movie['budget'], "at the box office")

if movie['revenue'] > movie['budget']:
  print ("10. It was a good investment")
else: print ("10. It was a flop")

boroughs = {
  'Manhattan': 1600000,
  'Brooklyn': 2600000,
  'Bronx': 1400000,
  'Queens': 2300000,
  'Staten Island': 470000
}
print("12. The population of Brooklyn is", boroughs['Brooklyn'])

#13) Display the combined population of all five boroughs.
print("13. The population off all 5 New York boroughs is", boroughs['Manhattan'] + boroughs['Brooklyn'] + boroughs['Bronx'] + boroughs['Queens'] + boroughs['Staten Island'])
#print("14. Percentage of New Yorkers who live in Manhattan:", boroughs['Manhattan'] / (boroughs['Manhattan'] + boroughs['Brooklyn'] + boroughs['Bronx'] + boroughs['Queens'] + boroughs['Staten Island']))
#print(boroughs.keys())
print("14. Percentage of New Yorkers who live in Manhattan:", boroughs['Manhattan'] / sum(boroughs.values()))

#14) Display what percent of NYC's population lives in Manhattan.

#print("5.", numbers.sort())  ASK...why does this come up with NONE? when you run it?





