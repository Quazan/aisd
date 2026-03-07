# =============================================================================
# Zadanie 3 – Drzewo Trie (Prefix Tree) – Autouzupełnianie
# =============================================================================
# OPIS PROBLEMU:
#   Implementujesz mechanizm podpowiedzi (autocomplete) dla wyszukiwarki
#   produktów. Zwykłe przeszukiwanie listy słów po każdym naciśnięciu klawisza
#   jest zbyt wolne. Drzewo Trie pozwala błyskawicznie sprawdzić, jakie słowa
#   zaczynają się od danego prefiksu.
#
#   Twoim zadaniem jest:
#     1. Implementacja wstawiania słowa do drzewa Trie.
#     2. Sprawdzenie, czy dane słowo istnieje w słowniku.
#     3. (Dla ambitnych) Znalezienie wszystkich słów zaczynających się od prefiksu.
#
# METODY / OPERACJE do poznania:
#   - Dzieci węzła:   Słownik {znak: Node} – kluczem jest litera, wartością kolejny węzeł.
#   - Is_end_of_word: Flaga (boolean) oznaczająca, że w tym miejscu kończy się słowo.
# =============================================================================

class TrieNode:
    def __init__(self):
        # Słownik przechowujący dzieci: {'l': Node, 'a': Node, ...}
        self.dzieci = {}
        # Czy dany węzeł jest ostatnią literą jakiegoś słowa
        self.czy_koniec = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # ============================================================
    # FUNKCJA 1 – Dodawanie słowa
    # ============================================================
    def wstaw(self, slowo: str):
        """Wstawia słowo do drzewa litera po literze."""
        aktualny = self.root
        for litera in slowo:
            # TODO:
            # 1. Jeśli litery nie ma w aktualny.dzieci -> dodaj nowy TrieNode().
            # 2. Przejdź do tego węzła (aktualny = aktualny.dzieci[litera]).
            pass
        # 3. Na samym końcu ustaw aktualny.czy_koniec = True
        pass

    # ============================================================
    # FUNKCJA 2 – Wyszukiwanie całego słowa
    # ============================================================
    def szukaj(self, slowo: str) -> bool:
        """Zwraca True, jeśli słowo znajduje się w Trie."""
        aktualny = self.root
        for litera in slowo:
            # TODO: Jeśli litery nie ma w dzieciach -> zwróć False.
            pass
        # Zwróć wartość aktualny.czy_koniec
        return False

# =============================================================================
# Demonstracja działania
# =============================================================================
if __name__ == "__main__":
    slownik = Trie()
    produkty = ["laptop", "lampa", "lato", "monitor", "myszka"]

    for p in produkty:
        slownik.wstaw(p)

    print("=== System Autouzupełniania Trie ===")
    print(f"Czy jest 'laptop'? {slownik.szukaj('laptop')}")  # Powinno być True
    print(f"Czy jest 'lampa'?  {slownik.szukaj('lampa')}")   # Powinno być True
    print(f"Czy jest 'rower'?  {slownik.szukaj('rower')}")   # Powinno być False