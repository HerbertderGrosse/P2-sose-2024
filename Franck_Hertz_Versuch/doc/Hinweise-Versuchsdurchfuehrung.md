# Hinweise für den Versuch Gammaspektroskopie

## Versuchsdurchführung



- Für die oszillographische Darstellung von $I_{\mathrm{A}}$ wird eine periodische Beschleunigungsspannung benötigt. Diese darf man aber nicht zu schnell ändern, da sich ein **stationärer Zustand in der Röhre** nur relativ langsam einstellt. Langsame Vorgänge sind z.B. die Bewegung und Rekombination der Ionen, sowie die Rückkehr von angeregten Zuständen in den Grundzustand, wenn diese optisch verboten sind. Das Betriebsgerät stellt eine periodische Sägezahnspannung zwischen $0-30\,\mathrm{V}$ zur Verfügung. Die Oszillographennutzung in diesem Modus empfiehlt sich zum Kennenlernen der Apparatur und beim Einstellen von Temperatur, $U_{1}$ und $U_{3}$. Um die Verhältnisse im quasi-stationären Zustand aufzuzeichnen, wird das Speicheroszilloskop mit der (langsamen) linearen Rampe oder per Hand als "Einmalvorgang" ausgelöst. Der Unterschied zu der sich wiederholenden Darstellung mit Hilfe der Sägezahnspannung wird in diesem Fall deutlich sichtbar. Die Daten ($U$-$I$-Wertepaare) können auf dem Rechner abgespeichert und anschließend analysiert werden.
- Der Heizofen für die Franck-Hertz-$\mathrm{Hg}$-Röhre ist mit einem $\mathrm{NiCr}$-$\mathrm{Ni}$ Temperaturfühler und mit einem Thermostaten ausgestattet. Bei Erreichen der Solltemperatur leuchtet die Leuchtdiode am Betriebsgerät grün. Der Ofen ist nicht geeignet, die Röhre homogen zu beheizen. Man kann beobachten, dass das $\mathrm{Hg}$ bevorzugt in bestimmten Bereichen der Glaswand kondensiert. Für den Dampfdruck ist die kälteste Stelle maßgebend. Ihre Temperatur kann von der des Temperaturfühlers geringfügig abweichen, auch wenn der empfindliche Teil des Temperaturfühlers sich im Ofen auf gleicher Höhe befindet.
- Eine weitere Konsequenz der nicht homogenen Beheizung der Franck-Hertz-$\mathrm{Hg}$-Röhre ist, dass es zu Ablagerungen von $\mathrm{Hg}$ an den Glaswänden kommen kann, wenn der Versuchsaufbau längere Zeit nicht in Betrieb ist. Kontinuierliche Ausgasungen von den Wänden der Röhre können gerade zu Beginn des Praktikumsbetriebs zu veränderlichem $\mathrm{Hg}$-Dampfdruck in der Röhre führen. Es empfiehlt sich daher die Röhre bereits einige Tage vor Beginn des Praktikumsbetriebs auszuheizen.  



### Aufgabe 1: Messanordnung

#### Aufgabe 1.2: Oszilloskopische Untersuchung des Signals

- Verwenden Sie für diese Aufgabe den MCA als Oszilloskop und ein Präparat Ihrer Wahl. Beobachten Sie die einlaufenden Signale. Beachten Sie die Einstellungen für $y$-Achsenabschnitt und Triggerschwelle. **Begründen Sie die Wahl des Präparat in Ihrem Protokoll.**  
- Um ein messbares Signal zu erhalten müssen Sie den Photondetektor bei einer Hochspannung (HV) von $U\approx600\,\mathrm{V}$ betreiben. Erhöhen Sie die Spannung vorsichtig, bis Sie erste Signale auf dem Oszilloskop sehen. 
- Diskutieren Sie in Ihrem Protokoll, welche Art von Signal Sie erwarten und beobachten.
- Diskutieren Sie in Ihrem Protokoll, wie sich die Signale für Photonen hoher oder niedriger Energie unterscheiden.
- Wenn Sie möchten können Sie Ihrem Protokoll ein Photo der Benutzeroberfläche zufügen. Ein Beispiel dafür, wie Sie externe Bilder direkt ins Jupyter-notebook einbinden können finden Sie [hier](https://gitlab.kit.edu/kit/etp-lehre/p1-praktikum/students/-/blob/main/tools/add_figures.ipynb).

#### Aufgabe 1.3: Spektrale Untersuchung des Signals

- Untersuchen Sie die Signale von $_{\hphantom{0}55}^{137}\mathrm{Cs}$, $_{27}^{60}\mathrm{Co}$ und $_{11}^{22}\mathrm{Na}$ **qualitativ**. Verwenden Sie hierzu den MCA als Spektrumanalysator. Diskutieren Sie in Ihrem Protokoll, welche Signale der oszilloskopischen Messung Sie jetzt wo im Spektrum erwarten. 
- Entscheiden Sie sich für einn Wert von $U$, den Sie dann für alle weiteren Messungen verwenden sollten. Begründen Sie Ihre Auswahl.

### Aufgabe 2: Analyse der Impulshöhenspektren

#### Aufgabe 2.1: Bestimmung des Untergrunds ohne Präparat

Führen Sie eine Leermessung durch, aus der Sie das Spektrum des erwarteten Untergrunds **ohne Präparat** bestimmen. Entscheiden Sie wie lange Sie diese Messung durchführen möchten. Dokumentieren und begründen Sie Ihre Entscheidung im Protokoll. 

#### Aufgabe 2.2: Bestimmung der Impulshöhenspektren verschiedener Präparate  

- Fügen Sie Ihrem Protokoll ein Diagramm des Spektrums für jedes Präparat ($_{\hphantom{0}55}^{137}\mathrm{Cs}$, $_{27}^{60}\mathrm{Co}$ und $_{11}^{22}\mathrm{Na}$) mit geeigneten Achsenbeschriftungen und Labels zu, so dass Sie die Spektren den Präparaten eindeutig zuordnen können. 
- Versuchen Sie **wirklich alle** charakteristischen Merkmale der jeweilgen Spektren zu klassifizieren und mit den damit assoziierten Prozessen im Photondetektor zu identifizieren. Sie können hierzu die matplotlib Funktion [annotate()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html) verwenden. Ein Beispiel hierfür finden Sie [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Gammaspektroskopie/tools/Annotations.ipynb). 
- Sie können die *cursor*-Funktion der graphischen Oberfläche dazu benutzen, um für jede Struktur die Kanäle der zentrale Position sowie des Bereichs zu bestimmen, in dem die entsprechende Struktur zu erkennen ist. Den Bereich können Sie bei der Bearbeitung der fogenden Aufgaben dazu nutzen, die Bereiche zu definieren, auf die Sie die Anpassung entsprechender Modelle einschränken möchten. Er sollte daher nach Möglichkeit etwa 2–3 Standardabweichungen ensprechen. **Notieren Sie sich die entsprechenden Kanäle für jede Struktur, die sie bestimmen möchten.**
- Sie können diese Spektren, für die erste Einreichung Ihres Protokolls (als Version v1) zunächst, **wie gemessen**, ins Protokoll aufnehmen. Auf der $x$–Achse sollten also die Kanäle des MCA oder entsprechende Histogramm-Bins stehen und das Spektrum sollte nicht auf den erwarteten Untergrund korrigiert sein. 
- **Die Primärdaten zur Erzeugung dieser Spektrum sollten Sie unbedingt vorhalten.** Für Ihre weitere Auswertung sollten Sie die Spketren dann sukzessive verbessern, indem Sie das erwartete Untergrundspektrum von den rohen Spektren subtrahieren und Ihre Kalibration aus **Aufgabe 2.3** auf die $x$-Achse anwenden, um Ihre Sprektren entsprechend aufzubereiten.

#### Aufgabe 2.3: Energie-Kalibration des Detektors 

- Nehmen Sie nun eine Kalibration von MCA-Kanälen (bzw. Histogramm-Bins) auf bekannte Photonenergien $E_{\gamma}$ vor. **Nutzen Sie hierzu alle Photonenergien, die Ihnen durch die Präparate zugänglich sind, verwenden Sie aber mindestens vier Punkte.**
- Sie können als Datenpunkte $i$ die Photopeaks, die Compton-Kanten und in einem Fall auch den Single-Escape Peak der Spektren für die Kalibration verwenden. Passen Sie an die entsprechenden Strukturen geeignete Modelle an, aus denen Sie für jeden Punkt $i$ die Energie $E_{\gamma}^{(i)}$ extrahieren können. 
- Für den Single-Escape und den Photopeak bietet sich eine [Normalverteilung](https://de.wikipedia.org/wiki/Normalverteilung) an, für die Compton-Kante die [Error function](https://en.wikipedia.org/wiki/Error_function). Beide sind aufgrund der statistischen Natur der zugrundeliegenden Prozesse sehr gut legitimiert. Aus allen Modellen sollten Sie einen Erwartungswert und eine Standardabweichung (für die spätere Verwendung in **Aufgabe 2.4**) bestimmen können.
- Entsprechende Beispiele für die Anpassung entsprechender Modelle finden Sie [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Gammaspektroskopie/tools). Beachten Sie, dass den eigentlichen Strukturen noch zusätzlich spektrale Komponenten aus überlagerten Prozessen unterliegen können, die Sie ggf. mit Hilfe eines zusätzlichen Polynom-Anteils in Ihrem Modell berücksichtigen können.
- Fügen Sie Ihrem Protokoll eine entsprechende Kalibrationskurve zu und passen Sie ein geeignetes Modell an diese Kurve an. 
- Sie können grundsätzlich von einem linearen Verlauf der Kalibrationskurve ausgehen. Nicht-Linearitäten können Sie z.B. dadurch testen, dass Sie ein Polynom höherer Ordnung anpassen und zeigen, dass die entsprechenden Parameter nach der Anpassung, im Rahmen ihrer aus der Anpassung bestimmten Unsicherheiten, mit Null verträglich sind. Beachten Sie auch den $\chi^{2}$-Wert der jeweiligen Anpassung. **Fügen Sie Ihrem Protokoll eine entsprechende Diskussion bei.**

#### Aufgabe 2.4: Relative Energie-Auflösung des Detektors

- Bestimmen Sie die relative Energieauflösung $\Delta E_{\gamma}/E_{\gamma}$ des Detektors als Funktion von $E_{\gamma}$ und fügen Sie Ihrem Protokoll eine entsprechende Darstellung zu. 

- Verwenden Sie hierzu am besten die Anpassungen der Normalverteilungen an die vorhandenen Photopeaks und ggf. den Single-Escape Peak in den Spektren, aus denen Sie die Erwartungswerte $\mu_{i}$ und Standardabweichungen $\sigma_{i}$ am einfachsten bestimmen können. Verwenden Sie dann entweder direkt $\sigma_{i}$ oder die daraus ermittelte [Halbwertsbreite](https://de.wikipedia.org/wiki/Halbwertsbreite) als Maß für die Energieauflösung des Detektors. 

- Als erwarteten Verlauf der relativen Energieauflösung können Sie z.B. das folgende Modell annehmen: 
  ```math
  \begin{equation*}
  \begin{split}
  \frac{\Delta E_{\gamma}}{E_{\gamma}}(A, B, C) 
  &= \frac{A}{\sqrt{E_{\gamma}}}\oplus\frac{B}{E_{\gamma}} \oplus C \\
  &=\sqrt{\frac{A^{2}}{E_{\gamma}}+\frac{B^{2}}{E^{2}_{\gamma}}+C^{2}} \\
  \end{split}
  \end{equation*}
  ```
  
  wobei $A$, $B$ und $C$ freie Parameter des Modells sind. Der Term zu $A $ entspricht dem Auflösungsverhalten aufgrund der zugrunde liegenden statistischen Prozesse. Beachten Sie, dass durchaus auch andere funktionale Zusammenhänge zur Auflösung beitragen können, die im oben angegebenen Modell mit den Parametern $B$ und $C$ verbunden sind.  Dabei kann es sich um Unsicherheiten aufgrund der Digitalisierung, Signalübertragung und anderen Quellen handeln. 

- Die erwartete Anzahl $\mu_{N_{\mathrm{e}}}$ der Elektronen an der Photokathode des im Photodetektor verbauten Photomultipliers können Sie dann aus Gleichung (**(4)** [hier](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/blob/main/Gammaspektroskopie/doc/Hinweise-Gammaspektroskopie.md)) anschätzen. **Nutzen Sie hierzu nur den Anteil der Auflösung der wirklich zum $1/\sqrt{E_{\gamma}}$-Verlauf gehört.** Fügen Sie Ihrem Protokoll eine entsprechende Darstellung zu.  

### Aufgabe 3: Detektorakzeptanz

- In die Akzeptanz des Detektors gehen Größen, wie die apparative Nachweiseffizienz $\epsilon$ aber auch die geometrische Akzeptanz $\Alpha$ des Detektors ein. Für isotrope Abstrahlung erwarten Sie für $\Alpha$ die Abhängigkeit
  ```math
  \begin{equation*}
  \Alpha\propto\frac{1}{d^{2}},
  \end{equation*}
  ```

  wenn $d$ der Abstand des Präparats vom Detektor ist.

- Bestimmen Sie die Rate aufgezeichneter Photonen für $_{\hphantom{0}55}^{137}\mathrm{Cs}$ bei fünf verschiedenen Abständen des Präparats von der Detektorstirnfläche und überprüfen Sie den erwarteten Zusammenhang. Stellen Sie die Datenpunkte in einem Diagramm dar und passen Sie ein geeignetes Modell daran an. 

- Den Effekt von Untergrundprozessen können Sie als konstante Rate in diesem Modell berücksichtigen. 

- Denn Effekt von pileup können Sie abschätzen, wenn Sie die untergrundkorrigierte Anzahl an Einträgen rechts des Photoleaks zählen, oder wenn Sie die Änderung der Rate als Funktion fon $d^{2}$ zu sätzlich als Funktion von $E_{\gamma}$ bestimmen.   

# Navigation

[Main](https://gitlab.kit.edu/kit/etp-lehre/p2-praktikum/students/-/tree/main/Gammaspektroskopie)