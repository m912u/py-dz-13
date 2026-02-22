# Скрипт для проверки файлов через сервис VirusTotal.

# **Настройка **:
Необходимо создать файл .env со следующим содержимым:
```env
API_KEY=api_ключ_от_virustotal
```

Необходимо указать файл, загружаемый на virustotal
```python
file_path = "eicar.com"
```


# **Запуск**:
```python
python virustotal.py
```

# **Пример работы**:
```
# python virustotal.py
Загружаем файл на VirusTotal: eicar.com
Файл загружен. ID: NDRkODg2MTJmZWE4YThmMzZkZT1yZT4yNzhhYmI6MmY6MTc3MTc7MTE5aa==
Ожидаем анализа...
РЕЗУЛЬТАТЫ ПРОВЕРКИ:
Обнаружено угроз: 66
Подозрительных: 0
Безопасных: 0
Неопределенных: 2
```