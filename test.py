import random

def distribute_candies(min_per_person, max_per_person, num_people, num_candies) -> list:
    candies_allocation = num_people * [min_per_person]

    left_out_candies = num_candies - num_people * min_per_person

    max_addtional_candies = max_per_person - min_per_person

    left_people = num_people 
    for i in range(num_people):
        left_people -= 1
        must_give_to_this_person = left_out_candies - left_people * max_addtional_candies
        if must_give_to_this_person > 0:
            candies_allocation[i] += must_give_to_this_person
            left_out_candies -= must_give_to_this_person
        else:
            addtional_candies_to_this_person = random.randint(0, min(max_addtional_candies, left_out_candies))
            candies_allocation[i] += addtional_candies_to_this_person
            left_out_candies -= addtional_candies_to_this_person
    
    return candies_allocation

a = distribute_candies(2,5,20,68)

print(a)

sum = 0
for i in a:
    sum += i

print(sum)