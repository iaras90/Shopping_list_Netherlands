#CREATOR INFO: 
#Creator: Ilse A. Ras
#Date of creation: 2024-10-31
#Latest update moment: 2024-10-31
#Latest update tasks: added butter and dessert options; added comments

#TODO: 
# Eventually import the shopping lists into an inventory checker. 

#Preliminaries: make sure the code works by importing the correct libraries
#We need to make random choices, so import random
import random
#We also need the current date and time, as we generate a seasonal menu with the current month as default input
from datetime import datetime
from datetime import date

#Right, we have a user. We want their name, so we can put their name on the outputs. 
name=input("What should I call you? ")
#We are polite, so we greet them. 
print("\nHello, "+name+".")

#Then we ask them if they actually want to make a menu. 
menu=input("\nDo you want to make a menu for the coming week? Y/N ")

#We ask for a capitalised input, but people aren't consistent. So let's capitalise. 
menu_caps=menu.capitalize()

#They're allowed to choose to not generate a menu. In that case, wish them goodbye. 
if menu_caps=="N":
    print("Okay, thanks. Have a great day!")

#Presumably, however, they're here to create a menu. 
else:
    #Then let's get the necessary date to make sure it's a seasonal menu
    #Get the date and show it to the user, because we're nice like that
    today=date.today()
    print("\nToday's date is "+str(today)+".")

    #For how many people are we making a menu?
    #For dinner?
    persons_dinner=int(input("\nOn how many people are we counting for dinner in the week for which we're making a menu? "))
    print("We're making dinner menus for "+str(persons_dinner)+".")

    #And how about for any other meals? 
    persons_other=int(input("\nAnd how many people for the other meals? "))
    print("We're making menus for other meals for "+str(persons_other)+".")

    #Let's also ask if there's any special plans that we need to take into account. 
    #We need both the day and the plans, so these need to be dictionaries. We first make empty ones, to add to. 
    spec_dinner_days={}
    spec_lunch_days={}
    spec_breakfast_days={}
    spec_brunch_days={}

    #Then we ask the questions, in the following order:
    #Do they have special plans?
    #If yes, for dinner?
    #If yes, for which days? And what are these plans?
    #And how about lunch? Days? Plans?
    #Breakfast? Days? Plans? 
    #Brunch? Days? Plans? 
    #Also make sure the answers are consistently capitalised, as we're going to need them again later. I don't care about the spelling of the plans. 
    special_meals=input("\nDo you have any special meals planned this week? Y/N ")
    special_meals_caps=special_meals.capitalize()
    if special_meals_caps =="Y":
        spec_dinner=input("Do you have special dinner plans for any particular day? Y/N ")
        spec_dinner_caps=spec_dinner.capitalize()
        while spec_dinner_caps=="Y":
            spec_dinner_day=input("For which day do you have special dinner plans? Please type the full day name (in English). ")
            spec_dinner_day_caps=spec_dinner_day.capitalize()
            spec_dinner_plan=input("What are you planning on that day? ")
            spec_dinner_days[spec_dinner_day]=spec_dinner_plan
            spec_dinner=input("Any other day? Y/N ")
            spec_dinner_caps=spec_dinner.capitalize()
        spec_lunch=input("Do you have special lunch plans for any particular day? Y/N ")
        spec_lunch_caps=spec_lunch.capitalize()
        while spec_lunch_caps=="Y":
            spec_lunch_day=input("For which day do you have special lunch plans? Please type the full day name (in English). ")
            spec_lunch_day_caps=spec_lunch_day.capitalize()
            spec_lunch_plan=input("What are you planning on that day? ")
            spec_lunch_days[spec_lunch_day]=spec_lunch_plan
            spec_lunch=input("Any other day? Y/N ")
            spec_lunch_caps=spec_lunch.capitalize()
        spec_breakfast=input("Do you have special breakfast plans for any particular day? Y/N ")
        spec_breakfast_caps=spec_breakfast.capitalize()
        while spec_breakfast_caps=="Y":
            spec_breakfast_day=input("For which day do you have special breakfast plans? Please type the full day name (in English). ")
            spec_breakfast_day_caps=spec_breakfast_day.capitalize()
            spec_breakfast_plan=input("What are you planning on that day? ")
            spec_breakfast_days[spec_breakfast_day]=spec_breakfast_plan
            spec_breakfast=input("Any other day? Y/N ")
            spec_breakfast_caps=spec_breakfast.capitalize()
        spec_brunch=input("Do you have special brunch plans for any particular day? Y/N ")
        spec_brunch_caps=spec_brunch.capitalize()
        while spec_brunch_caps=="Y":
            spec_brunch_day=input("For which day do you have special brunch plans? Please type the full day name (in English). ")
            spec_brunch_day_caps=spec_brunch_day.capitalize()
            spec_brunch_plan=input("What are you planning on that day? ")
            spec_brunch_days[spec_brunch_day]=spec_brunch_plan
            spec_brunch=input("Any other day? Y/N ")
            spec_brunch_caps=spec_brunch.capitalize()
        print("You have special meals planned! How fun! Items for these meals will not be included in the menu or on the shopping lists. ")
    
    #Time to actually get on with things 
    #We've got the date, now get the month from that date and clean it up for further use
    month=datetime.now()
    month_str=month.strftime("%B")
    month_caps=month_str.capitalize()

    #Check with user whether the current month is the month for which they want to write a menu
    month_choice=input("\nWe will generate a menu with seasonal vegetables and fruits from the month of "+month_caps+". Is that OK? Y/N ")
    month_choice_caps=month_choice.capitalize()

    #It's also definitely possible to make a menu for another month! In which case, we overwrite the month we use
    if month_choice_caps == "N":
        alt_month=input ("For which month would you prefer to generate a menu instead? Please type the full month name in English. ")
        month_caps=alt_month.capitalize()

    #We're doing seasonal menus and we draw our options from lists of acceptable foods per meal/category. Here is the part where we tell the program of the acceptable options. 
    #We will sort every list alphabetically, as that's nicer for the user to eventually read
    #Breakfast is easy and not seasonal
    breakfast_list=["Hipro Mango", "Hipro Banana", "Hipro Forest Fruit"]
    breakfast_list.sort()

    #The next meal is the mid-morning fruit snack, and of course fruits *are* seasonal. As such, we have separate lists for every month
    fruit_January=["stewed pears", "pears", "apples", "grapes"]
    fruit_January.sort()
    fruit_February=["stewed pears", "pears", "apples", "grapes"]
    fruit_February.sort()
    fruit_March=["stewed pears", "pears", "apples", "grapes"]
    fruit_March.sort()
    fruit_April=["stewed pears", "pears", "apples", "grapes", "strawberries"]
    fruit_April.sort()
    fruit_May=["stewed pears", "pears", "apples", "grapes", "strawberries"]
    fruit_May.sort()
    fruit_June=["rhubarb", "strawberries", "plums", "blueberries", "cherries", "blackberries", "raspberries", "nectarines", "peaches", "red currants", "blackcurrants"]
    fruit_June.sort()
    fruit_July=["rhubarb", "strawberries", "plums", "blueberries", "cherries", "blackberries", "raspberries", "nectarines", "peaches", "red currants", "blackcurrants"]
    fruit_July.sort()
    fruit_August=["rhubarb", "strawberries", "apricots", "apples", "blueberries", "blackberries", "grapes", "raspberries", "cherries", "nectarines", "pears", "peaches", "figs", "blackcurrants"]
    fruit_August.sort()
    fruit_September=["apples", "blueberries", "blackberries", "grapes", "raspberries", "kiwiberries", "nectarines", "pears", "peaches", "plums", "figs"]
    fruit_September.sort()
    fruit_October=["stewed pears", "pears", "apples", "grapes", "blackberries", "raspberries", "kiwiberries"]
    fruit_October.sort()
    fruit_November=["stewed pears", "pears", "apples", "grapes"]
    fruit_November.sort()
    fruit_December=["stewed pears", "pears", "apples", "grapes"]
    fruit_December.sort()

    #The current month OR the month chosen by the user determines which fruit list we'll use to create our menu
    if month_caps == "January":
        fruit_list2=(fruit_January)
    elif month_caps == "February": 
        fruit_list2=(fruit_February)
    elif month_caps == "March":
        fruit_list2=(fruit_March)
    elif month_caps == "April": 
        fruit_list2=(fruit_April)
    elif month_caps == "May": 
        fruit_list2=(fruit_May)
    elif month_caps == "June": 
        fruit_list2=(fruit_June)
    elif month_caps == "July": 
        fruit_list2=(fruit_July)
    elif month_caps == "August": 
        fruit_list2=(fruit_August)
    elif month_caps == "September": 
        fruit_list2=(fruit_September)
    elif month_caps == "October": 
        fruit_list2=(fruit_October)
    elif month_caps == "November": 
        fruit_list2=(fruit_November)
    elif month_caps == "December": 
        fruit_list2=(fruit_December)
    else: 
        fruit_list2 = "Something has gone wrong with the fruit list!"
    fruit_list2.sort()

    #The third meal of the day is lunch
    #Lunch is a multi-component meal, but none of these components are seasonal. So we just get a bunch of lists, which are valid throughout the year. 
    #We start with bread, because I'm European. I'm building a lunch sandwich here. 
    bread_list=["whole wheat buns"]
    bread_list.sort()

    #Sandwiches need lubrication
    butter_list=["margarine"]
    butter_list.sort()

    #Sandwiches are rubbish without filling, so choose a deli item for our sandwich
    deli_list=["ham"]
    deli_list.sort()

    #Any toppings?
    toppings_list=["mustard", "gherkins"]
    toppings_list.sort()

    #We need a drink for lunch!
    lunchdrink_list=["yakult"]
    lunchdrink_list.sort()

    #Moving on to the afternoon snack. This is also a simple list and not seasonal. 
    snack_list=["Btween bar", "Cheez dippers", "15 grams of nuts"]
    snack_list.sort()

    #Time for dinner
    #Vegetables should be central to dinner
    #Vegetables are seasonal, so we first have lists per month 
    veg_January=["sweet potato", "parsnip", "turnip", "celeriac", "witlof", "red cabbage", "leeks", "beets", "kale", "winter carrots", "pumpkin", "savoy cabbage", "sprouts", "onions", "veldsla", "white cabbage"]
    veg_January.sort()
    veg_February=["sweet potato", "parsnip", "turnip", "celeriac", "witlof", "red cabbage", "leeks", "beets", "kale", "winter carrots", "pumpkin", "sprouts", "onions", "veldsla", "white cabbage"]
    veg_February.sort()
    veg_March=["sweet potato", "parsnip", "turnip", "celeriac", "red cabbage", "leeks", "beets", "kale", "winter carrots", "green asparagus", "white asparagus", "kohlrabi", "purple asparagus", "lettuce", "cress", "cauliflower", "mushrooms", "roodlof", "savoy cabbage", "chard", "spinach", "sprouts", "onions", "veldsla", "witlof", "white cabbage"]
    veg_March.sort()
    veg_April=["green asparagus", "white asparagus", "spinach", "kohlrabi", "purple asparagus", "lettuce", "cress", "endive", "cauliflower", "mushrooms", "bok choi", "leeks", "beets", "roodlof", "chard", "onions", "witlof"]
    veg_April.sort()
    veg_May=["green asparagus", "white asparagus", "spinach", "kohlrabi", "purple asparagus", "lettuce", "cress", "endive", "cauliflower", "mushrooms", "bok choi", "leeks", "beets", "roodlof", "chard", "onions", "witlof"]
    veg_May.sort()
    veg_June=["green asparagus", "white asparagus", "spinach", "kohlrabi", "purple asparagus", "lettuce", "cress", "courgette", "romaine", "celery", "yellow courgette", "spring onion", "aubergine", "summer carrots", "endive", "chinese cabbage", "runner beans", "corn", "bok choi", "cucumber", "paprika", "iceberg lettuce", "butter lettuce", "fava beans", "tomatoes", "artichokes", "broccoli", "cauliflower", "peas", "kropsla", "mushrooms", "green beans", "savoy cabbage", "chard", "onions"]
    veg_June.sort()
    veg_July=["courgette", "romaine", "celery", "yellow courgette", "spring onion", "summer carrots", "chinese cabbage", "runner beans", "corn", "bok choi", "cucumber", "iceberg lettuce", "butter lettuce", "fava beans", "tomatoes", "endive", "artichokes", "aubergine", "cauliflower", "broccoli", "peas", "mushrooms", "paprika", "red cabbage", "savoy cabbage", "chard", "onions", "white cabbage", "carrots"]
    veg_July.sort()
    veg_August=["courgette", "romaine", "celery", "yellow courgette", "spring onion", "summer carrots", "chinese cabbage", "runner beans", "cucumber", "peas", "iceberg lettuce", "butter lettuce", "fava beans", "tomatoes", "artichokes", "endive", "aubergine", "cauliflower", "broccoli", "Chinese cabbage", "kropsla", "corn", "mushrooms", "bok choi", "paprika", "pumpkin", "red cabbage", "savoy cabbage", "chard", "onions", "white cabbage", "carrots"]
    veg_August.sort()
    veg_September=["courgette", "romaine", "celery", "yellow courgette", "spring onion", "aubergine", "summer carrots", "cauliflower", "chinese cabbage", "runner beans", "corn", "bok choi", "cucumber", "paprika", "peas", "iceberg lettuce", "butter lettuce", "fava beans", "tomatoes", "potatoes", "broccoli", "sprouts", "pumpkin", "white cabbage", "green beans", "endive", "artichokes", "mushrooms", "chard", "spinach", "onions", "carrots"]
    veg_September.sort()
    veg_October=["mushrooms", "broccoli", "sprouts", "pumpkin", "onions", "white cabbage", "green beans", "endive", "artichokes", "aubergine", "kale", "cauliflower", "chinese cabbage", "courgettes", "cucumber", "kropsla", "bok choi", "paprika", "parsnip", "leeks", "red beets", "red cabbage", "roodlof", "savoy cabbage", "chard", "runner beans", "spinach", "tomatoes", "veldsla", "witlof", "carrots"]
    veg_October.sort()
    veg_November=["mushrooms", "broccoli", "sprouts", "pumpkin", "onions", "white cabbage", "green beans", "endive", "cauliflower", "kale", "chinese cabbage", "courgettes", "parsnips", "leeks", "red beets", "red cabbage", "savoy cabbage", "chard", "veldsla", "witlof", "carrots"]
    veg_November.sort()
    veg_December=["mushrooms", "broccoli", "sprouts", "pumpkin", "onions", "white cabbage", "green beans", "sweet potato", "turnip", "celeriac", "witlof", "red cabbage", "leeks", "beets", "kale", "winter carrots", "endive", "parsnips", "savoy cabbage", "veldsla"]
    veg_December.sort()

    #And then we determine which list to use given the chose menu-making month
    if month_caps == "January":
        veg_list2=(veg_January)
    elif month_caps == "February": 
        veg_list2=(veg_February)
    elif month_caps == "March":
        veg_list2=(veg_March)
    elif month_caps == "April": 
        veg_list2=(veg_April)
    elif month_caps == "May": 
        veg_list2=(veg_May)
    elif month_caps == "June": 
        veg_list2=(veg_June)
    elif month_caps == "July": 
        veg_list2=(veg_July)
    elif month_caps == "August": 
        veg_list2=(veg_August)
    elif month_caps == "September": 
        veg_list2=(veg_September)
    elif month_caps == "October": 
        veg_list2=(veg_October)
    elif month_caps == "November": 
        veg_list2=(veg_November)
    elif month_caps == "December": 
        veg_list2=(veg_December)
    else: 
        veg_list2 = "Something has gone wrong with the vegetable list!"
    veg_list2.sort()

    #A solid dinner also includes a protein. This list is not seasonal. 
    protein_list=["chicken", "turkey", "eggs", "beef", "lean pork", "venison", "tofu", "paneer"]
    protein_list.sort()

    #Plain dinner can be boring, so let's give some options
    cuisines_list=["Greece & Cyprus", "Scandinavia", "Eastern Europe", "Germany", "Spain", "Italy", "France", "UK", "USA & Canada", "Mexico", "Central America", "Caribbean", "Argentina & Uruguay", "Chile, Peru & Bolivia", "Brazil", "Mediterranean", "Iran", "India", "Vietnam", "Thailand", "Korea", "Japan", "China", "Horn of Africa", "North Africa", "West Africa"]
    cuisines_list.sort()

    #Dinner ends with a pudding (in the English sense)
    dessert_list=["chocolate"]
    dessert_list.sort()

    #Right. Sometimes, there's just some options in these lists that you don't feel like this week, or that you're craving, so let's give our user the option to either add to
    #Or delete items from these list
    #But only if they actually want to!
    ingredients=input("Do you want to see the options available this month? Y/N ")
    ingredients_caps=ingredients.capitalize()

    #If they do, let's
    #1. Display the lists
    #2. Ask if they want to add anything
    #3. If yes, ask what they want to add
    #4. Revisit steps 2 and 3 until they stop wanting to add things
    #5. Display the final list
    if ingredients_caps=="Y":

        #second, let's give the user some options to add more
        print ("\nThe breakfast options for this month are: "+str(breakfast_list))
        bf_add=input("Would you like to add anything to the breakfast list? Y/N ")
        bf_add2=bf_add.capitalize()
        while bf_add2=="Y":
            bf_input=input("What would you like to add to the breakfast list? ")
            bf_input_lower=bf_input.lower()
            breakfast_list.append(bf_input_lower)
            bf_add=input("Would you like to add anything else to the breakfast list? Y/N ")
            bf_add2=bf_add.capitalize()
        else: 
            print("Thank you! Nothing else has been added to the breakfast list.")
        breakfast_list.sort()
        print ("\nThe new breakfast options for this month are: "+str(breakfast_list))

        #they should also be able to remove things off the lists
        bf_remove=input("Would you like to remove anything from the breakfast list? Y/N ")
        bf_remove2=bf_remove.capitalize()
        while bf_remove2=="Y":
            bf_input_pop=input("What would you like to remove from the breakfast list? ")
            if bf_input_pop in breakfast_list:
                index=breakfast_list.index(bf_input_pop)
                breakfast_list.pop(index)
            else: 
                print("Sorry! This item does not seem to be in the list. Please also check your spelling and capitalisation of this item. ")
            bf_remove=input("Would you like to remove anything else from the breakfast list? Y/N ")
            bf_remove2=bf_remove.capitalize()
        else: 
            print("Thank you! Nothing else has been removed from the breakfast list.")
        breakfast_list.sort()
        print ("\nThe new breakfast options for this month are: "+str(breakfast_list))

        #second, let's give the user the option to add more fruits
        print("\nThe fruit snack options for this month are: "+str(fruit_list2))

        #now the user can add more
        fruit_add=input("Would you like to add anything to the fruit list? Y/N ")
        fruit_add2=fruit_add.capitalize()
        while fruit_add2=="Y":
            fruit_input=input("What would you like to add to the fruit list? ")
            fruit_input_lower=fruit_input.lower()
            if month_caps == "January":
                fruit_January.append(fruit_input_lower)
            elif month_caps == "February": 
                fruit_February.append(fruit_input_lower)
            elif month_caps == "March":
                fruit_March.append(fruit_input_lower)
            elif month_caps == "April": 
                fruit_April.append(fruit_input_lower)
            elif month_caps == "May": 
                fruit_May.append(fruit_input_lower)
            elif month_caps == "June": 
                fruit_June.append(fruit_input_lower)
            elif month_caps == "July": 
                fruit_July.append(fruit_input_lower)
            elif month_caps == "August": 
                fruit_August.append(fruit_input_lower)
            elif month_caps == "September": 
                fruit_September.append(fruit_input_lower)
            elif month_caps == "October": 
                fruit_October.append(fruit_input_lower)
            elif month_caps == "November": 
                fruit_November.append(fruit_input_lower)
            elif month_caps == "December": 
                fruit_December.append(fruit_input_lower)
            fruit_add=input("Would you like to add anything else to the fruit list? Y/N ")
            fruit_add2=fruit_add.capitalize()
        else: 
            print("Thank you! Nothing else has been added to the fruit list.")
        fruit_list2.sort()
        print("\nThe new fruit options for this month are: "+str(fruit_list2))

        #they should also be able to remove things off the lists
        fruit_remove=input("Would you like to remove anything from the fruit list? Y/N ")
        fruit_remove2=fruit_remove.capitalize()
        while fruit_remove2=="Y":
            fruit_input_pop=input("What would you like to remove from the fruit list? ")
            if fruit_input_pop in fruit_list2:
                index=fruit_list2.index(fruit_input_pop)
                fruit_list2.pop(index)
            else: 
                print("Sorry! This item does not seem to be in the list. Please also check your spelling and capitalisation of this item. ")
            fruit_remove=input("Would you like to remove anything else from the fruit list? Y/N ")
            fruit_remove2=fruit_remove.capitalize()
        else: 
            print("Thank you! Nothing else has been removed from the fruit list.")
        fruit_list2.sort()
        print ("\nThe new fruit options for this month are: "+str(fruit_list2))

        #decide lunch options
        #breadddddd
        #Does the user want to add more?
        print ("\nLunch time! \nThe bread options for this month are: "+str(bread_list))
        bread_add=input("Would you like to add anything to the bread list? Y/N ")
        bread_add2=bread_add.capitalize()
        while bread_add2=="Y":
            bread_input=input("What would you like to add to the bread list? ")
            bread_input_lower=bread_input.lower()
            bread_list.append(bread_input_lower)
            bread_add=input("Would you like to add anything else to the bread list? Y/N ")
            bread_add2=bread_add.capitalize()
        else: 
            print("Thank you! Nothing else has been added to the bread list.")
        bread_list.sort()
        print ("\nThe new bread options for this month are: "+str(bread_list))

        #they should also be able to remove things off the lists
        bread_remove=input("Would you like to remove anything from the bread list? Y/N ")
        bread_remove2=bread_remove.capitalize()
        while bread_remove2=="Y":
            bread_input_pop=input("What would you like to remove from the bread list? ")
            if bread_input_pop in bread_list:
                index=bread_list.index(bread_input_pop)
                bread_list.pop(index)
            else: 
                print("Sorry! This item does not seem to be in the list. Please also check your spelling and capitalisation of this item. ")
            bread_remove=input("Would you like to remove anything else from the bread list? Y/N ")
            bread_remove2=bread_remove.capitalize()
        else: 
            print("Thank you! Nothing else has been removed from the bread list.")
        bread_list.sort()
        print ("\nThe new bread options for this month are: "+str(bread_list))

        #butter
        #does the user want to add more?
        print ("\nThe butter options for this month are: "+str(butter_list))
        butter_add=input("Would you like to add anything to the butter list? Y/N ")
        butter_add2=butter_add.capitalize()
        while butter_add2=="Y":
            butter_input=input("What would you like to add to the butter list? ")
            butter_input_lower=butter_input.lower()
            butter_list.append(butter_input_lower)
            butter_add=input("Would you like to add anything else to the butter list? Y/N ")
            butter_add2=butter_add.capitalize()
        else: 
            print("Thank you! Nothing else has been added to the butter list.")
        butter_list.sort()
        print ("\nThe new butter options for this month are: "+str(butter_list))

        #they should also be able to remove things off the lists
        butter_remove=input("Would you like to remove anything from the butter list? Y/N ")
        butter_remove2=butter_remove.capitalize()
        while butter_remove2=="Y":
            butter_input_pop=input("What would you like to remove from the butter list? ")
            if butter_input_pop in butter_list:
                index=butter_list.index(butter_input_pop)
                butter_list.pop(index)
            else: 
                print("Sorry! This item does not seem to be in the list. Please also check your spelling and capitalisation of this item. ")
            butter_remove=input("Would you like to remove anything else from the butter list? Y/N ")
            butter_remove2=butter_remove.capitalize()
        else: 
            print("Thank you! Nothing else has been removed from the butter list.")
        butter_list.sort()
        print ("\nThe new butter options for this month are: "+str(butter_list))

        #deli filling
        #does the user want to add more?
        print ("\nThe deli options for this month are: "+str(deli_list))
        deli_add=input("Would you like to add anything to the deli list? Y/N ")
        deli_add2=deli_add.capitalize()
        while deli_add2=="Y":
            deli_input=input("What would you like to add to the deli list? ")
            deli_input_lower=deli_input.lower()
            deli_list.append(deli_input_lower)
            deli_add=input("Would you like to add anything else to the deli list? Y/N ")
            deli_add2=deli_add.capitalize()
        else: 
            print("Thank you! Nothing else has been added to the deli list.")
        deli_list.sort()
        print ("\nThe new deli options for this month are: "+str(deli_list))

        #they should also be able to remove things off the lists
        deli_remove=input("Would you like to remove anything from the deli list? Y/N ")
        deli_remove2=deli_remove.capitalize()
        while deli_remove2=="Y":
            deli_input_pop=input("What would you like to remove from the deli list? ")
            if deli_input_pop in deli_list:
                index=deli_list.index(deli_input_pop)
                deli_list.pop(index)
            else: 
                print("Sorry! This item does not seem to be in the list. Please also check your spelling and capitalisation of this item. ")
            deli_remove=input("Would you like to remove anything else from the deli list? Y/N ")
            deli_remove2=deli_remove.capitalize()
        else: 
            print("Thank you! Nothing else has been removed from the deli list.")
        deli_list.sort()
        print ("\nThe new deli options for this month are: "+str(deli_list))
        
        #toppings
        #does the user want to add more?
        print ("\nThe toppings options for this month are: "+str(toppings_list))
        toppings_add=input("Would you like to add anything to the toppings list? Y/N ")
        toppings_add2=toppings_add.capitalize()
        while toppings_add2=="Y":
            toppings_input=input("What would you like to add to the toppings list? ")
            toppings_input_lower=toppings_input.lower()
            toppings_list.append(toppings_input_lower)
            toppings_add=input("Would you like to add anything else to the toppings list? Y/N ")
            toppings_add2=toppings_add.capitalize()
        else: 
            print("Thank you! Nothing else has been added to the toppings list.")
        toppings_list.sort()
        print ("\nThe new toppings options for this month are: "+str(toppings_list))

        #they should also be able to remove things off the lists
        toppings_remove=input("Would you like to remove anything from the toppings list? Y/N ")
        toppings_remove2=toppings_remove.capitalize()
        while toppings_remove2=="Y":
            toppings_input_pop=input("What would you like to remove from the toppings list? ")
            if toppings_input_pop in toppings_list:
                index=toppings_list.index(toppings_input_pop)
                toppings_list.pop(index)
            else: 
                print("Sorry! This item does not seem to be in the list. Please also check your spelling and capitalisation of this item. ")
            toppings_remove=input("Would you like to remove anything else from the toppings list? Y/N ")
            toppings_remove2=toppings_remove.capitalize()
        else: 
            print("Thank you! Nothing else has been removed from the toppings list.")
        toppings_list.sort()
        print ("\nThe new toppings options for this month are: "+str(toppings_list))

        #drink
        #does the user want to add more?
        print ("\nThe lunch drink options for this month are: "+str(lunchdrink_list))
        lunchdrink_add=input("Would you like to add anything to the lunch drink list? Y/N ")
        lunchdrink_add2=lunchdrink_add.capitalize()
        while lunchdrink_add2=="Y":
            lunchdrink_input=input("What would you like to add to the lunch drink list? ")
            lunchdrink_input_lower=lunchdrink_input.lower()
            lunchdrink_list.append(lunchdrink_input_lower)
            lunchdrink_add=input("Would you like to add anything else to the lunch drink list? Y/N ")
            lunchdrink_add2=lunchdrink_add.capitalize()
        else: 
            print("Thank you! Nothing else has been added to the lunch drink list.")
        lunchdrink_list.sort()
        print ("\nThe new lunch drink options for this month are: "+str(lunchdrink_list))

        #they should also be able to remove things off the lists
        lunchdrink_remove=input("Would you like to remove anything from the lunch drink list? Y/N ")
        lunchdrink_remove2=lunchdrink_remove.capitalize()
        while lunchdrink_remove2=="Y":
            lunchdrink_input_pop=input("What would you like to remove from the lunch drink list? ")
            if lunchdrink_input_pop in lunchdrink_list:
                index=lunchdrink_list.index(lunchdrink_input_pop)
                lunchdrink_list.pop(index)
            else: 
                print("Sorry! This item does not seem to be in the list. Please also check your spelling and capitalisation of this item. ")
            lunchdrink_remove=input("Would you like to remove anything else from the lunch drink list? Y/N ")
            lunchdrink_remove2=lunchdrink_remove.capitalize()
        else: 
            print("Thank you! Nothing else has been removed from the lunch drink list.")
        lunchdrink_list.sort()
        print ("\nThe new lunch drink options for this month are: "+str(lunchdrink_list))

        #decide afternoon snack options
        #does the user want to add more?
        print ("\nThe snack options for this month are: "+str(snack_list))
        snack_add=input("Would you like to add anything to the snack list? Y/N ")
        snack_add2=snack_add.capitalize()
        while snack_add2=="Y":
            snack_input=input("What would you like to add to the snack list? ")
            snack_input_lower=snack_input.lower()
            snack_list.append(snack_input_lower)
            snack_add=input("Would you like to add anything else to the snack list? Y/N ")
            snack_add2=snack_add.capitalize()
        else: 
            print("Thank you! Nothing else has been added to the snack list.")
        snack_list.sort()
        print ("\nThe new snack options for this month are: "+str(snack_list))

        #they should also be able to remove things off the lists
        snack_remove=input("Would you like to remove anything from the snack list? Y/N ")
        snack_remove2=snack_remove.capitalize()
        while snack_remove2=="Y":
            snack_input_pop=input("What would you like to remove from the snack list? ")
            if snack_input_pop in snack_list:
                index=snack_list.index(snack_input_pop)
                snack_list.pop(index)
            else: 
                print("Sorry! This item does not seem to be in the list. Please also check your spelling and capitalisation of this item. ")
            snack_remove=input("Would you like to remove anything else from the snack list? Y/N ")
            snack_remove2=snack_remove.capitalize()
        else: 
            print("Thank you! Nothing else has been removed from the snack list.")
        snack_list.sort()
        print ("\nThe new snack options for this month are: "+str(snack_list))

        # alright, time to determine dinner. Dinner is complex and has multiple components. 

        #firstly, vegetables
        #anything to add?
        print("\nThe vegetable options for this month are: "+str(veg_list2))
        veg_add=input("Would you like to add anything to the vegetable list? Y/N ")
        veg_add2=veg_add.capitalize()
        while veg_add2=="Y":
            veg_input=input("What would you like to add to the vegetable list? ")
            veg_input_lower=veg_input.lower()
            if month_caps == "January":
                veg_January.append(veg_input_lower)
            elif month_caps == "February": 
                veg_February.append(veg_input_lower)
            elif month_caps == "March":
                veg_March.append(veg_input_lower)
            elif month_caps == "April": 
                veg_April.append(veg_input_lower)
            elif month_caps == "May": 
                veg_May.append(veg_input_lower)
            elif month_caps == "June": 
                veg_June.append(veg_input_lower)
            elif month_caps == "July": 
                veg_July.append(veg_input_lower)
            elif month_caps == "August": 
                veg_August.append(veg_input_lower)
            elif month_caps == "September": 
                veg_September.append(veg_input_lower)
            elif month_caps == "October": 
                veg_October.append(veg_input_lower)
            elif month_caps == "November": 
                veg_November.append(veg_input_lower)
            elif month_caps == "December": 
                veg_December.append(veg_input_lower)
            veg_add=input("Would you like to add anything else to the vegetables list? Y/N ")
            veg_add2=veg_add.capitalize()
        else: 
            print("Thank you! Nothing else has been added to the vegetable list.")
        veg_list2.sort
        print("\nThe new vegetable options for this month are: "+str(veg_list2))

        #they should also be able to remove things off the lists
        veg_remove=input("Would you like to remove anything from the vegetables list? Y/N ")
        veg_remove2=veg_remove.capitalize()
        while veg_remove2=="Y":
            veg_input_pop=input("What would you like to remove from the vegetables list? ")
            if veg_input_pop in veg_list2:
                index=veg_list2.index(veg_input_pop)
                veg_list2.pop(index)
            else: 
                print("Sorry! This item does not seem to be in the list. Please also check your spelling and capitalisation of this item. ")
            veg_remove=input("Would you like to remove anything else from the vegetables list? Y/N ")
            veg_remove2=bf_remove.capitalize()
        else: 
            print("Thank you! Nothing else has been removed from the vegetables list.")
        veg_list2.sort()
        print ("\nThe new vegetables options for this month are: "+str(veg_list2))

        #dinner also includes a protein
        #the options adder:
        print ("\nThe protein options for this month are: "+str(protein_list))
        protein_add=input("Would you like to add anything to the protein list? Y/N ")
        protein_add2=protein_add.capitalize()
        while protein_add2=="Y":
            protein_input=input("What would you like to add to the protein list? ")
            protein_input_lower=protein_input.lower()
            protein_list.append(protein_input_lower)
            protein_add=input("Would you like to add anything else to the protein list? Y/N ")
            protein_add2=protein_add.capitalize()
        else: 
            print("Thank you! Nothing has been added to the protein list.")
        protein_list.sort()
        print ("\nThe new protein options for this month are: "+str(protein_list))

        #they should also be able to remove things off the lists
        protein_remove=input("Would you like to remove anything from the proteins list? Y/N ")
        protein_remove2=protein_remove.capitalize()
        while protein_remove2=="Y":
            protein_input_pop=input("What would you like to remove from the proteins list? ")
            if protein_input_pop in protein_list:
                index=protein_list.index(protein_input_pop)
                protein_list.pop(index)
            else: 
                print("Sorry! This item does not seem to be in the list. Please also check your spelling and capitalisation of this item. ")
            protein_remove=input("Would you like to remove anything else from the proteins list? Y/N ")
            protein_remove2=protein_remove.capitalize()
        else: 
            print("Thank you! Nothing else has been removed from the proteins list.")
        protein_list.sort()
        print ("\nThe new protein options for this month are: "+str(protein_list))

        #just plain veggies and proteins can be nice, but sometimes that gets boring. Let's spice things up with cuisine suggestions
        #and then they're allowed to add:
        print ("\nThe cuisine options for this month are: "+str(cuisines_list))
        cuisine_add=input("Would you like to add anything to the cuisines list? Y/N ")
        cuisine_add2=cuisine_add.capitalize()
        while cuisine_add2=="Y":
            cuisine_input=input("What would you like to add to the cuisines list? ")
            cuisine_input_capitalize=cuisine_input.capitalize()
            cuisines_list.append(cuisine_input_capitalize)
            cuisine_add=input("Would you like to add anything else to the cuisines list? Y/N ")
            cuisine_add2=cuisine_add.capitalize()
        else: 
            print("Thank you! Nothing has been added to the cuisines list.")
        cuisines_list.sort()
        print ("\nThe new cuisine options for this month are: "+str(cuisines_list))

        #they should also be able to remove things off the lists
        cui_remove=input("Would you like to remove anything from the cuisines list? Y/N ")
        cui_remove2=cui_remove.capitalize()
        while cui_remove2=="Y":
            cui_input_pop=input("What would you like to remove from the cuisines list? ")
            if cui_input_pop in cuisines_list:
                index=cuisines_list.index(cui_input_pop)
                cuisines_list.pop(index)
            else: 
                print("Sorry! This item does not seem to be in the list. Please also check your spelling and capitalisation of this item. ")
            cui_remove=input("Would you like to remove anything else from the cuisines list? Y/N ")
            cui_remove2=cui_remove.capitalize()
        else: 
            print("Thank you! Nothing else has been removed from the cuisines list.")
        cuisines_list.sort()
        print ("\nThe new cuisine options for this month are: "+str(cuisines_list))

        #and dinner ends on a pudding
        #and then they're allowed to add:
        print ("\nThe dessert options for this month are: "+str(dessert_list))
        dessert_add=input("Would you like to add anything to the dessert list? Y/N ")
        dessert_add2=dessert_add.capitalize()
        while dessert_add2=="Y":
            dessert_input=input("What would you like to add to the dessert list? ")
            dessert_input_capitalize=dessert_input.capitalize()
            dessert_list.append(dessert_input_capitalize)
            dessert_add=input("Would you like to add anything else to the dessert list? Y/N ")
            dessert_add2=dessert_add.capitalize()
        else: 
            print("Thank you! Nothing has been added to the dessert list.")
        dessert_list.sort()
        print ("\nThe new dessert options for this month are: "+str(dessert_list))

        #they should also be able to remove things off the lists
        cui_remove=input("Would you like to remove anything from the dessert list? Y/N ")
        cui_remove2=cui_remove.capitalize()
        while cui_remove2=="Y":
            cui_input_pop=input("What would you like to remove from the dessert list? ")
            if cui_input_pop in dessert_list:
                index=dessert_list.index(cui_input_pop)
                dessert_list.pop(index)
            else: 
                print("Sorry! This item does not seem to be in the list. Please also check your spelling and capitalisation of this item. ")
            cui_remove=input("Would you like to remove anything else from the dessert list? Y/N ")
            cui_remove2=cui_remove.capitalize()
        else: 
            print("Thank you! Nothing else has been removed from the dessert list.")
        dessert_list.sort()
        print ("\nThe new dessert options for this month are: "+str(dessert_list))

    #Alright! Now we know what foods we can include in our menu
    #Time to start picking some and adding them to our shopping list, categorised by shop area, and our menu
    #let's begin by making a bunch of empty shopping lists:
    breakfast_shopping_list=[]
    bread_shopping_list=[]
    dairy_shopping_list=[]
    deli_shopping_list=[]
    toppings_shopping_list=[]
    lunchdrink_shopping_list=[]
    snack_shopping_list=[]
    veg_saturday_shopping_list=[]
    protein_saturday_shopping_list=[]
    fruit_saturday_shopping_list=[]
    veg_wednesday_shopping_list=[]
    protein_wednesday_shopping_list=[]
    fruit_wednesday_shopping_list=[]
    sweets_shopping_list=[]

    #now we pick our menu items and add them simultaneously to the shopping list:
    def breakfast_picker():
        breakfast=(random.choice(breakfast_list))
        breakfast_shopping_list.append(breakfast)
        return breakfast

    #pick a fruit according to the month and add it to the shopping list. We first need one for saturday, because we shop for fresh items on saturday and on wednesday.
    def fruit_picker_sat():
        if month_caps == "January":
            fruit=(random.choice(fruit_January))
        elif month_caps == "February": 
            fruit=(random.choice(fruit_February))
        elif month_caps == "March":
            fruit=(random.choice(fruit_March))
        elif month_caps == "April": 
            fruit=(random.choice(fruit_April))
        elif month_caps == "May": 
            fruit=(random.choice(fruit_May))
        elif month_caps == "June": 
            fruit=(random.choice(fruit_June))
        elif month_caps == "July": 
            fruit=(random.choice(fruit_July))
        elif month_caps == "August": 
            fruit=(random.choice(fruit_August))
        elif month_caps == "September": 
            fruit=(random.choice(fruit_September))
        elif month_caps == "October": 
            fruit=(random.choice(fruit_October))
        elif month_caps == "November": 
            fruit=(random.choice(fruit_November))
        elif month_caps == "December": 
            fruit=(random.choice(fruit_December))
        else: 
            fruit_list2 = "Something has gone wrong with the fruit selection. Be creative!"
        fruit_saturday_shopping_list.append(fruit)
        return fruit

    #now for wednesday: 
    def fruit_picker_wed():
        if month_caps == "January":
            fruit=(random.choice(fruit_January))
        elif month_caps == "February": 
            fruit=(random.choice(fruit_February))
        elif month_caps == "March":
            fruit=(random.choice(fruit_March))
        elif month_caps == "April": 
            fruit=(random.choice(fruit_April))
        elif month_caps == "May": 
            fruit=(random.choice(fruit_May))
        elif month_caps == "June": 
            fruit=(random.choice(fruit_June))
        elif month_caps == "July": 
            fruit=(random.choice(fruit_July))
        elif month_caps == "August": 
            fruit=(random.choice(fruit_August))
        elif month_caps == "September": 
            fruit=(random.choice(fruit_September))
        elif month_caps == "October": 
            fruit=(random.choice(fruit_October))
        elif month_caps == "November": 
            fruit=(random.choice(fruit_November))
        elif month_caps == "December": 
            fruit=(random.choice(fruit_December))
        else: 
            fruit_list2 = "Something has gone wrong with the fruit selection. Be creative!"
        fruit_wednesday_shopping_list.append(fruit)
        return fruit

    #lunchtime!
    #pick bread!
    def bread_picker():
        bread=(random.choice(bread_list))
        bread_shopping_list.append(bread)
        return bread

    #pick butter
    def butter_picker():
        butter=(random.choice(butter_list))
        dairy_shopping_list.append(butter)
        return butter

    #pick sandwich fillings
    def deli_picker():
        deli=(random.choice(deli_list))
        deli_shopping_list.append(deli)
        return deli

    #pick toppings
    def toppings_picker():
        toppings=(random.choice(toppings_list))
        toppings_shopping_list.append(toppings)
        return toppings

    #pick a drink with lunch
    def lunchdrink_picker():
        lunchdrink=(random.choice(lunchdrink_list))
        lunchdrink_shopping_list.append(lunchdrink)
        return lunchdrink

    #pick an afternoon snack
    def snack_picker():
        snack=(random.choice(snack_list))
        snack_shopping_list.append(snack)
        return snack

    #dinnertime
    #pick a vegetable. This is a fresh product, so we have a shopping list for saturday
    def veg_picker_sat():
        if month_caps == "January":
            veg=(random.choice(veg_January))
        elif month_caps == "February": 
            veg=(random.choice(veg_February))
        elif month_caps == "March":
            veg=(random.choice(veg_March))
        elif month_caps == "April": 
            veg=(random.choice(veg_April))
        elif month_caps == "May": 
            veg=(random.choice(veg_May))
        elif month_caps == "June": 
            veg=(random.choice(veg_June))
        elif month_caps == "July": 
            veg=(random.choice(veg_July))
        elif month_caps == "August": 
            veg=(random.choice(veg_August))
        elif month_caps == "September": 
            veg=(random.choice(veg_September))
        elif month_caps == "October": 
            veg=(random.choice(veg_October))
        elif month_caps == "November": 
            veg=(random.choice(veg_November))
        elif month_caps == "December": 
            veg=(random.choice(veg_December))
        else: 
            veg = "Something has gone wrong with the vegetable selection. Be creative!"
        veg_saturday_shopping_list.append(veg)
        return veg

    #and for wednesday
    def veg_picker_wed():
        if month_caps == "January":
            veg=(random.choice(veg_January))
        elif month_caps == "February": 
            veg=(random.choice(veg_February))
        elif month_caps == "March":
            veg=(random.choice(veg_March))
        elif month_caps == "April": 
            veg=(random.choice(veg_April))
        elif month_caps == "May": 
            veg=(random.choice(veg_May))
        elif month_caps == "June": 
            veg=(random.choice(veg_June))
        elif month_caps == "July": 
            veg=(random.choice(veg_July))
        elif month_caps == "August": 
            veg=(random.choice(veg_August))
        elif month_caps == "September": 
            veg=(random.choice(veg_September))
        elif month_caps == "October": 
            veg=(random.choice(veg_October))
        elif month_caps == "November": 
            veg=(random.choice(veg_November))
        elif month_caps == "December": 
            veg=(random.choice(veg_December))
        else: 
            veg = "Something has gone wrong with the vegetable selection. Be creative!"
        veg_wednesday_shopping_list.append(veg)
        return veg

    #protein is also a fresh product. Saturday:
    def protein_picker_sat():
        protein=(random.choice(protein_list))
        protein_saturday_shopping_list.append(protein)
        return protein

    #Wednesday proteins: 
    def protein_picker_wed():
        protein=(random.choice(protein_list))
        protein_wednesday_shopping_list.append(protein)
        return protein

    #Also pick a cuisine, of course
    def cuisine_picker():
        cuisine=(random.choice(cuisines_list))
        return cuisine

    #And we end dinner with a pudding
    def dessert_picker():
        dessert=(random.choice(dessert_list))
        sweets_shopping_list.append(dessert)
        return dessert

    #FINALLY time to actually go ahead and make a menu
    #If they still want to do that, of course
    generate=input("\nWould you like to generate a menu? Y/N ")
    generate_capitalise = generate.capitalize()
    if generate_capitalise == "Y":
        
        #where do we want to store this menu? 
        menu_storage=input("In which directory do you want to store the menu? ")
        menu_filename=str(menu_storage)+"/"+str(name)+"'s Menu "+str(today)+".txt"

        #Let's write the menu straight to a file, so we can print it
        g=open(menu_filename,"x")
        g=open(menu_filename,"a")

        #Let's give some detail
        g.write(str(name)+"'s menu generated on "+str(today))

        day0="Saturday"
        g.write("\n\nSaturday afternoon: ")
        saturday_afternoon_snack=snack_picker()
        g.write("\nAfternoon snack: "+str(saturday_afternoon_snack))
        if day0 in spec_dinner_days:
            g.write("\n\nSpecial dinner plans: "+spec_dinner_days.get(day0))
        else: 
            g.write("\n\nDinner: ")
            saturday_protein=str(protein_picker_sat())
            g.write("\nProtein: "+saturday_protein)
            saturday_veg=str(veg_picker_sat())
            g.write("\nVegetables: "+saturday_veg)
            saturday_cuisine=str(cuisine_picker())
            g.write("\nTry this cuisine: "+saturday_cuisine)
            saturday_dessert=str(dessert_picker())
            g.write("\nDessert: "+saturday_dessert)

        day1="Sunday"
        g.write("\n\nSunday:")
        if day1 in spec_brunch_days:
            g.write("\nSpecial brunch plans: "+spec_brunch_days.get(day1))
        else: 
            if day1 in spec_breakfast_days:
                g.write("\nSpecial breakfast plans: "+spec_breakfast_days.get(day1))
            else: 
                sunday_breakfast=str(breakfast_picker())
                g.write("\nBreakfast: "+sunday_breakfast)
        sunday_fruit_snack=str(fruit_picker_sat())
        g.write("\n\nFruit snack: "+sunday_fruit_snack)
        if day1 not in spec_brunch_days:
            if day1 in spec_lunch_days:
                g.write("\n\nSpecial lunch plans: "+spec_lunch_days.get(day1))
            else:
                g.write("\n\nLunch: ") 
                sunday_bread=str(bread_picker())
                g.write("\nBread: "+sunday_bread)
                sunday_butter=str(butter_picker())
                g.write("\nButter: "+sunday_butter)
                sunday_deli=str(deli_picker())
                g.write("\nDeli items: "+sunday_deli)
                sunday_toppings=str(toppings_picker())
                g.write("\nToppings: "+sunday_toppings)
                sunday_lunchdrink=str(lunchdrink_picker())
                g.write("\nDrink: "+sunday_lunchdrink)
        sunday_afternoon_snack=str(snack_picker())
        g.write("\n\nAfternoon snack: "+sunday_afternoon_snack)
        if day1 in spec_dinner_days:
            g.write("\n\nSpecial dinner plans: "+spec_dinner_days.get(day1))
        else: 
            g.write("\n\nDinner: ")
            sunday_protein=str(protein_picker_sat())
            g.write("\nProtein: "+sunday_protein)
            sunday_veg=str(veg_picker_sat())
            g.write("\nVegetables: "+sunday_veg)
            sunday_cuisine=str(cuisine_picker())
            g.write("\nTry this cuisine: "+sunday_cuisine)
            sunday_dessert=str(dessert_picker())
            g.write("\nDessert: "+sunday_dessert)

        day2="Monday"
        g.write("\n\nMonday:")
        if day2 in spec_brunch_days:
            g.write("\nSpecial brunch plans: "+spec_brunch_days.get(day2))
        else: 
            if day2 in spec_breakfast_days:
                g.write("\nSpecial breakfast plans: "+spec_breakfast_days.get(day2))
            else: 
                monday_breakfast=str(breakfast_picker())
                g.write("\nBreakfast: "+monday_breakfast)
        monday_fruit_snack=str(fruit_picker_sat())
        g.write("\n\nFruit snack: "+monday_fruit_snack)
        if day2 not in spec_brunch_days:
            if day2 in spec_lunch_days:
                g.write("\n\nSpecial lunch plans: "+spec_lunch_days.get(day2))
            else:
                g.write("\n\nLunch: ") 
                monday_bread=str(bread_picker())
                g.write("\nBread: "+monday_bread)
                monday_butter=str(butter_picker())
                g.write("\nButter: "+monday_butter)
                monday_deli=str(deli_picker())
                g.write("\nDeli items: "+monday_deli)
                monday_toppings=str(toppings_picker())
                g.write("\nToppings: "+monday_toppings)
                monday_lunchdrink=str(lunchdrink_picker())
                g.write("\nDrink: "+monday_lunchdrink)
        monday_afternoon_snack=str(snack_picker())
        g.write("\n\nAfternoon snack: "+monday_afternoon_snack)
        if day2 in spec_dinner_days:
            g.write("\n\nSpecial dinner plans: "+spec_dinner_days.get(day2))
        else: 
            g.write("\n\nDinner: ")
            monday_protein=str(protein_picker_sat())
            g.write("\nProtein: "+monday_protein)
            monday_veg=str(veg_picker_sat())
            g.write("\nVegetables: "+monday_veg)
            monday_cuisine=str(cuisine_picker())
            g.write("\nTry this cuisine: "+monday_cuisine)
            monday_dessert=str(dessert_picker())
            g.write("\nDessert: "+monday_dessert)

        day3="Tuesday"
        g.write("\n\nTuesday:")
        if day3 in spec_brunch_days:
            g.write("\nSpecial brunch plans: "+spec_brunch_days.get(day3))
        else: 
            if day3 in spec_breakfast_days:
                g.write("\nSpecial breakfast plans: "+spec_breakfast_days.get(day3))
            else: 
                tuesday_breakfast=str(breakfast_picker())
                g.write("\nBreakfast: "+tuesday_breakfast)
        tuesday_fruit_snack=str(fruit_picker_sat())
        g.write("\n\nFruit snack: "+tuesday_fruit_snack)
        if day3 not in spec_brunch_days:
            if day3 in spec_lunch_days:
                g.write("\n\nSpecial lunch plans: "+spec_lunch_days.get(day3))
            else:
                g.write("\n\nLunch: ") 
                tuesday_bread=str(bread_picker())
                g.write("\nBread: "+tuesday_bread)
                tuesday_butter=str(butter_picker())
                g.write("\nButter: "+tuesday_butter)
                tuesday_deli=str(deli_picker())
                g.write("\nDeli items: "+tuesday_deli)
                tuesday_toppings=str(toppings_picker())
                g.write("\nToppings: "+tuesday_toppings)
                tuesday_lunchdrink=str(lunchdrink_picker())
                g.write("\nDrink: "+tuesday_lunchdrink)
        tuesday_afternoon_snack=str(snack_picker())
        g.write("\n\nAfternoon snack: "+tuesday_afternoon_snack)
        if day3 in spec_dinner_days:
            g.write("\n\nSpecial dinner plans: "+spec_dinner_days.get(day3))
        else: 
            g.write("\n\nDinner: ")
            tuesday_protein=str(protein_picker_sat())
            g.write("\nProtein: "+tuesday_protein)
            tuesday_veg=str(veg_picker_sat())
            g.write("\nVegetables: "+tuesday_veg)
            tuesday_cuisine=str(cuisine_picker())
            g.write("\nTry this cuisine: "+tuesday_cuisine)
            tuesday_dessert=str(dessert_picker())
            g.write("\nDessert: "+tuesday_dessert)

        day4="Wednesday"
        g.write("\n\nWednesday:")
        if day4 in spec_brunch_days:
            g.write("\nSpecial brunch plans: "+spec_brunch_days.get(day4))
        else: 
            if day4 in spec_breakfast_days:
                g.write("\nSpecial breakfast plans: "+spec_breakfast_days.get(day4))
            else: 
                wednesday_breakfast=str(breakfast_picker())
                g.write("\nBreakfast: "+wednesday_breakfast)
        wednesday_fruit_snack=str(fruit_picker_sat())
        g.write("\n\nFruit snack: "+wednesday_fruit_snack)
        if day4 not in spec_brunch_days:
            if day4 in spec_lunch_days:
                g.write("\n\nSpecial lunch plans: "+spec_lunch_days.get(day4))
            else:
                g.write("\n\nLunch: ") 
                wednesday_bread=str(bread_picker())
                g.write("\nBread: "+wednesday_bread)
                wednesday_butter=str(butter_picker())
                g.write("\nButter: "+wednesday_butter)
                wednesday_deli=str(deli_picker())
                g.write("\nDeli items: "+wednesday_deli)
                wednesday_toppings=str(toppings_picker())
                g.write("\nToppings: "+wednesday_toppings)
                wednesday_lunchdrink=str(lunchdrink_picker())
                g.write("\nDrink: "+wednesday_lunchdrink)
        wednesday_afternoon_snack=str(snack_picker())
        g.write("\n\nAfternoon snack: "+wednesday_afternoon_snack)
        if day4 in spec_dinner_days:
            g.write("\n\nSpecial dinner plans: "+spec_dinner_days.get(day4))
        else: 
            g.write("\n\nDinner: ")
            wednesday_protein=str(protein_picker_sat())
            g.write("\nProtein: "+wednesday_protein)
            wednesday_veg=str(veg_picker_sat())
            g.write("\nVegetables: "+wednesday_veg)
            wednesday_cuisine=str(cuisine_picker())
            g.write("\nTry this cuisine: "+wednesday_cuisine)
            wednesday_dessert=str(dessert_picker())
            g.write("\nDessert: "+wednesday_dessert)

        day5="Thursday"
        g.write("\n\nThursday:")
        if day5 in spec_brunch_days:
            g.write("\nSpecial brunch plans: "+spec_brunch_days.get(day5))
        else: 
            if day5 in spec_breakfast_days:
                g.write("\nSpecial breakfast plans: "+spec_breakfast_days.get(day5))
            else: 
                thursday_breakfast=str(breakfast_picker())
                g.write("\nBreakfast: "+thursday_breakfast)
        thursday_fruit_snack=str(fruit_picker_sat())
        g.write("\n\nFruit snack: "+thursday_fruit_snack)
        if day5 not in spec_brunch_days:
            if day5 in spec_lunch_days:
                g.write("\n\nSpecial lunch plans: "+spec_lunch_days.get(day5))
            else:
                g.write("\n\nLunch: ") 
                thursday_bread=str(bread_picker())
                g.write("\nBread: "+thursday_bread)
                thursday_butter=str(butter_picker())
                g.write("\nButter: "+thursday_butter)
                thursday_deli=str(deli_picker())
                g.write("\nDeli items: "+thursday_deli)
                thursday_toppings=str(toppings_picker())
                g.write("\nToppings: "+thursday_toppings)
                thursday_lunchdrink=str(lunchdrink_picker())
                g.write("\nDrink: "+thursday_lunchdrink)
        thursday_afternoon_snack=str(snack_picker())
        g.write("\n\nAfternoon snack: "+thursday_afternoon_snack)
        if day5 in spec_dinner_days:
            g.write("\n\nSpecial dinner plans: "+spec_dinner_days.get(day5))
        else: 
            g.write("\n\nDinner: ")
            thursday_protein=str(protein_picker_wed())
            g.write("\nProtein: "+thursday_protein)
            thursday_veg=str(veg_picker_wed())
            g.write("\nVegetables: "+thursday_veg)
            thursday_cuisine=str(cuisine_picker())
            g.write("\nTry this cuisine: "+thursday_cuisine)
            thursday_dessert=str(dessert_picker())
            g.write("\nDessert: "+thursday_dessert)

        day6="Friday"
        g.write("\n\nFriday:")
        if day6 in spec_brunch_days:
            g.write("\nSpecial brunch plans: "+spec_brunch_days.get(day6))
        else: 
            if day6 in spec_breakfast_days:
                g.write("\nSpecial breakfast plans: "+spec_breakfast_days.get(day6))
            else: 
                friday_breakfast=str(breakfast_picker())
                g.write("\nBreakfast: "+friday_breakfast)
        friday_fruit_snack=str(fruit_picker_sat())
        g.write("\n\nFruit snack: "+friday_fruit_snack)
        if day6 not in spec_brunch_days:
            if day6 in spec_lunch_days:
                g.write("\n\nSpecial lunch plans: "+spec_lunch_days.get(day6))
            else:
                g.write("\n\nLunch: ") 
                friday_bread=str(bread_picker())
                g.write("\nBread: "+friday_bread)
                friday_butter=str(butter_picker())
                g.write("\nButter: "+tuesday_butter)
                friday_deli=str(deli_picker())
                g.write("\nDeli items: "+friday_deli)
                friday_toppings=str(toppings_picker())
                g.write("\nToppings: "+friday_toppings)
                friday_lunchdrink=str(lunchdrink_picker())
                g.write("\nDrink: "+friday_lunchdrink)
        friday_afternoon_snack=str(snack_picker())
        g.write("\n\nAfternoon snack: "+friday_afternoon_snack)
        if day6 in spec_dinner_days:
            g.write("\n\nSpecial dinner plans: "+spec_dinner_days.get(day6))
        else: 
            g.write("\n\nDinner: ")
            friday_protein=str(protein_picker_wed())
            g.write("\nProtein: "+friday_protein)
            friday_veg=str(veg_picker_wed())
            g.write("\nVegetables: "+friday_veg)
            friday_cuisine=str(cuisine_picker())
            g.write("\nTry this cuisine: "+friday_cuisine)

            friday_dessert=str(dessert_picker())
            g.write("\nDessert: "+friday_dessert)

        day7="Saturday"
        g.write("\n\nSaturday morning:")
        if day7 in spec_brunch_days:
            g.write("\nSpecial brunch plans: "+spec_brunch_days.get(day7))
        else: 
            if day7 in spec_breakfast_days:
                g.write("\nSpecial breakfast plans: "+spec_breakfast_days.get(day7))
            else: 
                saturday_breakfast=str(breakfast_picker())
                g.write("\nBreakfast: "+saturday_breakfast)
        saturday_fruit_snack=str(fruit_picker_sat())
        g.write("\n\nFruit snack: "+saturday_fruit_snack)
        if day7 not in spec_brunch_days:
            if day7 in spec_lunch_days:
                g.write("\n\nSpecial lunch plans: "+spec_lunch_days.get(day7))
            else:
                g.write("\n\nLunch: ") 
                saturday_bread=str(bread_picker())
                g.write("\nBread: "+saturday_bread)
                saturday_butter=str(butter_picker())
                g.write("\nButter: "+saturday_butter)
                saturday_deli=str(deli_picker())
                g.write("\nDeli items: "+saturday_deli)
                saturday_toppings=str(toppings_picker())
                g.write("\nToppings: "+saturday_toppings)
                saturday_lunchdrink=str(lunchdrink_picker())
                g.write("\nDrink: "+saturday_lunchdrink)

        g.write("\n\nBon appetit!")
        g.write("")
    else:
        print("\nNo menu has been generated. ")
    g.close()

    #okay, time for the shopping lists

    #first we need to sort them alphabetically
    breakfast_shopping_list.sort()
    fruit_saturday_shopping_list.sort()
    fruit_wednesday_shopping_list.sort()
    bread_shopping_list.sort()
    dairy_shopping_list.sort()
    deli_shopping_list.sort()
    toppings_shopping_list.sort()
    lunchdrink_shopping_list.sort()
    snack_shopping_list.sort()
    veg_saturday_shopping_list.sort()
    veg_wednesday_shopping_list.sort()
    protein_saturday_shopping_list.sort()
    protein_wednesday_shopping_list.sort()
    sweets_shopping_list.sort()

    #then we count how often an item occurs in a shopping list
    #we then multiply by the amount required
    #and by the number of people attending that meal
    #breakfast
    def countOccurrence_bf(a):
        k = {}
        for j in a:
            if j in k:
                k[j] +=1*persons_other
            else:
                k[j] =1*persons_other
        return k

    #fruit
    def countOccurrence_fruit(a):
        k = {}
        for j in a:
            if j in k:
                k[j] +=2*persons_other
            else:
                k[j] =2*persons_other
        return k

    #lunch
    #bread
    def countOccurrence_bread(a):
        k = {}
        for j in a:
            if j in k:
                k[j] +=2*persons_other
            else:
                k[j] =2*persons_other
        return k
    
    #sandwich fillings
    def countOccurrence_deli(a):
        k = {}
        for j in a:
            if j in k:
                k[j] +=2*persons_other
            else:
                k[j] =2*persons_other
        return k

    #don't need to make any for butter or toppings
    #but we do need to transform the dictionaries back into actual lists
    toppings_shopping_list2=list(dict.fromkeys(toppings_shopping_list))
    dairy_shopping_list2=list(dict.fromkeys(dairy_shopping_list))

    #we do need them for lunch drinks
    def countOccurrence_drinks(a):
        k = {}
        for j in a:
            if j in k:
                k[j] +=1*persons_other
            else:
                k[j] =1*persons_other
        return k

    #afternoon snacks
    def countOccurrence_snacks(a):
        k = {}
        for j in a:
            if j in k:
                k[j] +=1*persons_other
            else:
                k[j] =1*persons_other
        return k

    #dinner
    #vegetables
    def countOccurrence_veg(a):
        k = {}
        for j in a:
            if j in k:
                k[j] +=200*persons_dinner
            else:
                k[j] =200*persons_dinner
        return k

    #proteins
    def countOccurrence_protein(a):
        k = {}
        for j in a:
            if j in k:
                k[j] +=125*persons_dinner
            else:
                k[j] =125*persons_dinner
        return k
    
    #dessert
    def countOccurrence_sweet(a):
        k = {}
        for j in a:
            if j in k:
                k[j] +=10*persons_dinner
            else:
                k[j] =10
        return k

    #do they even want one?
    shopping=input("\nWould you like to generate shopping lists based on this menu? Y/N ")
    shopping_capitalise=shopping.capitalize()
    
    #if yes, let's make them and write them straight to a txt-file for ease of printin
    if shopping_capitalise == "Y":

        #here, too, it's polite to ask where they want it stored
        shopping_storage=input("In which directory do you want to store the shopping list? ")
        shopping_filename=str(shopping_storage)+"/"+str(name)+"'s Shopping List "+str(today)+".txt"
        f=open(shopping_filename,"x")
        f=open(shopping_filename,"a")

        #some useful warnings
        f.write(name+"'s shopping lists: \n(The quantities in these lists are adjusted for the number of people for whom a menu has been generated.)")

        #a heading
        f.write("\n\nSaturday shop: ")
        #things we buy on Saturdays
        f.write("\nProteins (grams): "+str(countOccurrence_protein(protein_saturday_shopping_list)))
        f.write("\nDeli (slices): "+str(countOccurrence_deli(deli_shopping_list)))
        f.write("\nBread (items): "+str(countOccurrence_bread(bread_shopping_list)))
        f.write("\nDairy: "+str(dairy_shopping_list2))
        f.write("\nVegetables (grams): "+str(countOccurrence_veg(veg_saturday_shopping_list)))
        f.write("\nFruit (pieces/portions): "+str(countOccurrence_fruit(fruit_saturday_shopping_list)))
        f.write("\nToppings (no recommendations): "+str(toppings_shopping_list2))
        f.write("\nSweets (grams): "+str(countOccurrence_sweet(sweets_shopping_list)))
        f.write("\nAfternoon snacks (items): "+str(countOccurrence_snacks(snack_shopping_list)))
        f.write("\nBreakfast (items): "+str(countOccurrence_bf(breakfast_shopping_list)))
        f.write("\nLunch drinks (items): "+str(countOccurrence_drinks(lunchdrink_shopping_list)))

        #another heading
        f.write("\n\nWednesday top-up shop: ")
        f.write("\nProteins (grams): "+str(countOccurrence_protein(protein_wednesday_shopping_list)))
        f.write("\nVegetables (grams): "+str(countOccurrence_veg(veg_wednesday_shopping_list)))
        f.write("\nFruit (pieces/portions): "+str(countOccurrence_fruit(fruit_wednesday_shopping_list)))
        f.close()

    #If not, of course don't produce any shopping lists
    else:
        print("\nNo shopping lists have been generated. ")

    print("\nEnjoy your day!")
