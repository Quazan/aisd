import random
import time

# =============================================================================
#  METODY POMOCNICZE
# =============================================================================

def generate_random_array(size: int, min_val: int, max_val: int) -> list[int]:
    """
    Generuje listę size losowych liczb całkowitych z zakresu [min_val, max_val].
    Obsługuje ujemne wartości min_val bez ryzyka overflow.
    """
    return [random.randint(min_val, max_val) for _ in range(size)]


def print_array(array: list[int]) -> None:
    """Wypisuje zawartość listy w czytelnym formacie, np.: [ 3, 7, 1, 9, 4 ]"""
    print("[ " + ", ".join(str(x) for x in array) + " ]")


def is_sorted(array: list[int]) -> bool:
    """
    Sprawdza, czy lista jest posortowana niemalejąco (rosnąco).
    Przydatne do autoweryfikacji poprawności implementacji.
    """
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))


def swap(array: list[int], i: int, j: int) -> None:
    """Zamienia miejscami dwa elementy listy o indeksach i i j."""
    array[i], array[j] = array[j], array[i]


# =============================================================================
#  ALGORYTMY SORTOWANIA
# =============================================================================

def bubble_sort(array: list[int]) -> None:
    """
    Sortowanie bąbelkowe (Bubble Sort).

    Intuicja: Przechodzimy przez listę wielokrotnie. W każdym przejściu
    porównujemy sąsiednie pary elementów i zamieniamy je, jeśli są w złej
    kolejności. Największy element „wypływa" na koniec jak bąbelek powietrza
    w wodzie. Po każdym pełnym przejściu jeden element więcej jest na swoim
    miejscu, więc skracamy obszar porównań.

    Złożoność czasowa: O(n²) – przeciętny i pesymistyczny przypadek.
    Złożoność pamięciowa: O(1) – sortowanie w miejscu.
    """
    # TODO: Twoja implementacja
    pass


def selection_sort(array: list[int]) -> None:
    """
    Sortowanie przez wybieranie (Selection Sort).

    Intuicja: Dzielimy listę na część posortowaną (lewa) i nieposortowaną
    (prawa). W każdym kroku znajdujemy NAJMNIEJSZY element w części
    nieposortowanej i przenosimy go na koniec części posortowanej.
    Działamy jak przy układaniu kart – za każdym razem wybieramy najniższą.

    Złożoność czasowa: O(n²) – zawsze (niezależnie od danych wejściowych).
    Złożoność pamięciowa: O(1) – sortowanie w miejscu.
    """
    # TODO: Twoja implementacja
    pass


def insertion_sort(array: list[int]) -> None:
    """
    Sortowanie przez wstawianie (Insertion Sort).

    Intuicja: Podobnie jak przy układaniu kart w ręce – bierzemy kolejny
    element i „wsuwamy" go na właściwe miejsce wśród już posortowanych
    elementów po lewej stronie. Przesuwamy większe elementy w prawo, robiąc
    miejsce dla wstawianego elementu.

    Złożoność czasowa: O(n²) pesymistycznie, O(n) dla listy prawie posortowanej.
    Złożoność pamięciowa: O(1) – sortowanie w miejscu.
    """
    # TODO: Twoja implementacja
    pass


def _merge(array: list[int], left: int, mid: int, right: int) -> None:
    """
    Pomocnicza funkcja scalająca dwa posortowane podciągi array[left..mid]
    i array[mid+1..right] w jeden posortowany ciąg.

    Intuicja: Tworzymy tymczasową listę, do której kopiujemy elementy z obu
    podciągów, porównując je i wybierając mniejszy. Po scaleniu kopiujemy
    wynik z powrotem do oryginalnej listy.

    Złożoność czasowa: O(n) – gdzie n to liczba elementów w obu podciągach.
    Złożoność pamięciowa: O(n) – wymaga dodatkowej listy pomocniczej.
    """
    # TODO: Twoja implementacja
    pass

def _merge_sort(array: list[int], left: int, right: int) -> None:
    """
    Sortowanie przez scalanie (Merge Sort).

    Intuicja: Strategia „dziel i zwyciężaj". Dzielimy listę na dwie
    równe połowy, rekurencyjnie sortujemy każdą z nich, a następnie
    SCALAMY dwie posortowane połowy w jedną posortowaną listę.
    Scalanie polega na porównywaniu „czołowych" elementów obu połów
    i wybieraniu mniejszego.

    Złożoność czasowa: O(n log n) – zawsze.
    Złożoność pamięciowa: O(n) – wymaga dodatkowej listy pomocniczej.

    Wskazówka: Napisz pomocniczą funkcję merge(array, left, mid, right),
    która scala dwa podciągi.
    """
    # TODO: Twoja implementacja
    pass


def merge_sort(array: list[int]) -> None:
    """
    Interfejsowa funkcja sortowania przez scalanie (Merge Sort).
    Wywołuje funkcję _merge_sort z odpowiednimi parametrami początkowymi
    """
    _merge_sort(array, 0, len(array) - 1)

def _partition(array: list[int], low: int, high: int) -> int:
    """
    Schemat Lomuto – wyznacza indeks pivota po podziale.

    Pivot to ostatni element podciągu (array[high]).
    i to granica „strefy elementów <= pivot".
    Dla każdego j od low do high-1: jeśli array[j] <= pivot,
    poszerzamy strefę (i++) i zamieniamy array[i] z array[j].
    Na końcu wstawiamy pivot na pozycję i+1.
    """
    # TODO: Twoja implementacja
    return low


def _quick_sort(array: list[int], low: int, high: int) -> None:
    """
    Sortowanie szybkie (Quick Sort).

    Intuicja: Strategia „dziel i zwyciężaj". Wybieramy element zwany
    PIWOTEM (ang. pivot). Przestawiamy elementy listy tak, aby po lewej
    pivota znalazły się elementy mniejsze lub równe, a po prawej – większe.
    Następnie rekurencyjnie sortujemy obie części. Wybór dobrego pivota
    ma kluczowy wpływ na wydajność.

    Złożoność czasowa: O(n log n) przeciętnie, O(n²) pesymistycznie
    (gdy pivot jest zawsze min/max – np. dla posortowanej listy).
    Złożoność pamięciowa: O(log n) – stos rekurencji.
    """
    # TODO: Twoja implementacja
    pass

def quick_sort(array: list[int]) -> None:
    """
    Interfejsowa funkcja sortowania szybkiego (Quick Sort).
    Wywołuje funkcję _quick_sort z odpowiednimi parametrami początkowymi
    """
    _quick_sort(array, 0, len(array) - 1)


# =============================================================================
#  ALGORYTMY WYSZUKIWANIA
# =============================================================================

def linear_search(array: list[int], target: int) -> int:
    """
    Wyszukiwanie liniowe (Linear Search).

    Intuicja: Przeglądamy listę element po elemencie od lewej do prawej,
    aż znajdziemy szukaną wartość lub dojdziemy do końca. Działa na listach
    NIEPOSORTOWANYCH i posortowanych.

    Złożoność czasowa: O(n).
    Złożoność pamięciowa: O(1).

    Zwraca indeks pierwszego wystąpienia target lub -1 jeśli nie istnieje.
    """
    # TODO: Twoja implementacja
    return -1


def binary_search(array: list[int], target: int) -> int:
    """
    Wyszukiwanie binarne (Binary Search).

    Intuicja: Działa WYŁĄCZNIE na posortowanych listach. Sprawdzamy
    środkowy element: jeśli to szukana wartość – sukces! Jeśli szukana
    wartość jest mniejsza – szukamy w lewej połowie; jeśli większa –
    w prawej połowie. Za każdym krokiem eliminujemy połowę kandydatów.

    Złożoność czasowa: O(log n).
    Złożoność pamięciowa: O(1) – wersja iteracyjna.

    Zwraca indeks elementu target lub -1 jeśli nie istnieje.
    """
    # TODO: Twoja implementacja
    return -1


# =============================================================================
#  SCENARIUSZ TESTOWY
# =============================================================================

if __name__ == "__main__":

    # --- Konfiguracja testu ---
    SIZE = 25    # liczba elementów listy
    MIN  = 0     # minimalna wartość elementu
    MAX  = 100   # maksymalna wartość elementu

    print("=== Laboratorium: Algorytmy i Struktury Danych ===\n")

    # 1. Generowanie losowej listy
    array = generate_random_array(SIZE, MIN, MAX)
    target = array[SIZE // 2]  # wybieramy element ze środka jako cel wyszukiwania

    # 2. Wyświetlenie listy przed sortowaniem
    print("Lista przed sortowaniem: ", end="")
    print_array(array)

    # 3. Pomiar czasu sortowania
    #    Zamień wywołanie poniżej na funkcję, którą chcesz przetestować,
    #    np. selection_sort(array), insertion_sort(array) itp.
    #    Dla merge_sort użyj:  merge_sort(array, 0, len(array) - 1)
    #    Dla quick_sort użyj:  quick_sort(array, 0, len(array) - 1)
    start_time = time.perf_counter_ns()

    bubble_sort(array)  # <-- ZMIEŃ NA WYBRANĄ FUNKCJĘ

    end_time = time.perf_counter_ns()
    elapsed  = end_time - start_time

    # 4. Wyświetlenie listy po sortowaniu
    print("Lista po sortowaniu:     ", end="")
    print_array(array)

    # 5. Weryfikacja poprawności sortowania
    if is_sorted(array):
        print("\n✔ Sortowanie zakończone sukcesem!")
    else:
        print("\n✘ Błąd: lista NIE jest posortowana. Sprawdź implementację.")

    print(f"Czas wykonania: {elapsed} ns")

    # --- Przykładowy test wyszukiwania liniowego ---
    print("\n--- Test wyszukiwania liniowego ---")
    linear_index = linear_search(array, target)
    if linear_index != -1:
        print(f"Znaleziono wartość {target} pod indeksem: {linear_index}")
    else:
        print(f"Wartość {target} nie została znaleziona (sprawdź implementację linear_search).")

    # --- Przykładowy test wyszukiwania binarnego ---
    print("\n--- Test wyszukiwania binarnego ---")
    start_search = time.perf_counter_ns()
    index = binary_search(array, target)
    end_search = time.perf_counter_ns()
    search_elapsed = end_search - start_search

    if index != -1:
        print(f"Znaleziono wartość {target} pod indeksem: {index}")
    else:
        print(f"Wartość {target} nie została znaleziona (sprawdź implementację binary_search).")

    print(f"Czas wyszukiwania: {search_elapsed} ns")

