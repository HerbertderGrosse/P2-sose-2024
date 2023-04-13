<img src="./figures/Logo_KIT.svg" style="zoom:15%;float:right;" />

# Fakultät für Physik 

## Physikalisches Praktikum P2 für Studierende der Physik



Versuch P2-23, 24, 25 (Stand: März 2023)

[Raum F1-16](http://www-ekp.physik.uni-karlsruhe.de/~simonis/praktikum/layoutobjekte/Lageplan_P1.png)



# Laser-Optik, Teil B



## Motivation

Im Versuch "Laser-Optik, Teil A" haben Sie sich mit Hilfe einfacher Messungen mit den grundlegenden Eigenschaften und den Anwendungen von Lasern vertraut gemacht. In diesem Versuch können Sie Ihre experimentellen Erfahrungen um die Anwendung komplexerer interferometrischer Methoden zur Bestimmung kleinster Längenänderungen und um die Untersuchung der Eigenschaften doppelbrechender Kristalle mit Hilfe linear polarisierten Laserlichts erweitern. Den eigentlichen Versuchsteilen ist ein Demonstrationsversuch zur Veranschaulichung der Fourier-Transformation und ihrer Bedeutung in der Physik vorangestellt, der nahtlos an die Aufgaben des Versuchs "Laser-Optik, Teil A" anschließt. Beachten Sie hierzu die Hinweise zu diesem Versuch.

## Lernziele

Wir listen im Folgenden die wichtigsten **Lernziele** auf, die wir Ihnen mit dem Versuch **Laser-Optik, Teil B** vermitteln möchten: 

- Sie untersuchen den Zusammenhang zwischen dem physikalischen Phänomen der Beugung, als Streuung von (kohärentem) Licht und der Fourier-Transformation, am Beispiel der Beugung am Einfachspalt. Daei haben Sie die Möglichkeit eine vollautomatisierte Messanordnung genauer kennenzulernen.
- Sie untersuchen zwei Anwendungen für exakte interferometrische Messungen kleinster Längenänderungen. Dabei handelt es sich um die sehr kleinen (magnetostriktiven) Längenänderung von Nickel und um die direkte Bestimmung der Wellenlänge des verwendeten Laserlichts selbst.
- Sie untersuchen den Dopplereffekt von Licht, als intelligent durchdachte  Anwendung des Michelson-Interferometers. 
- Sie verwenden die Eigenschaft der linearen Polarisation des Laserlichts um den (Kristall im $\vec{B}$-Feld) Faraday- und (Kristall im $\vec{E}$-Feld) Pockels-Effekt zu studieren. Dabei bestimmen Sie verschiedene Materialkonstanten entsprechender doppelbrechender Kristalle.
- Sie untersuchen die optische Aktivität von Zuckerlösungen. Auch hierzu verwenden Sie die Eigenschaft der linearen Polarisation des kohärenten Laserlichts.

## Versuchsaufbau

Auf einer optischen Bank können neben einem $\mathrm{He}$-$\mathrm{Ne}$-Laser die optischen Aufbauten für die durchzuführenden Versuche montiert werden. Die Versuche befinden in separaten Kabinen. Ein Beispielaufbau ist in der folgenden Photographie abgebildet:   

<img src="./figures/LaserB.jpg" style="zoom:100%;" />

Für die verschiedenen Versuchsteile stehen Ihnen die folgenden Geräte und Materialien zur Verfügung: 

- Ein Experimentiertisch (mit $3\,\mathrm{m}$-Zeißschiene) mit diversen Verschiebereitern.
- Ein $2\,\mathrm{mW}$-$\mathrm{He}$-$\mathrm{Ne}$-Laser mit $\lambda_{0}=632,8\,\mathrm{nm}$ Wellenlänge (in geschlossener Bauweise mit integriertem Netzteil, mit polarisiertem Licht). 
- Ein Strahlaufweitungssystem (wie im Versuch Laser-Optik, Teil A), Justieraufbau mit Fassungen, Halter für Linsen und Blenden und ein großer weißer Schirm.
- Ein Multimeter (Voltcraft in verschiedenen Ausführungen).
- Ein Ampèremeter (Gossen Manometer, ohne Zusatzwiderstände $100\,\mathrm{mV}/1\,\mathrm{mA}$ (Vorsicht bei der Bedienung!), dazu [Shunt](https://de.wikipedia.org/wiki/Shunt_(Elektrotechnik))-Widerstände für $500\,\mathrm{mA}$ und für $5\,\mathrm{A}$ zur Messung der Spulenströme.
- Ein Funktionsgenerator FG 800/$0,2\,\mathrm{Hz}–200\,\mathrm{kHz}$.
- Ein Netzgerät für die Gleichspannung an der Pockelszelle, einstellbar bis $\approx1900\,\mathrm{V}$ mit integriertem Modulationstransformator.
- Jeweils ein Nieder (NF)- und Audiofrequenz(AF)-Verstärker.
- Stromversorgungsgerät/Labor-Netzgerät (stufenlos und kurzzeitig bis zu $4\,\mathrm{A}$ einstellbar).
- Ein Glan-Thompson Polarisationsfilter; Durchmesser $d=10\,\mathrm{mm}$, auf einem Stift drehbar montiert mit Winkelskala ([Extinktionsverhältnis](https://de.wikipedia.org/wiki/Extinktionsverh%C3%A4ltnis): $10^{5}/1$). **Diesen Filter dürfen Sie nicht im unaufgeweiteten Strahl benutzen!**
- In $25\,\mathrm{mm}$-Fassungen:
  - Ein Polarisationsfilter ohne Skala (nicht an allen Plätzen verfügbar),
  - Ein Spalt der Breite $0,4\,\mathrm{mm}$,
  - Eine Lochblende mit Durchmesser $1\,\mathrm{mm}$ (nicht an allen Plätzen verfügbar),
  - eine Irisblende,
  - Ein [Achromat](https://de.wikipedia.org/wiki/Achromat) mit Brennweite $f=10\,\mathrm{mm}$,
  - Sammellinsen mit Brennweiten $f=30\,\mathrm{mm}$, $60\,\mathrm{mm}$
    und $150\,\mathrm{mm}$ (die Linse mit $f=60\,\mathrm{mm}$ ist nicht an allen Plätzen verfügbar),
  - Tischlampe, Taschenlampe, 2 Laserschutzbrillen (nicht vollständigan allen Plätzen verfügbar).

-  Im Schrank:
  - Lichtdetektor Si-Photoelement BPW34 (kleinflächig), $2,7\,\mathrm{mm}\times2,7\,\mathrm{mm}$, nur im Elementbetrieb, d.h. ohne Betriebsspannung direkt an Spannungs- oder Strommessgerät angeschlossen, zu verwenden. Der Anschluss erfolgt an den mit "+" und "-" bezeichneten Stiften mit jeweils spezieller Leitung (einfach vorhanden).
  - Lichtdetektor Si-Photoelement, Durchmesser $d=12\,\mathrm{mm}$, wie bei Versuchsteil A (einfach vorhanden).
  - Lichtdetektor für moduliertes Licht (mit Photoelement $2,7\,\mathrm{mm}\times2,7\,\mathrm{mm}$, NF-Verstärker und Lautsprecher).
  - Ein Michelson-Interferometer mit Feinverstellung eines Spiegels durch $10:1$-Hebeluntersetzung und Mikrometerschraube, eine dazu aufsteckbare Antriebsrolle für Motorantrieb (drei mal vorhanden).
  - Ein Michelson-Interferometer, ein Spiegel auf einem $\mathrm{Ni}$- bzw. $\mathrm{Fe}$-Stab befestigt, Länge $\ell=105ß,\mathrm{mm}$, in einer Spule mit $n=2000$ Windungen (Jeweils einmal vorhanden).
  - Ein Synchronmotor ($1\,\mathrm{U/min}$, mit Antriebsrolle und Gummiriemen für die Bewegung des Interferometerspiegels.
  - Eine Küvette ($198\,\mathrm{mm}\times58\,\mathrm{mm}$, in einem Halter auf einem Stift, für optisch aktive Lösungen (zweimal in Plastik- und einmal in Glasausführung).
  - Haushaltszucker in zwei Gefäßen.
  - Eine Chemikalienwaage, $1\times$ Mettler H 315 auf einem Wägetisch und drei verschiedene mechanische Waagen.
  - Bechergläser, Messzylinder, Trichter.
  - Sorbose-Lösung (optisch aktiv, linksdrehend, Massenkonzentration $\beta=0,33\,\mathrm{g\,cm^{-3}}$.
  - Faraday-Modulator, Bleisilikatglas der Länge $\ell=75\,\mathrm{mm}$ in einer Spule mit $n=800$ Windungen.
  - Ein Radioapparat mit Zweitlautsprecherausgang und zugehöriger Anschlussleitung, als Modulationsquelle.
  - Ein Lichtdetektor für moduliertes Licht (mit Photoelement $2,7\,\mathrm{mm}\times2,7\,\mathrm{mm}$, NF-Verstärker und Lautsprecher.
  - Pockelszelle im Drehhalter mit Skala zur Angabe des Winkels zwischen Feld- und Laserpolarisationsrichtung, Lithiumniobat-Kristall,
    Höhe $h=2\,\mathrm{mm}$ (entspricht dem Elektrodenabstand), Länge $l=20\,\mathrm{mm}$, optische Achse parallel zur Feldrichtung.
  - Stimmgabel $1700\,\mathrm{Hz}$ ($2\times$), Maßband ($1\times$) , Stoppuhr ($5\times$).
  - Aufbau für die optische Bank mit Phototransistor, Schrittmotor und Endschaltern.
  - Vorverstärker, Schrittmotor- und Relais-Schnittstelle.
  - 2 Laserschutzbrillen (für das Betreuungspersonal).
  - Rechner (IBM-kompatibler PC 386SX) mit VGA-Graphikkarte, Graphik-Drucker, Maus, Festplatte, $1,2\,\mathrm{MB}$ und $1,44\,\mathrm{MB}$-Laufwerk und spezieller Schnittstellen-Karte (ADC, DAC, PIO), (nur einmal vorhanden).



## Wichtige Hinweise

- Bei diesem Versuch arbeiten Sie mit einem Laser, der entsprechend **gefährlich für Ihre Augen** sein kann. Gehen Sie daher **vorsichtig und verantwortungsbewusst** mit dem Laser um und halten Sie sich an die Anweisungen des/der Tutor:in.
- Achten Sie darauf, dass alle Personen im Raum bei der Durchführung des Versuchs eine **Schutzbrille** tragen. 
- Vermeiden Sie direkten Blickkontakt mit dem Laserstrahl und richten Sie ihn niemals auf andere Personen. Bleiben Sie beim Experimentieren in der Regel stehen, mit den Augen also weit oberhalb der Strahlhöhe.
- Stellen Sie sicher, dass die Laserleistung und -frequenz auf die vorgesehenen Werte eingestellt sind und überprüfen Sie dies regelmäßig während des Experiments.
- Beachten Sie, dass der Laserstrahl bei falscher Handhabung Schäden an optischen Elementen verursachen kann. Verwenden Sie nur die bereitgestellten optischen Elemente und reinigen Sie sie nur mit geeigneten Materialien.
- Vor dem Einschalten des Lasers müssen alle Geräte sorgfältig aufgebaut und justiert werden. Führen Sie diese Schritte **erst nach Rücksprache mit dem/der Tutor:in** durch.

## Durchführung

### **Aufgabe 1: Beugungsbild eines Spalts**

Hierbei handelt es sich um einen Demonstrationsversuch. Er soll von allen Gruppen gemeinsam und mit Unterstützung des Betreuers durchgeführt werden. Mithilfe eines auf einen Schrittmotor montierten Phototransistors messen Sie das Beugungsbild eines Spalts aus, der mit einem $\mathrm{He}$-$\mathrm{Ne}$-Laser ausgeleuchtet wird. Die gewonnenen Daten werden auf einem bereitstehenden Computer verarbeitet; aus der [Fourier-Rücktransformation](https://de.wikipedia.org/wiki/Fourier-Transformation) des aufgezeichneten Beugungsbildes erhalten Sie daraufhin das Bild des Spalts wieder. Dokumentieren und diskutieren Sie Ihre Beobachtungen. 

**Lösung:**

*Sie können Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.* 

---

### **Aufgabe 2: Anwendungen des [Michelson-Interferometers](https://en.wikipedia.org/wiki/Michelson_interferometer)**

**2.1:** Beobachten Sie interferometrisch die sehr geringe Abhängigkeit der Länge von Nickel vom Magnetfeld und bestimmen Sie den [Magnetostriktionskoeffizienten](https://de.wikipedia.org/wiki/Magnetostriktion).

**2.2:** Bestimmen Sie aus den beobachteten Änderungen des Interferenzbildes bei gemessener Verschiebung eines der Spiegel die Wellenlänge des Laserlichts.

**2.3:** Demonstrieren Sie den "[Dopplereffekt](https://de.wikipedia.org/wiki/Doppler-Effekt#Longitudinaler_Doppler-Effekt)" mit Lichtwellen im Fall $v\ll c$ und messen Sie interferometrisch eine extrem geringe Geschwindigkeit.

**2.4:** Bewegen Sie eine schwingende Stimmgabel von Ihrem Ohr weg und auf Ihr Ohr zu und zwar einmal mit und einmal ohne eine reflektierende Wand in der Nähe (akustisches Analogon zu Aufgabe 2.3). Dokumentieren und disutieren Sie Ihre Beobachtungen.

 **Lösung:**

*Sie können Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.* 

---

### **Aufgabe 3: Faraday- und Pockels-Effekt**

**3.1:**  Modulieren Sie die Intensität des Laserlichts durch Anwendung des [Faraday-Effekts](https://de.wikipedia.org/wiki/Faraday-Effekt), indem Sie das linear polarisierte Laserlicht erst einen Stab aus Bleisilikatglas im longitudinalen Magnetfeld einer Spule und dann einen Polarisationsfilter durchlaufen lassen.

**3.2:** Bestimmen Sie die [Verdet-Konstante](https://de.wikipedia.org/wiki/Verdet-Konstante) 
$$
\begin{equation*}
V \equiv \frac{\alpha}{B\,l}
\end{equation*}
$$
 

von Bleisilikatglas, wobei $B$ der Magnetfeldstärke und $l$ der Länge des Stabs entsprechen und $\alpha$ der Winkel ist, um den das linear polarisierte Licht beim Durchlaufen des Stabs gedreht wurde.

**3.3:**  Modulieren Sie die Intensität des Laserlichts durch Anwendung des [Pockels-Effekts](https://de.wikipedia.org/wiki/Pockels-Effekt), indem Sie das linear polarisierte Laserlicht einen Lithiumniobat-Kristall mit transversalem elektrischen Feld (Feldrichtung $45°$ gegen die Polarisationsrichtung des Laserlichts gedreht) und ein Polarisationsfilter ($90°$ gegen die Polarisationsrichtung des Laserlichts gedreht) durchlaufen lassen.

**3.4:** Bestimmen Sie die Konstante 
$$
\begin{equation*}
k \equiv \frac{\Delta n(E)}{E}
\end{equation*}
$$
für den Pockels-Effekt bei Lithiumniobat für die Wellenlänge des Laserlichts, wobei $\Delta n(E)$ der Änderung des Brechungsindex und $E$ der elektroschen Feldstärke ensprechen.

**Lösung:**

*Sie können Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.* 

---

### **Aufgabe 4: [Optische Aktivität](https://de.wikipedia.org/wiki/Optische_Aktivit%C3%A4t) (Saccharimetrie)**

**4.1:** Bestimmen Sie den [spezifischen Drehwinkel](https://de.wikipedia.org/wiki/Optische_Aktivit%C3%A4t#Spezifischer_Drehwinkel) 
$$
\begin{equation*}
\left[\alpha\right]_{\lambda}^{T} = \frac{\alpha}{\beta\,\ell}
\end{equation*}
$$


einer Haushaltszuckerlösung bei verschiedenen Massenkonzentrationen $\beta$ (gemessen in $\mathrm{g\,cm^{-3}}$) sowie die Drehrichtung. Dabei entsprechen $\alpha$ dem unspezifischen (gemessenen) Drehwinkel gemessen in $^{\circ}$ und $\ell$ der Länge des Lichtweges durch die Lösung (gemessen in $\mathrm{dm}$). Zeigen Sie, dass $\alpha\propto\ell$ und $\alpha\propto \beta$ gilt.  

Zum Nachweis von $\alpha\propto\ell$ genügt es zwei Messwerte aufzunehmen bei denen die Küvette mit der Probelösung einmal längs und einmal quer durchstrahlt wird. Zum Nachweis von $\alpha\propto\beta$ beginnen Sie z.B. bei $\beta\approx 0,3\,\mathrm{g\,cm^{-3}}$ und reduzieren die die KOnzentration, indem Sie Wasser zugießen. Diskutieren Sie von welchen weiteren Parametern $\alpha$ noch abhängt. 

Wenn Sie die Konzentration ändern, während Sie den durchtretenden Laserstrahl beobachten, scheint dieser "krummen Bahnen" zu folgen. Beachten Sie Ähnlichkeiten bei der optischen Aktivität und beim Faraday-Effekt.

**4.2:** Bestimmen Sie den spezifischen Drehwinkel einer entgegengesetzt drehenden [Sorbose](https://de.wikipedia.org/wiki/Sorbose)-Lösung mit vorgegebener Konzentration.

**Lösung:**

*Sie können Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.* 



