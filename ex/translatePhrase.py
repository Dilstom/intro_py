def translate(phrase):
    translated = ""
    for letter in phrase:
        if letter in "AEOIUaeoiu":
            translated += "g"
        else:
            translated +=letter
    return translated


print(translate(input("Enter a phrase: ")))
# translate("giraffe")