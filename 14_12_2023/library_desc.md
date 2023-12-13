# Library

## Opis projektu
Napisz program na podstawie kodu mini-projektu "CAR RENTAL", ktory zrobiliśmy ostatnim razem. Kod został wzbogacony o komentarze opisujące jego działanie, żeby było łatwiej go zrozumieć.

Nowy program to wirtualna biblioteka działająca na bardzo podobnej zasadzie, tzn. książki można wypożyczac, oddawać, dodawać, usuwać i wyswietlać informacje na ich temat. Do obsługi programu wykorzystamy dwie klasy:

## Klasy
### 1. Book
 - id (int)
 - title (String)
 - author (String)
 - publish_date (String)
 - available (true / false)

### 2. Library
 - file_name (String)
 - books [List of instances of the class Book]

## Dzialanie programu
Program ma dzialać w pętli, to znaczy nie trzeba go uruchamiać ponownie po wykonaniu każdego z działań (tak samo jak wypożyczalnia). 

### Uzytkownik na do wyboru: 
1. Dodaj nową ksiażkę
2. Usuń ksiazkę
3. Zobacz dane książki
4. Wypożycz ksiażkę
5. Wyjdź z programu

### Nowosc
Chciałbym żeby użytkownik po wyborze opcji nr 3 dostał kolejny wybór, czy chce wyszukać książke po ID czy po tytule, po dokonaniu wyboru książka jest wyszukiwana i wyświetlana na jego podstawie.

## Linki
[Wypozyczalnia klasy](https://github.com/Kuba2901/korki_rolnicza/blob/main/03_12_2023/rental/car_rental.py)\
[Wypozyczalnia main](https://github.com/Kuba2901/korki_rolnicza/blob/main/03_12_2023/rental/main.py)
