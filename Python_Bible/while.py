from random import choice

questions = ["why is the sky blue:?","why is the there a face on the moon?","why are all the dinos?:"]

question= choice(questions)

answer = input(question).strip()

while answer != "just because":
    answer = input("But why?:")




