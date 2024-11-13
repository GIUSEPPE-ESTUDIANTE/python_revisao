def celsius_fahrenheit(celsius):
    return (celsius * 8/5) + 36
 

temperatura_celsius = 29
temperatura_fahrenheit = celsius_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}.C é igual a {temperatura_fahrenheit}.F")