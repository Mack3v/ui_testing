# UI testing Project

Проект тестирования сайта [saucedemo](https://www.saucedemo.com/) с использованием Playwright, Python.  
Для локаторов и методов работы с элементами на страницах используется Page Object Model.  
В conftest стоит headless=True для корректного запуска в Docker. В случае ошибки создаются скриншоты (пример в репозитории)

## Описание тестов
<details>
<summary>Тест заказа товара</summary>

### test_item_order
Вход и выход в аккаунт осуществляется с помощью фикстур (login, logout)  
На вход передаются название товара для заказа и полное название товара для проверки в корзине  

### Шаги:
- Добавление в корзину с общей страницы товара (проверка отображения кнопки для удаления + иконки количества на корзине)
- Открытие корзины
- Открытие формы заказа
- Заполнение формы (случайные данные через faker)
- Открытие страницы подтверждения (проверка url)
- Проверка имени товара в заказе
- Финиш (проверка url)

</details>

<details>
<summary>Авторизация</summary>

### test_login_form_visibility
Проверка отображения формы для входа. Форма для ввода логина и пароля корректно отображается на странице при загрузке.

### test_authorization
Проверка входа пользователей с доступом. Успешная авторизацию пользователей с корректными учетными данными и переход на нужную страницу.

### test_negative_authorization
Проверка запрета входа для заблокированного пользователя. Заблокированный пользователь не может войти в систему и видит соответствующее сообщение об ошибке.

</details>

## Описание структуры

<details>
<summary>pages</summary>

**base_page** используется для общих методов работы со страницами и их наследования, а также компонентов  
**login_page**, **products_page**: для конкретных страниц сайта и работы с ними (локаторы и методы)
</details>

<details>
<summary>components</summary>

Здесь указаны компоненты сайта, которые могут использоваться на разных страницах.  
В данном случае используется меню-бургер, доступ к которому может понадобиться с любого раздела сайта (например, для выхода из профиля)

</details>

<details>
<summary>page_factory</summary>

Здесь создан базовый Component со своими методами, а от него уже необходимые на сайте: Button, Input, Title и т.д.  
Для каждого компонента можно задать собственные методы, что даёт возможность удобно их вызывать и не переписывать заново

</details>

<details>
<summary>data</summary>

В данном случае используется для генерации случайных данных для полей формы заказа 

</details>

<details>
<summary>Dockerfile</summary>

Для запуска тестов в стандартном контейнере PlayWright:
### Шаги:
- docker pull mcr.microsoft.com/playwright/python:v1.47.0-noble
- docker run -it --rm --ipc=host mcr.microsoft.com/playwright/python:v1.47.0-noble /bin/bash
- docker build -t my-playwright-tests .
- docker run --rm my-playwright-tests pytest -v --tb=short

</details>

<details>
<summary>pytest.ini</summary>

Для указания pytest.mark (помогает избежать лишних предупреждений)

</details>

<details>
<summary>Запуск</summary>

- git clone https://github.com/Mack3v/ui_testing.git
- pip install virtualenv
- virtualenv venv
- source venv/bin/activate или .\venv\Scripts\Activate (для PowerShell)
- pip install -r requirements.txt
- python -m pytest


</details>

https://t.me/qak1r
