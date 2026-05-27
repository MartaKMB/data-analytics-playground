-- cw 4: Pokaż ile w każdym z typów asortymemntów mamy tanich, średnich i drogich produktów
-- Tani kosztuje do 10zł, drogi powyżej średniej ceny produktu

SELECT ta.nazwa,
	CASE
		WHEN a.cena < 10 THEN 'tani'
		ELSE 'średni'
		END AS cenaopis
FROM asortyment a
	INNER JOIN typyasortymentu ta
	ON a.idtypyasortymentu = ta.idtypyasortymentu
GROUP BY ta.nazwa,
	CASE
		WHEN a.cena < 10 THEN 'tani'
		ELSE 'średni'
		END

-- grupowanie po kategoriach cen: FILTER

SELECT
    ta.nazwa,

    COUNT(*) FILTER (WHERE a.cena < 10) AS tani,

    COUNT(*) FILTER (WHERE a.cena >= 10) AS srednidrogi

FROM asortyment a
INNER JOIN typyasortymentu ta
    ON a.idtypyasortymentu = ta.idtypyasortymentu

GROUP BY ta.nazwa

-- podzial średnie i drogoe w odniesieniu do sredniej ceny
-- Nie używaj AVG(), SUM(), COUNT() bezpośrednio w FILTER. Najpierw policz agregację w CTE/podzapytaniu, potem filtruj po wyniku.

WITH srednie AS (
    SELECT
        ta.nazwa,
        AVG(a.cena) AS srednia_cena
    FROM asortyment a
    INNER JOIN typyasortymentu ta
        ON a.idtypyasortymentu = ta.idtypyasortymentu
    GROUP BY ta.nazwa
)

SELECT
    ta.nazwa,

    COUNT(*) FILTER (WHERE a.cena < 10) AS tani,
    COUNT(*) FILTER (WHERE a.cena > s.srednia_cena) AS drogi,
    COUNT(*) FILTER (WHERE a.cena < s.srednia_cena) AS sredni

FROM asortyment a
INNER JOIN typyasortymentu ta
    ON a.idtypyasortymentu = ta.idtypyasortymentu
INNER JOIN srednie s
    ON s.nazwa = ta.nazwa

GROUP BY ta.nazwa, s.srednia_cena

-- poprawna odpowiedź:
-- W PostgreSQL nie potrzebujesz PIVOT — FILTER robi tu dokładnie to samo: zamienia kategorie Tani / Sredni / Drogi na osobne kolumny.

WITH srednia AS (
    SELECT AVG(cena::decimal(10,2)) AS wartosc
    FROM asortyment
),
dane AS (
    SELECT
        ta.nazwa,
        CASE
            WHEN a.cena < 10 THEN 'Tani'
            WHEN a.cena > s.wartosc THEN 'Drogi'
            ELSE 'Sredni'
        END AS rodzaj
    FROM asortyment a
    INNER JOIN typyasortymentu ta
        ON a.idtypyasortymentu = ta.idtypyasortymentu
    CROSS JOIN srednia s
)

SELECT
    nazwa,
    COUNT(*) FILTER (WHERE rodzaj = 'Tani') AS tani,
    COUNT(*) FILTER (WHERE rodzaj = 'Sredni') AS sredni,
    COUNT(*) FILTER (WHERE rodzaj = 'Drogi') AS drogi
FROM dane
GROUP BY nazwa;