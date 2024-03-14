def celsius_na_fahrenheit(temperatura_c):
    temperatura_f = (temperatura_c * 9/5) + 32
    return temperatura_f

temperatura_c = 25
temperatura_f = celsius_na_fahrenheit(temperatura_c)
print(f"{temperatura_c} stopni Celsjusza to {temperatura_f} stopni Fahrenheita.")
