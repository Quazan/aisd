# =============================================================================
# Benchmark – list vs collections.deque
# =============================================================================
# Porównanie wydajności wbudowanej listy (list) i kolejki dwustronnej (deque)
# przy operacjach na POCZĄTKU oraz na KOŃCU struktury.
#
# Dlaczego różnica?
#   - list.insert(0, x) / list.pop(0) – O(n): cała zawartość musi być
#     przesunięta w pamięci przy każdej operacji na początku.
#   - deque.appendleft(x) / deque.popleft() – O(1): deque jest zoptymalizowana
#     do operacji na obu końcach dzięki strukturze blokowej (doubly-linked
#     list of fixed-size blocks).
# =============================================================================

import timeit
from collections import deque

N = 100_000   # liczba elementów używanych w każdym teście
POWT = 5      # liczba powtórzeń pomiaru (timeit wybierze najlepszy)

# =============================================================================
# 1. Dodawanie N elementów na POCZĄTEK struktury
# =============================================================================

czas_list_insert = timeit.timeit(
    stmt="for i in range(N): lst.insert(0, i)",
    setup="lst = []; N = " + str(N),
    number=POWT,
)

czas_deque_appendleft = timeit.timeit(
    stmt="for i in range(N): d.appendleft(i)",
    setup="from collections import deque; d = deque(); N = " + str(N),
    number=POWT,
)

# =============================================================================
# 2. Usuwanie N elementów z POCZĄTKU struktury
# =============================================================================

czas_list_pop0 = timeit.timeit(
    stmt="while lst: lst.pop(0)",
    setup=f"lst = list(range({N}))",
    number=POWT,
)

czas_deque_popleft = timeit.timeit(
    stmt="while d: d.popleft()",
    setup=f"from collections import deque; d = deque(range({N}))",
    number=POWT,
)

# =============================================================================
# 3. Dodawanie N elementów na KONIEC struktury (dla porównania – obie O(1))
# =============================================================================

czas_list_append = timeit.timeit(
    stmt="for i in range(N): lst.append(i)",
    setup="lst = []; N = " + str(N),
    number=POWT,
)

czas_deque_append = timeit.timeit(
    stmt="for i in range(N): d.append(i)",
    setup="from collections import deque; d = deque(); N = " + str(N),
    number=POWT,
)

# =============================================================================
# Wyniki
# =============================================================================

SEP = "=" * 60
COL = 32  # szerokość etykiety

def fmt(label: str, seconds: float) -> str:
    avg_ms = (seconds / POWT) * 1000
    return f"  {label:<{COL}} {avg_ms:>10.2f} ms  (avg z {POWT} powtórzeń)"

def speedup(slow: float, fast: float) -> str:
    return f"  → deque jest {slow / fast:.1f}x szybsze\n"

if __name__ == "__main__":
    print(SEP)
    print(f"  Benchmark: list vs deque  (N = {N:,})")
    print(SEP)

    print("\n[1] Dodawanie na POCZĄTEK (insert/appendleft)")
    print(fmt("list.insert(0, x)  × N:", czas_list_insert))
    print(fmt("deque.appendleft(x) × N:", czas_deque_appendleft))
    print(speedup(czas_list_insert, czas_deque_appendleft))

    print("[2] Usuwanie z POCZĄTKU (pop(0) / popleft)")
    print(fmt("list.pop(0) × N:", czas_list_pop0))
    print(fmt("deque.popleft() × N:", czas_deque_popleft))
    print(speedup(czas_list_pop0, czas_deque_popleft))

    print("[3] Dodawanie na KONIEC (append) – obie struktury O(1)")
    print(fmt("list.append(x) × N:", czas_list_append))
    print(fmt("deque.append(x) × N:", czas_deque_append))
    print(f"  → wyniki porównywalne (obie O(1) amortyzowane)\n")

    print(SEP)
    print("  Wniosek:")
    print("  Użyj deque zamiast list wszędzie tam, gdzie potrzebujesz")
    print("  wydajnych operacji na POCZĄTKU struktury (kolejka, stos LIFO")
    print("  dwukierunkowy, historia przeglądarki itp.).")
    print(SEP)

