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