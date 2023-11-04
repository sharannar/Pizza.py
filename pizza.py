# Prompt the user to input the number of people, slices per person, and slices per pizza pie.
num_people = int(input("Enter the number of people: "))
slices_per_person = int(input("Enter the number of slices each person will eat: "))
slices_per_pizza = int(input("Enter the number of slices in each pizza pie: "))

# Calculate the total number of slices needed.
total_slices_needed = num_people * slices_per_person

# Calculate the number of pizza pies needed to satisfy the demand.
if total_slices_needed % slices_per_pizza == 0:
    num_pizzas_needed = total_slices_needed // slices_per_pizza
else:
    num_pizzas_needed = total_slices_needed // slices_per_pizza + 1

# Display the result to the user.
print(f"You will need {num_pizzas_needed} pizza pie(s) to feed {num_people} people.")
