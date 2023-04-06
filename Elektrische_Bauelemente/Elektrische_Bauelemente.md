<img src="./figures/Logo_KIT.svg" style="zoom:15%;float:right;" />

# Fakultät für Physik

## Physikalisches Praktikum P2 für Studierende der Physik

Versuch P2-50, 51, 52 (Stand: April 2023)

[Raum F1-17](http://www-ekp.physik.uni-karlsruhe.de/~simonis/praktikum/layoutobjekte/Lageplan_P1.png)

# Elektrische Bauelemente

## Motivation

Die Eigenschaften eines elektrischen Bauelements hängen von vielen physikalischen Größen ab. Häufig wirkt sich dies besonders auf dessen Widerstand aus. Die vorherrschende Abhängigkeit gibt dem Bauteil seinen charakteristischen Namen: NTC- bzw. PTC-Widerstand weisen eine Temperaturabhängigkeit (Negative/Positive Temperature Coefficient) auf. Der VDR-Widerstand (Varistor, Voltage Dependent Resistance) reagiert auf Spannungsänderungen. Optoelektrische Bauteile wie Photowiderstand (LDR, Light Dependent Resistance), Photodiode und Phototransistor sind lichtempfindlich oder senden wie die Leuchtdiode (LED, Light Emitting Diode) Licht aus. Druckabhängige Bauelemente sind unter dem Namen Piezoelemente bekannt, da ihre Eigenschaften auf dem Piezoelektrischen Effekt beruhen. Supraleiter verlieren ihren elektrischen Widerstand unter bestimmten äußeren Bedingungen sogar gänzlich. Interessant ist zudem die Klassifizierung in Leiter, Halbleiter und Nichtleiter (Isolatoren) und die Untersuchung der besonderen Eigenschaften. Hier spielen Halbleiterbauelemente auf Grund ihrer Vielfalt die größte Rolle.

## Lernziele

- Die Eigenschaften verschiedener elektrischer Bauelemente sollen in diesem Versuch kennen gelernt werden.
- Außerdem sollen die Messmethoden zur Untersuchung der jeweiligen Eigenschaften kennengelernt werden.
- In der Auswertung stehen die Erklärung der beobachteten Effekte und die praktischen Anwendungsgebiete im Vordergrund.

## Versuchsaufbau

<img src="./figures/Versuchsaufbau.jpg" style="zoom:20%;" />

## Wichtige Hinweise

- Sie benötigen einen USB-Stick zur Datensicherung.

- **Aufgabe 1: Das Gehäuse des Ofens erhitzt sich stark! Vermeiden Sie jeglichen Kontakt mit der Oberfläche.**

- **Aufgabe 5: Flüssiger Stickstoff ($T=-196°\mathrm{C}$) kann schwere Kälteverbrennungen verursachen! Daher stets Handschuhe und Schutzbrille tragen.**

## Durchführung

### Aufgabe 1: Wheatstoneschen Brückenschaltung

**Messen Sie mit Hilfe der Wheatstoneschen Brückenschaltung die $P(T)$-Abhängigkeit verschiedener Bauteile im Bereich von Zimmertemperatur bis $\approx 150°\mathrm{C}$.**

<img src="./figures/Wheatstonesche_Brueckenschaltung.png" style="zoom:40%;float:right;" />

- Messen Sie dazu mit Hilfe der Versuchsbox (Schaltplan als Grafik) nacheinander den Widerstand von NTC und PT100 in Abhängigkeit von der jeweiligen Temperatur. Als Spannungsquelle dient das Netzgerät, welches eine Gleichspannung von $U=2\,\mathrm{V}$ liefert. Um die Erwärmung des Widerstands durch den Messstrom gering zu halten, soll dieser jeweils nur kurzzeitig eingeschaltet werden (durch Betätigung des Tasters). Als Brückeninstrument dient das Multimeter im mA(DC)-Bereich. Wählen Sie den Referenzwiderstand in der gleichen Größenordnung wie das zu messende Bauteil. (Überprüfen Sie den angegebenen Wert mit dem Multimeter.) Nehmen Sie beim Erwärmen des Ofens die Messreihe am NTC und beim Abkühlen die Messreihe am PT100 auf.

- Begründen Sie, warum die Messung mit Hilfe der Wheatstoneschen Brückenschaltung in diesem Falle sinnvoll ist.

- Stellen Sie die $R(T)$-Abhängigkeiten jeweils graphisch dar und schließen Sie daraus auf die Eigenschaften des Bauteils.

- Wählen Sie zur Auswertung für den NTC-Widerstand eine geeignete Auftragung, um die Koeffizienten $a$ und $b$ aus $R(T) = a \cdot e^{b/T}$ zu bestimmen. Überlegen Sie sich, wie man NTC-Widerstände zur Temperaturmessung, zur Füllstandsanzeige und zur Strombegrenzung verwenden kann.

- Für den PT100 gilt $R(T) = R_0 + c \cdot T$. Bestimmen Sie die Konstante $c$ und überprüfen Sie den Widerstand $R_0$ bei $0°\mathrm{C}$. Diskutieren Sie auch hier mögliche Einsatzgebiete.

---

### Aufgabe 2: Kennlinien

**Überlegen Sie sich im Vorfeld durch Anfertigung von Schaltskizzen,**

- wie eine Spannungsstabilisierung mit einer Zenerdiode zu realisieren wäre.
- wie der Varistor als Schutz gegen induzierte Spannungen an geschalteten Induktivitäten zu verwenden ist.
  
#### Aufgabe 2.1

**Nehmen Sie die Kennlinien folgender Bauteile am USB-Oszilloskop auf:**

- Silizium-Diode (SID)
- Germanium-Diode (GED)
- Zener-Diode (ZED)
- Varistor (VDR)
- Photodiode
- Photowiderstand
- LED (vier verschiedene Farben)

<img src="./figures/Kennlinienaufnahme.jpg" style="zoom:80%;float:right;" />

Für die Aufnahme der Kennlinien steht die Versuchsbox mit dem Schaltplan rechts zur Verfügung, an die das Eingangssignal über den Trenntransformator in Form einer sinusförmigen Wechselspannung ($f=100\,\mathrm{Hz}$) angelegt wird. Gemäß der Schaltung werden über einem Widerstand ($R=100\,Ω$) an Kanal A (CH A) und über dem jeweiligen Bauteil an Kanal B (CH B) Spannungen abgenommen. Mit Hilfe der XY-Darstellung der „PicoScope 6-Software“ kann dann die jeweilige Kennlinie aufgenommen werden.
Untersuchen Sie hierbei insbesondere:

- SID, GED und ZED auf ihre jeweilige Schwellenspannung und ggf. auch Zenerspannung
- Verhalten der Photodiode bei verschiedenen Beleuchtungen (z.B. auch Smartphone-Lampe)
- Verhalten des Photowiderstands bei verschiedenen Beleuchtungen
- Verschiedenfarbige LEDs auf ihre jeweilige Schwellenspannung und den Zusammenhang mit der Frequenz des emittierten Lichts

Interpretieren Sie die Kennlinien ausführlich und geben Sie charakteristische Punkte an. Berechnen Sie beim Photowiderstand aus der Steigung der Kennlinien den jeweiligen Widerstandswert. Schließen Sie auf typische Eigenschaften der Bauteile und leiten Sie daraus mögliche Anwendungen ab.

#### Aufgabe 2.2

**Untersuchen Sie qualitativ die Frequenzabhängigkeit einiger Bauelemente (bei $f=0,1\,\mathrm{kHz}$ bis $f=10\,\mathrm{kHz}$ ).**

---

### Aufgabe 3

**Beobachten Sie das Verhalten einer Photodiode unter Einfluss verschiedener Beleuchtungsstärken.**

Stellen Sie die Kennlinie einer Photodiode bei verschiedenen Beleuchtungsstärken dar und entnehmen Sie dieser jeweils den Sperrstrom. Verwenden Sie hierzu die Schaltung aus Aufgabe 2 aus der vorherigen Aufgabe bei $10\,\mathrm{Hz}$ sowie die regulierbare Experimentierleuchte mit Photodioden-Aufsatz. Beginnen Sie bei einer Lampenspannung von $2\,\mathrm{V}$ als niedrigste Stufe der Beleuchtung und beobachten Sie die Veränderung der Kennlinie bei zunehmender Spannung ($1\,\mathrm{V}$-Schritte) und Beleuchtungsstärke. Stellen Sie in der Auswertung den Zusammenhang zwischen Sperrstrom und Beleuchtungsstärke graphisch dar.

*Hinweis: Die Umrechnungstabelle zwischen Lampenspannung und Beleuchtungsstärke finden Sie im Unterordner `params` in `Umrechnung_Lampenspannung.csv`.*

---

### Aufgabe 4: Piezoelektrischer Effekt

**Untersuchen Sie den Piezoelektrischen Effekt am Piezoelement.**

- Beobachten Sie den direkten Piezoelektrischen Effekt am USB-Oszilloskop, indem Sie manuell verschiedene Drücke auf das Piezo-Plättchen ausüben. Machen Sie ein Frequenzsignal sichtbar, indem Sie mit dem Frequenzgenerator verschiedene Signale auf den Lautsprecher geben und diese auf das Piezoelement übertragen.
- Überprüfen Sie auch die Funktion des Piezoelements als Piezolautsprecher. Schließen Sie hierfür das Piezo-Element direkt an den Frequenzgenerator an.
- Beschreiben Sie Ihre Beobachtungen und nennen Sie Anwendungen des Piezoelektrischen Effekts.

---

### Aufgabe 5: Hochtemperatursupraleiter

**Bestimmen Sie die Sprungtemperatur eines  Hochtemperatursupraleiters.**

Messen Sie den Spannungsabfall am Hochtemperatursupraleiter mit Hilfe der fertig aufgebauten Vierleiterschaltung ($I_\mathrm{const}=63\,\mathrm{mA}$) und des Multimeters. Kühlen Sie die Probe von Raumtemperatur auf $77\,\mathrm{K}$ ab. Nutzen Sie hierfür den Temperaturgradienten über dem Stickstoff-Bad. Nehmen Sie eine Messreihe aus $U_\mathrm{gem}$ und zugehöriger Temperatur $T$ in $5\,\mathrm{K}$-Schritten auf. Beschreiben Sie das Verhalten des Hochtemperatursupraleiters.

- Tragen Sie zur Auswertung den Widerstand $R=U_\mathrm{gem}/I$ über der Temperatur $T$ auf und geben Sie die Sprungtemperatur an.
- Erklären Sie, warum zur Messung eine Vierleiterschaltung verwendet wird.

Beachten Sie, dass die Anzeige des Thermometers bei tiefen Temperaturen entsprechend der im Datenblatt angegebenen Tabelle `params/Temperatur_Korrektur.csv` vom wahren Wert abweicht. Für die Beurteilung der Sprungtemperatur beachten Sie, dass am Ort von Temperatursensor und Supraleiter ein hoher Temperaturgradient vorliegt.
