def show_all(notes):
    print('Заметки:')
    for note in notes:
        print(f"    {note['id']}. {note['title']}")


def show(note):
    print(f"Заметка({note['id']}):")
    print(f"    Заголовок: {note['title']}")
    print(f"    Содержание: {note['body']}")
    print(f"    Создана: {note['created_at'].strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"    Обновлена: {note['updated_at'].strftime('%Y-%m-%d %H:%M:%S')}")
