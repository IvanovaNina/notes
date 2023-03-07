import notes
import view


def index():
    if notes.empty():
        print('Заметок нет')
    else:
        view.show_all(notes.get_notes())


def create():
    title = input('Введите заголовок заметки:')
    body = input('Введите заметку:')
    notes.add(title, body)


def delete():
    if notes.empty():
        print('Заметок нет')
    else:
        while True:
            print('Введите номер заметки или 0 для отмены')
            view.show_all(notes.get_notes())
            note_id = int(input(':'))
            if note_id <= 0:
                return
            note = notes.get_note(note_id)
            if note is None:
                print('Неверный номер')
            else:
                notes.remove(note)
                return


def update():
    if notes.empty():
        print('Заметок нет')
    else:
        while True:
            print('Введите номер заметки или 0 для отмены')
            view.show_all(notes.get_notes())
            note_id = int(input(':'))
            if note_id <= 0:
                return
            note = notes.get_note(note_id)
            if note is None:
                print('Неверный номер')
            else:
                title = input('Введите заголовок заметки:')
                body = input('Введите заметку:')
                notes.edit(note, title, body)
                return


def show():
    if notes.empty():
        print('Заметок нет')
    else:
        while True:
            print('Введите номер заметки или 0 для отмены')
            view.show_all(notes.get_notes())
            note_id = int(input(':'))
            if note_id <= 0:
                return
            note = notes.get_note(note_id)
            if note is None:
                print('Неверный номер')
            else:
                view.show(note)
                return
