# Sprint_5

## Автотесты для Stellar Burgers

Проект содержит автоматизированные тесты для приложения **Stellar Burgers**. Тесты написаны на **Selenium3**


### Структура проекта
├── tests/ # Директория с тестами
│ ├── conftest.py # Конфигурация pytest, фикстуры
│ ├── test_registration.py # Тесты регистрации (2 теста)
│ ├── test_login.py # Тесты входа (4 теста)
│ ├── test_navigation.py # Тесты навигации (4 теста)
│ └── test_constructor.py # Тесты конструктора (3 теста)
├── pages/ # Page Object модели
│ ├── init.py
│ ├── main_page.py # Главная страница (конструктор)
│ ├── login_page.py # Страница авторизации
│ ├── register_page.py # Страница регистрации
│ ├── profile_page.py # Личный кабинет
│ └── forgotpass_page.py # Страница восстановления пароля
├── locators.py # Все локаторы элементов
├── generators.py # Генераторы тестовых данных
├── requirements.txt # Зависимости Python
└── README.md # Документация
