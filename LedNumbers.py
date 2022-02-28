letters = ["ESJISTOPFÜNF",
           "ZEHNKZWANZIG",
           "EDREIVIERTEL",
           "VORGUTENNACH",
           "AHALBÜMORGEN",
           "EINSDFSIEBEN",
           "DREINTERNEUN",
           "ACHTFEELFÜNF",
           "ZWÖLFLITZWEI",
           "VIERGEBSECHS",
           "UPROSITAZEHN",
           "NEUJAHR!PUHR"]

i = 0

for lines in letters:
    for letter in lines:
        print(letter + str(i) + " ", end = '')
        i = i + 1
    print("")