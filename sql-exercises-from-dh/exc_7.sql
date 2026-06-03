-- cw 7: Policz ile sztuk kupiono każdego z typów asortymentów dla przedziałów wiekowych
-- do 30 | 30-39 | 40-49 | co najmniej 50

SELECT
	CASE
		WHEN sredni_wiek < 30 THEN 'do 30'
		WHEN sredni_wiek < 40 THEN '30 - 39'
		WHEN sredni_wiek < 50 THEN '40 - 49'
		ELSE 'co najmniej 50'
	END AS przedzial_wiekowy,
	typ_asortymentu, liczba_sztuk
FROM assortyment_summary_correct

-- poprawione:

-- CREATE OR REPLACE VIEW avg_age_sales AS
SELECT
    typ_asortymentu,
    CASE
        WHEN sredni_wiek < 30 THEN 'do 30'
        WHEN sredni_wiek < 40 THEN '30-39'
        WHEN sredni_wiek < 50 THEN '40-49'
        ELSE 'co najmniej 50'
    END AS przedzial_wiekowy,
    SUM(liczba_sztuk) AS liczba_sztuk
FROM assortyment_summary_correct
GROUP BY
    typ_asortymentu,
    CASE
        WHEN sredni_wiek < 30 THEN 'do 30'
        WHEN sredni_wiek < 40 THEN '30-39'
        WHEN sredni_wiek < 50 THEN '40-49'
        ELSE 'co najmniej 50'
    END;

-- poprawne rozwiązanie:

CREATE OR REPLACE VIEW avg_age_sales AS
WITH cte AS (
    SELECT
        typ_asortymentu AS typ,
        liczba_sztuk,
        CASE
            WHEN sredni_wiek < 30 THEN '<30'
            WHEN sredni_wiek < 40 THEN '30-39'
            WHEN sredni_wiek < 50 THEN '40-49'
            ELSE '>50'
        END AS przedzial
    FROM assortyment_summary_correct
)
SELECT
    typ,
    COALESCE(SUM(liczba_sztuk) FILTER (WHERE przedzial = '<30'), 0) AS "<30",
    COALESCE(SUM(liczba_sztuk) FILTER (WHERE przedzial = '30-39'), 0) AS "30-39",
    COALESCE(SUM(liczba_sztuk) FILTER (WHERE przedzial = '40-49'), 0) AS "40-49",
    COALESCE(SUM(liczba_sztuk) FILTER (WHERE przedzial = '>50'), 0) AS ">50"
FROM cte
GROUP BY typ;

-- inne wersje

SELECT
    typ_asortymentu AS typ,
    COALESCE(SUM(liczba_sztuk) FILTER (WHERE sredni_wiek < 30), 0) AS "<30",
    COALESCE(SUM(liczba_sztuk) FILTER (WHERE sredni_wiek >= 30 AND sredni_wiek < 40), 0) AS "30-39",
    COALESCE(SUM(liczba_sztuk) FILTER (WHERE sredni_wiek >= 40 AND sredni_wiek < 50), 0) AS "40-49",
    COALESCE(SUM(liczba_sztuk) FILTER (WHERE sredni_wiek >= 50), 0) AS ">50"
FROM assortyment_summary_correct
GROUP BY typ_asortymentu;

SELECT *
FROM avg_age_sales