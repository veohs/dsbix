# dsbix
Eine aktualisierte Version der DSBApi von nerrixde.
Installieren Sie alle Anforderungen, bevor Sie installieren, oder verwenden Sie einfach 'pip install dsapi'.

Kontaktieren Sie mich auf Github (https://github.com/zfqtim) oder schreiben Sie mir eine E-Mail an zfq@tuta.io, wenn es Probleme gibt.

Dieses Repository funktioniert momentan, also werde ich es nicht aktualisieren, es sei denn, es gibt eine Art Änderung.

# Installation
Entweder mit `pip pip install dsbix` oder manuell `pip install git+https://github.com/zfqtim/dsbix.git#egg=dsbix`.

## Usage

Alle Arrays

> [!Important]
> Da DSBMobile von jeder Schule anders eingerichtet wird, kann es sein, **dass die Values vertauscht sind**.
> Ändert diese einfach, bis ihr die richtigen eures Stundenplanes habt.

| Key | Value | Notiz |
| :---         |     :---:      |          ---: |
|type|	Entfall|	Art des Eintrags|
|class|	10a|	Klasse|
|lesson|	1-2|	Schulstunde|
|room|	5.02|	(Neuer) Raum|
|new_subject|	F|	Neuer Kurs|
|subject|	M|	Ursprüngliches Fach / Kurs|
|new_teacher|	Boi|	Neuer Lehrer|
|teacher|	Grob|	Ursprünglicher Lehrer|
|date|	18.03.2024|	Datum|
|day|	Montag|	Wochentag|
|updated|	18.03.2024 15:13|	Letztes Update|

# Implentierung
Ich habe als Beispiel eine Version progranmmiert welche nach auswahl mir alle Änderungen der nächsten zwei Tage anzeigt. Wenn die Werte bei euch nicht Stimmen lest meine Notiz hierüber.
```
import dsbix


def fetch_entries_by_day(dsbclient, klasse, wanted_day):
    days = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag"]
    if wanted_day.capitalize() not in days:
        return "Ungültiger Tag. Bitte geben Sie einen gültigen Tag ein."

    entries = dsbclient.fetch_entries()
    final = []

    for s in range(len(entries)):
        for i in range(len(entries[s])):
            if entries[s][i]["class"] == klasse:
                if entries[s][i]["day"] == wanted_day.capitalize():
                    lesson = entries[s][i]["lesson"]
                    subject = entries[s][i]["new_subject"]
                    teacher = entries[s][i]["room"]
                    oldsubject = entries[s][i]["subject"]
                    room = entries[s][i]["new_teacher"]
                    vertreter = entries[s][i]["type"]
                    text = entries[s][i]["text"]
                    final.append({"lesson":lesson, "new_subject": subject, "room":room, "old_subject":oldsubject, "teacher":teacher, "type":vertreter, "text":text})

    message = f"Am {wanted_day.capitalize()} gibt es {str(len(final))} Einträge. "
    for s in final:
        message += f"In der {s['lesson']}. Stunde hast du {s['teacher']} mit {s['room']} in {s['old_subject']}. Grund dafür ist {s['text']}. "
    return message

klasse = "10a"
dsbclient = dsbix.DSBApi("299761", "cicero2223", tablemapper=['class','lesson','new_subject','room','subject','new_teacher','type','text'])

wanted_day = input("Geben Sie den gewünschten Tag ein (z.B. Montag): ")
result = fetch_entries_by_day(dsbclient, klasse, wanted_day)
print(result)
```


