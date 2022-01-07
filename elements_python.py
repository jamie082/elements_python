#!/usr/bin/python3

list_item_two = ['apples', 'oranges', 'pears', 'apricots']

list_item_two.append("celery")

print("ADD (1) or REMOVE (2) elements\n")

user_input = input("> ")

if user_input == "1":
    print("Add Element to List")
    special_val = "add"
elif user_input == "2":
    print("Remove Element to List")
    special_val = "remove"

i = 1

while i < 4: # Output list
    for fruit in list_item_two:
      print(f"{i} fruit of type: {fruit}")
      i += 1

print("\nLength of elements: ", len(list_item_two))

input_val = input(f"What element to {special_val}? ") # if add or remove

# insert element
if special_val == "add":
   list_item_two.append(input_val)

elif special_val == "remove":
   list_item_two.remove(input_val) # this works

print("Now the list is: ", list_item_two)
