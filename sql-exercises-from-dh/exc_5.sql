-- cw 5: Znajdź asortyment z 3 (trzecią) najlepszą sprzedażą, liczba sztuk

SELECT z.idasortyment,
	a.nazwa,
	SUM(z.ilosc) AS sumasprzedazy
FROM zakupy z
	INNER JOIN asortyment a
		ON z.idasortyment = a.idasortyment
GROUP BY z.idasortyment, a.nazwa
ORDER BY sumasprzedazy DESC
LIMIT 1 OFFSET 2
-- LIMIT 3

-- rozwiazanie:

WITH sprzedaz AS (
    SELECT
        a.nazwa,
        SUM(z.ilosc) AS sumasprzedazy,
        ROW_NUMBER() OVER (
            ORDER BY SUM(z.ilosc) DESC
        ) AS nrwiersza
    FROM asortyment a
    INNER JOIN zakupy z
        ON a.idasortyment = z.idasortyment
    GROUP BY a.nazwa
)
SELECT *
FROM sprzedaz
WHERE nrwiersza = 3;