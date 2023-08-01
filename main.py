    # 1
players = {'Вилли Сомерсет': '173см', 'Нэйт Робинсон': '170см', 'Херм Клоц': '170см', 'Спад Уэбб': '168см', 'Эрл Бойкинс': '165см'}
print('Баскетболисты:', players)
while True:
    print('Меню: \n'
          '0 - Выход; \n'
          '1 - Добавить баскетболиста; \n'
          '2 - Удалить; \n'
          '3 - Найти; \n'
          '4 - Заменить.')
    choice = int(input('Введите номер пункта меню: '))
    if choice == 1:
        name = input('Введите ФИО баскетболиста: ')
        height = input('Введите рост: ')
        players[name] = height
    elif choice == 2:
        deleted = input('Введите ФИО баскетболиста, которого необходимо удалить: ')
        players.pop(deleted)
    elif choice == 3:
        find = input('Введите ФИО, кого необходимо найти: ')
        if find in players:
            print(f'Рост баскетболиста {find}: {players[find]}')
        else:
            print(f'Баскетболист {find} не найден.')
    elif choice == 4:
        name = input('Введите ФИО баскетболиста, которого необоходимо заменить: ')
        players.pop(name)
        new_name = input('Введите ФИО баскетболиста, которого необоходимо добавить: ')
        new_height = input('Введите рост нового игрока: ')
        players[new_name] = new_height
    elif choice == 0:
        print('До новых встреч!')
        break
    else:
        print('Введен неверный пункт меню!!!!!!')
    print('Актуальный список игроков: ', players)

    # 2
wordbook = {}
print('Англо-французский словарь пуст, необходимо добавить элементы.')
while True:
    print('Меню: \n'
          '0 - Выход; \n'
          '1 - Добавить слово; \n'
          '2 - Удалить; \n'
          '3 - Найти; \n'
          '4 - Заменить.')
    choice = int(input('Введите номер пункта меню: '))
    if choice == 1:
        first = input('Введите слово: ')
        translate = input('Введите перевод: ')
        wordbook[first] = translate
    elif choice == 2:
        deleted = input('Введите слово, которое необходимо удалить: ')
        wordbook.pop(deleted)
    elif choice == 3:
        find = input('Введите слово, которое необходимо найти: ')
        if find in wordbook:
            print(f'Перевод слова {find}: {wordbook[find]}')
        else:
            print(f'Слово {find} не найдено.')
    elif choice == 4:
        name = input('Введите слово, которое необоходимо заменить: ')
        wordbook.pop(name)
        new_first = input('Введите слово, которое необоходимо добавить: ')
        new_translate = input('Введите перевод слова: ')
        wordbook[new_first] = new_translate
    elif choice == 0:
        print('До новых встреч!')
        break
    else:
        print('Введен неверный пункт меню!!!!!!')
    print('Актуальный список слов: ', wordbook)

    # 3
firm = {}
print('Информация о сотрудниках отсутствует, необходимо добавить элементы.')
while True:
    print('Меню: \n'
              '0 - Выход; \n'
              '1 - Добавить сотрудника; \n'
              '2 - Удалить; \n'
              '3 - Найти; \n'
              '4 - Заменить.')
    choice = int(input('Введите номер пункта меню: '))
    if choice == 1:
        name = input('Введите ФИО сотрудника: ')
        phone = input('Введите телефон сотрудника: ')
        email = input('Введите email сотрудника: ')
        position = input('Введите название должности сотрудника: ')
        room_number = input('Введите номер кабинета сотрудника: ')
        skype = input('Введите Skype сотрудника: ')
        firm[name] = {'Телефон': phone, 'Email': email,
                      'Должность': position, 'Номер кабинета': room_number,
                      'Skype': skype}
        print(f'Информация о сотруднике {name} добавлена в базу.')
    elif choice == 2:
        name = input('Введите ФИО сотрудника: ')
        if name in firm:
            del firm[name]
            print(f'Информация о сотруднике {name} удалена из базы.')
        else:
            print(f'Сотрудник {name} не найден в базе.')
    elif choice == 3:
        name = input('Введите ФИО сотрудника: ')
        if name in firm:
            print(f'Информация о сотруднике {name}: {firm[name]}')
        else:
            print(f'Сотрудник {name} не найден в базе.')
    elif choice == 4:
        name = input('Введите ФИО сотрудника: ')
        if name in firm:
            phone = input('Введите новый телефон сотрудника: ')
            email = input('Введите новый email сотрудника: ')
            position = input('Введите новое название должности сотрудника: ')
            room_number = input('Введите новый номер кабинета сотрудника: ')
            skype = input('Введите новый Skype сотрудника: ')
            firm[name] = {'Телефон': phone, 'Email': email,
                          'Должность': position, 'Номер кабинета': room_number,
                          'Skype': skype}
            print(f'Информация о сотруднике {name} обновлена.')
        else:
            print(f'Сотрудник {name} не найден в базе.')
    elif choice == 0:
        print('До новых встреч!')
        break
    else:
        print('Введен неверный пункт меню!!!!!!')
    print('Актуальная информация о сотрудниках:', firm)

    # 4
book_collection = {}
print('Книжная коллекция пуста, необходимо добавить элементы.')
while True:
    print('Меню: \n'
              '0 - Выход; \n'
              '1 - Добавить книгу; \n'
              '2 - Удалить; \n'
              '3 - Найти; \n'
              '4 - Заменить.')
    choice = int(input('Введите номер пункта меню: '))
    if choice == 1:
        author = input('Введите автора книги: ')
        title = input('Введите название книги: ')
        genre = input('Введите жанр книги: ')
        year = int(input('Введите год выпуска книги: '))
        pages = int(input('Введите количество страниц в книге: '))
        publisher = input('Введите название издательства: ')
        book_collection[title] = {'Автор': author, 'Жанр': genre,
                                  'Год выпуска': year, 'Количество страниц': pages,
                                  'Издательство': publisher}
        print(f'Информация о книге {title} добавлена в базу.')
    elif choice == 2:
        title = input('Введите название книги: ')
        if title in book_collection:
            del book_collection[title]
            print(f'Информация о книге {title} удалена из базы.')
        else:
            print(f'Книга {title} не найдена в базе.')
    elif choice == 3:
        title = input('Введите название книги: ')
        if title in book_collection:
            print(f'Информация о книге {title}: {book_collection[title]}')
        else:
            print(f'Книга {title} не найдена в базе.')
    elif choice == 4:
        title = input('Введите название книги: ')
        if title in book_collection:
            author = input('Введите автора книги: ')
            genre = input('Введите жанр книги: ')
            year = int(input('Введите год выпуска книги: '))
            pages = int(input('Введите количество страниц в книге: '))
            publisher = input('Введите название издательства: ')

            book_collection[title] = {'Автор': author, 'Жанр': genre,
                                      'Год выпуска': year, 'Количество страниц': pages,
                                      'Издательство': publisher}
            print(f'Информация о книге {title} обновлена.')
        else:
            print(f'Книга {title} не найдена в базе.')
    elif choice == 0:
        print('До новых встреч!')
        break
    else:
        print('Введен неверный пункт меню!!!!!!')
    print('Актуальная книжная коллекция: ', book_collection)