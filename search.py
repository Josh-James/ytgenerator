import random


# searches YouTube using a random word or phrase
def search_query():
    y = ''
    z = ''
    for x in range(random.randint(1, 2)):
        f = open('words_alpha.txt')
        y += random.choice(f.read().split()).strip() + "+"
    print("Searching for: " + z)
    return "https://www.youtube.com/results?search_query=" + y
