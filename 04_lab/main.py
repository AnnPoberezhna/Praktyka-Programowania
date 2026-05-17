from abc import ABC, abstractmethod
# KROK 2
class Zadanie:
    def __init__(self, typ, dane):
        self.typ = typ
        self.dane = dane

# KROK 1 i 3: Bazowa klasa
class ObiektObslugujacy(ABC):
    def __init__(self):
        self._nastepny = None

    def ustaw_nastepnego(self, nastepny_obiekt):
        self._nastepny = nastepny_obiekt
        return nastepny_obiekt 

    @abstractmethod
    def obsluz(self, zadanie):
    # Domyślne przekierowanie, jeśli obiekt sam nie obsłuży żądania (Krok 3)
        if self._nastepny:
            return self._nastepny.obsluz(zadanie)
        
        print("Koniec łańcucha: Żądanie nie zostało obsłużone przez żadne ogniwo.")
        return None

# KROK 4
class UwierzytelnienieHandler(ObiektObslugujacy):
    def obsluz(self, zadanie):
        print("1. Sprawdzam uwierzytelnienie...")
        if zadanie.dane.get("zalogowany") == True:
            print(" -> Uwierzytelnienie pomyślne. Przekazuję dalej.")
            return super().obsluz(zadanie)
        else:
            print("Błąd: Użytkownik niezalogowany! Przerywam łańcuch.")
            return "Odrzucono"

class WalidacjaHandler(ObiektObslugujacy):
    def obsluz(self, zadanie):
        print("2. Sprawdzam walidację danych...")
        if zadanie.dane.get("koszyk_pusty") == False:
            print(" -> Dane poprawne (koszyk nie jest pusty). Przekazuję dalej.")
            return super().obsluz(zadanie)
        else:
            print("Błąd: Koszyk jest pusty! Przerywam łańcuch.")
            return "Odrzucono"


# KROK 5
if __name__ == "__main__":

    uwierzytelnienie = UwierzytelnienieHandler()
    walidacja = WalidacjaHandler()

    # Budowanie łańcucha: Uwierzytelnienie -> Walidacja
    uwierzytelnienie.ustaw_nastepnego(walidacja)

    poprawne_zadanie = Zadanie("zamowienie", {"zalogowany": True, "koszyk_pusty": False})
    brak_logowania = Zadanie("zamowienie", {"zalogowany": False, "koszyk_pusty": False})
    pusty_koszyk = Zadanie("zamowienie", {"zalogowany": True, "koszyk_pusty": True})

    print("--- SCENARIUSZ 1: Wszystko poprawne ---")
    uwierzytelnienie.obsluz(poprawne_zadanie)

    print("\n--- SCENARIUSZ 2: Użytkownik niezalogowany ---")
    uwierzytelnienie.obsluz(brak_logowania)

    print("\n--- SCENARIUSZ 3: Pusty koszyk (Przejdzie logowanie, padnie na walidacji) ---")
    uwierzytelnienie.obsluz(pusty_koszyk)