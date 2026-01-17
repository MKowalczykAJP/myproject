from shop.models.product import Product
from shop.logic.cart import Cart

def main():
    print("*** Generowanie asortymentu ***")
    p1 = Product("Laptop", 4500.00, "Elektronika")
    p2 = Product("Myszka", 220.00, "Elektronika")
    p3 = Product("Jabłko", 1.25, "Jedzenie")
    p4 = Product("Chleb", 3.00, "Jedzenie")

    print(f"Utworzono produkty:")
    print(f"{p1}")
    print(f"{p2}")
    print(f"{p3}")
    print(f"{p4}")

    print("\n*** Testowanie operatorów *** ")
    print(f"Czy {p1.name} == {p2.name}? {p1 == p2}")
    print(f"Czy cena {p2.name} < cena {p1.name}? {p2 < p1}") 
    print(f"Czy {p1.name} == {p1.name}? {p1 == p1}") 
    print(f"Czy cena {p4.name} < cena {p3.name}? {p4 < p3}") 
    
    products_list = [p1, p2, p3, p4]
    print(f"\nProdukty nieposortowane: {[p.name for p in products_list]}")
    products_list.sort()
    print(f"Produkty posortowane: {[p.name for p in products_list]}")
    
    print(f"\nDługość nazwy produktu '{p1.name}': {len(p1)}")

    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p3)
    
    print(f"\nLiczba produktów w koszyku: {len(cart)}")
    print(f"Czy {p2.name} jest w koszyku? {p2 in cart}")
    print(f"Czy {p4.name} jest w koszyku? {p4 in cart}")
    
    print("\n*** Zawartość koszyka ***")
    print(cart)
    
    print("\n*** Usuwanie produktu z koszyka ***")
    cart.remove_product(p2)
    print(f"Usunięto {p2.name}. Obecna liczba produktów w koszyku: {len(cart)}")
    print(cart)

if __name__ == "__main__":
    main()
