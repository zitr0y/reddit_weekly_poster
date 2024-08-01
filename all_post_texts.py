####################################################################################################
# Description: This file contains the text for the different posts that are created by the bot.
# Change title and text to your liking.
####################################################################################################

post1_title = "Internationale Releases des letzten Monats"
post1_text = """
**Willkommen zum monatlichen Austausch über die besten internationalen Releases!**

Wir alle wissen, dass Deutschrap von verschiedensten Einflüssen geprägt wird, und deshalb ist es wichtig,
einen Blick über den Tellerrand zu werfen und zu sehen, was in der globalen Rap-Szene passiert. 
Wer als Rapper nur Hiphop hört betreibt Inzest, aber wer nur deutschen Hiphop hört ist noch schlimmer dran, oder so.

Lasst uns wissen, welche internationalen Künstler euch im Moment besonders begeistern und 
welche Tracks bei euch rauf und runter laufen so wie Treppensteiger.
"""

post2_title = "Was läuft bei euch zur Zeit an Musik?"
post2_text = """
**Es ist wieder Zeit: Teilt, was bei euch läuft!**

Habt ihr Orwürmer oder einfach ein paar Banger auf Lager? Dann packt sie hier in die Kommentare!
Hoffentlich können wir die seltenen Perlen des Deutschraps beleuchten und vielleicht findet von euch 
ja auch jemand eine(n) neue(n) Lieblingskünstler(in).

Ansonsten halt einfach Musik die Bock macht.
"""

post3_title = "Monatlicher Collabo-Thread"
post3_text = """
**Hier findet ihr jeden Monat aktuell an kooperation interessierte Künstler.**

Du machst Musik (oder Artwork, Videos, Mastering,...)? Du willst damit nicht allein bleiben?
Dann poste einen Kommentar, in dem du deine Kunst vorstellst und auch darlegst, was du dir von einer 
Kooperation erwartest. Möchtest du z.B. einen Gastpart auf nem Raptrack, einen Beat oder ein Coverart?

**Egal was, pack es hier rein und hoffentlich findest du genau wonach du suchst.**
"""

post4_title = "Reflektion-Thread: Was war gut die letzten ~4 Wochen?"
post4_text = """
**Willkommen im monatlichen Reflektion-Thread!**

Release-Freitage sind aufgrund der schieren Masse an neuer Musik oft überwältigend.
Klar, erste Eindrücke über Releases kann man teilen, aber viele Tracks und Alben altern 
deutlich besser (oder schlechter) als ihr erster Eindruck.

Dafür ist dieser Thread: **Was war die letzte Zeit wirklich gut und ist es Wert nicht verpasst zu werden?** 
Teilt und diskutiert es hier in den Kommentaren!
"""

post5_title = "Der 5. Monatsthread: Gebt uns Feedback zum Subreddit!"
post5_text = """
**Der Subreddit-Feedback-Thread**

___

Jeder zweite Monat hat 5 Wochen, und deshalb gibt es auch einen 5. Monatsthread. Aber nur alle 2 Monate.

Wir hatten die Idee, dass zweimonatlich eigentlich ein guter Zeitraum ist, um regelmäßig von euch Feedback zu sammeln. Wir wollen das Subreddit stetig verbessern und umso mehr input wir kriegen, desto besser können wir das auch tun.

Schreibt alles konstruktive was ihr wollt, oder orientiert euch an folgenden Fragen:


- **Wollt ihr mehr oder weniger von bestimmten Inhalten?**
- **Was gefällt euch (derzeit) besonders gut?**
- **Was gefällt euch (derzeit) nicht?**
- **Gibt es etwas, was wir sofort ändern sollten?**
- **Gibt es etwas, was wir langfristig ändern sollten?**
- **Habt ihr eine Idee um selbst dazu beizutragen, das Subreddit zu verbessern?**

Vielen Dank für euer Feedback!

Liebe Grüße, die Mods

"""

####################################################################################################
# End of changeable title and text. Do not change anything below this line.
####################################################################################################



post_contents = {
    "post1_internationale_releases": {"title": post1_title, "text": post1_text},
    "post2_was_hoert_ihr": {"title": post2_title, "text": post2_text},
    "post3_collabothread": {"title": post3_title, "text": post3_text},
    "post4_reflektion_releases": {"title": post4_title, "text": post4_text},
    "post5_versteckter_thread": {"title": post5_title, "text": post5_text}
}

def append_link(with_link):
    link_extra_text = f"""
___

^^Zum ^^letzten ^^Thread ^^zu ^^dem ^^Thema ^^geht ^^es ^^hier: ^^https://www.reddit.com/r/GermanRap/comments/{with_link}"""
    return link_extra_text

def get_post_text(post_name, with_link):
    """
    Get the title and text content for a given post.

    Args:
        post_name (str): The name of the post.
        with_link (str): Whether to append a link to the text content. If empty, no link will be appended, otherwise append_link will be called and the string will be added.

    Returns:
        tuple: A tuple containing the title and text content of the post.
    """
    post_info = post_contents.get(post_name, {})
    title = post_info.get("title", "")
    text = post_info.get("text", "")
    
    if with_link:
        text += append_link(with_link)
    
    return title, text