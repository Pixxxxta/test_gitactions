# Тест-кейс: Проверка ГИБДД по номеру автомобиля без штрафов

### **ID тест-кейса:** TC-001

#### **Группа для запуска:** 1

##### **Test-name:** test_no_fines_car_number

**Описание:**  
Проверка ГИБДД по номеру автомобиля без штрафов

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Номер автомобиля: `В864РУ`
- Регион: `102`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в проверку штрафов ГИБДД
5. Проверить на наличие прошлых проверок с таким же автомобильным номером
6. Если такого номера в прошлых проверках нет 
    - 6.1. Нажать на кнопку "Добавить документ"
    - 6.2. Выбрать тип проверяемого документа - "Автомобиль"
    - 6.3. Ввести номер автомобиля в поле с номером
    - 6.4. Ввести регион в поле с регионом
    - 6.5. Нажать на кнопку "Проверить"
7. Если такой номер есть среди прошлых проверок:
   - 7.1 Нажать на этот номер 
8. Проверить наличие на экране надписи "ШТРАФОВ НЕТ, ПОЗДРАВЛЯЕМ!"


## Ожидаемый результат:

- Наличие на экране надписи "ШТРАФОВ НЕТ, ПОЗДРАВЛЯЕМ!"

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения



# Тест-кейс: Проверка ГИБДД по номеру автомобиля со штрафами

### **ID тест-кейса:** TC-002

#### **Группа для запуска:** 2

##### **Test-name:** test_have_fines_car_number

**Описание:**  
Проверка ГИБДД по номеру автомобиля со штрафами

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Номер автомобиля: `А555АА`
- Регион: `16`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в проверку штрафов ГИБДД
5. Проверить на наличие прошлых проверок с таким же автомобильным номером
6. Если такого номера в прошлых проверках нет 
    - 6.1. Нажать на кнопку "Добавить документ"
    - 6.2. Выбрать тип проверяемого документа - "Автомобиль"
    - 6.3. Ввести номер автомобиля в поле с номером
    - 6.4. Ввести регион в поле с регионом
    - 6.5. Нажать на кнопку "Проверить"
7. Если такой номер есть среди прошлых проверок:
   - 7.1 Нажать на этот номер 
8. Проверить наличие заполненного ФИО плательщика
   - 8.1. Если ФИО пустое или стоит "-", то заполнить входным параметром
   - 8.2. Если заполнено, то оставить как есть
9. Нажать кнопку "Оплатить"
10. Проверить наличие формы для оплаты


## Ожидаемый результат:

- Наличие на экране формы для оплаты штрафов

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка ГИБДД по водительскому удостоверению без штрафов

### **ID тест-кейса:** TC-003

#### **Группа для запуска:** 3

##### **Test-name:** test_no_fines_driver_num

**Описание:**  
Проверка ГИБДД по водительскому удостоверению без штрафов

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Водительское удостоверение: `9905723885`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в проверку штрафов ГИБДД
5. Проверить на наличие прошлых проверок с таким же водительским удостоверением
6. Если такого номера в прошлых проверках нет 
    - 6.1. Нажать на кнопку "Добавить документ"
    - 6.2. Выбрать тип проверяемого документа - "Водитель"
    - 6.3. Ввести водительское удостоверение в поле для ввода
    - 6.4. Нажать на кнопку "Проверить"
7. Если такое водительское удостоверение есть среди прошлых проверок:
   - 7.1 Нажать на это водительское удостоверение
8. Проверить наличие на экране надписи "ШТРАФОВ НЕТ, ПОЗДРАВЛЯЕМ!"


## Ожидаемый результат:

- Наличие на экране надписи "ШТРАФОВ НЕТ, ПОЗДРАВЛЯЕМ!"

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка ГИБДД по водительскому удостоверению со штрафами

### **ID тест-кейса:** TC-004

#### **Группа для запуска:** 4

##### **Test-name:** test_have_fines_driver_num

**Описание:**  
Проверка ГИБДД по водительскому удостоверению со штрафами

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Водительское удостоверение: `1231231231`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в проверку штрафов ГИБДД
5. Проверить на наличие прошлых проверок с таким же автомобильным номером
6. Если такого номера в прошлых проверках нет 
    - 6.1. Нажать на кнопку "Добавить документ"
    - 6.2. Выбрать тип проверяемого документа - "Водитель"
    - 6.3. Ввести Водительское удостоверение в поле для ввода
    - 6.4. Нажать на кнопку "Проверить"
7. Если такое водительское удостоверение есть среди прошлых проверок:
   - 7.1 Нажать на это водительское удостоверение
8. Проверить наличие заполненного ФИО плательщика
   - 8.1. Если ФИО пустое или стоит "-", то заполнить входным параметром
   - 8.2. Если заполнено, то оставить как есть
9. Нажать кнопку "Оплатить"
10. Проверить наличие формы для оплаты


## Ожидаемый результат:

- Наличие на экране формы для оплаты штрафов

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка ГИБДД по UIN без штрафов

### **ID тест-кейса:** TC-005

#### **Группа для запуска:** 5

##### **Test-name:** test_no_fines_UIN

**Описание:**  
Проверка ГИБДД по номеру автомобиля без штрафов

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- УИН: `18810578230828569031`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в проверку штрафов ГИБДД
5. Проверить на наличие окна с прошлыми проверками
6. Если такое окно появилось: 
    - 6.1. Нажать на кнопку "Добавить документ"
7. Выбрать тип проверяемого документа - "УИН"
8. Ввести УИН в поле для ввода
9. Нажать на кнопку "Проверить"
10. Проверить наличие на экране надписи "ШТРАФОВ НЕТ, ПОЗДРАВЛЯЕМ!"


## Ожидаемый результат:

- Наличие на экране надписи "ШТРАФОВ НЕТ, ПОЗДРАВЛЯЕМ!"

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка судебных задолженностей без штрафов

### **ID тест-кейса:** TC-006

#### **Группа для запуска:** 5

##### **Test-name:** test_payment_courts_debts_page_no_arrears

**Описание:**  
Проверка судебных задолженностей без штрафов

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- ФИО: `Хазиев Дмитрий Артурович`
- Дата рождения: `08.11.2002`
- Регион для проверки долгов: `Республика Башкортостан`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в проверку судебных задолженностей
5. Проверить на наличие прошлых проверок с такими же тестовыми реквизитами
6. Если такой проверки нет 
    - 6.1. Нажать на кнопку "Добавить документ"
    - 6.2. Ввести ФИО на русском языке
    - 6.3. Ввести дату рождения
    - 6.4. Открыть выпадающий список для региона проверки
    - 6.5. Ввести регион в строку поиска
    - 6.6. Нажать на нужный регион
    - 6.7. Нажать на кнопку "Проверить"
7. Если такая проверка есть среди прошлых проверок:
   - 7.1 Нажать на эту проверку
8. Проверить наличие на экране надписи "ШТРАФОВ НЕТ, ПОЗДРАВЛЯЕМ!"


## Ожидаемый результат:

- Наличие на экране надписи "ШТРАФОВ НЕТ, ПОЗДРАВЛЯЕМ!"

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка судебных задолженностей со штрафами

### **ID тест-кейса:** TC-007

#### **Группа для запуска:** 6

##### **Test-name:** test_payment_courts_debts_page_have_arrears

**Описание:**  
Проверка судебных задолженностей со штрафами

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- ФИО: `Максуди Иннокентий Рустемович`
- Дата рождения: `09.03.1986`
- Регион для проверки долгов: `Республика Татарстан (Татарстан)`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в проверку судебных задолженностей
5. Проверить на наличие прошлых проверок с такими же тестовыми реквизитами
6. Если такой проверки нет 
    - 6.1. Нажать на кнопку "Добавить документ"
    - 6.2. Ввести ФИО на русском языке
    - 6.3. Ввести дату рождения
    - 6.4. Открыть выпадающий список для региона проверки
    - 6.5. Ввести регион в строку поиска
    - 6.6. Нажать на нужный регион
    - 6.7. Нажать на кнопку "Проверить"
7. Если такая проверка есть среди прошлых проверок:
   - 7.1 Нажать на эту проверку
8. Проверить наличие заполненного ФИО плательщика
   - 8.1. Если ФИО пустое или стоит "-", то заполнить входным параметром
   - 8.2. Если заполнено, то оставить как есть
9. Нажать кнопку "Оплатить"
10. Проверить наличие формы для оплаты


## Ожидаемый результат:

- Наличие на экране появилась форма для оплаты штрафов

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка МВД по паспорту иностранного гражданина без штрафов

### **ID тест-кейса:** TC-008

#### **Группа для запуска:** 1

##### **Test-name:** test_no_fines_mvd

**Описание:**  
Проверка МВД по паспорту иностранного гражданина без штрафов

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Тип документа: `Паспорт иностранного гражданина`
- Номер паспорта: `FA6169954`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в проверку штрафов МВД
5. Проверить на наличие прошлых проверок с такими же тестовыми реквизитами
6. Если такой проверки нет 
    - 6.1. Нажать на кнопку "Добавить документ"
    - 6.2. Открыть выпадающий список с типом документа
    - 6.3. Выбрать нужный тип документа
    - 6.4. Ввести номер документа в поле для ввода
    - 6.5. Нажать на кнопку "Проверить"
7. Если такая проверка есть среди прошлых проверок:
   - 7.1 Нажать на эту проверку
8. Проверить наличие на экране надписи "ШТРАФОВ НЕТ, ПОЗДРАВЛЯЕМ!"


## Ожидаемый результат:

- Наличие на экране надписи "ШТРАФОВ НЕТ, ПОЗДРАВЛЯЕМ!"

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка МВД по паспорту иностранного гражданина со штрафами

### **ID тест-кейса:** TC-009

#### **Группа для запуска:** 2

##### **Test-name:** test_have_fines_mvd

**Описание:**  
Проверка МВД по паспорту иностранного гражданина со штрафами

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Тип документа: `Паспорт иностранного гражданина`
- Номер паспорта: `FA2684557`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в проверку штрафов МВД
5. Проверить на наличие прошлых проверок с такими же тестовыми реквизитами
6. Если такой проверки нет 
    - 6.1. Нажать на кнопку "Добавить документ"
    - 6.2. Открыть выпадающий список с типом документа
    - 6.3. Выбрать нужный тип документа
    - 6.4. Ввести номер документа в поле для ввода
    - 6.5. Нажать на кнопку "Проверить"
7. Если такая проверка есть среди прошлых проверок:
   - 7.1 Нажать на эту проверку
8. Проверить наличие заполненного ФИО плательщика
   - 8.1. Если ФИО пустое или стоит "-", то заполнить входным параметром
   - 8.2. Если заполнено, то оставить как есть
9. Нажать кнопку "Оплатить"
10. Проверить наличие формы для оплаты


## Ожидаемый результат:

- Наличие на экране формы для оплаты штрафов

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Оплата патента с правильными реквизитами

### **ID тест-кейса:** TC-010

#### **Группа для запуска:** 1

##### **Test-name:** test_payment_patent

**Описание:**  
Оплата патента с правильными реквизитами

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Серия и номер патента: `77 2204315436`
- Дата выдачи патента: `01.01.2020`
- Фамилия (на русском языке): `АБДУРОСУЛОВ`
- Имя (на русском языке): `ДОСТОН`
- Серия и номер паспорта: `FA6169953`
- ИНН: `971510764678`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в оплату патента
5. Проверить на наличие прошлых проверок с таким же номером патента
6. Если такой проверки нет 
    - 6.1. Нажать на кнопку "Добавить патент"
    - 6.2. Ввести серию и номер патента в соответствующее поле для ввода
    - 6.3. Ввести дату выдачи патента в соответствующее поле для ввода
    - 6.4. Ввести фамилию на русском языке в соответствующее поле для ввода
    - 6.5. Ввести фамилию на русском языке в соответствующее поле для ввода
    - 6.6. Ввести серию и номер в соответствующее поле для ввода
    - 6.7. Ввести ИНН в соответствующее поле для ввода
    - 6.8. Нажать на кнопку "Оплатить"
7. Если такая проверка есть среди прошлых проверок:
   - 7.1 Нажать на эту проверку
   - 7.2 Нажать на кнопку "Оплатить"
8. Проверить наличие формы для оплаты


## Ожидаемый результат:

- Наличие на экране формы для оплаты штрафов

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Оплата патента с неправильным форматом ИНН

### **ID тест-кейса:** TC-011

#### **Группа для запуска:** 1

##### **Test-name:** test_payment_patent_with_wrong_inn

**Описание:**  
Оплата патента с неправильными реквизитами

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Серия и номер патента: `77 2204315436`
- Дата выдачи патента: `01.01.2020`
- Фамилия (на русском языке): `АБДУРОСУЛОВ`
- Имя (на русском языке): `ДОСТОН`
- Серия и номер паспорта: `FA6169953`
- ИНН: `971510764677`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в оплату патента
5. Проверить на наличие прошлых проверок с таким же номером патента
6. Если такой проверки нет 
    - 6.1. Нажать на кнопку "Добавить патент"
    - 6.2. Ввести серию и номер патента в соответствующее поле для ввода
    - 6.3. Ввести дату выдачи патента в соответствующее поле для ввода
    - 6.4. Ввести фамилию на русском языке в соответствующее поле для ввода
    - 6.5. Ввести фамилию на русском языке в соответствующее поле для ввода
    - 6.6. Ввести серию и номер в соответствующее поле для ввода
    - 6.7. Ввести ИНН в соответствующее поле для ввода
    - 6.8. Нажать на кнопку "Оплатить"
7. Если такая проверка есть среди прошлых проверок:
   - 7.1 Нажать на эту проверку
   - 7.2 Нажать на кнопку "Оплатить"
8. Проверить наличие формы для оплаты


## Ожидаемый результат:

- Наличие на экране формы для оплаты штрафов

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка оплаты госпошлины - город Москва

### **ID тест-кейса:** TC-012

#### **Группа для запуска:** 7

##### **Test-name:** test_search_state_duty_moscow_city

**Описание:**  
Проверка оплаты госпошлины в населённом пункте - Москва

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Категория пошлины: `За выдачу паспорта гражданина Российской Федерации`
- Населённый пункт: `Москва`
- Отделение: `УВД по ЦАО`
- Документ, удостоверяющий личность: `Паспорт иностранного гражданина`
- Номер документа: `FA6169953`
- Фио: `АБДУРОСУЛОВ ДОСТОН`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в оплату госпошлины
5. Нажать на выпадающий список для выбора категории госпошлины
6. Выбрать нужную категорию
7. Нажать на выпадающий список для выбора населенного пункта
8. Выбрать нужный населенный пункт
9. Нажать на выпадающий список для выбора отделения
10. Выбрать нужное отделения
11. Нажать на выпадающий список для выбора документа, удостоверяющего личность
12. Выбрать нужный тип документа
13. Ввести номер документа в соответствующее поле
14. Ввести фио в соответствующее поле
15. Нажать кнопку "Оплатить"
16. Проверить наличие формы для оплаты


## Ожидаемый результат:

- Наличие на экране формы для оплаты

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка оплаты госпошлины - город Казань

### **ID тест-кейса:** TC-013

#### **Группа для запуска:** 7

##### **Test-name:** test_search_state_duty_kazan_city

**Описание:**  
Проверка оплаты госпошлины в населённом пункте - Казань

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Категория пошлины: `За выдачу паспорта гражданина Российской Федерации`
- Населённый пункт: `Казань`
- Документ, удостоверяющий личность: `Паспорт иностранного гражданина`
- Номер документа: `FA6169953`
- Фио: `АБДУРОСУЛОВ ДОСТОН`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в оплату госпошлины
5. Нажать на выпадающий список для выбора категории госпошлины
6. Выбрать нужную категорию
7. Нажать на выпадающий список для выбора населенного пункта
8. Выбрать нужный населенный пункт
9. Нажать на выпадающий список для выбора документа, удостоверяющего личность
10. Выбрать нужный тип документа
11. Ввести номер документа в соответствующее поле
12. Ввести фио в соответствующее поле
13. Нажать кнопку "Оплатить"
14. Проверить наличие формы для оплаты


## Ожидаемый результат:

- Наличие на экране формы для оплаты

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка оплаты госпошлины - город Санкт-Петербург

### **ID тест-кейса:** TC-014

#### **Группа для запуска:** 7

##### **Test-name:** test_search_state_duty_spb_city

**Описание:**  
Проверка оплаты госпошлины в населённом пункте - Санкт-Петербург

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Категория пошлины: `За выдачу паспорта гражданина Российской Федерации`
- Населённый пункт: `Санкт-Петербург`
- Документ, удостоверяющий личность: `Паспорт иностранного гражданина`
- Номер документа: `FA6169953`
- Фио: `АБДУРОСУЛОВ ДОСТОН`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в оплату госпошлины
5. Нажать на выпадающий список для выбора категории госпошлины
6. Выбрать нужную категорию
7. Нажать на выпадающий список для выбора населенного пункта
8. Выбрать нужный населенный пункт
9. Нажать на выпадающий список для выбора документа, удостоверяющего личность
10. Выбрать нужный тип документа
11. Ввести номер документа в соответствующее поле
12. Ввести фио в соответствующее поле
13. Нажать кнопку "Оплатить"
14. Проверить наличие формы для оплаты


## Ожидаемый результат:

- Наличие на экране формы для оплаты

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка оплаты госпошлины - город Нижний Новгород

### **ID тест-кейса:** TC-015

#### **Группа для запуска:** 7

##### **Test-name:** test_search_state_duty_nn_city

**Описание:**  
Проверка оплаты госпошлины в населённом пункте - Нижний Новгород

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Категория пошлины: `За выдачу паспорта гражданина Российской Федерации`
- Населённый пункт: `Нижний Новгород`
- Документ, удостоверяющий личность: `Паспорт иностранного гражданина`
- Номер документа: `FA6169953`
- Фио: `АБДУРОСУЛОВ ДОСТОН`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в оплату госпошлины
5. Нажать на выпадающий список для выбора категории госпошлины
6. Выбрать нужную категорию
7. Нажать на выпадающий список для выбора населенного пункта
8. Выбрать нужный населенный пункт
9. Нажать на выпадающий список для выбора документа, удостоверяющего личность
10. Выбрать нужный тип документа
11. Ввести номер документа в соответствующее поле
12. Ввести фио в соответствующее поле
13. Нажать кнопку "Оплатить"
14. Проверить наличие формы для оплаты


## Ожидаемый результат:

- Наличие на экране формы для оплаты

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка оплаты госпошлины - город Самара

### **ID тест-кейса:** TC-016

#### **Группа для запуска:** 7

##### **Test-name:** test_search_state_duty_samara_city

**Описание:**  
Проверка оплаты госпошлины в населённом пункте - Самара

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Категория пошлины: `За выдачу паспорта гражданина Российской Федерации`
- Населённый пункт: `Самара`
- Документ, удостоверяющий личность: `Паспорт иностранного гражданина`
- Номер документа: `FA6169953`
- Фио: `АБДУРОСУЛОВ ДОСТОН`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в оплату госпошлины
5. Нажать на выпадающий список для выбора категории госпошлины
6. Выбрать нужную категорию
7. Нажать на выпадающий список для выбора населенного пункта
8. Выбрать нужный населенный пункт
9. Нажать на выпадающий список для выбора документа, удостоверяющего личность
10. Выбрать нужный тип документа
11. Ввести номер документа в соответствующее поле
12. Ввести фио в соответствующее поле
13. Нажать кнопку "Оплатить"
14. Проверить наличие формы для оплаты


## Ожидаемый результат:

- Наличие на экране формы для оплаты

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка оплаты госпошлины - город Другой

### **ID тест-кейса:** TC-017

#### **Группа для запуска:** 7

##### **Test-name:** test_search_state_duty_another_city

**Описание:**  
Проверка оплаты госпошлины в населённом пункте не из списка представленных городов

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Категория пошлины: `За выдачу паспорта гражданина Российской Федерации`
- Населённый пункт: `Другой`
- ИНН получателя: `7707089101`
- Р/С получателя: `03100643000000017300`
- БИК банка получателя: `004525988`
- ОКТМО получателя: `45382000`
- Документ, удостоверяющий личность: `Паспорт иностранного гражданина`
- Номер документа: `FA6169953`
- Фио: `АБДУРОСУЛОВ ДОСТОН`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в оплату госпошлины
5. Нажать на выпадающий список для выбора категории госпошлины
6. Выбрать нужную категорию
7. Нажать на выпадающий список для выбора населенного пункта
8. Выбрать нужный населенный пункт
9. Ввести ИНН получателя в соответствующее поле
10. Ввести Р/С получателя в соответствующее поле
11. Ввести БИК банка получателя в соответствующее поле
12. Ввести ОКТМО получателя в соответствующее поле
13. Нажать на выпадающий список для выбора документа, удостоверяющего личность
14. Выбрать нужный тип документа
15. Ввести номер документа в соответствующее поле
16. Ввести фио в соответствующее поле
17. Нажать кнопку "Оплатить"
18. Проверить наличие формы для оплаты


## Ожидаемый результат:

- Наличие на экране формы для оплаты

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка налогов по ИНН без штрафов

### **ID тест-кейса:** TC-018

#### **Группа для запуска:** 1

##### **Test-name:** test_payment_taxes_page_inn_no_arrears

**Описание:**  
Проверка налогов по ИНН без штрафов

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Тип документа проверки: `ИНН`
- Номер документа: `780204893183`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в проверку оплаты налогов
5. Проверить на наличие прошлых проверок с таким же ИНН
6. Если такого ИНН в прошлых проверках нет 
    - 6.1. Нажать на кнопку "Добавить документ"
    - 6.2. Выбрать тип проверяемого документа - "ИНН"
    - 6.3. Ввести ИНН в соответствующее поле
    - 6.4. Нажать на кнопку "Проверить"
7. Если такой ИНН есть среди прошлых проверок:
   - 7.1 Нажать на нужный ИНН 
8. Проверить наличие на экране надписи "ШТРАФОВ НЕТ, ПОЗДРАВЛЯЕМ!"


## Ожидаемый результат:

- Наличие на экране формы для оплаты

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка налогов по ИНН со штрафами

### **ID тест-кейса:** TC-019

#### **Группа для запуска:** 2

##### **Test-name:** test_payment_taxes_page_inn_have_arrears

**Описание:**  
Проверка налогов по ИНН со штрафами

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Тип документа проверки: `ИНН`
- Номер документа: `540363052918`
- ФИО плательщика: `Антонио Бандерас`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в проверку оплаты налогов
5. Проверить на наличие прошлых проверок с таким же ИНН
6. Если такого ИНН в прошлых проверках нет 
    - 6.1. Нажать на кнопку "Добавить документ"
    - 6.2. Выбрать тип проверяемого документа - "ИНН"
    - 6.3. Ввести ИНН в соответствующее поле
    - 6.4. Нажать на кнопку "Проверить"
7. Если такой ИНН есть среди прошлых проверок:
   - 7.1 Нажать на нужный ИНН 
8. Проверить наличие заполненного ФИО плательщика
   - 8.1. Если ФИО пустое или стоит "-", то заполнить входным параметром
   - 8.2. Если заполнено, то оставить как есть
9. Нажать кнопку "Оплатить"
10. Проверить наличие формы для оплаты


## Ожидаемый результат:

- Наличие на экране формы для оплаты

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка налогов по УИН без штрафов

### **ID тест-кейса:** TC-020

#### **Группа для запуска:** 3

##### **Test-name:** test_payment_taxes_page_uin_no_arrears

**Описание:**  
Проверка налогов по УИН без штрафов

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Тип документа проверки: `УИН`
- Номер документа: `18810578230828569031`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в проверку оплаты налогов
5. Проверить на наличие прошлых проверок с таким же УИН
6. Если такого ИНН в прошлых проверках нет 
    - 6.1. Нажать на кнопку "Добавить документ"
    - 6.2. Выбрать тип проверяемого документа - "УИН"
    - 6.3. Ввести ИНН в соответствующее поле
    - 6.4. Нажать на кнопку "Проверить"
7. Если такой ИНН есть среди прошлых проверок:
   - 7.1 Нажать на нужный ИНН 
8. Проверить наличие на экране надписи "ШТРАФОВ НЕТ, ПОЗДРАВЛЯЕМ!"


## Ожидаемый результат:

- Наличие на экране формы для оплаты

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения


# Тест-кейс: Проверка налогов по УИН со штрафами

### **ID тест-кейса:** TC-021

#### **Группа для запуска:** 4

##### **Test-name:** test_payment_taxes_page_uin_have_arrears

**Описание:**  
Проверка налогов по УИН со штрафами

**Предусловия:**  
- Приложение установлено на устройство.

## Реквизиты:

- Тип документа проверки: `УИН`
- Номер документа: `Таких тестовых реквизитов нет`
- ФИО плательщика: `Антонио Бандерас`

## Шаги выполнения:

1. Открыть приложение
2. Выбрать язык - "Русский"
3. Перейти на страницу с платежами
4. Перейти в проверку оплаты налогов
5. Проверить на наличие прошлых проверок с таким же УИН
6. Если такого ИНН в прошлых проверках нет 
    - 6.1. Нажать на кнопку "Добавить документ"
    - 6.2. Выбрать тип проверяемого документа - "УИН"
    - 6.3. Ввести ИНН в соответствующее поле
    - 6.4. Нажать на кнопку "Проверить"
7. Если такой ИНН есть среди прошлых проверок:
   - 7.1 Нажать на нужный ИНН 
8. Проверить наличие заполненного ФИО плательщика
   - 8.1. Если ФИО пустое или стоит "-", то заполнить входным параметром
   - 8.2. Если заполнено, то оставить как есть
9. Нажать кнопку "Оплатить"
10. Проверить наличие формы для оплаты


## Ожидаемый результат:

- Наличие на экране формы для оплаты

## Примечания:

- Тест выполняется на Android версии 10
- После каждого действия сохраняется скриншот с названием шага выполнения