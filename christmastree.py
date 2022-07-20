# A function that draws a Christmas tree. The argument is the number of the levels.
# Christmas balls appear on a random position on a random row of each level.
# Christmas balls can't apper on the highest and lowest rows and on the edges of the tree.

import random


def pick_a_random(word):
    length = len(word)
    number = random.randint(1, length - 2)
    return number


def draw_christmas_tree(number):
    icon = "*"
    space = " "
    for x in range(1, number+1):
        a = space*(3+(number-x))
        d = icon*x+(icon*(x-1))
        b = space*(2+(number-x))
        e = icon*(x+2)+(icon*(x-1))
        c = space*(1+(number-x))
        f = icon*(x+4)+(icon*(x-1))

        mylist = [d, e, f]

        if x == 1 and number != 1:
            random_row_index = random.randint(1, len(mylist)-1)
        elif x == 1 and number == 1:
            random_row_index = 1
        elif x == number:
            random_row_index = random.randint(0, len(mylist)-2)
        else:
            random_row_index = random.randint(0, len(mylist)-1)

        my_choice = mylist[random_row_index]

        random_number = pick_a_random(my_choice)
        my_choice_1 = my_choice[:random_number]
        my_choice_2 = "@"
        my_choice_3 = my_choice[random_number+1:]
        my_new_choice = my_choice_1 + my_choice_2 + my_choice_3

        if random_row_index == 0:
            print(a, my_new_choice)
        else:
            print(a, d)

        if random_row_index == 1:
            print(b, my_new_choice)
        else:
            print(b, e)

        if random_row_index == 2:
            print(c, my_new_choice)
        else:
            print(c, f)

#tests
draw_christmas_tree(1)
draw_christmas_tree(3)
draw_christmas_tree(5)
