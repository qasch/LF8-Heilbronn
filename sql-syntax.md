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

### WHERE und LIKE

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

Ergebnisse nach einem bestimmten Kriterium gruppieren bzw. mehrere gleiche Einträge zu einem zusammenführen. 

```
-- alle Umschühler ermitteln, die am gleichen Ort leben
SELECT
  *
FROM
  umschueler, orte
WHERE
  orte.postleitzahl = umschueler.postleitzahl
GROUP BY
  orte.postleitzahl;
```

```
-- Durchschnittsgrösse aller Personen pro Ort ermitteln
SELECT 
    AVG (groesse) 
FROM
    Person
GROUP BY
    ort;
```

### HAVING

Aggregatfunktionen können **nicht** in einer ```WHERE```-Klausel verwendet werden, da die ```WHERE```-Klausel immer nur eine einzige Zeile prüfen kann.

Für diese Fälle nutzt mann ```HAVING```.

```
--ACHTUNG FALSCH !!!

SELECT
  ort.ortsname, COUNT(*) AS 'Anzahl Umschüler pro Ort'
FROM
  umschueler, ort
WHERE
  ort.id = umschueler.ort_id 
  AND
    'Anzahl Umschüler pro Ort' > 2; -- hier ist der Fehler
GROUP BY
    ort.id;
```

```
-- Das ist die richtige Lösung

SELECT
  ort.ortsname, COUNT(*) AS 'Anzahl Umschüler pro Ort'
FROM
  umschueler, ort
WHERE
  ort.id = umschueler.ort_id
GROUP BY
    ort.id
HAVING
  'Anzahl Umschüler pro Ort' > 2;
```

### JOIN

In SQLite gibt es einen ```INNER JOIN``` und einen ```LEFT JOIN```. 

Andere SQL Dialekte haben zusätzlich einen ```RIGHT JOIN``` und eine ```FULL JOIN``` oder ```OUTER JOIN```. 

Die gebräuchlichste Art des ```JOIN(T)S``` ist der ```INNER JOIN```, welcher auf zwei Arten vollzogen werden kann:

```
-- inner join ohne Schlüsselwort JOIN

SELECT 
    u.vorname, u.nachname, o.ortsname
FROM 
    umschueler u, ort o
WHERE 
    u.ort_id = o.id; 
```

```
-- inner join mit Schlüsselwort JOIN

SELECT 
    u.vorname, u.nachname, o.ortsname
FROM 
    umschueler u
JOIN
    ort o
ON
    u.ort_id = o.id; 
```

Der ```INNER JOIN``` (das ```INNER``` kann weggelassen werden), gibt die Datensätze beider Tabellen aus, die miteinander verknüpft sind.

Ein ```LEFT JOIN``` hingegen liefert **sämtliche** Werte der linken Tabelle, auch wenn keine Verknüpfung mit einem Datensatz der rechten Tabelle besteht und zusätzlich alle Datensätze der rechten Tabelle, die mit der linken verknüpft sind.

Ein ```LEFT JOIN``` kann einfach in einen ```RIGHT JOIN``` überführt werden, indem man die beiden Tabellen vertauscht.

```
SELECT 
    u.vorname, u.nachname, o.ortsname
FROM 
    ort o
LEFT JOIN
    umschueler u
ON
    u.ort_id = o.id; 

```

Hier werden jetzt auch die Orte ausgegeben, in denen keiner der Umschüler lebt.

### Tabelle löschen

```
DROP TABLE ort;
```

### Datensätze löschen

Folgendes Statement löscht alle Datensätze der Tabelle Ort. Im Gegensatz zum ```DROP TABLE``` bleibt aber die Datenbankstuktur erhalten.

```
DELETE FROM ort;
```

Einzelne Datensätze können über eine Einschränkung mit ```WHERE``` gelöscht werden.

```
DELETE FROM 
    ort
WHERE
    id = 5;
```


### Datensätze ändern

```
UPDATE 
    ort
SET
    ortsname = "Kassel"
WHERE 
    plz = 34121;
```


### Normalisierung

#### 1. Normalform

Alle Attributwerte müssen atomar vorliegen, können also nicht weiter unterteilt werden.

#### 2. Normalform

Alle Nicht-Schlüssel-Attribute hängen vom gesamten Primärschlüssel ab.

#### 3. Normalform

Alle Nicht-Schlüssel-Attribute sind voneinander unabhängig.
