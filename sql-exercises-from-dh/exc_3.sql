-- cw 3: ile jest kobiet i mezczyzn wsrod pracownikow
-- przedoststania cyfra: parzysta = K, nieparzysta = M

SELECT COUNT(pesel)
FROM pracownicy

SELECT
	CASE
		WHEN LENGTH(pesel) <> 11 THEN 'błędny PESEL'
		
		WHEN CAST(SUBSTRING(pesel FROM 10 FOR 1) AS INTEGER) % 2 = 0
			THEN 'K'			
			ELSE 'M'
		END AS plec,
	COUNT(pesel) iloscosob
FROM pracownicy
GROUP BY
	CASE
		WHEN LENGTH(pesel) <> 11 THEN 'błędny PESEL'
		
		WHEN CAST(SUBSTRING(pesel FROM 10 FOR 1) AS INTEGER) % 2 = 0
			THEN 'K'			
			ELSE 'M'
		END

SELECT plec,
	COUNT(*) AS iloscosob
FROM(
	SELECT
		CASE
			WHEN LENGTH(pesel) <> 11 THEN 'błędny PESEL'
		
			WHEN CAST(SUBSTRING(pesel FROM 10 FOR 1) AS INTEGER) % 2 = 0
				THEN 'K'			
				ELSE 'M'
			END AS plec
	FROM pracownicy
) p
GROUP BY plec

-- prawidłowe rozwiązanie:

SELECT
    CASE
        WHEN pesel ~ '^[0-9]{9}[02468][0-9]$' THEN 'Kobieta'
        ELSE 'Mężczyzna'
    END AS plec,
    COUNT(*) AS ilosc
FROM pracownicy
GROUP BY plec;