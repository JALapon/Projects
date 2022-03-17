print("Hello!" * 2,"Welcome to the property calculator")

print("insert" + "Information:")

#sqft = 100 square feet cost 100 dollars per square foot.
#furn = 200 estimated cost of each piec of furniture.

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

print(market_average >= cost_of_house)

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
#Is the house in good condition
#10: -0 great condition
#9: -5000 good condition
#8: -10000 decsent
#7: -20000 needs work
#6: -40000 poor condition
#5-0: Not salvagable
#damage = input("Enter if a number based on the condition of the house: ")





#Requirements for sprint 1
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

                      

                 
                



