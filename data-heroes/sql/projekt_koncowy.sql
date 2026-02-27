/* 
	zadanie 1 (ograniczenie do 2024 roku)
	
	Sprawdź, które produkty (po nazwie) były najczęściej kupowane w ramach promocji z rabatem.
	Wyświetl top 5 produktów z największą liczbą sprzedaży z rabatem (czyli liczba zamówień danego produktu z rabatem). 
*/

SELECT TOP 5
	p.Nazwa_Produktu
	,COUNT(DISTINCT z.Zamowienie_ID) AS Liczba_Zakupow
FROM Zamowione_Produkty zp
	JOIN Produkty p ON zp.Produkt_ID = p.Produkt_ID
	JOIN Zamowienia z ON zp.Zamowienie_ID = z.Zamowienie_ID
WHERE
	z.Data_Zlozenia_Zamowienia >= '2024-01-01'
	AND z.Data_Zlozenia_Zamowienia < '2025-01-01'
	AND zp.Rabat_Procent > 0
GROUP BY p.Nazwa_Produktu
ORDER BY Liczba_Zakupow DESC;


/* 
	zadanie 2 (ograniczenie do 2024 roku)
	
	Przygotuj zestawienie klientów, którzy skorzystali z rabatu w roku 2024.
	Wyświetl dla każdego klienta:
	- imię i nazwisko
	- email
	- miasto
	- łączną wartość zakupów produktów z rabatem
	- łączną kwotę zaoszczędzoną dzięki rabatowi
	- łączną liczbę zakupionych z rabatem produktów
*/

SELECT TOP 15
	k.Imie
	,k.Nazwisko
	,k.Adres_Email
	,k.Miasto
	,SUM(zp.Cena_Sprzedazy*zp.Ilosc) AS Wartosc_Zakupow_z_Rabatem
	,SUM(zp.Cena_Zakupu*(1+zp.Marza_Procent)*zp.Rabat_Procent*zp.Ilosc) AS Oszczednosc
	,COUNT(zp.Ilosc) AS Ilosc_Sztuk
FROM Klienci k
	JOIN Zamowienia z ON k.Klient_ID = z.Klient_ID
	JOIN Zamowione_Produkty zp ON z.Zamowienie_ID = zp.Zamowienie_ID
WHERE
	z.Data_Zlozenia_Zamowienia >= '2024-01-01'
	AND z.Data_Zlozenia_Zamowienia < '2025-01-01'
	AND zp.Rabat_Procent > 0
GROUP BY k.Imie, k.Nazwisko, k.Adres_Email, k.Miasto
ORDER BY Oszczednosc DESC;