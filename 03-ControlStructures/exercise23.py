dog_age = int(input("Enter the dog's age in human years: "))
if dog_age <= 2:
    human_years = dog_age * 10.5
else:
    human_years = 2 * 10.5 + (dog_age - 2) * 4
print(f"The dog's age in dog's years is {human_years}.")