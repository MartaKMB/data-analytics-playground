-- cw 6: stworz widok

CREATE VIEW assortyment_summary AS
SELECT a.nazwa, ta.nazwa AS typ_asortymentu, a.cena, ROUND((a.cena - (a.cena * 0.23))::numeric, 1) AS cena_netto, z.ilosc, ROUND(AVG(k.wiek)::numeric, 1) AS sredni_wiek
FROM asortyment a
JOIN typyasortymentu ta
ON a.idtypyasortymentu = ta.idtypyasortymentu
JOIN zakupy z
ON a.idasortyment = z.idasortyment
JOIN klienci k
ON z.idklient = k.idklienci
GROUP BY a.nazwa, ta.nazwa, a.cena, z.ilosc;

-- all views
SELECT *
FROM pg_views;

DROP VIEW assortyment_summary;
DROP VIEW asortyment_summary;

--poprawna odpowiedz

CREATE OR REPLACE VIEW assortyment_summary_correct AS
SELECT
    a.nazwa AS nazwa_asortymentu,
    ta.nazwa AS typ_asortymentu,
    ROUND(a.cena::numeric, 2) AS cena_brutto,
    ROUND((a.cena / 1.23)::numeric, 2) AS cena_netto,
    SUM(z.ilosc) AS liczba_sztuk,
    ROUND(COALESCE(AVG(k.wiek), 0)::numeric, 1) AS sredni_wiek
FROM asortyment a
JOIN typyasortymentu ta
    ON a.idtypyasortymentu = ta.idtypyasortymentu
JOIN zakupy z
    ON z.idasortyment = a.idasortyment
JOIN klienci k
    ON k.idklienci = z.idklient
LEFT JOIN zwroty zw
    ON zw.idzakupy = z.idzakupy
WHERE zw.idzwroty IS NULL
GROUP BY
    a.nazwa,
    ta.nazwa,
    a.cena;

SELECT *
FROM assortyment_summary_correct;