# SQL Syntax

SQL ist generell *Case-Insensitive*, d.h. es gibt keinen Unterschied zwischen Gross- und Kleinschreibung.

## Datensätze ausgeben

### SELECT

Alle Datensätze der Tabelle ```table``` ausgeben:

```
SELECT * FROM table

SELECT <welche Spalten> FROM <aus welcher Tabelle>
```

Bestimmte Spalten aus der Tabelle ```table``` ausgeben:

```
SELECT <spalte1, spalte2, spalte3> FROM table;
```

Die Reihenfolge der Spalten kann beliebig festgelegt werden:

```
SELECT <spalte2, spalte3, spalte1> FROM table;
```

### WHERE

Mit dem Schlüsselwort ```WHERE``` kann die Ausgabe auf bestimmte Einträge eingeschränkt werden.

Der Gleichheitsoperator ```=``` prüft auf **exakte** Gleichheit.

```
SELECT * FROM Customers WHERE Country = 'Germany';

SELECT * FROM table WHERE spalte1 = <gewünschter Wert>
```

Wollen wir eine *Übereinstimmung* ermitteln, müssen wir den ```LIKE``` Operator verwenden, ggf. mit einem *Platzhalter* wie ```%``` (ein beliebig oft vorkommendes beliebiges Zeichen) oder ```_``` (exakt *ein* beliebiges Zeichen).

```
SELECT * FROM [Customers]
WHERE City LIKE 'Lon%';

SELECT * FROM [Customers]
WHERE City LIKE 'Londo_';
```

### COUNT

Anzahl der gesuchten/gewünschten Datensätze ausgeben:

```
SELECT COUNT(*) FROM Customers WHERE Country = 'Germany';
```

### AS

Mit ```AS``` kann ein Alias (z.B. für Spaltennamen) definiert werden:

```
SELECT COUNT(*) AS 'anzahl von Kunden aus London' 
FROM Customers 
WHERE Country = 'Germany';
```

### ORDER BY

Datensätze basierend auf einer bestimmten Spalte sortiert ausgeben lassen

```
SELECT * 
FROM Products
ORDER BY Price;
```

Standardmässig werden die Datensätze aufsteigend ausgegeben. Folgendes Statement ist mit obigem identisch.

```ASC```-> *ascending* -> aufsteigend

```
SELECT * 
FROM Products
ORDER BY Price ASC;
```

Ausgabereihenfolge kann aber auch umgekehrt werden:

```DESC``` -> *descending* -> absteigend

```
SELECT * 
FROM Products
ORDER BY Price DESC;
```

### LIMIT

Die Anzazl der auszugebenden Datensätze kann hiermit beeinflusst werden.

Ausgabe von nur 10 Datensätzen:

```
SELECT *
FROM Customers
LIMIT 10;
```

Ausgabe des Produkts mit dem höchsten Preis:

```
SELECT * 
FROM Products
ORDER BY PRICE DESC
LIMIT 1;
```

### Aggregatfunktionen

- ```COUNT``` Anzahl
- ```MIN``` Minimum
- ```MAX``` Maximum
- ```AVG``` Durchschnitt
- ```SUM``` Summe

**Achtung:** Keine der Aggregatfunktionen kann in einem ```WHERE``` Statement verwendet werden!

Folgendes führt zu einem **Fehler**:

```
-- Vorsicht, syntaktisch FALSCh, führt zu Fehler!
SELECT * 
FROM Products
WHERE MIN(Price);
```

#### MIN / MAX

Gibt den kleinsten / grössten Wert einer Spalte aus. 

```
SELECT MIN(Price) FROM Products;
SELECT MAX(Price) FROM Products;
```

### ROUND

Ergebnisse (aus z.B.```AVG```) runden.

```
SELECT ROUND(AVG(Price)) FROM Products;

-- auf nur 2 Nachkommastellen runden:
SELECT ROUND(AVG(Price, 2)) FROM Products;
```

### GROUP BY
