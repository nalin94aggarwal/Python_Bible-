email = input("What is your email address? :").strip()

user = email[:email.index("@")]
domain = email[email.index("@")+1:]
output = "Your usename is {} and domain name is {}".format(user,domain)
print(output)
