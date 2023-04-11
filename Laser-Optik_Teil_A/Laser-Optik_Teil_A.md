<img src="./figures/Logo_KIT.svg" style="zoom:15%;float:right;" />

# Fakultät für Physik 

## Physikalisches Praktikum P2 für Studierende der Physik



Versuch P2-16, 17, 18 (Stand: März 2023)

[Raum F1-29](http://www-ekp.physik.uni-karlsruhe.de/~simonis/praktikum/layoutobjekte/Lageplan_P1.png)



# Laser-Optik, Teil A



## Motivation

Mit diesem Versuch lernen Sie die grundlegenden Konzepte von [Lasern](https://de.wikipedia.org/wiki/Laser) und ihrer Anwendung in der modernen Physik kennen. Darüber hinaus können Sie Ihr Verständnis der Eigenschaften von Licht und elektromagnetischen Wellen vertiefen. 

Das Laser (*light amplification by stimulated emission of radiation*)-Prinzip beruht auf der 1916 von Albert Einstein erstmals beschriebenen stimulierten Emission elektromagnetischer Wellen. Der erste funktionsfähige Maser –noch im Mikrowellenbereich– wurde 1954 von [Charles Townes](https://de.wikipedia.org/wiki/Charles_H._Townes) realisiert. Die Übertragung des Maser-Prinzips zu den kürzeren Wellenlängen des sichtbaren Lichts gelang [Theodore Maiman](https://de.wikipedia.org/wiki/Theodore_Maiman) 1960 mit dem ersten [Rubinlaser](https://de.wikipedia.org/wiki/Rubinlaser). Seitdem wurden die Eigenschaften und Leistungsfähigkeit von Lasern kontinuierlich erweitert und verbessert. Laser sind eine brillante Quelle für [hoch-kohärentes Licht](https://de.wikipedia.org/wiki/Koh%C3%A4renzl%C3%A4nge). Sie sind damit Wegbereiter für interferometrische Längenmessungen oder die Untersuchung quantenmechanisch verschränkter Zustände. Sie finden Anwendung beim Nachweis von [Gravitationswellen](https://de.wikipedia.org/wiki/Gravitationswelle) sowie bei der Erzeugung von Qbits im [Quantencomputing](https://de.wikipedia.org/wiki/Quantencomputer). Von der Kommunikation und Datenspeicherung bis zur Materialbearbeitung und Medizin sind Laser zu wichtigen Werkzeugen in Wissenschaft und Technik geworden. 

## Lernziele

Wir listen im Folgenden die wichtigsten **Lernziele** auf, die wir Ihnen mit dem Versuch **Laser-Optik, Teil A** vermitteln möchten: 

- Sie machen sich mit dem Funktionsprinzip und den Eigenschaften eines Lasers vertraut.
- Sie üben sich darin optische Bauelemente entlang eines Laserstrahls auszurichten.
- Sie verwenden den Laser als ideale (kohärente) Lichtquelle für verschiedene Beugungs- und Interferenzmessungen.
- Sie erstellen eine holographische Abbildung.
- Sie erfahren, wie Laser in modernen Forschungsfeldern sowie der Kommunikation, der medizinischen Diagnostik und der Materialbearbeitung eingesetzt werden.

## Versuchsaufbau

Auf einer optischen Bank können neben einem $\mathrm{He}$-$\mathrm{Ne}$-Laser mehrere optische Bauelemente montiert werden. Zur Verfügung stehen mehrere Spalte, Blenden und Gitter, wie in der folgenden Photographie abgebildet:   

<img src="./figures/LaserA.jpg" style="zoom:100%;" />

Für die verschiedenen Versuchsteile stehen Ihnen die folgenden Geräte und Materialien zur Verfügung: 

- Ein offener $\mathrm{He}$-$\mathrm{Ne}$-Laser, (Spindler & Hoyer Typ 500, zu Demonstrationszwecken). Der Laser hat eine Leistung von $P=2\,\mathrm{mW}$ bei einer Wellenlänge von $\lambda=632,8\,\mathrm{nm}$. Er verfügt über ein Entladungsrohr, (um eine horizontale Achse gekippte) Brewster-Fenster, zwei Resonatorspiegel (mit Reflexionsgraden $R=99,7\,\%$ und $R=98\,\%$), entsprechende Schutzkappen, ein Versorgungsgerät, Filterkappen und ein Justierkreuz. Der Bereich zwischen Spiegel und Brewster-Fenster ist für Experimente zugänglich. **Dieser Aufbau ist nur einfach vorhanden!**
- $\mathrm{He}$-$\mathrm{Ne}$-Laser, Polytec PL-610P, mit einer Leistung von $P=5\,\mathrm{mW}$ (in geschlossener Bauform mit integriertem Netzteil, für polarisiertes Licht, siehe Bild). Ein solcher Laser befindet sich an allen Plätzen.
- Ein Experimentiertisch (mit $3\,\mathrm{m}$-Zeißschiene), diverse Reiter und Verschiebereiter.
- Ein kleinflächiger Lichtdetektor mit Phototransistor, in einem Gehäuse mit Anschlussbuchsen für eine Betriebsgleichspannung zwischen $9-15\,\mathrm{V}$ und ein entsprechendes Messinstrument. Dieser Lichtdetektor besitzt, durch eine entsprechende Frontlinse, eine ausgeprägte [Richtcharakteristik](https://de.wikipedia.org/wiki/Richtcharakteristik). Er ist sehr lichtempfindlich und leicht übersteuerbar. Er ist deshalb nur für geringe Lichtintensität vorgesehen.
- Ein Netzgerät ($2\times15\,\mathrm{V}$), für den Phototransistor. Sie können $1\times15\,\mathrm{V}$ sowohl an der roten als auch an der schwarzen Buchse abgreifen. 
- Ein großflächiger Lichtdetektor mit $\mathrm{Si}$-Photoelement (Durchmesser der Photodiode $d=12\,\mathrm{mm}$). Betreiben Sie diesen Lichtdetektor nur im Elementbetrieb, d.h. schließen Sie ihn ohne Betriebsspannung direkt an ein Spannungs- oder Strommessgerät an.
- Vielfachmessinstrument (Metex 3800 mit digitaler LCD-Anzeige (alle benötigten Messbereiche sind verfügbar), mit gleichem Innenwiderstand für alle Gleichstrombereiche. Daher ist die Anzeige auch über die Bereichsgrenzen hinaus proportional zur Intensität im $\mathrm{Si}$-Photoelement; Achtung: Verwenden Sie für die Schalterstellung des $20\,\mathrm{A}$-Bereichs die spezielle $20\,\mathrm{A}$-Buchse, die allgemeine $\mathrm{A}$-Buchse ist nur für Messungen im $20\,\mu\mathrm{A}$-Bereich vorgesehen.
- Strahlaufweitungssystem, bestehend aus einer Mikrobank auf einem Stift. Auf der Mikrobank befinden sich in entsprechenden Haltern spezielle, für die Laserlicht-Wellenlänge korrigierte Linsen mit Brennweiten von $f_{1}=10\,\mathrm{mm}$ und $f_{2}=150\,\mathrm{mm}$ im Abstand $f_{1}+f_{2}$, als [telezentrisches System](https://de.wikipedia.org/wiki/Telezentrisches_Objektiv). 
- Justieraufbau, bestehend aus einer Mikrobank auf einem Stift. Auf der Mikrobank befinden sich drei verschiebbare $25\,\mathrm{mm}$-Bauteil-Halter, von denen mindestens einer transversal justierbar ist. 
- Diverse Halter für Linsen, Blenden, Hologramme und sonstiges.
- Ein Eisen-Schirm mit Haftmagneten, um Papier daran zu befestigen, ein Planspiegel auf einem Stift mit Kugelgelenk.
- Eine Mattscheibe (in einem Halter auf einem Stift), eine Glasplatte (in einem Halter, drehbar um die horizontale Achse, mit Winkelskala).
- Ein Polarisationsfilter (mit Durchmesser $d=10\,\mathrm{cm}$, auf einem Stift, drehbar, mit Winkelskala). **Diesen sollten Sie nicht im unaufgeweiten Strahl benutzen!**
- Ein Hologramm ($8,5\,\mathrm{cm}\times10\,\mathrm{cm}$), in einem Halter auf einem Stift.
- Im Dia-Format: 
  - Strichgitter mit $570\,\mathrm{Strichen/mm}$, 
  - Kreuzgitter mit $13,4\,\mathrm{Strichen/mm}\times15\,\mathrm{Strichen/mm}$, 
  - Kreuzgitter mit $2,6\,\mathrm{Strichen/mm}\times3,8\,\mathrm{Strichen/mm}$;
  - Kreisblende mit Durchmessern $d=1;\,1.5;\,2\,\mathrm{mm}$.
- In $25\,\mathrm{mm}$-Fassungen: 
  - Strichgitter mit $100\,\mathrm{Strichen/cm}$, 
  - Kreuz- und Wabengitter (ohne Dimensionsangabe), 
  - Beugungsordnungsblende mit 5 speziellen Öffnungen, 
  - Beugungskante, 
  - Lochblende, mit Durchmesser $d=1\,\mathrm{mm}$, 
  - Scheibenblende, mit Durchmesser $d=1\,\mathrm{mm}$, 
  - Beugungssteg mit Breite $b=0,3\,\mathrm{mm}$, 
  - Verschiedene Spalten mit Breite $b=0,2\,\mathrm{mm}$, $0,3\,\mathrm{mm}$ und $0,4\,\mathrm{mm}$.
  - Doppelspalte mit Spaltbreite $b=0,25\,\mathrm{mm}$ und Abstand $\ell=0,5\,\mathrm{mm}$ und Spaltbreite $b=0,25\,\mathrm{mm}$ und Abstand $\ell=0,75\,\mathrm{mm}$, 
  - Dreifachspalt mit Spaltbreite $b=0,25\,\mathrm{mm}$ und Abstand $\ell=0,5\,\mathrm{mm}$, 
  - Vierfachspalt mit Spaltbreite $b=0,2\,\mathrm{mm}$ und Abstand $\ell=0,3\,\mathrm{mm}$,
  - Einstellspalt, Irisblende, Polarisationsfilter ohne Skala.
  - Linsen mit verschiedenen Brennweiten zwischen $10-150\,\mathrm{mm}$.
- Tischlampe, Taschenlampe, Maßband, Reinigungsutensilien.


## Wichtige Hinweise

- Bei diesem Versuch arbeiten Sie mit einem Laser, der entsprechend **gefährlich für Ihre Augen** sein kann. Gehen Sie daher **vorsichtig und verantwortungsbewusst** mit dem Laser um und halten Sie sich an die Anweisungen des/der Tutor:in.
- Achten Sie darauf, dass alle Personen im Raum bei der Durchführung des Versuchs eine **Schutzbrille** tragen. 
- Vermeiden Sie direkten Blickkontakt mit dem Laserstrahl und richten Sie ihn niemals auf andere Personen. Bleiben Sie beim Experimentieren in der Regel stehen, mit den Augen also weit oberhalb der Strahlhöhe.
- Stellen Sie sicher, dass die Laserleistung und -frequenz auf die vorgesehenen Werte eingestellt sind und überprüfen Sie dies regelmäßig während des Experiments.
- Beachten Sie, dass der Laserstrahl bei falscher Handhabung Schäden an optischen Elementen verursachen kann. Verwenden Sie nur die bereitgestellten optischen Elemente und reinigen Sie sie nur mit geeigneten Materialien.
- Vor dem Einschalten des Lasers müssen alle Geräte sorgfältig aufgebaut und justiert werden. Führen Sie diese Schritte **erst nach Rücksprache mit dem/der Tutor:in** durch.

## Durchführung

### **Aufgabe 1: Bestimmung des [Brewsterwinkels](https://de.wikipedia.org/wiki/Brewster-Winkel)**

Bei Gaslasern wird das [Entladungsrohr](https://de.wikipedia.org/wiki/Gasentladungsr%C3%B6hre) meist mit "Brewster-Fenstern" abgeschlossen. Überlegen Sie sich den Sinn dafür und demonstrieren Sie die Notwendigkeit. Gehen Sie dabei wie folgt vor: 

Montieren Sie einen drehbaren Plattenhalter mit planparalleler, sorgfältig geputzter Glasscheibe vor den Laser, verändern Sie den Einfallswinkel und beobachten Sie die Strahlintensität. Bestimmen Sie den Brewsterwinkel, und daraus den Brechungsindex $n$ des Glases. Sie können das Minimum der Reflexion ohne Intensitätsmessung an der Zimmerdecke beobachten. Für die Beobachtung des Maximums der Transmission können Sie z.B. das Si-Photoelement mit geeignetem Messinstrument benutzen. Ein solches Vorgehen ist aber ungenauer als die Beobachtung des Minimums. Diskutieren Sie warum dies so ist.

**Lösung:**

*Sie können Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.* 

---

### **Aufgabe 2: Beugung an Spalt, Steg, Kreisloch, Kreisblende und Kante**

**2.1:** Bestimmen Sie aus der Lage der Beugungsmaxima und -minima die nur ungefähr angegebenen Breiten ($b_{1}\approx 0,2\,\mathrm{mm}$ und $b_{2}\approx 0,3\,\mathrm{mm}$) der beiden Spalten.

**2.2:** Vergleichen Sie die Beugungsfigur eines gleichbreiten Steges mit der des entsprechenden Spalts ([Babinetsches Theorem](https://de.wikipedia.org/wiki/Babinetsches_Prinzip)).

**2.3:** Betrachten Sie die Beugungsbilder einer Kreisöffnung, einer gleichgroßen Kreisscheibe sowie einer Kante. Diskutieren Sie warum die Mitte der Beugungsfigur (der [Poisson-Fleck](https://de.wikipedia.org/wiki/Poisson-Fleck)) einer Scheibenblende stets hell ist.

**2.4:** Bestimmen Sie aus seiner Beugungsfigur den Durchmesser eines Haares. Vergleichen Sie das Ergebnis mit dem einer Messung mit Mikrometerschraube.

 **Lösung:**

*Sie können Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.* 

---

### **Aufgabe 3: Beugung an Mehrfachspalten und Gittern**

**3.1:**  Bestimmen Sie Spaltbreite $b$ und den -abstand ($\ell$) eines der Doppelspalte aus dessen Beugungsbild.

**3.2:** Machen Sie eine Voraussage und beobachten Sie dann: 

1. wie sich das Beugungsbild bei Verwendung eines zweiten Doppelspalts ändert; und 
2. wie sich das Beugungsbild des Dreifachspalts von dem des Doppelspalts (jeweils mit Spaltbreite $b=0,25\,\mathrm{mm}$, Spaltabstand $\ell=0,5\,\mathrm{mm}$) unterscheidet.


**3.3:**  Bestimmen Sie die Gitterkonstante $g$ eines der Strichgitter. Beobachten Sie das Beugungsbild. Diskutieren Sie welche Rolle dabei die Ausleuchtung spielt.

**3.4:** Beobachten Sie Beugungsbilder von Kreuz- und Wabengittern.

**Lösung:**

*Sie können Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.* 

---

### **Aufgabe 4: Abbildung nichtselbstleuchtender Gegenstände ([Abbésche Theorie](https://de.wikipedia.org/wiki/Auflösung_(Mikroskopie)#Abbe-Limit))**

Zeigen Sie, dass für die Abbildung durchstrahlter Objekte das Beugungsmuster des Lichts eine wichtige Rolle spielt. Gehen Sie dabei wie folgt vor:

Beleuchten Sie, je nach Wahl, ein Waben- oder Strichgitter (mit $100\,\mathrm{Strichen/cm}$) mit parallelem Licht und bilden Sie das Beugungsbild mit Hilfe einer Linse mit $150\,\mathrm{mm}$ Brennweite auf eine Mattscheibe ab. Sie können das Licht zuvor mit Hilfe eines fernen Planspiegels umlenken, so dass Sie die Mattscheibe in Lasernähe neben der optischen Bank positionieren und das Beugungsbild beim Justieren beobachten können. 

Eine [Beugungsordnungsblende](https://de.wikipedia.org/wiki/Beugungsscheibchen) in der bildseitigen Brennebene der Linse lässt das Beugungslicht entweder nur 0. oder 0. und 1. Ordnung durch. Da die Beugungsordnungsblende schwierig zu justieren ist, können Sie die 0. Ordnung auch mit einer Kreisblende (mit Durchmesser $d=1\,\mathrm{mm}$) ausblenden. Beobachten Sie das jeweils auf der Mattscheibe entstehende Bild. Versuchen Sie auch die Beobachtung der folgenden zwei weiteren Fälle: **Nur die 1. Ordnung** oder **nur die 2. Ordnung** passieren die Beugungsordnungsblende. Gitter, Linse und die dazu passende Beugungsordnungsblende werden in einem Justieraufbau montiert, die Beugungsordnungsblende kommt dabei in die nach allen Richtungen transversal zum Strahl verschiebbare Fassung. Zeichnen Sie zu diesem Versuch bei der Vorbereitung den Strahlengang. Wie könnte man den beobachteten Effekt benutzen, um etwa bei einem digitalisiert empfangenen Zeitungsbild das störende Raster verschwinden zu lassen? (Stichwort 'Image Enhancement'; Literatur: [Hecht/Zajac](Hecht/Zajac))

**Lösung:**

*Sie können Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.* 

---

### **Aufgabe 5: Holographie** 

Reproduzieren Sie ein Hologramm. Vergleichen Sie das reelle mit dem virtuellen Bild.

Weiten Sie den Laserstrahl hierzu jeweils geeignet auf. Überzeugen Sie sich davon, dass Sie wirklich **dreidimensional** beobachten können, d.h. dass sich je nach Beobachtungsposition die Perspektive ändert und zunächst Verborgene Details des Hologramms ggf. sichtbar werden. Das reelle Bild kann auf einem Schirm (weißes Papier) aufgefangen werden. Bewegen Sie den Schirm durch das Strahlungsfeld. Zeigen Sie, dass die Information über ein Gegenstandsdetail nicht nur an einer bestimmten Stelle des Hologramms gespeichert ist. Decken Sie hierzu verschiedene Bereiche des zunächst weit ausgeleuchteten Hologramms ab. Dokumentieren und diskutieren Sie Ihre Beobachtungen.

**Lösung:**

*Sie können Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.* 
