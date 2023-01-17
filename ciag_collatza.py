# Ciag Collatza
x = int(input("Podaj liczbe <int> od 1 do 100: "))
if 1 <= x <= 100:
    print(f"Podano: {x}")
    print("Elementy ciagu: ")
    # jesli wartosc jest poprawna to jest pierwszym elementem ciagu
    dlugosc = 1
    print(float(x))
    # wyliczamy kolejne elementy
    while x != 1:
        if x % 2 == 0:
            x = x/2
        else:
            x = (3*x) + 1
        dlugosc += 1
        print(float(x))
    print(f"Dlugosc ciagu: {dlugosc} elementow")
else:
    print("Podano nieprawidłowa liczbe")
