# Kursy

Kursy są podzielone na lekcje każda lekcja jest zapisana w pliku JSON.
W głownym katalogu repozytorium znajduje się katalog "courses".
W nim poszczególne katalogi kursów. W każdym katalogu powinien
znajdować się plik "manifest.json" oraz katalog "lessons"
zawierający poszczególne lekcje.

## Przykładowy układ katalogów


+ 📂 courses
    - 📂 english
        - 🗎 manifest.json
        - 📂 lessons
            - 🗎 colors.json
            - 🗎 animals.json
            - 🗎 present_perfect.json

            ... etc.
    - 📂 spanish

        ...
    - 📂 portuguese
    
        ...
    - 📂 french

        ...

# Plik manifest.json

Plik musi zawierać kolejne klucze: 

+ "name" - Zawiera wyświetlaną nazwę kursu.
+ "lessons" - Tablica nazw plików kolejnych lekcji.

# Pliki lekcji

Plik lekcji musi zawierać następujące klucze:

+ "name" - Nazwa lekcji czego dotyczy konkretna lekcja.
+ "description" - Krótki opis konkretnej lekcji.
+ "tasks" - Tablica zadań konkretnej lekcji. 
    Obiekt zadania zależy od typu zadania.
    Dokładny opis każdego typu zadań
    kluczy instancji zadania znajduje się
    w pliku tasks.md
