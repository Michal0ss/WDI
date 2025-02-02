# Sudoku składa się kwadratu o wymiarach 9 × 9 podzielonego na 9 małych kwadratów o wymiarach 3 × 3.
# W poprawnym rozwiązaniu: w każdym wierszu, każdej kolumnie i każdym małym kwadracie znajdują się
# cyfry 1 − 9. W tablicy T[9][9] zawierającej poprawne rozwiązanie, ktoś je złośliwie uszkodził, zamieniając
# miejscami dwa małe kwadraty. Wiemy, że zamienione kwadraty leżały w różnych wierszach i różnych kolumnach.
# Zamiana spowodowała, że niektóre wiersze i niektóre kolumny zawierają powtarzające się cyfry.
# Proszę napisać funkcję repeair(T), która naprawi uszkodzoną tablicę. Do funkcji należy przekazać tablicę
# zawierającą uszkodzone rozwiązanie, funkcja powinna zwrócić informację czy zamiana dotyczyła środkowego
# małego kwadratu.