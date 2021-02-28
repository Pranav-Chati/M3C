from person import Person
from device import Device

AGE_GROUPS = ["2-11", "12-17", "18-49", "50-64", "65+"]


def get_age_group(a):
    if 2 < a < 12:
        return 0
    elif a < 18:
        return 1
    elif a < 50:
        return 2
    elif a < 65:
        return 3
    elif a > 64:
        return 4


tarik = Person(2, True)

family_people = int(input("How many people are in your family? \n"))

family = []

for person in range(family_people):

    age = int(input(f"\nWhat age is individual {person + 1}?\n"))
    age_group = get_age_group(age)

    is_heavy_internet_user = False

    if age > 17:
        heavy_user_input = input("Are they a heavy internet user? t/f.\n").lower()
        if heavy_user_input == "t" or heavy_user_input == "true":
            is_heavy_internet_user = True

    new_individual = Person(age_group, is_heavy_internet_user)
    family.append(new_individual)

aggregate_bandwidth = 0

for person in family:
    aggregate_bandwidth += person.max_bandwidth()

print(f"\nThe total bandwidth recommended is {aggregate_bandwidth} Mbps.")
