def get_full_name(first_name: str, last_name: str) -> str:
    full_name = f"{first_name} {last_name}"
    return full_name.title()

def get_name_with_age(name: str, age: int) -> str:
    name_with_age = name + "is this old: " + str(age)
    return name_with_age.capitalize()

print(get_full_name('john', 'doe'))
