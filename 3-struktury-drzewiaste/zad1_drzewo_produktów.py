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

    Jeśli produkt o takim samym ID już istnieje w drzewie,
    jest ignorowany — nie dodajemy duplikatów.
    """
    if korzen is None:
        return nowy_wezel

    # TODO: Porównaj ID nowego węzła z ID korzenia i rekurencyjnie wstaw go
    #       do odpowiedniego poddrzewa (lewego lub prawego).
    #       Obsłuż też przypadek duplikatu — węzeł z tym samym ID ignorujemy.
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
    # TODO: Rekurencyjnie przeszukuj drzewo — porównuj szukane ID z bieżącym węzłem
    #       i decyduj, w którą stronę iść. Obsłuż przypadek nieznalezienia produktu.
    pass


# ============================================================
# FUNKCJA 3 – Wyświetlanie (In-order Traversal)
# ============================================================
def wyswietl_katalog(korzen: ProduktNode):
    """
    Wypisuje katalog produktów posortowany po ID (rosnąco).
    """
    if korzen:
        # TODO: Zastosuj obchód in-order (lewo → węzeł → prawo),
        #       żeby wypisać produkty posortowane rosnąco po ID.
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

    print("\n-- Test duplikatu --")
    wstaw(katalog, ProduktNode(30, "DUPLIKAT Słuchawek"))
    print(f"Szukam ID 30 po próbie wstawienia duplikatu: {szukaj(katalog, 30)}")
    # Powinno nadal zwrócić "Słuchawki ANC", nie "DUPLIKAT Słuchawek"