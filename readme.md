# Oracle-Scripts-Execution
Zadaniem aplikacji jest wywołanie skryptów SQL znajdujących się w plikach .sql

Przed uruchomieniem:
1. Pliki .sql należy umieścić w katalogu 'sql_source'
2. W pliku config.ini należy wprowadzić parametry bazy danych Oracle
3. Można również zdefiniować kody błędów Oracle, które będą ignorowane (config.ini - [Errors] excluded)

Działanie aplikacji:
1. Pliki .sql są wywoływane w kolejności alfabetycznej
2. Pliki, które w całości zostaną przetworzone bez błędów są przenoszone do katalogu 'sql_executed'
3. W przypadku wystąpienia błędu podczas wykonywania skryptów działanie programu jest przerywane
4. W katalogu 'log' zapisywane są komunikaty zwracane przez bazę danych