temperatura = float(input("Informe a temperatura: "))
unidade_origem = input("Informe a unidade de origem (Celsius, Fahrenheit, Kelvin): ").strip().lower()
unidade_destino = input("Informe a unidade de destino (Celsius, Fahrenheit, Kelvin): ").strip().lower()

if unidade_origem == "celsius":
    if unidade_destino == "fahrenheit":
        temperatura_convertida = (temperatura * 9/5) + 32
    elif unidade_destino == "kelvin":
        temperatura_convertida = temperatura + 273.15
    else:
        temperatura_convertida = temperatura
elif unidade_origem == "fahrenheit":
    if unidade_destino == "celsius":
        temperatura_convertida = (temperatura - 32) * 5/9
    elif unidade_destino == "kelvin":
        temperatura_convertida = (temperatura - 32) * 5/9 + 273.15
    else:
        temperatura_convertida = temperatura
elif unidade_origem == "kelvin":
    if unidade_destino == "celsius":
        temperatura_convertida = temperatura - 273.15
    elif unidade_destino == "fahrenheit":
        temperatura_convertida = (temperatura - 273.15) * 9/5 + 32
    else:
        temperatura_convertida = temperatura
else:
    print("Unidade de origem inválida.")
    temperatura_convertida = None

if temperatura_convertida is not None:
    print(f"A temperatura convertida é: {temperatura_convertida:.2f} {unidade_destino.capitalize()}")