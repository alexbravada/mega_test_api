# mega_test_api
API обработчик состояний приложений

Структура:
    app.py - тут содержится API  
    worker.py - выполняет функцию опроса БД на выявление аварий приложений каждые N минут.  
    senderrors.py - импортируемый в worker.py модуль отправки письма с текстом на эл.почту администратора   
    requirements.txt - список пакетов для установки в виртуальное окружение  
    
    
ИНСТРУКЦИЯ ПО ЗАПУСКУ ПРИЛОЖЕНИЯ:
  1. установить пакеты из requirements.txt   
      2. Открыть worker.py и ввести почту (Яндекса!) администратора или несколько имейлов получателей ошибок.    
        2.1. список на строчке №51 в функции mail_to_admin(error_message_to_admin, ['CHANGE_ME@yandex.ru'])  
        2.2 Настроить корректное время (в минутах) между отправкой статуса от приложений можно в строке №43 в переменной minute_responce = 1 (по умолчанию)  
        2.3 Настроить период (в минутах) вызова функции check_all_apps() можно на строке №59 schedule.every(период).minutes.do(scan_db)      
      3. Открыть окно в Terminal и запустить команду:  python worker.py    
      4. При этом запустится опрос состояний приложений, хранящихся в БД appInfo и в случае "аварий", будет посылать сообщение на почту администратору  
      5. Открыть новый Terminal, не закрывая первый и ввести python app.py  (для инициализации БД, если она ещё не была создана)  
      6. Для тестирования API в консоли, следует завершить процесс app.py с помощью Ctrl+C   
      7. Ввести python в текущий Terminal, а затем сделать несколько импортов:  
      8. from app import app, client  (достаточно только для отправки post запроса)  
      9. from models import *   (для того, чтобы из консоли делать запись в БД)  
      10. Пример передачи запроса к /api/apps/: client.post('/api/apps/', json = {"app_id":23, "message":"OK:200"})  ИЛИ client.post('/api/apps/', json = {"app_id":23})  
      11. Пример записи в БД:   
        11.1 var = appInfo(app_id = 999, message = "OK")  
        11.2 session.add(var)  
        11.3 session.commit()     


ЧТО МОЖНО БЫЛО БЫ ЕЩЁ РЕАЛИЗОВАТЬ?
    - Можно реализовать API к таблице, в которой будут храниться и удаляться актуальные работающие приложения (app_id),
    для того, чтобы проверять только актуальные id-приложений и не выдавать сообщения об авариях лишний раз.  
    
    # да, можно записать неактуальные app_id просто в список руками




