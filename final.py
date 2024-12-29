user_name = input('Введите имя пользователя')
content = input('Введите описание вашей заметки')
status = input('Введите статус заметки')
created_date = input('Введите дату создания заметки \'в формате дд.мм\'')
issue_date = input('Введите планируемую дату окончания заметки  \'в формате дд.мм\'')
title1 = input("Введите первый заголовок")
title2 = input("Введите второй заголовок")
note = [user_name, content, status, created_date, issue_date, [ title1, title2 ]
        ]
print(note)