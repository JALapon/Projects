print("Hello!" * 2,"Welcome to the property calculator")

print("insert" + "Information:")


#sqft = 100 square feet cost 100 dollars per square foot.
#furn = 200 estimated cost of each piece of furniture.

#1.
amount_of_sqft = int(input("Enter square footage: "))
sqft = int(input("multiply by: "))
cost = amount_of_sqft * sqft
print(cost)


#2.
#true = under market avg
#false = above market avg
market_average = int(input("Enter avg amount ")) # depends on area
cost_of_house = int(input("Enter cost amount "))

#num1= cost of your house
#num2= cost of average house
print(market_average >= cost_of_house)

def getSmaller(num1,num2):
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    return smaller

def main():
    userInput1 = int(input("Enter cost of your house: "))
    userInput2 = int(input("Enter average cost: "))

    smallerNumber = getSmaller(userInput1,userInput2)
    print("The Smaller of the two numbers is", smallerNumber)

main()

#3.
#if under market value input to find remainder
market_average = int(input("Enter avg amount "))
cost_of_house = int(input("Enter cost amount "))

print(market_average % cost_of_house)

#4.
#if house is furnished input
Furnished = input("Enter if house is furnished a number above 1: ")
house_is_furn = int(Furnished)
if(house_is_furn > 0):
    print("Yes furnished")
else:
    print("Not furnished")

#5a.
#if furnished add to cost of house,if not skip to 6.
#add how many pieces of furn first.
amnt_of_furn = int(input("Enter amount of furniture "))
furn = int(input("Enter cost of furniture "))
total = amnt_of_furn * furn
print(total)

#5b.
#if furnished add to total cost of house
house_cost = int(input("Enter house cost: "))
furn_cost = int(input("Enter furn cost: "))
total_added = house_cost + furn_cost
print(total_added)

#6.
score = 11
for x in range (score):
    print(x, end=" ")
#Is the house in good condition.Enter a number below based on what you belive is the condition of your house.
#9-10: -0 great condition
#8-9: -5000 good condition
#7-8: -10000 decsent
#6-7: -20000 needs work
#5-6: -40000 poor condition
#4-5: salvagable
#0-4:Reconsider
score = float(input("Enter the level of your house: "))
if score > 10:
    print("Error")
elif score >= 9:
    print("Great Condition")
elif score >= 8 and score <= 9:
    print("Good Condition")
elif score >= 7 and score <= 8:
    print("Decsent")
elif score >= 6 and score <= 7:
    print("Needs Work")
elif score >= 5 and score <= 6:
    print("Poor Condition")
elif score >= 4 and score <= 5:
    print("salvagable")
elif score >= 0 and score <= 4:
    print("Reconsider")
else:
    print("Error")


#Other ways to find certain prices and cost. Sprint 2 Inspection requirements.

#find how many times the cost of your house fits into average cost
Average_cost_house = int(input("Enter avg cost: "))
Your_house_cost = int(input("Enter cost for your house: "))
cost = Average_cost_house // Your_house_cost
print(cost)

#what is your house worth if doubled
Your_house_cost = int(input("Enter cost for your house: "))
To_the_power = int(input("Enter the power: "))
cost = Your_house_cost ** To_the_power
print(cost)

#the difference between your and the average cost of a house in florida
Your_house = int(input("Enter your house cost: "))
Average_house = int(input("Enter average house cost: "))
difference = Your_house - Average_house
print("difference: ",format(difference, "d"), "$" ,sep="")

#what average cost divided by your house cost is
Average_house = int(input("Enter avg House cost: "))
Your_house = int(input("Enter your house cost: "))
Answer = Average_house / Your_house
print("Answer: ",format(Answer, ".2f"),"%", sep="")

#If selling what kind of people are moving out with you.
doAgain = "yes"
while doAgain == ("yes"):
    Person = input("Enter the people that live with you: ")
    doAgain = input("Type 'yes' to enter another person or anything else to stop: ")
print("Done!")

#Adding a custm cost of furniture to eachother.
total = 0
for x in range (5):
    number = int(input("Enter price of furniture: "))
    total += number
    print("The total cost of furniture is:",total)

#Buying furniture for future home.
total = 0
for x in range (5):
    number = int(input("Enter price of furniture: "))
    total -= number
    print("The total cost of furniture is:",total)

#Is there profit in your house.
house_cost = input("Enter cost of your house: ")
avg_cost = input("Enter cost of average cost: ")
if not(house_cost > avg_cost or avg_cost < house_cost):
    print("Profit")
else:
    print("No Profit")
    
#Other way of writing profit in a shorter way
house_cost = input("Enter cost of your house: ")
avg_cost = input("Enter cost of average cost: ")
if(house_cost != avg_cost):
    print("No Profit")
else:
    print("Profit")

                 
                



