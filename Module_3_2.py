def send_email(message, recipient, sender="university.help@gmail.com"):
    if (not sender.endswith(('.ru', '.com', '.net')) or not recipient.endswith(('.ru', '.com', '.net')) or not '@' in sender or not '@' in recipient):
        return f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}"
    elif sender == recipient:
        return f"Нельзя отправить письмо самому себе!"
    elif recipient == 'vasyok1337@gmail.com':
        return f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}"
    else:
        return f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}"


print(send_email('Это сообщение для проверки связи',  'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', 'urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', 'urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', 'urban.teacher@mail.ru'))
