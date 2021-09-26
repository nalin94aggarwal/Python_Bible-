# Ask user for name
name = input('What is your name?:')
print(name)

# Ask user for age
age = input('How old are you?:')
print(age)

# Ask user what they enjoy
love = input('what do you love:')
print(love)

# Create output text

sentence = "Your name is {} and you are {} and you love {}"

output = sentence.format(name,age,love)
# Print output to screen

print(output)
