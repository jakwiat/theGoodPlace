# theGoodPlace
Repozytorium zawiera demo technologiczne aplikacji Codzienne Wyzwania - planera aktywności, mającego na celu pomoc dzieciom na spektrum autyzmu. Projekt powstał w ramach hackathonu Cog_HACK 2021.

Rozwiązanie, przygotowane w pełni w języku Python, ma postać tekstowej aplikacji konsolowej, która prezentuje podstawowe funkcjonalności docelowej aplikacji:
1. Od strony rodzica
  - tworzenie planu dnia dziecka przez dodawanie zadań na podstawie podstawowych pakietów (modules) z przypisanymi do nich prostymi krokami (tasks)
  - monitorowanie postępów i osiągnięć podopiecznego 
  - kreowanie własnych szablonów zadań z wykorzystaniem własnych zdjęć, filmików i dźwięków
  - wgląd w trofea
  - wgląd w kalendarz i możliwość planowania do przodu, zaglądania do tyłu, wyświetlania zadań z dnia lub całego miesiąca
2. Od strony dziecka:
  - prosty interfejs przedstawiający wyłącznie dzisiejsze zadania
  - możliwość wejścia w zadanie i poruszanie się po krokach (aplikacja zapisuje postęp w wykonaniu zadania)
  - możliwość obejrzenia zdobytych nagród za wykonane zadania

Każde zadanie, krok i nagroda mają docelowo przypisane media - obrazek, w późniejszym etapie również dźwięk

Dane techniczne:
- Python 3.7
- wykorzystane biblioteki: datetime, os, random
