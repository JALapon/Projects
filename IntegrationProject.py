"""
Name:Julio Lapon
Date Finished: 4/22/22
Sources: Professor Michael Osheroff, Andrew Krupp

This is my integration project that is a property calculator that roughly
 calculates teh cost of your based on square footage of your house and
 other items.
"""


def get_int_input(prompt):
    """
Here we ask the user to input the square footage of their property, so we
can determine an estimated amount of what their house is worth.

    """
    input_validation_is_still_happening = True
    while input_validation_is_still_happening:
        try:
            variable = int(input(prompt))
            input_validation_is_still_happening = False
            if variable < 0:
                print("Value cannot be negative. ")
                input_validation_is_still_happening = True
        except ValueError:
            print("Please enter a whole number. Error code 1")
        except UnboundLocalError:
            print("Please enter a value. Error code 2")
        except:
            print("Something went wrong. Error unknown")
    return variable


amount_sqft = get_int_input("Please enter the square footage of your house: ")
cost_of_house = amount_sqft * 100
print("The price of your house based on square footage is:", "$",
      cost_of_house)


def get_int_input(prompt):
    """
In this function we determine whether the average cost or the cost of the
house is worth more by asking the user to input the average cost of a house
 in their local area.

    """
    input_validation_is_still_happening = True
    while input_validation_is_still_happening:
        try:
            variable = int(input(prompt))
            input_validation_is_still_happening = False
            if variable < 0:
                print("Value cannot be negative. ")
                input_validation_is_still_happening = True
        except ValueError:
            print("Please enter a whole number. Error code 1")
        except UnboundLocalError:
            print("Please enter a value. Error code 2")
        except:
            print("Something went wrong. Error unknown")
    return variable


average_house_cost = get_int_input(
    "Please enter the average cost of a house depending on your area: ")

if average_house_cost > cost_of_house:
    print("The average house is worth more by", "$",
          average_house_cost - cost_of_house)
elif average_house_cost < cost_of_house:
    print("Your house is is more valuable by", "$",
          cost_of_house - average_house_cost)
elif average_house_cost == cost_of_house:
    print("The average cost and the cost of your house are the same.")


def get_int_input(prompt):
    """
In this function we multiply the amount of furniture the user has entered
 by an approximation amount and add it to the cost of the house,

    """
    input_validation_is_still_happening = True
    while input_validation_is_still_happening:
        try:
            variable = int(input(prompt))
            input_validation_is_still_happening = False
            if variable < 0:
                print("Value cannot be negative. ")
                input_validation_is_still_happening = True
        except ValueError:
            print("Please enter a whole number. Error code 1")
        except UnboundLocalError:
            print("Please enter a value. Error code 2")
        except:
            print("Something went wrong. Error unknown")
    return variable


if_house_is_furnished = get_int_input(
    "Please enter the amount of pieces of furniture you have.If you have no "
    "furniture put 0: ")

cost_of_house_with_furn = if_house_is_furnished * 200 + cost_of_house
print("The price of your house with furniture is", "$",
      cost_of_house_with_furn)


def get_int_input(prompt):
    """
Here we ask a person to rate the quality of their house from 1 to 10 that way
 we can determine whether the price of the house needs to be lowered depending
  on if there is damage to the house.

    """
    input_validation_is_still_happening = True
    while input_validation_is_still_happening:
        try:
            variable = int(input(prompt))
            input_validation_is_still_happening = False
            if variable < 0:
                print("Value cannot be negative. ")
                input_validation_is_still_happening = True
            elif variable > 10:
                print("Value cannot be bigger than 10.")
                input_validation_is_still_happening = True
        except ValueError:
            print("Please enter a whole number. Error code 1")
        except UnboundLocalError:
            print("Please enter a value. Error code 2")
        except:
            print("Something went wrong. Error unknown")
    return variable


house_rating = get_int_input("From 1 to 10 what condition is your house in: ")

if house_rating == 10:
    print("Your house is in perfect condition and won't lose any value.",
          "In total your house is worth:", "$", cost_of_house_with_furn - 0)
elif 8 <= house_rating <= 9:
    print(
        "Your house is in need of very minor repairs and will lose a $1000 "
        "in value.", "In total your house is worth:",
        "$", cost_of_house_with_furn - 1000)
elif 6 <= house_rating <= 7:
    print(
        "Your house is in need of some repairs and will lose $5000 in value.",
        "In total your house is worth:", "$", cost_of_house_with_furn - 5000)
elif 4 <= house_rating <= 5:
    print("House in need of major repairs and will lose $10,000 in value.",
          "In total your house is worth:", "$",
          cost_of_house_with_furn - 10000)
elif 0 <= house_rating <= 3:
    print("House will need to be demolished and will lose all value.",
          "In total your house is approximately worth:",
          "$", cost_of_house_with_furn - cost_of_house_with_furn)
else:
    print("What did you do. Error 999999")

print("Here are other statistics about your house:")


def get_int_input(prompt):
    """
In this function we are asking for the total cost of custom pieces of
furniture, so it can be added to the of the house.

    """
    input_validation_is_still_happening = True
    while input_validation_is_still_happening:
        try:
            variable = int(input(prompt))
            input_validation_is_still_happening = False
            if variable < 0:
                print("Value cannot be negative. ")
                input_validation_is_still_happening = True
        except ValueError:
            print("Please enter a whole number. Error code 1")
        except UnboundLocalError:
            print("Please enter a value. Error code 2")
        except:
            print("Something went wrong. Error unknown")
    return variable


custom_cost_furniture = get_int_input("Please enter the total amount of money"
                                      " your custom pieces of furniture cost. "
                                      "If you have no furniture type 0.: ")

total_cost_with_custom_furniture = cost_of_house + custom_cost_furniture
print("The total cost of your house with your custom furniture is: ", "$",
      total_cost_with_custom_furniture)

print(
    "Here is how many times more either the average cost of a house or your "
    "house is worth.")
print("IMPORTANT MESSAGE: The amount of times it is worth more is calculated"
      " before furniture or rating of house is inputted.")

if average_house_cost > cost_of_house:
    print("The average house is worth more by", "X",
          cost_of_house / average_house_cost, "times more.")
elif average_house_cost < cost_of_house:
    print("Your house is is more valuable by", "X",
          average_house_cost / cost_of_house, "times more.")
elif average_house_cost == cost_of_house:
    print("The average cost and the cost of your house are the same."
          "Therefore the percentage difference is 0%")

# Here we have the requirements needed for the integration project. While these
# lines of code are her they are not part of the main program and are here to
# fulfill the main requirements. As well these lines of code are here as I
# could not fit them in to the main project, or I could not increase the
# security to use them as a part of the main project.
print("IMPORTANT NOTE: These next questions are not required to be answered "
      "and are only to meet the requirement of this project.")

# Enter the people who live with you.
doAgain = "yes"
while doAgain == "yes":
    Person = input("Enter the people that live with you: ")
    doAgain = input("Type 'yes' to enter another person or anything else to "
                    "stop: ")
print("Done!")

# Your house price if it was doubled
your_house_doubled = cost_of_house ** 2
print("The price of your home squared is:", your_house_doubled)

# Find how many times the cost of your house fits into average cost.
if average_house_cost > cost_of_house:
    print("Your house fits into the average house cost",
          average_house_cost // cost_of_house, "times.")
elif average_house_cost < cost_of_house:
    print("The average house fits into your house",
          cost_of_house // average_house_cost, "times")


def get_int_input(prompt):
    """
This is if the customer wants to buy furniture.

    """
    input_validation_is_still_happening = True
    while input_validation_is_still_happening:
        try:
            variable = int(input(prompt))
            input_validation_is_still_happening = False
            if variable < 0:
                print("Value cannot be negative. ")
                input_validation_is_still_happening = True
        except ValueError:
            print("Please enter a whole number. Error code 1")
        except UnboundLocalError:
            print("Please enter a value. Error code 2")
        except:
            print("Something went wrong. Error unknown")
    return variable


buy_furniture = get_int_input("Enter the cost of the furniture you are "
                              "buying: ")

furn_total = 0
for x in range(5):
    furn_total -= buy_furniture
    print("The total cost of furniture is:", furn_total)
