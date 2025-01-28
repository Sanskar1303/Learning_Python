def temp(C):
    F = C * (9/5) + 32
    return F
C = float(input('Enter temprature in Degree Celsius: '))
print("temp in fahrenheit", temp(C))
