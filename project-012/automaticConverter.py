from temperatureConverter import conver_temperature

value = float(input("input the temperature: "))
from_unit= input("from kelvin/celsius/fahrenheit: ").lower()
to_unit = input("to kelvin/celsius/fahrenheit: ").lower()

desimal = int(input("how many desimal: "))

result = conver_temperature(value,from_unit,to_unit)

print(f"Result: {result} {to_unit}")