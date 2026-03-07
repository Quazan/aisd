import heapq

# Nasza kolejka zgłoszeń (priorytet, opis)
# W heapq mniejsza liczba = wyższy priorytet (Min-Heap)
bilety = []

if __name__ == "__main__":
    # Dodajemy zgłoszenia z różnymi priorytetami
    heapq.heappush(bilety, (3, "Błąd w stopce"))
    heapq.heappush(bilety, (1, "AWARIA SERWERA"))
    heapq.heappush(bilety, (2, "Klient VIP nie może się zalogować"))

    # Pobieramy najważniejsze zadanie
    priorytet, zadanie = heapq.heappop(bilety)
    print(f"Robimy teraz: {zadanie}")  # Wypisze AWARIA SERWERA
