# Используйте образ с Python 3.10
FROM python:3.10

# Укажите рабочий каталог
WORKDIR /app

# Скопируйте файлы в рабочий каталог
COPY . .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Укажите команду для запуска приложения Streamlit
CMD ["streamlit", "run", "main.py"]