import statistics

def analize_numbers():
    while True:
        data = input("Podaj liczby całkowite oddzielone spacją: ")
        if not data:
            print("Nie wprowadzono żadnych danych.")
            continue
        try:
            numbers = [int(x) for x in data.strip().split()]
        except ValueError:
            print("Podaj liczby całkowite oddzielone spacją!")
            continue
        length = len(numbers)
        total = sum(numbers)
        average = total/length
        positiveNumbers = len([x for x in numbers if x > 0])
        negativeNumbers = len([x for x in numbers if x < 0])
        zeros = numbers.count(0)
        maximum = max(numbers)
        minimum = min(numbers)
        reversedOrder = list(reversed(numbers))
        variance = statistics.variance(numbers) if len(numbers) > 1 else 0
        deviation = statistics.stdev(numbers) if len(numbers) > 1 else 0

        print("\nWyniki analizy:\n")
        print(f"Liczba wszystkich wartości: {length}\n")
        print(f"Suma liczb: {total}\n")
        print(f"Średnia: {average}\n")
        print(f"Liczba dodatnich liczb: {positiveNumbers}\n")
        print(f"Liczba negatywnych liczb: {negativeNumbers}\n")
        print(f"Liczba zer: {zeros}\n")
        print(f"Wariancja: {variance}\n")
        print(f"Odchylenie standardowe: {deviation}\n")
        print(f"Największa wartość: {maximum}\n")
        print(f"Najmniejsza wartość: {minimum}\n")
        print(f"Liczby w odwrotnej kolejności: {reversedOrder}\n")
        saveAsFile = input("\nCzy chcesz zapisać wyniki do pliku? (t/n): ").lower()
        if saveAsFile == 't':
            with open("wyniki_analizy.txt", "w", encoding="utf-8") as file:
                file.write("Wyniki analizy:\n")
                file.write(f"Liczba wszystkich wartości: {length}\n")
                file.write(f"Suma liczb: {total}\n")
                file.write(f"Średnia: {average}\n")
                file.write(f"Liczba dodatnich liczb: {positiveNumbers}\n")
                file.write(f"Liczba ujemnych liczb: {negativeNumbers}\n")
                file.write(f"Liczba zer: {zeros}\n")
                file.write(f"Wariancja: {variance}\n")
                file.write(f"Odchylenie standardowe: {deviation}\n")
                file.write(f"Największa wartość: {maximum}\n")
                file.write(f"Najmniejsza wartość: {minimum}\n")
                file.write(f"Liczby w odwrotnej kolejności: {reversedOrder}\n")
            print("Wyniki zapisano do pliku o nazwie 'wyniki_analizy.txt'")
        restart = input("\nCzy chcesz przeprowadzić kolejną analizę? (t/n): ").lower()
        if restart != 't':
            print("Zakończono działanie programu!")
            break

analize_numbers()