# =============================================================================
# Zadanie 1 – Drzewo Binarne Poszukiwań (Binary Search Tree - BST)
# =============================================================================
# OPIS PROBLEMU:
#   Budujesz system wyszukiwania produktów po ich numerze ID.
#   W zwykłej liście szukanie zajmuje O(n). W BST, dzięki strukturze,
#   w której mniejsze wartości są po lewej, a większe po prawej,
#   skracamy czas szukania do O(log n).
#
#   Twoim zadaniem jest:
#     1. Implementacja wstawiania nowego produktu do drzewa (zachowując porządek).
#     2. Implementacja wyszukiwania produktu po ID.
#     3. Wyświetlenie wszystkich produktów w kolejności rosnącej (In-order).
#
# METODY / WŁAŚCIWOŚCI do poznania:
#   - Lewe dziecko (left):   wartości < rodzic
#   - Prawe dziecko (right): wartości > rodzic
#   - Rekurencja:            metoda wywołuje samą siebie dla poddrzewa.
# =============================================================================

class ProduktNode:
    def __init__(self, id_produktu: int, nazwa: str):
        self.id = id_produktu
        self.nazwa = nazwa
        self.lewo = None
        self.prawo = None


# ============================================================
# FUNKCJA 1 – Wstawianie do drzewa
# ============================================================
def wstaw(korzen: ProduktNode, nowy_wezel: ProduktNode) -> ProduktNode:
    """
    Wstawia nowy_wezel do drzewa BST zgodnie z zasadą:
    mniejsze ID na lewo, większe ID na prawo.
    """
    if korzen is None:
        return nowy_wezel

    # TODO: Porównaj id nowego węzła z id korzenia:
    #   1. Jeśli nowy.id < korzen.id -> idź do lewego poddrzewa (rekurencja).
    #   2. Jeśli nowy.id > korzen.id -> idź do prawego poddrzewa.
    # Wskazówka: korzen.lewo = wstaw(korzen.lewo, nowy_wezel)
    pass
    return korzen


# ============================================================
# FUNKCJA 2 – Wyszukiwanie w drzewie
# ============================================================
def szukaj(korzen: ProduktNode, szukane_id: int) -> str:
    """
    Przeszukuje drzewo w poszukiwaniu produktu o danym ID.
    Zwraca nazwę produktu lub informację o braku.
    """
    # TODO:
    #   1. Jeśli korzen jest None -> zwróć "Nie znaleziono".
    #   2. Jeśli szukane_id == korzen.id -> zwróć korzen.nazwa.
    #   3. Jeśli szukane_id < korzen.id -> szukaj w lewym poddrzewie.
    #   4. W przeciwnym razie -> szukaj w prawym poddrzewie.
    pass


# ============================================================
# FUNKCJA 3 – Wyświetlanie (In-order Traversal)
# ============================================================
def wyswietl_katalog(korzen: ProduktNode):
    """
    Wypisuje katalog produktów posortowany po ID (rosnąco).
    """
    if korzen:
        # TODO: Zastosuj rekurencję In-order:
        #   1. Odwiedź lewe poddrzewo.
        #   2. Wypisz aktualny węzeł: print(f"[{korzen.id}] {korzen.nazwa}")
        #   3. Odwiedź prawe poddrzewo.
        pass


# =============================================================================
# Demonstracja działania
# =============================================================================
if __name__ == "__main__":
    print("=== Katalog Produktów (BST) ===\n")

    # Tworzymy korzeń (środek zakresu, żeby drzewo było w miarę zbalansowane)
    katalog = ProduktNode(50, "Laptop Gamingowy")

    # Dodajemy produkty
    produkty_do_dodania = [
        (20, "Myszka bezprzewodowa"),
        (70, "Monitor 4K"),
        (10, "Klawiatura mechaniczna"),
        (30, "Słuchawki ANC"),
        (60, "Kabel HDMI"),
        (80, "Podkładka pod mysz")
    ]

    for id_p, nazwa in produkty_do_dodania:
        wstaw(katalog, ProduktNode(id_p, nazwa))

    print("-- Pełny katalog (posortowany po ID) --")
    wyswietl_katalog(katalog)

    print("\n-- Wyszukiwanie produktów --")
    print(f"Szukam ID 30: {szukaj(katalog, 30)}")
    print(f"Szukam ID 99: {szukaj(katalog, 99)}")