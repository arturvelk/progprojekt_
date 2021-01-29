# progprojekt
Progprojektem, remélem nem szar.

Röviden leírom itt hogy mi a lényege, illetve hogy mit szerettem volna amit nem tudtam megcsinálni.

Láthatjátok az aoc.py fájlt, amiben benne van minden függvény amit írtam, illetve minden package amire szükségem lesz. Több dolgot is használtam a főbbeket azért le is írom, használtam az aocd packaget, hogy kinyerjek valamiféle adatot arról, hogy az adott embernek mennyi csillagja van az advent of codeon, emellett a googel API rendszerét is használtam és a gspread packaget, amivel együtt tudtam szerkeszteni egy google docsot amiben az a táblázat van hogy kinek hány csillagja van (itt most egyenlőre csak Andor, Sebi és én vagyok, mert a többieket nem akartam zavarni azzal hogy elküldjék a session cookiejukat). Nos ezek a főbb packagek amiket használtam, emellett még használtam a yagmailt amivel küldöm az emailt Benyának.

Amit csinál a projekt:

Ez a working.py file kb és a példa.ipynb menete
Azoknak az egyéneknek (Andor, Sebi, én) akiknek megvan a session ID-jük, nekik leszedi az advent of coderól azt, hogy mennyi csillagjuk van az adott évben (2020), adott futás pillanatában. Ezt utána feltölti az aoc_data nevű google spreadsheetbe, miután mindegyik emberen végigmegy és feltöltötte a spreadsheetbe, leszedi az adatot, hozzávág az aljára egy szumma sort és elküldi ezt a dataframet pdf-ben benyának, vagy bárkinek akit megadok. 
