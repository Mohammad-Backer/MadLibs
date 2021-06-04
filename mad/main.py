"""
This is a MADLIB program
It asks the user for a String input
He will be asked for an adjective, adverb, noun, verb, etc...
Then they will be rearranged into a story.
"""
import os

def Theme():
    """
    The user will be presented with multiple options for a theme of the story.
    """
    Themes = os.listdir("Themes")
    CleanedThemes = []
    for T in Themes:
        CleanedThemes.append(T.replace(".txt",""))

    return CleanedThemes


def ChooseTheme ():
    """
    The user will choose one of the themes presented with the help of the method Theme
    """
    lamda = 0
    Themes = {i+1 : Theme()[i] for i in range(0,len(Theme()))}
    for i in range(0,len(Theme())) :
        print(str(i+1) + "-" + Themes[i+1])
    while lamda == 0:
        UserInput = input("Please Enter which theme would you like: ")
        try:
            UserInput = int(UserInput)
            if UserInput > 0 and UserInput <= len(Theme()):
                ChosenTheme = Themes[UserInput]
                print("You have chosen: " + ChosenTheme)
                lamda +=1
                return ChosenTheme
            else:
                print("Your input does not exist")
        except Exception:
            print("Your input does not exist")

def EnterWords (replace) :
    replaced = []
    count = len(replace)
    i = 0 
    while i<count:
        wordformat = replace[i]
        j = input("Please enter an " + wordformat + ":")
        if j in word_dict[wordformat]:
            replaced.append(j)
            i +=1
        else:
            print("This is not the right format of the word.\nPlease try again! ")

    return replaced

ct = ChooseTheme()
path = "Themes/" + ct + ".txt"


pathToadjectives = "words/adjectives/28K adjectives.txt"
pathToadverbs = "words/adverbs/6K adverbs.txt"
pathTonouns = "words/nouns/91K nouns.txt"
pathToPrepositions = "words/prepositions/prepositions.txt"
pathToverbs = "words/verbs/31K verbs.txt"

with open(pathToadjectives) as a:
    adjectives = a.readlines()
    adjectives1 = [adj.strip("\n") for adj in adjectives]
    a.close()

with open(pathToadverbs) as ad:
    adverbs = ad.readlines()
    adverbs1 = [adj.strip("\n") for adj in adverbs]
    ad.close()

with open(pathTonouns) as n:
    nouns = n.readlines()
    nouns1 = [adj.strip("\n") for adj in nouns]
    n.close()

with open(pathToPrepositions) as p:
    prepo = p.readlines()
    prepo1 = [adj.strip("\n") for adj in prepo]
    p.close()

with open(pathToverbs) as v:
    verbs = v.readlines()
    verbs1 = [adj.strip("\n") for adj in verbs]
    v.close()
    
word_dict = {
    "<adjective>":adjectives1,
    "<adverb>":adverbs1,
    "<noun>":nouns1,
    "<preposition>":prepo1,
    "<verb>":verbs1
}

replaceble = [] 
with open(path) as f:
    lines = f.readlines()
    for l in lines:
        words = l.split(" ")
        for w in words:
            if w.startswith("<"):
                replaceble.append(w)
    replaced = EnterWords(replaceble)
    f.close()

i = 0
upgraded = [] 
for l in lines:
    words = l.split()
    for w in words:
        if w.startswith("<"):
            w = replaced[i]
            i += 1
        upgraded.append(w)

print("Your story is : \n")

s = ""
for u in upgraded:
    s += u
    s += " " 

print(s)

Decision = input("Do You want to save your story ?\nIf yes enter Y if not enter anything else: \n")

pathToStories = "Stories/story"

if Decision == 'Y' or Decision == 'y':
    addi = 1
    while addi > 0:
        try:
            f = open(pathToStories + str(addi), 'x')
            f.close()
            break
        except Exception:
            addi +=1  
    f1 = open(pathToStories + str(addi), 'w')
    f1.write(s)
    f1.close()
    print("File saved! See you next time!")
else:
    print("See you next time!")


