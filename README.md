<<<<<<< HEAD
=======

>>>>>>> 4204cb919a7c01216af26d73a9f7d714832af8b2
python  main.py --generate

python main.py --generate --lenght 16 --uppercase --digits --special

python main.py -g -l 16 -u -d -s

python main.py -g -l 16 -u -d -s --save --service gmail --login esheke@gmail.com

python main.py --find gmail


Должна быть длина наличие спец символов цифр регистра 
<<<<<<< HEAD
=======
Поиск необходимого пароля 
>>>>>>> 4204cb919a7c01216af26d73a9f7d714832af8b2

Запуск с детализацией:
python -m unittest -v

Запуск отдельных групп тестов:
python -m unittest test_generator -v
python -m unittest test_storage -v

Создание отчета о покрытии:
pip install coverage
coverage run run_tests.py
coverage report
coverage html

практияеская:
поиск пароля:
python main.py --find gmail

список всех паролей:
python main.py --list

добавить запись:
python main.py --generate --save --service twitch --login olgalihac@gmail.com

удаление записи:
python main.py --delete gmail

проверка в PostgreSQL:
"C:\Program Files\PostgreSQL\17\bin\psql.exe" -U postgres -d password_manager -c "SELECT * FROM passwords;"

подключение к бд:
"C:\Program Files\PostgreSQL\17\bin\psql.exe" -U postgres -d password_manager

показать что табл создана:
\dt

проверить структуру таблицы:
\d passwords

покакзать все данные:
SELECT * FROM passwords;