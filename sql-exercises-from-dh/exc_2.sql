-- cw 2: Ile każdego z asortymentów sprzedało się w marcu, kwietniu i maju?
-- Przedstaw miesiące w osobnych kolumnach

SELECT
	a.nazwa,
	SUM(za.ilosc) AS sprzedano,
	EXTRACT(MONTH FROM za.datazakupu) AS miesiac
FROM Asortyment a
	INNER JOIN Zakupy za
		ON a.idasortyment = za.idasortyment
	WHERE EXTRACT(MONTH FROM za.datazakupu) IN (3, 4, 5)
	GROUP BY EXTRACT(MONTH FROM za.datazakupu), a.nazwa
	ORDER BY EXTRACT(MONTH FROM za.datazakupu)

-- miesiace w kolumnach z pomocą AI:

SELECT
    a.Nazwa,

    SUM(CASE
        WHEN EXTRACT(MONTH FROM z.DataZakupu) = 3
        THEN z.Ilosc
        ELSE 0
    END) AS marzec,

    SUM(CASE
        WHEN EXTRACT(MONTH FROM z.DataZakupu) = 4
        THEN z.Ilosc
        ELSE 0
    END) AS kwiecien,

    SUM(CASE
        WHEN EXTRACT(MONTH FROM z.DataZakupu) = 5
        THEN z.Ilosc
        ELSE 0
    END) AS maj

FROM Zakupy z
JOIN Asortyment a
    ON a.IdAsortyment = z.IdAsortyment

GROUP BY a.Nazwa
ORDER BY a.Nazwa;

-- poprawna odpowiedź:

SELECT
    a.Nazwa,
    COALESCE(SUM(z.Ilosc) FILTER (WHERE EXTRACT(MONTH FROM z.DataZakupu) = 3), 0) AS Marzec,
    COALESCE(SUM(z.Ilosc) FILTER (WHERE EXTRACT(MONTH FROM z.DataZakupu) = 4), 0) AS Kwiecien,
    COALESCE(SUM(z.Ilosc) FILTER (WHERE EXTRACT(MONTH FROM z.DataZakupu) = 5), 0) AS Maj
FROM Asortyment a
LEFT JOIN Zakupy z
    ON a.IdAsortyment = z.IdAsortyment
GROUP BY a.Nazwa
ORDER BY a.Nazwa;

-- zamiena miesiąca na kolumny: osobna agregacja warunkowa dla każdego miesiąca
-- SUM(wartość) FILTER (WHERE warunek)