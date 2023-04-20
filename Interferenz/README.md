# Hinweise für den Versuch "Interferenz"

Literatur zum Thema *Interferenz* findet sich in fast allen Physik- und speziell Optik-Lehrbüchern.

Im Folgenden befinden sich außerdem Informationen, die sehr gut als Anregung für die Vorbereitung verwendet werden können.

## Beugungsgitter

Für die Intensität $I$ in Abhängigkeit von Beobachtungswinkel $\alpha$, Wellenlänge $\lambda$, Gitterkonstante (Gitterperiode) $g$, verwendeter Anzahl $N$ der Gitterspalte und Breite $b$ des einzelnen Spalts
gilt
$$
I = \left(\frac{\sin\beta}{\beta}\right)^2 \cdot \left(\frac{\sin(N\Phi)}{\sin\Phi}\right)^2 = f_{\mathrm{S}} · f_{\mathrm{G}} = f_{\mathrm{S}} · \frac{f_1}{f_2},
$$
mit $\beta = \pi\,b/\lambda\,\sin\alpha$ und $\Phi = \pi\,g/λ\,\sin\alpha$.

- Der erste Faktor $f_{\mathrm{S}}$ beschreibt die Beugung am einzelnen Gitterspalt. Er wirkt als *Einhüllende* für die $I$-Kurve und wird auch als *Spaltfunktion* bezeichnet.
- Der zweite Faktor $f_{\mathrm{G}}$ beschreibt das Zusammenwirken aller Gitterspalte und wird auch als *Gitterinterferenzfunktion* bezeichnet. Der Faktor $f_{\mathrm{G}}$ hat (Haupt-)Maxima der Höhe $N$ bei den Winkeln $\alpha$, für die sowohl $f_1=0$ als auch $f_2=0$ gilt. An diesen Stellen ($\alpha = \arcsin (kλ/g)$, Ordnung $k \in N_0$) werden Linien beobachtet, sofern $f_{\mathrm{S}}$ dort keine Nullstelle aufweist. Bei großer Spaltanzahl $N$ liegen die Nullstellen ($f_1 = 0$, $f_2 \neq 0$) zwischen den Hauptmaxima so dicht, dass die Intensität dort nur vergleichsweise sehr geringe Werte erreicht (*Dunkelheit*). Die Halbwertsbreite der Linie bei einem Hauptmaximum ist etwa gleich dem Abstand zur benachbarten Nullstelle. Die Linienschärfe wird also mit zunehmender Spaltanzahl $N$ besser. Aus diesen Überlegungen folgt der Ausdruck $\lambda/\delta\lambda = kN$ für das *Auflösungsvermögen* des Gitters.
- Die angegebene Intensitätsformel gilt für ein spezielles ideales Gitter für das die folgenden Eigenschaften erfüllt:
  - bei $b$ herrscht perfekte Transmission ohne Phasenunterschiede;
  - bei $g$-$b$ herrscht perfekte Extinktion;
  - über das ganze Gitter herrscht perfekte Periodizität vor.
  - Ferner wird die auftreffende Lichtwelle als ebene Welle parallel zur Gitterfläche vorausgesetzt.
- Man erhält diese Formel, wenn man sich die Gitteröffnungen mit äquidistanten kohärenten Emittern besetzt denkt, deren Amplituden im Beobachtungspunkt $\vec{r}$ summiert werden und die Anzahl der Emitter dann gegen Unendlich gehen lässt. Reale Gitter weichen z.T. erheblich von diesen idealisierten Bedingungen ab.
- Neben diesem Gittertyp gibt es noch eine ganze Reihe weiterer. Einige Beispiele werden im Folgenden diskutiert:
  - Bei sinusförmig schwankender Durchlässigkeit (*Sinusgitter*) erhält man nur Linien 1. Ordnung. Solche Gitter kann man z.B. durch Photographie von Interferenzbildern herstellen.
  - *Phasengitter* sind überall durchsichtig, aber die Brechzahl ändert sich periodisch. Aufgrund der resultierenden Dichteunterschiede erhält man ein solches Gitter z.B. bei
  stehenden Schallwellen in Flüssigkeiten.
  - Weiter gibt es Reflexionsgitter, sowohl ebene und auch solche mit geneigten Furchen. Letztere (*Echelette-Gitter*) liefern die Hauptintensität in die 1. Ordnung statt nutzlos in die 0. Ordnung.
  - Schließlich seien neben den bisher genannten eindimensionalen Gittern noch zwei- und dreidimensionale erwähnt.

## Spalt

Einige Gedanken zum Spalt, der sich am Eingang des Spektrometers befindet. Es handelt sich hierbei nicht um eine Öffnung des Gitters, das in diesem Versuch verwendet wird.

1. Das Gitter wird im Idealfall mit Parallellicht (d.h. eine ebene Wellenfront) beleuchtet. Da es keine Spektrallampe (überhaupt keine Lampe) als Punktlichtquelle gibt, die man in den Brennpunkt einer idealen Linse stellen könnte, muss ein von einer ausgedehnten Gasentladung durchleuchteter schmaler Spalt als Ersatz dienen. Für die Sichtbarkeit der zu beobachtenden Linien muss der Spalt eine gewisse Mindestbreite haben. Soll die Formel für das Auflösungsvermögen des Gitters die Unterscheidung von Differenzen der Wellenlänge von $\Delta\lambda$ zulassen, darf das beobachtete Spaltbild aber nicht breiter sein als die aus der Intensitätsformel folgende Linienbreite.

- Frage: Wie breit dürfte der Spalt höchstens eingestellt werden?

2. Beobachtbare Interferenz (stationäres Hell-Dunkel-Muster) setzt ausreichende Kohärenz des Lichtes voraus. Da Licht von spontan und unabhängig strahlenden Atomen aus einem ausgedehnten räumlichen Bereich benutzt wird, benötigt man den Spalt (auch *Kohärenzspalt*), als effektive Begrenzung des Durchmessers der Lichtquelle. Dadurch wird erreicht, dass die möglichen Wegunterschiede des Lichtes von allen beitragenden Quellen (Atomen) klein gegen eine halbe Wellenlänge sind. Das erzwingt die *Kohärenzbedingung* $d\,\sin\epsilon << \lambda/2$, wobei $d$ die Quellen- bzw. Spaltbreite und $\epsilon$ den halben Öffnungswinkel des benutzten Lichtbündels beschreibt.

- Frage: Wie breit dürfte der Spalt höchstens eingestellt werden, um die Linsendurchmesser des Spektrometers (und damit auch die Spaltanzahl des Gitters) ausnutzen zu können?

## Spektralllampe

Die normale Lebensdauer angeregter Atomzustände (d.h. weder "verbotene" Übergänge, noch "metastabile" Zustände) ist etwa $10\,\mathrm{ns}$. Daraus folgt nach der [Heisenbergschen Unschärferelation](https://de.wikipedia.org/wiki/Heisenbergsche_Unsch%C3%A4rferelation) eine natürliche Energie- und damit Wellenlängenunschärfe $\Delta\lambda\approx10^{-5}\,\mathrm{nm}$. Da aber in einer Gasentladung die strahlenden Atome nicht in Ruhe sind, tritt zusätzlich Linienverbreiterung durch den [Doppler-Effekt](https://de.wikipedia.org/wiki/Doppler-Effekt) auf. Das angeregte Gas in den verwendeten Lampen ist nicht viel heißer als Zimmertemperatur. Die kinetische Gastheorie liefert die mittlere Teilchengeschwindigkeit von $\langle v\rangle\approx600\,\mathrm{m/s}$.

Die Dopplerverbreiterung (bis auf Faktoren nahe 1) ist 
$$
\begin{equation*}
\Delta \lambda\approx \frac{\langle v\rangle}{c}\lambda \, 2 \times 10^{-6} \lambda\approx 10^{-3}\,\mathrm{nm}.
\end{equation*}
$$
Man sieht, dass die Dopplerverbreiterung im Vergleich zu dem mit Praktikumsmitteln auflösbaren $\Delta\lambda$ noch keine Rolle spielt. Die *Stoßverbreiterung*, ein weiterer Effekt, der die Lebensdauer verkürzt und die Spektrallinie verbreitert, spielt wegen des niedrigen Druckes in den verwendeten Lampen eine noch geringere Rolle.

