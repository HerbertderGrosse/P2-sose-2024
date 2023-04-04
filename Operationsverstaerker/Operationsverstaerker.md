<img src="./figures/Logo_KIT.svg" style="zoom:15%;float:right;" />

# Fakultät für Physik

## Physikalisches Praktikum P2 für Studierende der Physik

Versuch P2-56, 60, 61 (Stand: April 2023)

[Raum F1-15](http://www-ekp.physik.uni-karlsruhe.de/~simonis/praktikum/layoutobjekte/Lageplan_P1.png)

# Operationsverstärker

## Motivation

Einfache elektrische Verstärkerschaltungen sind vielfach verwendete Hilfsmittel im physikalischen Labor. Jeder Experimentalphysiker (und auch jeder Physiklehrer) sollte in der Lage sein, Sie bei Bedarf rasch zu konzipieren und aufzubauen.

## Lernziele

Bei diesem Versuch lernen Sie zwei Grundbausteine von Verstärkerschaltungen kennen: den Transistor und
den Operationsverstärker.

Im Vordergrund steht dabei die Anwendung dieser beiden Elemente in konkreten Schaltungen und nicht ihr "halbleiterphysikalisches Innenleben", das erst in späteren Vorlesungen behandelt werden wird. Hier genügen zunächst einfache Modellvorstellungen

## Versuchsaufbau

Dies ist der Arbeitsplatz an dem der Versuch durchegführt wird.

<img src="./figures/Operationsverstaerker.jpg" style="zoom:50%;" />

Alle Schaltungen werden auf diesem Experimentierboard aufgebaut. Es besteht aus vier Bereichen, die für verschiedene Aufgabenteile verwendet werden.

1. Transistor: Hier wird die Emitterschaltung aus Aufgabe 1 aufgebaut.
2. Operationsverstärker 1 und 2: In diesem Bereich werden die Aufgaben 2.1 - 4.2 aufgebaut. Links und rechts beﬁndet sich jeweils ein bereits an die Spannungsversorgung angeschlossener Operationsverstärker. In der Mitte ist ein $10\,\mathrm{kΩ}$ Potentiometer angebracht.
3. Operationsverstärker 3: Dieser OPV ist nicht an die Spannungsversorgung angeschlossen und wird bei keiner der Aufgaben 1 bis 4 verwendet.
4. Spannungsversorgung: Hier ist das Netzteil untergebracht, das die OPV mit $±15\,\mathrm{V}$ versorgt (blau: $−15\,\mathrm{V}$, weiß: $+15\,\mathrm{V}$, schwarz: $0\,\mathrm{V}$ / GND).

<img src="./figures/Experimentierboard.png" style="zoom:30%;" />

## Wichtige Hinweise

## Durchführung

### Aufgabe 1: Emitterschaltung eines Transistors

Das ist die am häufigsten verwendete Transistorverstärkerschaltung. Verwenden Sie dafür aber hier nicht zuviel Zeit. Die Aufgaben zum Operationsverstärker (ab Aufgabe 2) sollen vorrangig erarbeitet werden.

#### Aufgabe 1.1

Bauen Sie auf der Experimentier-Steckplatine den einstufigen gleichstromgegengekoppelten Transistorverstärker auf.

- Welche Funktionen haben die einzelnen Bauelemente, speziell $R_e$?
- Überprüfen Sie die Lage des Arbeitspunktes.
- Wozu dient der Kondensator $C_e$?
- Erläutern Sie Sinn und Wirkungsweise der Gegenkopplung.

#### Aufgabe 1.2

Führen Sie dem Verstärker als Eingangssignal eine Dreieckspannung mittlerer Frequenz (ca. $1\,\mathrm{kHz}$) zu und beobachten Sie oszilloskopisch das Ausgangssignal und bestimmen Sie die Verstärkung.

- Stellen Sie durch Variation der Amplitude des Eingangssignals verschiedene Ausgangsamplituden (etwa $3V_{SS}$ und $10V_{SS}$) ein und beurteilen Sie die Qualität des Verstärkers.

#### Aufgabe 1.3

Entfernen Sie den Emitterkondensator $C_e$. Beobachten Sie wieder das Ausgangssignal bei verschiedenen Amplituden und bestimmen Sie die Verstärkung dieses stromgegengekoppelten Verstärkers.

- Warum finden Sie gerade den Wert $R_c/R_e$ als Verstärkungsfaktor?
- Erklären Sie die Wirkungsweise der Gegenkopplung durch $R_e$ (Stromgegengekoppelter Verstärker).

#### Aufgabe 1.4

Bestimmen Sie die Verstärkung des Strom- und Gleichstromgegengekoppelten Verstärkers für verschiedene Frequenzen ($10,\:25,\:50,\:100\;\mathrm{und}\:500\,\mathrm{Hz}$ sowie  $1,\:5,\:10,\:50\:\mathrm{und}\:100\,\mathrm{kHz}$). Besonders wichtig ist hierbei der Frequenzbereich $10\,\mathrm{Hz}$ bis $500\,\mathrm{Hz}$.

- Plotten Sie für beide Schaltungen den Verlauf der Verstärkung und erklären Sie diesen.

---

### Aufgabe 2: Grundschaltung eines Operationsverstärkers

#### Aufgabe 2.1

Bauen Sie auf der Experimentier-Steckplatine mit einem Operationsverstärker einen nichtinvertierenden Verstärker mit etwa zehnfacher Verstärkung.

- Überprüfen Sie die Funktion der Schaltung.
- Führen Sie dem Eingang eine Dreieckspannung mittlerer Frequenz ($1\,\mathrm{kHz}$) zu und beobachten Sie oszilloskopisch das Ausgangssigna1.
- Vergleichen Sie die experimentell und rechnerisch ermittelten Verstärkungsfaktoren.

#### Aufgabe 2.2

Demonstrieren Sie den hohen Eingangswiderstand und den kleinen Ausgangswiderstand dieser Schaltung mit Hilfe geeigneter Verfahren.

#### Aufgabe 2.3

Bestimmen Sie die Verstärkung in Abhängigkeit von der Frequenz ($10\:\mathrm{und}\:100\,\mathrm{Hz}$ sowie $1,\:10,\:25,\:50,\:75\:\mathrm{und}\:100\,\mathrm{kHz}$).

- Wählen Sie als Eingangssignal eine Sinuswechselspannung mit einer Amplitude von $0,5V_{SS}$ und beobachten Sie das Ausgangssignal oszilloskopisch.
- Können Sie die bei hohen Frequenzen auftretenden Verzerrungen erklären?

---

### Aufgabe 3: Die invertierende Grundschaltung

Dies ist wohl die wichtigste Grundschaltung von Operationsver-
stärkern.

#### Aufgabe 3.1

Bauen Sie mit einem Operationsverstärker einen invertierenden Verstärker mit zehnfacher Verstärkung auf.

- Überprüfen Sie die Funktion und erklären Sie die Wirkungsweise der Schaltung.
- Leiten Sie die Verstärkung her.

#### Aufgabe 3.2

Bauen Sie einen „Addierer“ für zwei Eingangssignale auf. Als Eingangssignale können Sie Dreieck-, Rechteck- oder Sinusspannung (bis $1\,\mathrm{kHz}$) und eine mit den auf der Platine vorhandenen Potentiometern realisierbare regelbare Gleichspannungen im Bereich $-15\,\mathrm{V}$ bis $+15\,\mathrm{V}$ verwenden.

- Beobachten Sie die Ausgangsspannung oszilloskopisch. Schalten Sie den Eingang des Oszilloskops auf „DC-Kopplung“, damit die Gleichspannung korrekt dargestellt wird.

#### Aufgabe 3.3

Bauen Sie den „lntegrierer“ auf. Schalten Sie wieder zurück auf „AC-Kopplung“. Verwenden Sie als Eingangssignal Rechteck- und Dreieckspannungen niedriger Frequenz (im Bereich $50\,\mathrm{Hz}$ bis $100\,\mathrm{Hz}$) und großer Amplitude.

- Beobachten Sie wieder oszilloskopisch.
- Erklären Sie die Wirkungsweise der Schaltung (ohne
Berücksichtigung des Widerstandes $R_s$, der nur der Stabilisierung des Integrierers dient).

#### Aufgabe 3.4

Bauen Sie den „Differenzierer“ auf.

- Testen Sie die Funktion mit Rechteck- und Dreiecksignalen (im Bereich $50\,\mathrm{Hz}$ bis $500\.\mathrm{Hz}$).
- Erklären Sie die Wirkungsweise der Schaltung.

---

### Aufgabe 4: Komplexere Schaltungen mit Operationsverstärkern

Im Folgenden werden nun einige etwas komplexere Schaltungen aufgebaut und untersucht.

- Welche der beiden Grundschaltungen erkennen Sie dabei amhäufigsten wieder?

#### Aufgabe 4.1

Bauen Sie mit einem Operationsverstärker einen idealen Einweggleichrichter auf und überprüfen Sie seine Funktion mit verschiedenen Eingangswechselspannungssignalen ($f<1\,\mathrm{kHz}$).

- Was sind die Vorteile dieser Schaltung gegenüber einer einfachen Gleichrichterschaltung mit einer Diode und einem Widerstand? Probieren Sie es aus!
- Wofür könnte ein solcher idealer Gleichrichter Verwendung finden?

#### Aufgabe 4.2

Bauen Sie mit zwei Operationsverstärkern einen Generator für Dreieck- und Rechtecksignale auf.

- Erklären Sie die Funktionsweise der angegebenen Schaltung. 

*Hinweis: Einer der Operationsverstärker arbeitet als Schwellenwertschalter, der andere als Integrierer.*

#### Aufgabe 4.3

Bauen Sie die so genannte „Programmierte Differentialgleichung 2. Ordnung“ auf. Diese Generatorschaltung zur Erzeugung von Sinuswechselspannungen ermöglicht die Simulation einer Integralgleichung 2. Ordnung. Sie erkennen die beiden hintereinandergeschalteten Integrierer. Mit dem Potentiometer können Sie die Dämpfung der Schwingung einstellen. Die Schwingungsamplitude wächst an oder klingt ab, je nachdem ob Sie den Schleifer des Potentiometers aus der Mittelstellung nach rechts oder nach links gedreht haben.

- Versuchen Sie, durch Variation des Potentiometerwiderstands die drei Fälle - Schwingfall, aperiodischer Grenzfall und Kriechfall - zu simulieren.

*Hinweis: Eine genaue Beschreibung dieser Schaltung finden Sie in "Tietze, Schenk: Halbleiterschaltungstechnik".*
