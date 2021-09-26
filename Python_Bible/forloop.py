sentence = input("Enter the sentence in which you want to count:").strip().lower()
vowel=0
consonent =0
for letter in sentence:
    if letter in ["a","e","i","o","u"]:
        vowel = vowel + 1
    elif letter == " ":
        pass
    else:
        consonent = consonent + 1


print("There are {} vowels and {} consonents in the sentence".format(vowel,consonent))
