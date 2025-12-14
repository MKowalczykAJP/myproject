import math
import sys

def pobierz_dane(prompt, jednostka):
    while True:
        try:
            wejscie = input(f"Podaj {prompt} w {jednostka} (lub wpisz 'q' aby zakończyć): ").strip().lower()
            
            if wejscie == 'q':
                return 'q'
            
            wartosc = float(wejscie)
            
            if wartosc <= 0:
                print("Wprowadzona wartość musi być większa od zera. Spróbuj ponownie.")
                continue
            
            return wartosc
            
        except ValueError:
            print("To nie jest prawidłowa liczba. Użyj cyfr i ewentualnie kropki dla części dziesiętnej.")

def oblicz_bmi(masa_kg, wzrost_cm):
    
    wzrost_m = wzrost_cm / 100
    
    if wzrost_m == 0:
        return None, "Błąd: Wzrost nie może wynosić zero."

    bmi_niezaokraglone = masa_kg / (wzrost_m ** 2)
    bmi_zaokraglone = round(bmi_niezaokraglone, 2)
    
    if bmi_zaokraglone < 18.5:
        interpretacja = "Niedowaga"
    elif 18.5 <= bmi_zaokraglone < 25.0:
        interpretacja = "Waga prawidłowa"
    elif 25.0 <= bmi_zaokraglone < 30.0:
        interpretacja = "Nadwaga"
    else: 
        interpretacja = "Otyłość"
        
    return bmi_zaokraglone, interpretacja

def uruchom_kalkulator_bmi():
    
    print("=========================================")
    print("Kalkulator Wskaźnika Masy Ciała (BMI) ")
    print("=========================================")
    print("Wpisz 'q' w dowolnym momencie, aby zakończyć program.")
    
    osoba = 1
    
    while True:
        print(f"\n--- Dane dla Osoby {osoba} ---")
        
        wzrost_cm = pobierz_dane("wzrost", "cm")
        if wzrost_cm == 'q':
            break
            
        masa_kg = pobierz_dane("masę ciała", "kg")
        if masa_kg == 'q':
            break
            
        bmi, interpretacja = oblicz_bmi(masa_kg, wzrost_cm)
        
        if bmi is None:
            print(interpretacja)
            continue
            
        print("\n--- Wynik ---")
        print(f"Twój BMI wynosi: **{bmi}**")
        print(f"Interpretacja: **{interpretacja}**")
        
        osoba += 1
        
    print("\nProgram zakończony. Dziękujemy za skorzystanie z kalkulatora BMI.")

if __name__ == "__main__":
    uruchom_kalkulator_bmi()