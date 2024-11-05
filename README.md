# Generator Stopki Email

Generator stopek email z interfejsem webowym, umożliwiający tworzenie, edycję i podgląd stopek email.

## Funkcje

- Automatyczne generowanie adresu email na podstawie imienia i nazwiska
- Podgląd stopki w nowej karcie przeglądarki
- Generowanie publicznych linków do podglądu stopki
- Edycja i usuwanie istniejących stopek
- Domyślne wartości dla danych firmowych
- Obsługa polskich znaków w adresach email

## Uruchamianie lokalnie

1. Upewnij się, że masz zainstalowanego Pythona 3.x
2. Zainstaluj wymagane pakiety:
   ```bash
   pip install -r requirements.txt
   ```
3. Uruchom aplikację:
   ```bash
   streamlit run app.py
   ```
   lub kliknij dwukrotnie na plik `run.command`

## Wdrożenie na Streamlit Cloud (publiczny dostęp)

1. Utwórz konto na [Streamlit Cloud](https://streamlit.io/cloud)
2. Połącz swoje konto GitHub ze Streamlit Cloud
3. Utwórz nowe repozytorium na GitHub i wgraj tam kod aplikacji
4. W Streamlit Cloud:
   - Kliknij "New app"
   - Wybierz repozytorium z kodem
   - Ustaw główny plik jako "app.py"
   - Kliknij "Deploy"
5. Po wdrożeniu:
   - Zaktualizuj BASE_URL w `.streamlit/secrets.toml` na adres twojej aplikacji
   - Wgraj zaktualizowany plik na GitHub
   - Streamlit Cloud automatycznie zaktualizuje aplikację

## Konfiguracja

Wszystkie domyślne wartości (stanowiska, oddziały, adresy, dane firmowe) można skonfigurować w pliku `config.json`.

## Struktura projektu

- `app.py` - Główna aplikacja Streamlit
- `template.py` - Szablon HTML stopki email
- `config.json` - Plik konfiguracyjny z domyślnymi wartościami
- `run.command` - Skrypt do łatwego uruchamiania aplikacji lokalnie
- `.streamlit/secrets.toml` - Konfiguracja Streamlit (np. BASE_URL)
- `requirements.txt` - Lista wymaganych pakietów Python
- `signatures/` - Katalog z zapisanymi stopkami (tworzony automatycznie)

## Użytkowanie

1. **Lista Stopek**
   - Przeglądaj istniejące stopki
   - Otwórz podgląd w nowej karcie
   - Kopiuj link do publicznego podglądu
   - Edytuj lub usuń stopki

2. **Nowa Stopka**
   - Wypełnij dane pracownika
   - Dodaj zdjęcie profilowe (link)
   - Dostosuj dane firmowe
   - Zapisz i uzyskaj link do podglądu

## Podgląd publiczny

Każda stopka ma unikalny link do podglądu, który można udostępnić innym osobom. Link jest generowany automatycznie po zapisaniu stopki.

Po wdrożeniu na Streamlit Cloud, linki do podglądu będą publicznie dostępne przez internet, co umożliwi łatwe udostępnianie stopek innym osobom.

## Przechowywanie danych

W wersji lokalnej, wszystkie dane są przechowywane w katalogu `signatures/`. Przy wdrożeniu na Streamlit Cloud, należy pamiętać, że:
- Dane są przechowywane tymczasowo i mogą zostać zresetowane przy ponownym wdrożeniu
- Dla trwałego przechowywania danych, należy rozważyć podłączenie bazy danych
