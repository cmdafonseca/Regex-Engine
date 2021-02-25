import collections


def tallest_people(**kwargs):
    highest = max(kwargs.values())
    for name, height in sorted(kwargs.items()):
        if height == highest:
            print(f"{name} : {height}")

