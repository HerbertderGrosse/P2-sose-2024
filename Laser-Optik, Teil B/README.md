# Hinweise für den Versuch: "Laser-Optik, Teil B" 

##  Aufgabe 1: Beugungsfigur eines Spaltes

### Hinweise zur Durchführung:

Das Experiment hat demonstrativen Charakter. Es soll mit den übrigen Gruppen gemeinsam und mit Unterstützung des Betreuers ausgeführt werden. Ein Phototransistor mit schmalem Spalt wird rechnergesteuert von einem Schrittmotor durch die Beugungsfigur geführt und die Intensitäten werden gemessen. Der Verstärkungsfaktor eines Vorverstärkers wird dabei rechnergesteuert um bis zu drei Zehnerpotenzen verändert und an die jeweilige Intensität angepasst. Die intensitätsproportionalen Gleichspannungen werden durch einen Analog-Digital-Wandler (ADC) digitalisiert und im Rechner gespeichert. Das Rechnerprogramm enthält neben den Steuerroutinen (z.B. für den Schrittmotor und für die Verstärkerumschaltung) und den Messroutinen (z.B. für die A/D-Wandlung nach dem Prinzip der sukzessiven Approximation) auch Auswerteroutinen. Eine dieser Routinen setzt voraus, dass ein Einfachspalt als Beugungsobjekt dient. Dann kann zu den Wurzeln aus der Intensität jeweils das richtige Vorzeichen ergänzt und so eine Amplitudenfigur gewonnen werden. Ein FFT-Programm ('Fast Fourier Transform') transformiert diese dann zurück in ein Spaltbild. Die Darstellungen der Beugungsfigur und des berechneten Spaltbildes am Bildschirm können als Hardcopy am Drucker ausgegeben werden. Wegen der bei der Messung von Beugungsfiguren komplizierterer Objekte fehlenden Phaseninformation ist das Verfahren der Fourier-Rücktransformation dann nicht so einfach. Über Einzelheiten des Versuchsaufbaus, der Elektronik und des Programms informiert bei Interesse gerne das Personal im Praktikum. Beim Versuch wird aber keine Befassung mit Details erwartet.



---

## Aufgabe 2:  Anwendungen des Michelson-Interferometers  

### Hinweise zur Durchführung:

**2.1:** Einer der Interferometerspiegel sitzt bei diesem Interferometer auf der Stirnfläche des untersuchten Ni-Stabes, der von einer Spule umgeben ist. Der Strom durch die Spule soll nicht über 0,5A betragen und jeweils nur kurz eingeschaltet sein, weil sonst die thermische Ausdehnung den Magnetostriktionseffekt überdeckt. Nutzen Sie beide Stromrichtungen.

**2.2:** Ab hier wird ein anderes Interferometer als bei *2.1* benutzt! Notieren Sie mehrere Verschiebungen und die zugehörigen Anzahlen von Wechseln in der Interferenzfigur, denn die Auswertung soll mit Ausgleichsrechnung erfolgen.

**2.3:** Der Betreuer gibt Hinweise zur geeigneten Justierung des Interferometers. Der bewegte Spiegel stellt bei diesem Versuch sowohl einen bewegten Empfänger als auch eine bewegte Quelle dar. Bestimmen Sie $\Delta \nu$ durch Auszählen der Intensitätsschwankungen über bekannte Zeiten (Stoppuhr). Berechnen Sie dann aus $\Delta \nu$ und $\lambda$(Laser) die Spiegelgeschwindigkeit, die Sie zum Vergleich auch auf direkte Weise ermitteln sollen. Dass hier von Dopplereffekt gesprochen wird, obwohl es sich wie bei *2.2* um Änderungen der Interferenzfigur bei veränderter Spiegellage handelt, ist kein Widerspruch sondern eine äquivalente Beschreibung.



---

## Aufgabe 3: Faraday-Effekt und Pockels-Effekt
### Hinweise zur Durchführung:

**3.1:** Die Magnetfeldspule speisen Sie vom Zweitlautsprecher-Ausgang eines MP3-Players. Fangen Sie das modulierte Licht mit dem Photoelement in der Frontplatte des NF-Verstärkers mit Lautsprecher auf. Suchen Sie die günstigste Stellung des Polarisationsfilters (in der Nähe des Intensitätsminimums). Warum werden die hohen Frequenzen hier wohl so deutlich hörbar benachteiligt? Stellen Sie hier und bei den weiteren Aufgaben das Polarisationsfilter an Stellen möglichst großen Strahlquerschnitts auf!

**3.2:** Betreiben Sie dazu die Spule mit Gleichstrom. Wegen der Gefahr der Zerstörung und wegen hinderlicher Strahlkrümmung bei starker Erwärmung sind maximal 3A für kurze Zeit erlaubt. Eventuell sind Abkühlungspausen nötig. Wegen des kleinen Drehwinkels $\alpha$ ist die erreichbare Genauigkeit recht schlecht. Nutzen Sie beide Stromrichtungen aus. So gewinnen Sie immerhin den Faktor 2. Sie können probeweise statt der direkten Winkelmessungen auch Intensitätsmessungen machen und das [Malussche Gesetz](https://en.wikipedia.org/wiki/Polarizer#Malus.27s_law_and_other_properties) ausnutzen.

**3.3:**  Die Kondensatorplatten (Elektroden) am Kristall werden an die Serienschaltung von Gleichspannung (wenige 100V) und NF-Spannung (vom Lautsprecher-Ausgang eines MP3-Players über einen Transformator) angeschlossen. Moduliertes Licht wird mit dem Photoelement in der Frontplatte des NF-Verstärkers mit Lautsprecher an einer günstigen Stelle des Strahlungsfeldes empfangen. Das Laserlicht wird mit einer +10mm-Linse stark divergent gemacht. Dieses divergente Licht wird mit einer +30mm-Linse im Zentrum der Pockelszelle fokussiert, damit es die Zelle ohne Reflexion an den Seitenflächen des Kristalls passiert. Das austretende Licht liefert hinter einem Polarisationsfilter auf einem Schirm ein großflächiges Bild mit Hyperbelstruktur. Erläutern Sie das Zustandekommen dieses Bildes.

**3.4:** Die Anordnung ist die bei *3.3* beschriebene ohne NF-Einkopplung. Variieren Sie die Spannung an der Pockelszelle von -2000V bis +2000V und notieren Sie die Werte, bei denen im Zentrum der Hyperbelfigur Helligkeitsextrema (Maxima oder Minima) auftreten. Nummerieren Sie diese Extrema fortlaufend und bestimmen Sie die Steigung der Ausgleichsgeraden "Spannung über Nummer". Die Steigung heißt 'Halbwellenspannung'. Sie erhalten daraus $d\phi /dU$, die Änderung der Phasenverschiebung   $\phi = \frac{2 \pi}{\lambda_0} (n_{a0} - n_0)s = \frac{2\pi}{\lambda_0} \Delta n \cdot s$   zwischen ordentlichem und außerordentlichem Strahl längs der Strecke $s$ mit der Änderung der angelegten Spannung $U$. Mit der bekannten Vakuumwellenlänge $\lambda_0$ des Laserlichts und den bekannten geometrischen Daten des $LiNbO_3$-Kristalls ergibt sich dann die Konstante $k$. Beim Messen kann auf ein Photoelement mit Messinstrument verzichtet und auf das Auge vertraut werden. Beachten Sie, dass der verwendete Kristall auch ohne elektrisches Feld schon doppelbrechend ist. Beachten Sie die Ähnlichkeiten bei der Veränderung der Doppelbrechung bei mechanischer Spannung und bei Einwirkung eines elektrischen Feldes.


---

## Aufgabe 4: 

### Hinweise zur Durchführung:

**4.2:** Spülen Sie vor dem Einfüllen der Sorboselösung die Küvette gründlich. Zuckerreste stören! Verändern Sie hier die Konzentration nicht, und füllen Sie die vergleichsweise teure Lösung in die Flasche zurück.



---

## 
