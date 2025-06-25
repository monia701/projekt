Bijatyka 2D - Gra kosmos

Gra kosmos to prosta gra walki stworzona w języku Python z wykorzystaniem biblioteki pygame.
Gra została przygotowana jako projekt zaliczeniowy i spełnia wymagania na ocenę dobrą.

Dwóch graczy steruje swoimi postaciami na jednej arenie. Każdy gracz może poruszać się w lewo i prawo, skakać oraz atakować przeciwnika.
Celem gry jest zredukowanie paska życia przeciwnika (HP) do zera. Każda postać startuje z 10 punktami życia (HP).

Podczas rozgrywki co kilka sekund na planszy pojawia się power-up w postaci serduszka. Gracze mogą je zbierać, aby zregenerować 1 punkt HP.
Gra posiada scrollowaną kamerę, dzięki której tło areny przesuwa się w lewo lub prawo, tak aby obaj gracze byli widoczni.

Gra zawiera oprawę dźwiękową — muzykę w tle oraz efekty dźwiękowe przy trafieniach.
Po zakończeniu rozgrywki wynik (zwycięzca) jest zapisywany do pliku wyniki.txt.
Gracze mogą ponownie rozpocząć grę bez konieczności zamykania programu.

Sterowanie:

Gracz 1:
Ruch w lewo - A
Ruch w prawo - D
Skok - W
Atak - F

Gracz 2:
Ruch w lewo - strzałka w lewo (←)
Ruch w prawo - strzałka w prawo (→)
Skok - strzałka w górę (↑)
Atak - Enter


Celem gry jest pokonanie przeciwnika — czyli zredukowanie jego paska życia do zera.
Po wygranej wyświetlane jest odpowiednie podsumowanie i gracze mogą rozpocząć nową rundę.
