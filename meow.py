# it generates the random meow lorem which is shown in index.html
import random as rd

meows = ("meoww ", "mew ", "meow ", "meeoww ", "meeow ")

string = ""
words = 0
while words <= 50:
    meow = rd.choice(meows)
    if words == 0:
        meow = meow.capitalize()
    string += meow
    words += 1

print(string)
