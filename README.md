# PhotoPeopleCounter_API - Aplikacja do Detekcji Twarzy i Zliczania Osób
 Projekt został opracowany w ramach modułu "Technologie chmurowe" na studiach podyplomowych "Uczenie Maszynowe i Data Science". 
 
#### Autor: Joanna Maszybrocka

## Opis
Aplikacja, napisana jest w języku Python, wykorzystuje klasyfikator kaskadowy Haar z biblioteki OpenCV do identyfikacji twarzy i zliczania osób na zdjęciach. Użytkownik ma możliwość przesyłania zdjęć do analizy na trzy różne sposoby:

- Wczytywanie obrazów bezpośrednio z dysku serwera.
- Przesyłanie obrazów przez użytkownika.
- Pobieranie obrazów z podanego URL.

## Działanie
Aplikacja:
- przeprowadza analizę, identyfikuje twarze i na tej podsatwie zwraca liczbę osób.
- Zapewnia również obraz z zaznaczonymi twarzami i obraz oryginalny.

## Wymagania
- Flask: Framework do tworzenia aplikacji webowych w Pythonie, służy do obsługi żądań HTTP i renderowania HTML.
- OpenCV (cv2): Biblioteka do przetwarzania obrazów, wykorzystywana do wykrywania i analizy twarzy na obrazach.
- NumPy: Biblioteka do przetwarzania danych, wspiera operacje na obrazach w OpenCV.
- requests: Umożliwia wykonywanie żądań HTTP, używana do pobierania obrazów z internetu.
- io: Biblioteka do obsługi operacji wejścia/wyjścia, potrzebna do przetwarzania obrazów.

## Uruchamianie aplikacji

Gdy aplikacja zostanie uruchomiona, zostanie uruchomiony lokalny serwer deweloperski. Możesz uzyskać do niego dostęp, otwierając przeglądarkę internetową i wpisując adres http://localhost:5000/. Na tej stronie zostanie wyświetlony interfejs użytkownika Twojej aplikacji do analizy obrazów, co umożliwi Ci przetestowanie jej funkcjonalności.