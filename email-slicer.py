email = input("Enter your Email: ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"Your username is {username} and domain used is {domain}")
