#define your operations

def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit -32) * 5/9

def celcius_to_kelvin(celcius):
    return celcius + 273.5

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.5

def kelvin_to_celcius(kelvin):
    return kelvin - 273.5

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.5) * 9/5 + 32

conversion = {
    ('celsius','fahrenheit') : celcius_to_fahrenheit,
    ('celsius','kelvin') : celcius_to_kelvin,
    
    ('fahrenheit','celsius'): fahrenheit_to_celcius,
    ('fahrenheit','kelvin') : fahrenheit_to_kelvin,
    
    ('kelvin', 'celsius') : kelvin_to_celcius,
    ('kelvin','fahrenheit') : kelvin_to_fahrenheit,
}

def conver_temperature(value,from_unit,to_unit):
    if from_unit == to_unit:
        return value
    
    key = (from_unit,to_unit)
    
    if key not in conversion:
        raise ValueError("konversi tidak tersedia")
    
    return conversion[key](value)


def viewMenu():
    print("-Temperature Conventer Menu-")
    print("1. celsius to fahrenheit & kelvin")
    print("2. fahrenheit to celsius & kelvin")
    print("3. kelvin to celsius & fahrenheit")
    print("4. exit")

while True:
    viewMenu()
    choice = input("select an option (1/2/3/4): ")
    
    try:
        
        if choice == '1':
            celsius = float(input("input your celsius temperature: "))
            desimal = int(input("how many decimal numbers behind the comma: "))
            print(f"Fahrenheit: {celcius_to_fahrenheit(celsius):.{desimal}f}")
            print(f"kelvin: {celcius_to_kelvin(celsius):.{desimal}f}")
        elif choice == '2':
            fahrenheit = float(input('input your fahrenheit temperature: '))
            desimal = int(input("how many decimal numbers behind the comma: "))
            print(f"Celsius: {fahrenheit_to_celcius(fahrenheit):.{desimal}f}")
            print(f"Kelvin: {fahrenheit_to_kelvin(fahrenheit):.{desimal}f}")
        elif choice == '3':
            kelvin = float(input("input your kelvin temperature: "))
            desimal = int(input("how many decimal numbers behind the comma: "))
            print(f"Celsius: {kelvin_to_celcius(kelvin):.{desimal}f}")
            print(f"Fahrenheit: {kelvin_to_fahrenheit(kelvin):.{desimal}f}")
        elif choice == '4':
            break
        else:
            print("please, choose a valid input")
    except Exception as e:
        print(e)