# Тест-кейсы

---

### <u> Позитивный тест-кейс: успешная отправка формы с валидными данными </u>

Предусловие:
Открыт браузер. Пользователь находится на странице https://practice-automation.com/form-fields/

Шаги:

1. Заполнить поле Name значением Amir.
2. Заполнить поле Password значением 1234qwer.
3. В списке What is your favorite drink? выбрать Milk и Coffee.
4. В списке What is your favorite color? выбрать Yellow.
5. В поле Do you like automation? выбрать значение yes.
6. Заполнить поле Email значением molibdenum@mail.ru
.
В поле Message ввести строку, сформированную по блоку Automation tools на странице. Итоговое значение: 5 Katalon Studio.
Нажать кнопку Submit.

Ожидаемый результат:
Появляется alert с текстом "Message received!"

---

### <u> Негативный тест-кейс: форма не отправляется без заполнения обязательного поля Name </u>

Предусловие:
Открыт браузер. Пользователь находится на странице https://practice-automation.com/form-fields/

Шаги:

1. Оставить поле Name пустым.
2. Заполнить поле Password значением 1234qwer.
3. В списке What is your favorite drink? выбрать Milk и Coffee.
4. В списке What is your favorite color? выбрать Yellow.
5. В поле Do you like automation? выбрать значение yes.
6. Заполнить поле Email значением molibdenum@mail.ru
.
В поле Message ввести строку, сформированную по блоку Automation tools на странице. Итоговое значение: 5 Katalon Studio.
Нажать кнопку Submit.

Ожидаемый результат:
Форма не отправляется. Alert с текстом "Message received!" не появляется. Для поля Name срабатывает браузерная проверка обязательного заполнения, поле не проходит валидацию.

---