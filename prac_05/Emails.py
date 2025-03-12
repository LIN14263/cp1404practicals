dict_names = {}
email = input("E-mail:")
email_list = email.split("@")
while email != "":
    name = (" ".join(email_list[0].split("."))).title()
    is_name = input(f"Is your name {name}? (Y/n)").lower()
    if is_name == "y" or is_name == "":
        dict_names[name] = email
    else:
        correct_name = input("Name:")
        dict_names[correct_name] = email
    email = input("E-mail:")
    email_list = email.split("@")
for name, e_address in dict_names.items():
    print(f"{name} ({e_address})")
