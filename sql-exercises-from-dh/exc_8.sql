-- cw 8: Stwórz procedurę składowaną umożliwiającą sprzedaż podając niepełną nazwę produktu i id kupującego

-- proby
SELECT idasortyment, idklient, datazakupu, ilosc
FROM zakupy
ORDER BY idklient DESC, idasortyment DESC

SELECT nazwa
	FROM asortyment
	WHERE idasortyment = 15

INSERT INTO zakupy(idasortyment, idklient, datazakupu, ilosc)
VALUES (2, 92, '2016-06-04 11:26:00', 2)

WITH nazwa_produktu AS (
	SELECT a.nazwa, a.idasortyment
		FROM asortyment a
		JOIN zakupy z
		ON a.idasortyment = z.idasortyment
	),
	id_z_nazwa AS (
		SELECT idasortyment
			FROM nazwa_produktu
			WHERE nazwa ILIKE 'pip%'
	)

SELECT *
FROM id_z_nazwa
LIMIT 1

-- poprawne rozwiazanie
-- wskazówka: w procedurze nie trzeba kombinować z CTE, prościej użyć zmiennych

CREATE OR REPLACE PROCEDURE sprzedaj(
    p_nazwa TEXT,
    p_id_klienta INT,
    p_ilosc INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_id_asortyment INT;
    v_liczba_pasujacych INT;
BEGIN
    SELECT COUNT(*)
    INTO v_liczba_pasujacych
    FROM asortyment
    WHERE nazwa ILIKE '%' || p_nazwa || '%';

    IF v_liczba_pasujacych = 1 THEN

        SELECT idasortyment
        INTO v_id_asortyment
        FROM asortyment
        WHERE nazwa ILIKE '%' || p_nazwa || '%';

        INSERT INTO zakupy (
            idasortyment,
            idklient,
            datazakupu,
            ilosc
        )
        VALUES (
            v_id_asortyment,
            p_id_klienta,
            NOW(),
            p_ilosc
        );

    ELSE
        RAISE EXCEPTION
            'Nazwa asortymentu jest niejednoznaczna lub nie znaleziono takiego asortymentu';
    END IF;
END;
$$;

CALL sprzedaj('fret', 92, 1);

SELECT *
FROM klienci
WHERE idklienci = 92;

-- dodane zabezpieczenia:

CREATE OR REPLACE PROCEDURE sprzedaj(
    p_nazwa TEXT,
    p_id_klienta INT,
    p_ilosc INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_id_asortyment INT;
    v_liczba_pasujacych INT;
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM klienci
        WHERE idklienci = p_id_klienta
    ) THEN
        RAISE EXCEPTION 'Klient o id % nie istnieje', p_id_klienta;
    END IF;

    SELECT COUNT(*)
    INTO v_liczba_pasujacych
    FROM asortyment
    WHERE nazwa ILIKE '%' || p_nazwa || '%';

    IF v_liczba_pasujacych = 0 THEN
        RAISE EXCEPTION 'Nie znaleziono produktu pasującego do nazwy: %', p_nazwa;

    ELSIF v_liczba_pasujacych > 1 THEN
        RAISE EXCEPTION 'Nazwa produktu "%" jest niejednoznaczna. Znaleziono % produktów.',
            p_nazwa, v_liczba_pasujacych;

    ELSE
        SELECT idasortyment
        INTO v_id_asortyment
        FROM asortyment
        WHERE nazwa ILIKE '%' || p_nazwa || '%';

        INSERT INTO zakupy (
            idasortyment,
            idklient,
            datazakupu,
            ilosc
        )
        VALUES (
            v_id_asortyment,
            p_id_klienta,
            NOW(),
            p_ilosc
        );
    END IF;
END;
$$;

CALL sprzedaj('żółw', 1, 1);



