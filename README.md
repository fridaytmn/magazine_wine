# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Установка

Вам потребуется Python3 для выполнения данного кода. Если он у Вас не установлен, то перейдите на сайт http://www.python.org и загрузите Python последней версии и установите на вашу операционную систему.

После окончания установки Python3:

Для проверки работоспособности в командной строке выполните команду

```python --version```<br>

Если всё прошло без проблем, то вы увидите подобный вывод:

```Python 3.x```

После этого нужно в командной строкe перейти в папку с проектом 

```cd path```

где path это путь в папку с проектом например `C:\python\`

и затем выполнить команду <br>

```pip install -r requirements.txt```

## Запуск

- Заполните файл excel по примеру и сохраните его:
![image](https://user-images.githubusercontent.com/88648536/234756319-74f0603e-2f0b-4fb3-9db5-16ab62aac804.png)
- В колонку "картинка" необходимо поместить название фото вина, которую нужно разместить в `images` в папке проекта
- Колонка "Акция" позволяет добавлять ленточку "Выгодное предложение" на фото товара, если этого не требуется, ничего не указывайте в этой колонке
- Запустите сайт командой

```python3 main.py -f PATH```

Вместо `PATH` требуется ввести путь до файла например `C:\python\wine3.xlsx` или `wine3.xlsx` если файл находится в папке с кодом

- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).
- Вы должны увидеть следующий сайт (наполнение зависит от того что заполнено в excel файле)
![image](https://user-images.githubusercontent.com/88648536/234756527-7c4f66b7-22e3-45ba-b0c3-34542db23f0d.png)
![image](https://user-images.githubusercontent.com/88648536/234756562-2f2b1bc0-0f29-4d4e-87d1-cb02582f3518.png)
![image](https://user-images.githubusercontent.com/88648536/234756621-74e90519-e34e-478b-8fc2-bd769bad7f2b.png)
![image](https://user-images.githubusercontent.com/88648536/234756757-073aa75b-c857-4041-9a70-9206297f5fe4.png)


## Цели проекта

Код написан в учебных целях
