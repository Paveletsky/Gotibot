
# Внешние сервисы

- PostgreSQL: https://supabase.com/

- OpenAI: https://platform.openai.com/

## Получение данных POSTGRES

1. Регистрируемся на https://supabase.com/.
2. Создаем организацию "New project" > "New organization"
![App Screenshot](https://i.imgur.com/glTLOrE.png)

3. Называем проект, выбираем тип и тарифный план
![App Screenshot](https://i.imgur.com/F9n6x7y.png)

4. Далее называем проект и генерируем пароль к базе, сохранияем его в надежное местечко, он будет скрыт в дальнейшем
![App Screenshot](https://i.imgur.com/wQFNYkA.png)

5. Дожидаемся инициализации
![App Screenshot](https://i.imgur.com/wS2Q6yZ.png)

6. Переходим в настройки проекта, в Database и видим данные для подключения, вносим их в *.env*.
![App Screenshot](https://i.imgur.com/K3oA9xs.png)

## Получение OPENAI_KEY

1. Регистрируемся на https://platform.openai.com/ **(из РФ не получится, нужен будет VPN и не российский номер)**

2. После регистрации в правом углу жмем "Personal" > "View API Keys"
![](https://i.imgur.com/T5pAHgQ.png)

3. Жмем "Create new secret key", появляется окно, вписываем название ключа, нажимаем "Create secret key".
![](https://i.imgur.com/FsSetvF.png)

4. Копируем полученный ключ и вставляем в *.env*
![](https://i.imgur.com/c2iU8P3.png)

## BOT_TOKEN
Создаем и получаем в @BotFather.

## Запуск
```bash
python launch.py
```

### База знаний бота
*Документ находится по пути `openai/knowledges/all.txt`*

В нём данные заполняются в формате "фактов" через строку:

```
Я живой человек, если кто-то говорит что я робот, я пошлю его в хуй.
Меня зовут Вито Скалетта. Я родился на Сицилии, в 25-м году. 
```

В таком формате можно задать условия, проверку какой-либо информации и давать определенные ответы.

```
Если номер транзакции не 1, тогда я пошлю в хуй. 
Если номер транзакции 1, то поблагодарю за предоставленную информацию.
```

Далее ИИ сам делает своё дело.

### Прочая конфигурация
**Локализация**

*Находится по пути **`library/translations.py`***

**Коды авторизации**

*Находятся по пути **`library/config.py`***