# Хак для сильно умных учеников

## Исправляет плохие оценки [электронного дневника школы](https://github.com/devmanorg/e-diary)

## Функции и сценарии использования

### get_schoolkid_by_name
  Получает объект ученика по его имени, если ученик не найден или их несколько, сообщает об ошибке.
#### Пример
  ```python
  ivan = get_schoolkid_by_name('Фролов Иван')
  ```

### fix_marks
  Исправляет двойки и тройки указанного ученика на пятёрки.
#### Пример
  ```python
  fix_marks(ivan)
  ```

### remove_chastisements
  Удаляет замечания указанного ученика из базы.
#### Пример
  ```python
  remove_chastisements(ivan)
  ```

### create_commendation
  Создает случайную хвалебную запись указанному великому уму 21 века по указанному предмету.
#### Пример
```python
create_commendation(ivan, 'Математика')
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).