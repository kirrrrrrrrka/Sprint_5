import random
import string

def generate_email(cohort=35):
    names = ['test', 'user']
    surnames = ['testov', 'pupkin']
    n = random.choice(names)
    s = random.choice(surnames)
    r = ''.join(random.choices(string.digits, k=3))
    d = random.choice(['yandex.ru', 'mail.ru'])
    return f"{n}_{s}_{cohort}_{r}@{d}"

# В файле generators.py измените функцию generate_password:

def generate_password(min_length=6):
    """Генерация пароля (минимум 6 символов)"""
    import random
    import string
    
    # Гарантируем минимум 6 символов
    length = max(min_length, 6)
    
    # Буквы (верхний и нижний регистр), цифры
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    
    # Создаем пароль с гарантией наличия разных типов символов
    password_parts = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
    ]
    
    # Добавляем остальные символы
    all_chars = lowercase + uppercase + digits
    for _ in range(length - 3):
        password_parts.append(random.choice(all_chars))
    
    # Перемешиваем для случайности
    random.shuffle(password_parts)
    
    return ''.join(password_parts)

def generate_name():
    return random.choice(['Иван', 'Мария', 'Алексей'])