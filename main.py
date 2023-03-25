# https://github.com/frozuu/TEB_PY/

class Pracownik:
    def __init__(self, imie, nazwisko, wiek, stanowisko, zarobki):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.stanowisko = stanowisko
        self.zarobki = zarobki

    def __str__(self):
        return f"Imię: {self.imie}\nNazwisko: {self.nazwisko}\nWiek: {self.wiek}\nStanowisko: {self.stanowisko}\nZarobki: {self.zarobki}\n"


try:
    with open("pracownicy.txt", "w") as file:
        file.write("Jan Kowalski;45;kierownik;\n")
        file.write("Adam Nowak;32;mechanik;\n")
        file.write("Zofia Kyrs;25;kasjerka;\n")
        file.write("Adrian Kryk;37;mechanik;\n")
        file.write("Marta Prokop;40;mechanik;\n")
        file.write("Dorota Rytel;39;kierowca;\n")

    with open("pracownicy.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            data = line.strip().split(";")
            if data[2] == "kierownik":
                zarobki = 6700
            elif data[2] == "mechanik":
                zarobki = 4300
            elif data[2] == "kasjerka":
                zarobki = 3800
            elif data[2] == "kierowca":
                zarobki = 4100
            else:
                raise ValueError(f"Nieprawidłowe stanowisko: {data[2]}")

            file.write(f"{line.strip()};{zarobki}\n")
        file.truncate()

    with open("pracownicy.txt", "r") as file:
        for line in file:
            data = line.strip().split(";")
            pracownik = Pracownik(data[0], data[1], data[2], data[3], data[4])
            print(pracownik)

except FileNotFoundError:
    print("Nie znaleziono pliku")
except ValueError as e:
    print(e)
except Exception as e:
    print("Wystąpił błąd:", e)
