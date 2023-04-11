<img src="./figures/Logo_KIT.svg" style="zoom:15%;float:right;" />

# Fakultät für Physik

## Physikalisches Praktikum P2 für Studierende der Physik

Versuch P2-72, 73, 83 (Stand: April 2023)

[Raum F2-19](http://www-ekp.physik.uni-karlsruhe.de/~simonis/praktikum/layoutobjekte/Lageplan_P1.png)

# Gamma Spektroskopie und Statistik

## Motivation

Bei Experimenten der Kern- und Elementarteilchenphysik ist neben den Fragen nach Art, Ort, Richtung und Zeitpunkt die Frage nach der Energie der auftretenden Strahlung besonders wichtig. Für die $\gamma$-Spektroskopie gibt es, wie auch für die anderen Teilchenarten, eine ganze Reihe von Nachweismethoden, von denen die mit Szintillator, Photokathode und Sekundärelektronenvervielfacher (SEV) besonders verbreitet ist. So werden z.B. auch in den Großexperimenten des LHCs am CERN Photonen mit Szintillationszählern vermessen.

## Lernziele

In diesem Versuch lernen Sie die experimentelle Technik von Szintillationszählern und die zugehörigen elektronischen Geräte kennen. Für das Verständnis der Methode bedarf es der Beschäftigung mit den drei Wechselwirkungsprozessen von $\gamma$-Strahlung mit Materie. Schließlich liefern die bei der Szintillationsspektroskopie auftretenden statistischen Vorgänge noch Anlass zu einer etwas eingehenderen Beschäftigung mit statistischen Gesetzmäßigkeiten.

## Versuchsaufbau

<img src="./figures/Gammaspektroskopie.jpg" style="zoom:40%;" />

## Wichtige Hinweise

- Die Kernphysik-Räume stellen einen innerbetrieblichen Überwachungsbereich dar. Hier gelten nach der Strahlenschutzverordnung besondere Regeln, die unbedingt zu beachten sind.
- Kernphysikalische Versuche dürfen erst nach Teilnahme an der Strahlenschutzbelehrung (die im Regelfall während der Vorbesprechung zum Praktikum stattfindet) durchgeführt werden.
- Der Zugang zum Bunker für radioaktive Präparate ist nur den Betreuern gestattet.
- **Bitte USB-Stick mitbringen, um die Daten bei Bedarf mit nach Hause nehmen zu können.**

## Durchführung

### Aufgabe 0: Einarbeitung in das CASSY–LAB Systems

Die Datenerfassung erfolgt über das Vielkanal-Interface des CASSY–LAB Systems. Das Bedienungshandbuch des CASSY Systems ist vor Ort vorhanden und liegt [hier](http://www-ekp.physik.uni-karlsruhe.de/~simonis/praktikum/Manuals/CassyLab-2-Handbuch.pdf) in elektronischer Form vor.

- Zur Durchführung des Versuches ist die Kenntnis der ersten dreißig Seiten von Nutzen und sollten schon zur Versuchsvorbereitung gelesen werden.
- Starten Sie das CASSY Programm und machen Sie sich damit vertraut.
- Stellen Sie die geeigneten Parameter in dem Messparameterfenster ein. Es empfiehlt sich, dieses Fenster für schnelleres Arbeiten weiterhin offen zu halten.
- Der dynamische Bereich des Detektors soll durch geeignete Einstellung der Betriebsspannung am SEV (Sehen Sie sich die Ausgangsimpulse des SEV am Oszilloskop an.) und der Software-Verstärkung möglichst voll ausgenutzt werden. Die Spannung ist gut eingestellt, wenn die Signale der höchsten Gamma-Linie gerade noch nicht in Sättigung gehen ($\approx900\,\mathrm{V}$).

---

### Aufgabe 1: Impulshöhenspektren

#### Aufgabe 1.1

**Messen Sie das Impulshöhenspektrum der $\gamma$-Strahlung von Cs-137, Na-22 und von Co-60 sowie das Untergrundspektrum mit Hilfe des 1024-Kanalbetriebs des Impulshöhenanalysators.**

- Stellen Sie die Programmparameter in dem *Parameterfenster* entsprechend ein. Der dynamische Detektorbereich soll vom Impulshöhenspektrum der höherenergetischen Strahlung (Co-60, $1173\,\mathrm{keV}$ und $1333\,\mathrm{keV}$), ausgenutzt und unverändert auch bei der Messung an Cs-137 ($662\,\mathrm{keV}$) und Na-22 ($511\,\mathrm{keV}$ und $1275\,\mathrm{keV}$) benutzt werden.
- Das Entstehen eines Impulshöhenspektrums mit der Zeit kann am Bildschirm verfolgt werden. Der Abstand Präparat - Szintillator soll jeweils so gewählt werden, dass die effektiven Zählraten für Co-60, Na-22 und Cs-137 etwa gleich sind und $400/\mathrm{s}$ bis $800/\mathrm{s}$ betragen. Diese effektive Zählrate (Mittel über alle Kanäle) wird im Fenster Eigenschaften angezeigt.
- Überprüfen Sie, welchen Einfluss das Untergrundspektrum auf die Messung hat, und korrigieren Sie ggf. die Spektren.

*Hinweis: Bitte vergessen Sie nicht, auch Zwischenergebnisse abzuspeichern, um etwaigen Datenverlust vorzubeugen.*

#### Aufgabe 1.2

**Deuten Sie die erhaltenen Impulshöhenspektren aufgrund der verschiedenen Wechselwirkungsprozesse von $\gamma$-Strahlung mit Materie.**

Dazu ist es zweckmäßig, anhand des Photopeaks von Cs-137 eine Energieskalierung vorzunehmen und dann die gemessenen und die berechneten Energien an Stellen, bei denen Besonderheiten im Impulshöhenspektrum zu erwarten sind, zu vergleichen.

- Berechnen Sie dafür bereits in der Vorbereitung die Energien der Comptonkanten.

Das Programm unterstützt den Benutzer bei der Analyse eines Spektrums: Zeigt der Cursor in das zu analysierende Spektrum und drückt man die rechte Maustaste, so werden verschiedene Analysewerkzeuge angeboten. Zusätzlich können Sie erklärenden Text in die Diagramme einfügen und diese dann ausdrucken.

- Diskutieren Sie auch die statistischen Effekte, welche die "Verschmierung" des erhaltenen Impulshöhenspektrums, besonders deutlich bei den Photopeaks, bewirkt haben.
- Schätzen Sie die Anzahl der Elektronen $n_e$ ab, die bei einem Impuls, der zum Photopeak bei Cs-137 beiträgt, von der Photokathode emittiert wurden. $n_e$ charakterisiert die Auflösung eines Detektors.
- Überprüfen Sie die Linearität der Apparatur, indem Sie die Information aus den drei Spektren verwenden.
- Mit unveränderten Einstellungen können noch Spektren (oder ein Überlagerungsspektrum) mit weiteren radioaktiven Quellen aufgenommen werden. Geeignet sind Am-241 ($59,5\,\mathrm{keV}$) und Co-57 ($122\,\mathrm{keV}$). Der Betreuer kann Ihnen diese Quellen aushändigen.

---

### Aufgabe 2: Aktivität des Cs-137-Präparats

**Bestimmen Sie die Aktivität des Cs-137-Präparats.**

Verwenden Sie die Zählraten, die vom Programm berechnet und angezeigt werden, und die Nachweiswahrscheinlichkeit (Diagramm "Quotient Anzahl der ... Quanten") des benutzten Szintillatorkristalls im gewählten Abstand und bei der betreffenden Strahlungsenergie.

- Welche Effekte berücksichtigt das Diagramm, wenn bei seiner Verwendung kein weiterer Effekt mehr in die Rechnung einfließen muss?
- Bei wenigstens drei verschiedenen Abständen Quelle-Szintillatorstirnfläche sollte gemessen und ein Ausgleichswert berechnet werden.
- Prüfen Sie, ob eine Totzeitkorrektur der Zählraten notwendig ist.

---

### Aufgabe 3: Röntgenemission

Verwenden Sie die Cs-Quelle um an Materialien mit schwerem $Z$ Röntgenemission zu erzeugen. Legen Sie dazu die entsprechenden Materialien direkt auf den Szintillator. Erhöhen Sie die Messgenauigkeit für niedrige Energien durch Erhöhen der Detektorspannung. Zur genauen Peakbestimmung sollte der Gaussfit
verwendet werden.

#### Aufgabe 3.1

**Führen Sie eine Energiekalibration anhand der Ba- $K_\alpha$ und Pb- $K_\alpha$ Röntgenlinie durch und stellen Sie die gemessene Energie gegen $Z^2$ für alle vorhandenen Elemente auf**

Informationen zum Moseleyschen Gesetz befinden sich [hier](https://de.wikipedia.org/wiki/Moseleysches_Gesetz) und eine Tabelle der $K_\alpha$-Übergangsenergien ist in `params/Moseley-Gesetz.csv`.

#### Aufgabe 3.2

**Bestimmen Sie anhand Ihres Diagramms das "unbekannte Element".**

---

### Aufgabe 4: Statistik

#### Aufgabe 4.1

**Untersuchen Sie die statistische Verteilung von gemessenen Ereignisanzahlen bei häufig
wiederholter Messung von Untergrundstrahlung unter stets gleichen Bedingungen.**

- Wählen Sie dazu im *Parameterfenster: Vielkanalmessung, 256 Kanäle* und *wiederholende Messung* bei einer Messzeit von 1 Sekunde. Nehmen Sie einen statistischen Daten-Pool von mindestens 150 Spektren auf.

Sie erhalten eine Tabelle mit 150 Spalten (Spektren) und 256 Zeilen (Kanäle, Energieintervalle). Keiner der Einträge ist vorhersagbar sondern hängt nur von der Statistik des radioaktiven Zerfalls ab, der einen natürlichen Zufallsgenerator darstellt.

Bilden Sie zwei Stichproben mit je 150 Zahlen, indem Sie:

1. die Zählrate aus nur einem Teil eines Spektrums aufintegrieren, so dass der Mittelwert der 150 Summen ungefähr 3 beträgt.
2. die Gesamtzählrate der einzelnen Spektren verwenden.

#### Aufgabe 4.2

**Berechnen Sie von beiden Stichproben den Mittelwert $x_\mathrm{m}$, die Standardabweichung $s$ der Einzelmesswerte und die Standardabweichung $s_\mathrm{x_\mathrm{m}}$ des Mittelwertes.**

Prüfen Sie, ob die Standardabweichung der Einzelmesswerte gleich der Wurzel aus dem Mittelwert ist, wie die theoretisch zu erwartende Poisson-Verteilung es verlangt.

#### Aufgabe 4.3

**Stellen Sie die Stichproben als Häufigkeitsverteilungen graphisch dar, und tragen Sie in das jeweilige Diagramm auch die mit Hilfe von $x_\mathrm{m}$ berechnete Poisson-Verteilung und die mit Hilfe von $x_\mathrm{m}$ und $s$ berechnete Gaußverteilung (=Normalverteilung) ein.**

- Machen Sie eine Aussage über die Ersetzbarkeit der Poissonverteilung durch die Gaußverteilung in Abhängigkeit vom Mittelwert.

#### Aufgabe 4.4

**Prüfen Sie mit Hilfe des Chi-Quadrat-Tests bei einer vernünftig gewählten Signifikanzzahl die folgenden Hypothesen.**

1. Die Stichproben stammen aus einer normalverteilten Grundgesamtheit.
2. Die Stichproben stammen aus einer poissonverteilten Grundgesamtheit.

### Anhang: Hilfe zur Bearbeitung von Aufgabe 4 mit EXCEL

Importieren Sie die von CASSY-Lab gespeicherten LAB Dateien in EXCEL (Einstellungen: “getrennt“, Trennzeichen: “Tabulator“). Im Mittelteil enthält diese Datei einen großen Tabellenblock mit allen Spektren als Spaltenvektoren. Die relevanten Zahlen stehen in Zeilen, die mit NAN (*not a number*) beginnen. Zur Auswertung generiert man in einer EXCEL-Tabelle eine Spalte mit den Einträgen zum Beispiel “=Summe(C10:C26)“, “=Summe(D10:D26)“, “=Summe(E10:E26)“, ... bzw. “=Summe(C1:C256)“, “=Summe(D1:D256)“, “=Summe(E1:E256)“, ...

Mit der Häufigkeitsfunktion kann man dann zur weiteren Analyse die Häufigkeitsverteilung dieser Stichproben erhalten. Erstellen Sie dazu eine Spalte mit den Klassen (z.B. Zahlen 1 bis 40), markieren Sie die Zellen der Spalte, die die Häufigkeiten aufnehmen sollen. Unter *Einfügen/Funktion* finden Sie die Funktion *Häufigkeit*. Wählen Sie für *Daten* die Werte einer Stichprobe und für *Klassen* die Zellen der Klassenspalte. Beim Verlassen der Funktion bestätigen Sie mit *Strg-Umschalt-Eingabe*, damit die Formel als Matrixfunktion eingegeben wird.
