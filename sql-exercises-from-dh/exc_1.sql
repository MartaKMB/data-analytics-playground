-- cw 1: zobaczyć wszystkie 81 rodzajów asortymentów

SELECT a.Nazwa,
	SUM(za.Ilosc) - SUM(z.Ilosc) AS StanMagazynu
FROM Asortyment a
	LEFT JOIN ZamowieniaAsortyment za
	ON za.IdAsortyment = a.IdAsortyment
	LEFT JOIN Zakupy z
	ON z.IdAsortyment = a.IdAsortyment
GROUP BY a.Nazwa

-- niby ok ALE, poprawna odpowiedź:

SELECT
    a.Nazwa,
    COALESCE(zam.IloscZamowien, 0) - COALESCE(zak.IloscZakupow, 0) AS StanMagazynowy
FROM Asortyment a
	LEFT JOIN (
	    SELECT
	        z.IdAsortyment,
	        SUM(z.Ilosc) AS IloscZakupow
	    FROM Zakupy z
	    LEFT JOIN Zwroty zw
	        ON z.IdZakupy = zw.IdZakupy
	    WHERE zw.IdZakupy IS NULL
	    GROUP BY z.IdAsortyment
	) zak
	    ON a.IdAsortyment = zak.IdAsortyment
	LEFT JOIN (
	    SELECT
	        za.IdAsortyment,
	        SUM(za.Ilosc) AS IloscZamowien
	    FROM ZamowieniaAsortyment za
	    INNER JOIN Zamowienia z
	        ON za.IdZamowienie = z.IdZamowienia
	    GROUP BY za.IdAsortyment
	) zam
	    ON a.IdAsortyment = zam.IdAsortyment;

-- wniosek: Najpierw agreguję każdą tabelę faktów osobno. Dopiero potem łączę wyniki.
