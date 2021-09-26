def foo(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))

        

def add (*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return(total)


def about(name, age, like):
    sentence = "Meet {} they are {} years old and they like {}".format(name,age,like)
    return sentence

dictionary = {"name":"Nalin", "age":35,"like":"Cricket"}

print(about(**dictionary))


