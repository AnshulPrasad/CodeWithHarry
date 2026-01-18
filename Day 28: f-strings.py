letter = "My name is {1} and I am from {0}"
country = "India"
name = "Anshul"
age = 22.0179

print(letter.format(name, country))
print(f"My name is {name} and I am from {country} and my age is {age:.2f}")
print("My name is {name} and I am from {country} and my age is {age:.2f}")
print(f"My name is {{name}} and I am from {{country}} and my age is {{age:.2f}}")
