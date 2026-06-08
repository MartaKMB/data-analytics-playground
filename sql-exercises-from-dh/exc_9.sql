-- cw 9: Stwórz funkcję umożliwiającą losowanie liczb całkowitych dla zadanego przedziału 
-- Wykorzystaj funkcję do znalezienia Id losowego klienta

SELECT idklienci, imie
FROM Klienci
ORDER BY RANDOM()
LIMIT 1

-- poprawna odpowiedź (z funkcją):

CREATE OR REPLACE FUNCTION losuj(od int, do_ bigint)
RETURNS bigint
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN floor(random() * (do_ - od + 1) + od)::bigint;
END;
$$;

WITH numer AS (
    SELECT losuj(1, (SELECT count(*) FROM klienci)) AS nr_wiersza
),
klienci_z_numerem AS (
    SELECT
        row_number() OVER (ORDER BY idklienci) AS nr_wiersza,
        idklienci
    FROM klienci
)
SELECT k.idklienci
FROM klienci_z_numerem k
JOIN numer n ON k.nr_wiersza = n.nr_wiersza;