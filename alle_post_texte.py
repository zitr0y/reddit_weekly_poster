
import logging 
import os
# Get the directory of the script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Set the current working directory to the directory of the script
os.chdir(dir_path)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='posterscript.log')


#################################################################################
# Hier einfach Texte ersetzen, jeweils einen für wenn es vorher schon einen Post gab, 
# dessen link im Programm gespeichert wurde, und einen ohne. Im Zweifel beide ohne!
#################################################################################

def post1_internationale_releases_text(with_link, variation):
    
    title = """Internationale Releases des letzten Monats"""
    
    if with_link:
        logging.info(f'Choosing text option with previously existing link: {with_link}')
        text = f"""**Willkommen zum monatlichen Austausch über die besten internationalen Releases!**
        
Wir alle wissen, dass Deutschrap von verschiedensten Einflüssen geprägt wird, und deshalb ist es wichtig, 
einen Blick über den Tellerrand zu werfen und zu sehen, was in der globalen Rap-Szene passiert. Wer als Rapper nur Hiphop hört betreibt Inzest, aber wer nur deutschen Hiphop hört ist noch schlimmer dran, oder so. 

Lasst uns wissen, welche internationalen Künstler euch im Moment besonders begeistern und welche Tracks bei euch rauf und runter laufen so wie Treppensteiger. 

___

^^Zum ^^letzten ^^Thread ^^zu ^^dem ^^Thema ^^geht ^^es ^^hier: ^^https://www.reddit.com/r/GermanRap/comments/{with_link}

    """
    else:
        logging.info(f'Choosing text option without previously existing link.')
        text = """**Willkommen zum monatlichen Austausch über die besten internationalen Releases!**
        
Wir alle wissen, dass Deutschrap von verschiedensten Einflüssen geprägt wird, und deshalb ist es wichtig, 
einen Blick über den Tellerrand zu werfen und zu sehen, was in der globalen Rap-Szene passiert. Wer als Rapper nur Hiphop hört betreibt Inzest, aber wer nur deutschen Hiphop hört ist noch schlimmer dran, oder so. 

Lasst uns wissen, welche internationalen Künstler euch im Moment besonders begeistern und welche Tracks bei euch rauf und runter laufen so wie Treppensteiger. 

    """
        
    return title, text

def post2_was_hoert_ihr_text(with_link, variation):

    title = """Was läuft bei euch zur Zeit an Musik?"""
    
    if with_link:
        logging.info(f'Choosing text option with previously existing link: {with_link}')
        text = f"""**Es ist wieder Zeit: Teilt, was bei euch läuft!**

Habt ihr Orwürmer oder einfach ein paar Banger auf Lager? Dann packt sie hier in die Kommentare! 
Hoffentlich können wir die seltenen Perlen des Deutschraps beleuchten und vielleicht findet von euch ja auch jemand eine(n) neue(n) Lieblingskünstler(in).

Ansonsten halt einfach Musik die Bock macht.    

___

^^Zum ^^letzten ^^Thread ^^zu ^^dem ^^Thema ^^geht ^^es ^^hier: ^^https://www.reddit.com/r/GermanRap/comments/{with_link}
    
    """
    else:
        logging.info(f'Choosing text option without previously existing link.')
        text = """**Es ist wieder Zeit: Teilt, was bei euch läuft!**

Habt ihr Orwürmer oder einfach ein paar Banger auf Lager? Dann packt sie hier in die Kommentare! 
Hoffentlich können wir die seltenen Perlen des Deutschraps beleuchten und vielleicht findet von euch ja auch jemand eine(n) neue(n) Lieblingskünstler(in).

Ansonsten halt einfach Musik die Bock macht.    
    
    """
    return title, text

def post3_collabothread_text(with_link, variation):
    
    title = """Monatlicher Collabo-Thread"""

    if with_link:
        logging.info(f'Choosing text option with previously existing link: {with_link}')
        text = f"""**Hier findet ihr jeden Monat aktuell an kooperation interessierte Künstler.** 
    
Du machst Musik (oder Artwork, Videos, Mastering,...)? Du willst damit nicht allein bleiben? 
Dann poste einen Kommentar, in dem du deine Kunst vorstellst und auch darlegst, was du dir von einer Kooperation erwartest. Möchtest du z.B. einen Gastpart auf nem Raptrack, einen Beat oder ein Coverart?
    
**Egal was, pack es hier rein und hoffentlich findest du genau wonach du suchst.**   


___

^^Zum ^^letzten ^^Thread ^^zu ^^dem ^^Thema ^^geht ^^es ^^hier: ^^https://www.reddit.com/r/GermanRap/comments/{with_link}
    """
    else:
        logging.info(f'Choosing text option without previously existing link.')
        text = """**Hier findet ihr jeden Monat aktuell an kooperation interessierte Künstler.** 
    
Du machst Musik (oder Artwork, Videos, Mastering,...)? Du willst damit nicht allein bleiben? 
Dann poste einen Kommentar, in dem du deine Kunst vorstellst und auch darlegst, was du dir von einer Kooperation erwartest. Möchtest du z.B. einen Gastpart auf nem Raptrack, einen Beat oder ein Coverart?
    
**Egal was, pack es hier rein und hoffentlich findest du genau wonach du suchst.**   
    """
    return title, text

def post4_reflektion_releases_text(with_link, variation):

    title = """Reflektion-Thread: Was war gut die letzten ~4 Wochen?"""

    if with_link:
        logging.info(f'Choosing text option with previously existing link: {with_link}')
        text = f"""**Willkommen im monatlichen Reflektion-Thread!**
    
Release-Freitage sind aufgrund der schieren Masse an neuer Musik oft überwältigend. 
Klar, erste Eindrücke über Releases kann man teilen, aber viele Tracks und Alben altern deutlich besser (oder schlechter) als ihr erster Eindruck.
    
Dafür ist dieser Thread: **Was war die letzte Zeit wirklich gut und ist es Wert nicht verpasst zu werden?** Teilt und diskutiert es hier in den Kommentaren!

___

^^Zum ^^letzten ^^Thread ^^zu ^^dem ^^Thema ^^geht ^^es ^^hier: ^^https://www.reddit.com/r/GermanRap/comments/{with_link}
    """
    else:
        logging.info(f'Choosing text option without previously existing link.')
        text = """**Willkommen im monatlichen Reflektion-Thread!**
    
Release-Freitage sind aufgrund der schieren Masse an neuer Musik oft überwältigend. 
Klar, erste Eindrücke über Releases kann man teilen, aber viele Tracks und Alben altern deutlich besser (oder schlechter) als ihr erster Eindruck.
    
Dafür ist dieser Thread: **Was war die letzte Zeit wirklich gut und ist es Wert nicht verpasst zu werden?** Teilt und diskutiert es hier in den Kommentaren!
    """
    return title, text

def post5_versteckter_thread_text(with_link, variation):
    title = """Der versteckte 5. Monatsthread: Merch-Appreciation und Vorschläge für zukünftige Special-Threads!"""
    
    if with_link:
        logging.info(f'Choosing text option with previously existing link: {with_link}')
        text = f"""**Willkommen im versteckten 5. Wochenthread**
        
___

Was nicht jedem bewusst immer direkt bewusst ist (mir), ist, dass jeder zweite Monat 5 Wochen hat. 
Und hier kommt ihr ins Spiel: Jeden 2. Monat gibt es einen Special-Thread, in dem wir uns über ein spezielles Thema austauschen können, welches nicht jeden Monat behandelt wird.
Uns fehlen hier noch Vorschläge für zukünftige Special-Threads, also haut mal raus, was euch so einfällt! 

Diesen Monat: **Merch-Appreciation und Vorschläge für zukünftige Special-Threads!**

Zeigt hier euer Lieblingsmerch und schreibt uns Ideen für zukünftige Special-Threads.

^^Zum ^^letzten ^^versteckten ^^Monatsthread ^^geht ^^es ^^hier: ^^https://www.reddit.com/r/GermanRap/comments/{with_link}
        
        """
    else:
        logging.info(f'Choosing text option without previously existing link.')
        text = """**Willkommen im versteckten 5. Wochenthread**
        
___

Was nicht jedem bewusst immer direkt bewusst ist (mir), ist, dass jeder zweite Monat 5 Wochen hat. 
Und hier kommt ihr ins Spiel: Jeden 2. Monat gibt es einen Special-Thread, in dem wir uns über ein spezielles Thema austauschen können, welches nicht jeden Monat behandelt wird. 
Uns fehlen hier noch Vorschläge für zukünftige Special-Threads, also haut mal raus, was euch so einfällt! 

Diesen Monat: **Merch-Appreciation und Vorschläge für zukünftige Special-Threads!**

Zeigt hier euer Lieblingsmerch und schreibt uns Ideen für zukünftige Special-Threads.
        
        """
    #elif variation == 1:
    #    pass
    #elif variation == 2:
    #    pass # To be implemented
    #elif variation == 3:
    #    pass
    #elif variation == 4:
    #    pass
    #elif variation == 5:
    #    pass
    return title, text

