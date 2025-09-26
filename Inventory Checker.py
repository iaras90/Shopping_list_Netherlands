#TODO:
#Before printing shopping lists, import the shopping lists written by the menu generator

#what should we have in stock?
cat_cupboard={"litter": 1, "cat snacks": 1,"kibble": 1, "wet food pouches": 12, "wet food tins": 4}
cat_list={}

washing_machine={"colour detergent": 1, "white detergent": 1, "oxyclean": 1, "stain remover": 1, "fine wash detergent": 1}
cleaning_list={}

top_cupboard_left={"fine salt": 1, "sea salt": 1, "kosher salt": 1}
seasonings_list={}

top_cupboard_middle={"kitchen roll": 4}
wipes_list={}

x={"placeholder": 0}
y={}

#how should we handle it if we're missing an item?
def inventory_checker(inventory_list,shopping_list):
    for item,value in inventory_list.items():
        check=input("Do we have "+str(value)+" "+str(item)+"? Y/N ")
        check_caps=check.capitalize()
        if check_caps=="N":
            quantity=int(input("How much do we need of this item? "))
            shopping_list.update({item: quantity})

#it takes time to move locations, let's give a moment to pause. 
def ready_check():
    ready=input("Press Y when ready to proceed to taking inventory. ")
    ready_caps=ready.capitalize()

print("Let's start in the cat cupboard.")
ready_check()
inventory_checker(cat_cupboard,cat_list)
print("Let's move to the washing machine area.")
ready_check()
inventory_checker(washing_machine,cleaning_list)
print("Moving on to the kitchen, starting with the top cupboard above the fridge.")
ready_check()
inventory_checker(top_cupboard_left,seasonings_list)
print("We're going into the fridge, top to bottom, left to right, door to inside.")
ready_check()
inventory_checker(x,y)
print("Now the freezer, top to bottom.")
ready_check()
inventory_checker(x,y)
print("Moving on to the top cupboard in the middle.")
ready_check()
inventory_checker(top_cupboard_middle,wipes_list)

shopping_list=input("Do you want to generate shopping lists based on the inventory check? Y/N ")
shopping_list_caps=shopping_list.capitalize()
if shopping_list_caps=="Y":
    if seasonings_list==True:
        print("Seasonings: "+str(seasonings_list))
    if cat_list==True:
        print("Cat items: "+str(cat_list))
    if wipes_list==True:
        print("Wipes: "+str(wipes_list))
    if cleaning_list==True:
        print("Cleaning: "+str(cleaning_list))
else:
    print("No shopping lists will be generated. ")