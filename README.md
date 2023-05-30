установка

`pip3 install -r requirements.txt`

`python3 manage.py makemigrations`

`python3 manage.py migrate`


запуск через Docker

`docker build -t weather_app .`

`docker run -p 8000:8000 weather_app`

запуск через systemd

скопируйте файл weather-check.service в папку /etc/systemd/system/

`sudo systemctl start weather-check`

запуск через демон

`python3 weather_socket.py &`

TODO 
* JWT