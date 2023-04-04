<img src="./figures/Logo_KIT.svg" style="zoom:15%;float:right;" />

# Fakultät für Physik 

## Physikalisches Praktikum P2 für Studierende der Physik



Versuch P2-33, 34 (Stand: März 2023)

[Raum F1-08](http://www-ekp.physik.uni-karlsruhe.de/~simonis/praktikum/layoutobjekte/Lageplan_P1.png)



# Spezifische Wärmekapazität



## Motivation

Im Jahr 1819 veröffentlichten die Physiker [Pierre Dulong](https://de.wikipedia.org/wiki/Pierre_Louis_Dulong) und [Alexis Petit](https://de.wikipedia.org/wiki/Alexis_Th%C3%A9r%C3%A8se_Petit) nach eingehenden Untersuchungen die Vermutung, dass die [molare Wärmekapazität](https://de.wikipedia.org/wiki/Molare_W%C3%A4rmekapazit%C3%A4t) für alle aus einzelnen Atomen zusammengesetzten Festkörper den gleichen Wert 
$$
C_{M} = 3\,R=24,9\,\mathrm{J\,mol^{-1}K^{-1}}
$$
haben könnte, wobei $R$ der idealen Gaskonstante entspricht. Diese Vermutung konnte später durch eine entsprechende Vorhersage aus der [statistischen Thermodynamik](https://de.wikipedia.org/wiki/Statistische_Thermodynamik) erklärt werden. Eine Konsequenz dieser Vorhersage war, dass $C_{M}$ für einatomige Festkörper konstant sein sollte. Später stellte sich jedoch heraus, dass die $C_{M}$ bei sehr tiefen Temperaturen ($T$) eine deutliche $T$-Abhängigkeit aufwies und und gegen Null strebte, ein Verhalten, dass im Rahmen der statistischen Thermodynamik nicht zu erklären war. Albert Einstein ([*Annalen der Physik*, 22 (1907)](http://echo.mpiwg-berlin.mpg.de/MPIWG:7BQGFZHC)) konnte dieses Phänomen als erster unter der Annahme erklären, dass Schwingungen im Festkörper, ebenso wie Strahlung in einem [Schwarzen Körper](https://de.wikipedia.org/wiki/Schwarzer_K%C3%B6rper) nur in Energiequanten aufgenommen und abgegeben werden können. Mit diesem Versuch unternehmen Sie erste Schritte in die Festkörperphysik: Sie haben die Möglichkeit mit einfachsten Methoden die Aussagen des Dulong-Petit Gesetzes für Aluminium und ein weiteres Metall experimentell nachzuprüfen und mit Hilfe von Flüssigstickstoff den Temperaturverlauf von $C_{M}$, ebenfalls an Aluminium, zu untersuchen. Damit weisen Sie eine der ersten Bruchstellen der klassischen Physik und einen der ersten Quanteneffekte im Praktikumsversuch selbst nach. 

## Lernziele

Wir listen im Folgenden die wichtigsten **Lernziele** auf, die wir Ihnen mit dem Versuch **Spezifische Wärmekapazität** vermitteln möchten: 

- Sie üben sich in der Planung, Dokumentation und Durchführung einfacher Experimente zur Bestimmung der [spezifischen Wärmekapazität](https://de.wikipedia.org/wiki/Spezifische_W%C3%A4rmekapazit%C3%A4t) verschiedener Metalle.
- Sie üben sich im gewissenhaften und exakten Experimentieren, sowie in der Abschätzung und Minimierung systematischer Effekte bei der Planung und Durchführung Ihrer Experimente.
- Sie untersuchen den Einfluss der Umgebung auf Experimente, die mit Wärme zu tun haben ([Wärmegang](https://de.wikipedia.org/wiki/W%C3%A4rme%C3%BCbergangskoeffizient)).
- Sie untersuchen die Abhängigkeit der spezifischen Wärmekapazität von der Temperatur, ein Phänomen, das im Rahmen der klassischen Thermodynamik nicht erklärt werden kann. 
- Sie üben sich im Umgang mit verantwortungsvollen [Flüssigstickstoff](https://de.wikipedia.org/wiki/Fl%C3%BCssigstickstoff) und führen ein Experiment bei tiefen Temperaturen durch. 
- Sie nutzen dabei den [thermoelektsichen Effekt](https://de.wikipedia.org/wiki/Thermoelektrizit%C3%A4t) zur Temperaturmessung.  


## Versuchsaufbau

Für die verschiedenen Versuchsteile stehen Ihnen die folgenden Geräte und Materialien zur Verfügung: 

- Ein [Dewargefäß](https://de.wikipedia.org/wiki/Dewargef%C3%A4%C3%9F) aus Glas ($V=250\,\mathrm{cm}^{3}$) als Kalorimeter, mit einem Plexiglasdeckel mit Einfüllöffnung und einem Trichter.
- Ein Halbleiterthermometer mit Digitalanzeige (in Schritten von $0,1^{\circ}\mathrm{C}$).
- Ein Quecksilberthermometer mit einem Messbereich von $-3$ bis $+50^{\circ}\mathrm{C}$ (mit Skaleneinteilungen von $0,2^{\circ}\mathrm{C}$). 
- Ein elektrischer Heisswasserbereiter ($V=300\,\mathrm{cm}^{3}$). 
- Eine Präzisionswaage. 
- Diverse Aluminium-, Messing- und Kupferzylinder, sowie Aluminium-, Blei-, Zinn-, Kupfergranulat. 
- Verschiedene weitere Messzylinder, [Erlenmeyerkolben](https://de.wikipedia.org/wiki/Erlenmeyerkolben), Bechergläser und Dewargefäße.
- Ein Aluminium-Hohlzylinder ($m=338\,\mathrm{g}$) mit eingebauter Heizwicklung ($I_{\mathrm{max}}=2\,\mathrm{A}$) und einem eingebauten Ni-CrNi-[Thermoelement](https://de.wikipedia.org/wiki/Thermoelement). Die Thermospannung als Funktion der Temperatur finden Sie im *params*-Verzeichnis in Ihrem gitlab-Repository (Dateiname: [*calibration.csv*](https://git.scc.kit.edu/etp-lehre/p2-for-students/-/blob/main/Spezifische_Waermekapazitaet/params/calibration.csv)). Die Stromversorgung für den Heizdraht liefert bis zu $5\,\mathrm{A}$ bei max. $16\,\mathrm{V}$.
- Einen Edelstahl- und einen Nalgene-Isolierbehälter (für Aufgabe 2).
- Ein Computer mit Picoscope TC08, als Datenlogger.
- Schutzbrillen, Schutzhandschuhe und Pinzetten.

<img src="./figures/Waermekapazitaet.jpg" style="zoom:60%;" />

## Wichtige Hinweise

- Der Umgang mit flüssigem Stickstoff erfordert besondere Vorsicht! Spritzer von flüssigem Stickstoff auf der Haut können bereits zu **schweren Verbrennungen** führen können. Tragen Sie daher immer Schutzhandschuhe und eine Schutzbrille im Umgang mit flüssigem Stickstoff!
- Werfen Sie keine Gegenstände in die Dewargefäße, da diese sonst leicht zerstört werden können.

## Durchführung

### Aufgabe 1: Spezifische Wärmekapazität im Wärmebad

Bestimmen Sie so genau, wie es mit den verfügbaren Geräten möglich ist, die spezifische Wärmekapazität von Aluminium und noch einem weiteren Metall, durch das Herstellen von Mischtemperaturen in einem Glas-Kalorimeter. Hierzu stehen Ihnen die Metalle Kupfer, Messing, Blei und Zinn zur Verfügung. 

Finden Sie durch Überlegung und dokumentierte Vergleichsexperimente heraus, wie ein solcher Versuch am besten durchzuführen ist. Wichtige Fragen, die Sie dabei für sich beantworten sollten sind z.B.: 

- Sollten Sie lieber ein kompaktes Metallstück benutzen oder ein Granulat? 
- Sollten Sie zur Herstellung der Mischtemperatur heißes Metall und kaltes Wasser verwenden oder umgekehrt? 
- Ist Wasser oder eine andere Flüssigkeit geeigneter? 
- Was sind günstigste Anfangs- bzw. Endtemperaturen für Ihre Messung? 
- Welche Massen (für Wasser und Metall) sollten Sie benutzen und wie und wann sollten Sie diese bestimmen? 
- Sollten Sie auf Massenfehler durch anhaftendes Wasser oder durch die an das Kalorimeter und Zubehör abgegebene Wärmemenge (Wärmegang) berücksichtigen? 
- Was ist ein geeignetes Thermometer in Hinblick auf Genauigkeit, Ablesbarkeit, oder störende Masse? 
- Genügt Ihnen jeweils eine Temperaturablesung oder sollten Sie Messung der Temperatur in Abhängigkeit von der Zeit bestimmen?
- Wäre es sinnvoll Hilfsmessungen, mit bekannten Sollergebnissen (z.B. mit Wasser-Wasser-Gemischen) vorzunehmen?

Beschreiben und begründen Sie Ihre Versuchsplanung, **messen Sie sorgfältig und dokumentieren Sie Ihr vorgehen.** Wiederholen Sie Messungen zur Abschätzung statistischer Variationen. Variieren Sie das Verfahren in den oben genannten Punkten, um systematische Effekte abzuschätzen. Äußern Sie sich am Ende der Auswertung noch einmal abschließend zum gewählten Verfahren und geben Sie mit Begründungen an, welche Versuchsbedingungen Sie wählen würden, wenn Sie den Versuch nochmal durchführen würden.

**Lösung:**

*Sie können Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.* 

---

### Aufgabe 2: Spezifische Wärmekapazität als Funktion der Temperatur

Messen Sie die spezifische Wärmekapazität von Aluminium in Abhängigkeit von der Temperatur in einem Bereich zwischen $100-300\,\mathrm{K}$. Kühlen Sie den Aluminium-Hohlzylinder mit flüssigem Stickstoff im Nalgene-Isolierbehälter auf $-196^{\circ}\mathrm{C}$ ab. Bereiten Sie den Edelstahl-Isolierbehälter durch Ausschwenken mit flüssigem Stickstoff auf die Aufnahme des kalten Aluminium-Hohlzylinders vor. Heizen Sie dann mit Hilfe der eingebauten Heizwicklung den Aluminium-Hohlzylinder innerhalb des Edelstahl-Isolierbehälters mit konstanter Heizleistung wieder auf und zeichnen Sie mit Hilfe des Datenloggers den Temperaturverlauf als Funktion der Zeit auf. 

Zu diesem Zweck ist ein NiCr-Ni-Thermoelement im Aluminium-Hohlzylinder befestigt; mit Hilfe von Eiswasser können Sie dem Thermoelement eine stabile Referenztemperatur von $0^{\circ}\mathrm{C}$ zur Verfügung stellen.

Sie können diese Messung schon starten, noch bevor Sie mit Aufgabe 1 beginnen. Sie läuft, abgesehen von gelegentlichen Kontrollen der Heizleistung, automatisch ab. Für die Berücksichtigung der dem Aluminium-Zylinder trotz Wärmeisolation durch die Umgebung zugeführten Wärme benötigen Sie eine zweite, gleichartige Messung, bei der die elektrische Heizung ausgeschaltet bleibt (eine sog. Nullmessung, zur Bestimmung des Wärmegangs). Eine solche Messung dauert $24$ Stunden, sie lässt sich also nicht an einem Versuchstag durchführen. Sie können daher einen entsprechenden Datensatz für Ihre Auswertung im *params*-Verzeichnis Ihres gitlab-Repositories finden, die Sie für Ihre Auswertung verwenden können (Dateiname: [*waermegang.csv*](https://git.scc.kit.edu/etp-lehre/p2-for-students/-/blob/main/Spezifische_Waermekapazitaet/params/waermegang.csv)).

 **Lösung:**

*Sie können Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.* 

