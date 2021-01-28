import random
import pyjokes

jokes = ["I threw a boomerang a few years ago.\n I now live in constant fear",
         "You don't need a prachute to go skydiving.\n You need a parachute to go skydiving twice",
         "My Grandfather has a heart of a lion\n And a lifetime ban at the the zoo",
         "Women only call me ugly until they find out how much money I make.\nThen they call me ugly and poor.",
         "You are never completely useless,\n you can always serve as a bad example.",
         "A Roman walks into a bar, sticks two fingers up to the barman and says, Five beers please.",
         "What's the difference between a well dressed man on a bicycle, and a poorly dressed man on a tricycle?,\nAttire!",
         "I invented a new word,\n plagiarism",
         "Helvetica and Times New Roman walk into a bar...\n'Get out of here!' shouts the bartender. 'We don't serve your type.'",
         "Did you hear about the new restaurant called 'Karma?'\nThere’s no menu you get what you deserve.",
         pyjokes.get_joke()]

lst = []


def joke_choice():
    joke = random.choice(jokes)

    return joke
