# get access to extra features 
import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)
# random.randint(a, b)
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).