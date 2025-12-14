import sys

#generator czyta linie z pliku
def czytaj_linie(nazwa_pliku):
    with open(nazwa_pliku, 'r', encoding='utf-8') as f:
        for linia in f:
            yield linia.strip()

#generator filtruje linie według poziomu logowania
def filtruj_logi(gen, poziom):
    for linia in gen:
        if poziom in linia:
            yield linia

#generator zlicza statystyki poziomów logów
def licz_statystyki(gen):
    stat = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for linia in gen:
        for klucz in stat:
            if klucz in linia:
                stat[klucz] += 1
        yield stat  #zwraca statystyki po każdej linii

#przykład użycia
if __name__ == "__main__":
    #porównanie zużycia pamięci - zależne od pliku dla listy, stałe dla generatora
    linie = [linia.strip() for linia in open("log.txt", encoding="utf-8")]
    print("Lista:", sys.getsizeof(linie))

    gen = czytaj_linie("log.txt")
    print("Generator:", sys.getsizeof(gen))

    #filtrowanie logów
    print("\n🔴 Linie z poziomem ERROR:")
    for linia in filtruj_logi(czytaj_linie("log.txt"), "ERROR"):
        print(linia)

    #liczenie statystyk
    print("\n📈 Statystyki logów:")
    stat_gen = licz_statystyki(czytaj_linie("log.txt"))
    for stat in stat_gen:
        pass
    print(stat)