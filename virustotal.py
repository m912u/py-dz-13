import requests
import os
import time
from dotenv import load_dotenv

# Путь к файл для проверки
file_path = "eicar.com"
#file_path = "not-a-virus.txt"

# Загружаем .env файл и получаем из него ключ api
load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY не установлен в env!")
    
# Проверяем существует ли файл
if not os.path.exists(file_path):
    raise ValueError(f"Ошибка: Файл '{file_path}' не найден!")
    
print(f"Загружаем файл на VirusTotal: {file_path}")
    
upload_url = "https://www.virustotal.com/api/v3/files"
headers = {"x-apikey": api_key}
    
with open(file_path, "rb") as file:
    files = {"file": file}
    response = requests.post(upload_url, headers=headers, files=files)
    
if response.status_code != 200:
    print(response.text)
    raise ValueError(f"Ошибка загрузки: {response.status_code}")
    
# Получаем ID файла для проверки результата
file_id = response.json()["data"]["id"]
print(f"Файл загружен. ID: {file_id}")
print("Ожидаем анализа...")

time.sleep(15)
    
# Получаем результат анализа
result_url = f"https://www.virustotal.com/api/v3/analyses/{file_id}"
result_response = requests.get(result_url, headers=headers)
    
if result_response.status_code != 200:
    raise ValueError(f"Ошибка получения результата: {result_response.status_code}")
    
# Вывод результата
result = result_response.json()
stats = result["data"]["attributes"]["stats"]
    
print("РЕЗУЛЬТАТЫ ПРОВЕРКИ:")
print(f"Обнаружено угроз: {stats['malicious']}")
print(f"Подозрительных: {stats['suspicious']}")
print(f"Безопасных: {stats['harmless']}")
print(f"Неопределенных: {stats['undetected']}")