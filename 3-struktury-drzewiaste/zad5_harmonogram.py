# =============================================================================
# Zadanie 5 – Harmonogram Sprintu (heapify, nsmallest, nlargest)
# =============================================================================
# OPIS PROBLEMU:
#   Jesteś project managerem w zespole scrumowym. Masz listę zadań w backlogu –
#   każde zadanie ma przypisaną liczbę dni pozostałych do deadline'u.
#   Musisz szybko odpowiadać na pytania:
#     - "Które 3 zadania są NAJPILNIEJSZE?" (najmniej dni do deadline'u)
#     - "Które 3 zadania mam najwięcej czasu na zrobienie?"
#
#   Moglibyśmy sortować listę za każdym razem – ale to O(n log n).
#   heapq.heapify() przekształca istniejącą listę w kopiec w O(n),
#   a nsmallest/nlargest dają nam top-K elementów bez pełnego sortowania.
#
#   Twoim zadaniem jest:
#     1. Zamiana listy zadań w kopiec (heapify).
#     2. Znalezienie N najpilniejszych zadań (nsmallest).
#     3. Znalezienie N zadań z największym zapasem czasu (nlargest).
#     4. Dodanie nowego zadania do istniejącego harmonogramu (heappush).
#
# METODY / OPERACJE do poznania:
#   - Zamień listę w kopiec:   heapq.heapify(lista)            – O(n), IN-PLACE
#   - N najmniejszych:         heapq.nsmallest(n, iterable)    – O(n log k)
#   - N największych:          heapq.nlargest(n, iterable)     – O(n log k)
#   - Dodaj do kopca:          heapq.heappush(kopiec, element) – O(log n)
#   - Klucz sortowania:        nsmallest(n, lista, key=lambda x: x[0])
#
# WAŻNE:
#   heapify() modyfikuje listę IN-PLACE – nie zwraca nowej listy!
#   Po heapify() lista NIE wygląda jak posortowana, ale lista[0] to minimum.
# =============================================================================

import heapq

# Typ reprezentujący zadanie: (dni_do_deadline: int, nazwa: str, priorytet_biznesowy: str)
Zadanie = tuple[int, str, str]


# ============================================================
# FUNKCJA 1 – Utwórz harmonogram (heapify)
# ============================================================
def utworz_harmonogram(zadania: list[Zadanie]) -> list[Zadanie]:
    """
    Przekształca podaną listę zadań w kopiec (min-heap po dniach do deadline'u).
    Zwraca tę samą listę (już jako kopiec) – heapify działa in-place.

    Intuicja: heapify() przestawia elementy listy tak, żeby spełniały własność
    kopca – bez pełnego sortowania. Efekt: lista[0] to zadanie z najkrótszym
    deadline'em, ale reszta NIE jest posortowana.

    Złożoność czasowa:  O(n) – szybciej niż sortowanie O(n log n)!
    Złożoność pamięciowa: O(1) – modyfikacja in-place
    """
    # TODO:
    #   1. Wywołaj heapq.heapify(zadania) – przekształca listę in-place.
    #   2. Wypisz komunikat, np.:
    #      f"Harmonogram gotowy. Liczba zadań: {len(zadania)}"
    #      f"Najbliższy deadline: {zadania[0][1]} (za {zadania[0][0]} dni)"
    #   3. Zwróć `zadania`.
    pass


# ============================================================
# FUNKCJA 2 – Znajdź N najpilniejszych zadań
# ============================================================
def najpilniejsze(harmonogram: list[Zadanie], n: int) -> list[Zadanie]:
    """
    Zwraca listę n zadań z NAJMNIEJSZĄ liczbą dni do deadline'u.

    Intuicja: nsmallest() nie niszczy harmonogramu – zwraca nową listę
    n elementów posortowanych rosnąco. Idealny do codziennego stand-upu:
    "Co robimy w tym tygodniu?"

    Złożoność czasowa:  O(n log k), gdzie k = n (żądana liczba wyników)
    Złożoność pamięciowa: O(k) – tylko k elementów w wyniku
    """
    # TODO:
    #   1. Użyj heapq.nsmallest(n, harmonogram), aby pobrać n elementów
    #      z najmniejszą wartością pierwszego pola krotki (dni_do_deadline).
    #   2. Zapisz wynik do zmiennej, np.: pilne = heapq.nsmallest(n, harmonogram)
    #   3. Wypisz nagłówek: f"--- Top {n} najpilniejszych zadań ---"
    #   4. Iteruj po wyniku i wypisuj:
    #      f"  [{dni}d] {nazwa} ({priorytet})"
    #      (rozpakuj krotkę: dni, nazwa, priorytet = zadanie)
    #   5. Zwróć listę wynikową.
    pass


# ============================================================
# FUNKCJA 3 – Znajdź N zadań z największym zapasem
# ============================================================
def najluzniejsze(harmonogram: list[Zadanie], n: int) -> list[Zadanie]:
    """
    Zwraca listę n zadań z NAJWIĘKSZĄ liczbą dni do deadline'u.
    Przydatne gdy szukamy zadań do "odkładania na później".

    Intuicja: nlargest() to odwrotność nsmallest() – wyciąga maksima.
    Używamy jej, gdy interesuje nas "ogon" rozkładu, nie szczyt.

    Złożoność czasowa:  O(n log k)
    Złożoność pamięciowa: O(k)
    """
    # TODO:
    #   1. Użyj heapq.nlargest(n, harmonogram), aby pobrać n zadań
    #      z największą wartością pierwszego pola (dni_do_deadline).
    #   2. Zapisz wynik i wypisz nagłówek: f"--- Top {n} zadań z zapasem czasu ---"
    #   3. Iteruj i wypisuj (tak samo jak w `najpilniejsze`).
    #   4. Zwróć listę wynikową.
    pass


# ============================================================
# FUNKCJA 4 – Dodaj nowe zadanie do harmonogramu
# ============================================================
def dodaj_zadanie(harmonogram: list[Zadanie], dni: int, nazwa: str, priorytet_biz: str) -> None:
    """
    Dodaje nowe zadanie do istniejącego harmonogramu (kopca).

    Intuicja: Po heapify() lista jest kopcem – możemy spokojnie używać
    heappush(), żeby dodawać nowe elementy. Kopiec sam zadba o porządek.
    NIE wolno używać zwykłego list.append() – zniszczyłoby własność kopca!

    Złożoność czasowa:  O(log n)
    Złożoność pamięciowa: O(1)
    """
    # TODO:
    #   1. Utwórz krotkę: zadanie = (dni, nazwa, priorytet_biz)
    #   2. Wywołaj heapq.heappush(harmonogram, zadanie).
    #   3. Wypisz: f"[+] Dodano: {nazwa} (deadline za {dni} dni, {priorytet_biz})"
    pass


# =============================================================================
# FUNKCJE POMOCNICZE (dostarczone – nie musisz ich zmieniać)
# =============================================================================
def _separator(tytul: str) -> None:
    print(f"\n{'=' * 55}")
    print(f"  {tytul}")
    print('=' * 55)


def _wyswietl_wszystkie(harmonogram: list[Zadanie]) -> None:
    """Wypisuje wszystkie zadania posortowane wg deadline'u (nie niszczy kopca)."""
    if not harmonogram:
        print("  Harmonogram jest pusty.")
        return
    for dni, nazwa, priorytet in sorted(harmonogram):
        pasek = "█" * min(dni, 30) + "░" * (30 - min(dni, 30))
        print(f"  [{dni:>3}d] {pasek} {nazwa} ({priorytet})")


# =============================================================================
# Demonstracja działania – uruchom plik, aby sprawdzić swoje rozwiązanie
# =============================================================================
if __name__ == "__main__":
    print("=== Harmonogram Sprintu – heapify / nsmallest / nlargest ===\n")

    # Backlog zadań: (dni_do_deadline, nazwa, priorytet_biznesowy)
    backlog: list[Zadanie] = [
        (14, "Migracja bazy danych do PostgreSQL",    "WYSOKI"),
        (3,  "Hotfix: błąd w module płatności",       "KRYTYCZNY"),
        (30, "Refaktoryzacja modułu raportów",        "NISKI"),
        (7,  "Integracja z API kuriera",              "WYSOKI"),
        (21, "Dokumentacja REST API",                 "SREDNI"),
        (2,  "Naprawa błędu logowania OAuth",         "KRYTYCZNY"),
        (45, "Migracja na Python 3.13",               "NISKI"),
        (10, "Testy wydajnościowe load balancera",    "WYSOKI"),
    ]

    # --- Krok 1: Zamień backlog w kopiec ---
    _separator("Tworzenie harmonogramu (heapify)")
    harmonogram = utworz_harmonogram(backlog)

    # --- Krok 2: Podgląd całego harmonogramu ---
    _separator("Pełny harmonogram (posortowany wg deadline'u)")
    _wyswietl_wszystkie(harmonogram)

    # --- Krok 3: Co robimy w tym tygodniu? ---
    _separator("Top 3 najpilniejsze zadania (stand-up)")
    najpilniejsze(harmonogram, 3)

    # --- Krok 4: Co możemy odłożyć? ---
    _separator("Top 3 zadania z największym zapasem")
    najluzniejsze(harmonogram, 3)

    # --- Krok 5: Nowe zgłoszenie z zewnątrz ---
    _separator("Nowe zadanie wpada w trakcie sprintu")
    dodaj_zadanie(harmonogram, 1, "PRODUKCJA: błąd 500 na stronie głównej", "KRYTYCZNY")
    dodaj_zadanie(harmonogram, 60, "Aktualizacja polityki cookies", "NISKI")

    # --- Krok 6: Aktualne top 3 po zmianach ---
    _separator("Top 3 najpilniejsze po aktualizacji")
    najpilniejsze(harmonogram, 3)

    _separator("Pełny harmonogram po aktualizacji")
    _wyswietl_wszystkie(harmonogram)
