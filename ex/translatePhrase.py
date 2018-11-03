def translate(phrase):
    translated = ""
    for letter in phrase:
        if letter in "AEOIUaeoiu":
            if letter.isupper():
                translated += "G"
            else:
                translated += "g"
        else:
            translated +=letter
    return translated


print(translate(input("Enter a phrase: ")))
# translate("giraffe")