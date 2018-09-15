# Развертывание
1. Перейти в папку, куда вы собираетесь копировать, и выполнить 
`git clone https://github.com/ExplosiveJam/tehnotrack_django.git`
2. Создать и запустить виртуальное окружение 
```
virtualenv env --no-site-packages
source env/bin/activate
```
3. Установить зависимости проекта `pip install -r project/requirements.txt`
4. Далее действовать по инструкции https://djbook.ru/examples/77/, до п.6
5. Выполнить скрипт project/fill.py
6. Выполнить 
```
cd project
./manage.py migrate
./manage.py createsuperuser
./manage runserver
```
