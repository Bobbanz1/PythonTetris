# Wordfreq
# Take a string as the argument and return a dictionary containing unique words in the string as keys and number of times the word is encountered as the value of the key in question.
#
# Thought process
# We take in the string
# Define an empty dictionary
# Split the string into a list held inside a variable
# Loop through it and check if it's an empty string. If it is then we will skip the element and continue looking.
# Check if it exists in the dictionary already, if it does then grab the value and increment it by one.
# If it doesn't exist, add it to the dictionary with the value of 1.
def wordfreq(text: str) -> dict:
    # Cats returns again, used as a dictionary here
    cats = {}
    # Early return of empty dictionary if the string is completely empty.
    if text == "":
        return cats
    # Split it and store the values as lists. We will assume every word is separated by a whitespace.
    hounds = text.split(sep=" ")
    for stuff in hounds:
        # Safety measure, if we encounter an empty entry in the list then skip the entry and continue with the next one.
        if stuff == "":
            continue
        # If the thingy exists in the dictionary then increment it by 1.
        if stuff in cats:
            cats[stuff] = cats[stuff] + 1
        else:
            # If it doesn't exist then create it and give it the value of 1
            cats[stuff] = 1
    # Return the dictionary, even if it might be empty.
    return cats


# Testing Samples
# {"hej": 2, "på": 1, "dig": 1}
# print(wordfreq("hej hej på dig"))
# {"python": 2, "programmering": 1}
# print(wordfreq("python programmering python"))
# {"test": 3}
# print(wordfreq("test test test"))
# {"ett": 1, "två": 2, "tre": 1}
# print(wordfreq("ett två tre två"))
# {}
# print(wordfreq(""))
