-- cw 10: Uruchom procedurę z poprzedniego zadania dla losowego produktu, losowego klienta i losowej liczby sztuk.
-- Wykorzystaj funkcję z poprzedniego zadania, ale przynajmniej jedną losową rzecz znajdź bez wykorzystywania losowania Id/numeru wiersza

CREATE OR REPLACE FUNCTION losuj(od int, do_ bigint)
RETURNS bigint
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN floor(random() * (do_ - od + 1) + od)::bigint;
END;
$$;

WITH numer AS (
    SELECT losuj(1, (SELECT count(*) FROM asortyment)) AS nr_wiersza
),
asortyment_z_numerem AS (
    SELECT
        row_number() OVER (ORDER BY idasortyment) AS nr_wiersza,
        idasortyment
    FROM asortyment
)
SELECT a.idasortyment
FROM asortyment_z_numerem a
JOIN numer n ON a.nr_wiersza = n.nr_wiersza;

-- prawidłowe rozwiązanie:

DO $$
DECLARE
    nazwa_asortymentu varchar;
    id_klienta int;
    ilosc int;
BEGIN

    -- losowy produkt
    SELECT nazwa
    INTO nazwa_asortymentu
    FROM asortyment
    ORDER BY random()
    LIMIT 1;

    -- losowy klient
    SELECT idklienci
    INTO id_klienta
    FROM klienci
    ORDER BY random()
    LIMIT 1;

    -- losowa ilość
    ilosc := losuj(1,10);

    -- wywołanie procedury
    CALL sprzedaj(
        nazwa_asortymentu,
        id_klienta,
        ilosc
    );

END $$;

-- początek / koniec:

DO $$
BEGIN
    RAISE NOTICE 'Hello World!';
END $$;