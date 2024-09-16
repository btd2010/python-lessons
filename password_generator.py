# Last 3 letters of first_name, last_name are sliced into a password

password_generator = lambda first_name, last_name: first_name[len(first_name)-3:] + last_name[len(last_name)-3:]

first_name = "Ben"
last_name = "Daws"

temp_password = password_generator(first_name, last_name)
print(temp_password)
