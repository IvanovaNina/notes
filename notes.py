from datetime import datetime
import provider

notes = []


def get_notes() -> list:
    global notes
    return notes


def get_note(note_id):
    global notes
    return next((note for note in notes if int(note['id']) == note_id), None)


def empty() -> bool:
    global notes
    return len(notes) == 0


def add(title, body):
    global notes
    created_at = datetime.now()
    notes.append({
        'id': next_id(),
        'title': title,
        'body': body,
        'created_at': created_at,
        'updated_at': created_at
    })
    provider.save(notes)
    print(notes)


def edit(note, title, body):
    if title != '':
        note['title'] = title
    if body != '':
        note['body'] = body
    note['updated_at'] = datetime.now()
    provider.save(notes)


def remove(note):
    global notes
    notes.remove(note)
    provider.save(notes)


def load():
    global notes
    notes = provider.load()


def next_id() -> int:
    global notes
    note_id = 0
    for note in notes:
        if int(note['id']) > note_id:
            note_id = int(note['id'])
    return note_id + 1
