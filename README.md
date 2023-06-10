# Урок 11. Домашнее задание <br>

---

> **main.py** - файл запуска программы <br>

Создать простое Flask приложение, которое бы работало с небольшой текстовой базой данных пользователей. Данные будут загружаться из файла JSON, работа с данными должна быть вынесена в функции, тестировать приложение рекомендуется с помощью Postman.

### **Шаг 1 – скопируйте данные**

Сохраните данные из раскрывашки ниже в JSON файл candidates.json.

- Содержание файла (раскрой меня!)
    
    ```python
    # candidates.json
    
    [
      {
        "id": 1,
        "name": "Adela Hendricks",
        "picture": "https://picsum.photos/200",
        "position": "Go разработчик",
        "gender": "female",
        "age": 40,
        "skills": "go, python"
      },
      {
        "id": 2,
        "name": "Sheri Torres",
        "picture": "https://picsum.photos/200",
        "position": "Delphi developer",
        "gender": "female",
        "age": 26,
        "skills": "Delphi, pascal, fortran, basic"
      },
      {
        "id": 3,
        "name": "Burt Stein",
        "picture": "https://picsum.photos/200",
        "position": "Team lead",
        "gender": "male",
        "age": 33,
        "skills": "делегирование, пользоваться календарем, обсуждать важные вопросы"
      },
      {
        "id": 4,
        "name": "Bauer Adkins",
        "picture": "https://picsum.photos/200",
        "position": "CTO",
        "gender": "male",
        "age": 37,
        "skills": "very important face"
      },
      {
        "id": 5,
        "name": "Day Holloway",
        "picture": "https://picsum.photos/200",
        "position": "HR manager",
        "gender": "male",
        "age": 35,
        "skills": "LinkedIn, telegram, spam, spam, spam"
      },
      {
        "id": 6,
        "name": "Austin Cochran",
        "picture": "https://picsum.photos/200",
        "position": "python-develop",
        "gender": "male",
        "age": 26,
        "skills": "python, html"
      },
      {
        "id": 7,
        "name": "Sheree Love",
        "picture": "https://picsum.photos/200",
        "position": "Django developer",
        "gender": "female",
        "age": 33,
        "skills": "Python, Django, flask"
      }
    ]
    ```
    

### Шаг 2 – напишите нужные функции

В отдельном файле, например, `utils.py`, напишите функции, которые будут получать данные. Названия функций вы  можете поменять на другие. 

- `load_candidates_from_json(path)` – возвращает список всех кандидатов
- `get_candidate(candidate_id)` – возвращает одного кандидата по его id
- `get_candidates_by_name(candidate_name)` – возвращает кандидатов по имени
- `get_candidates_by_skill(skill_name)` – возвращает кандидатов по навыку

Протестируйте каждую функцию отдельно, затем импортируйте функции в главный файл приложения. 

### **Шаг 3**

Установите Flask, скопируйте код минимального приложения 

Создайте представление для  `/`.

Выведите список всех кандидатов в формате:

```python
<h1>Все кандидаты</h1>
<p><a href="/candidate/<x>">Имя кандидата</a></p>
<p><a href="/candidate/<x>">Имя кандидата</a></p>
```

Вам понадобится создать шаблон, назовите его `list.html`

Необходимо сделать так, чтобы ссылки вели на странички кандидатов

### Шаг 4

Создайте представление для  `candidate/<x>`, который бы выводил данные про кандидата так: 

```python
<h1>Имя кандидата</h1>
<p>Позиция кандидата</p>
<img src="(картинка)" width=200/>
<p>Навыки кандидата</p>
```

Вам понадобится создать шаблон, назовите его `single.html` или `card.html`

**Шаг 5**

Создайте представление `/search/<candidate_name>` для поиска по совпадению

Выведите тех кандидатов, в имени у которых содержится `candidate_name`

```python
<h1>найдено кандидатов 2</h2>
<p><a href="/candidate/<x>">Leo Black</a></p>
<p><a href="/candidate/<x>">Leo Brown</a></p>
```

Вам понадобится создать шаблон, назовите его `search.html` 

**Шаг 6**

Создайте представление `/skill/<skill_name>` для поиска по навыкам.

Выведите тех кандидатов, в списке навыков у которых содержится `skill`.

```python
<h1>Найдено со скиллом X: 2/h2>
<p><a href="/candidate/<x>">Имя кандидата</a></p>
<p><a href="/candidate/<x>">Имя кандидата</a></p>
```

Вам понадобится создать шаблон, назовите его `skill.html`