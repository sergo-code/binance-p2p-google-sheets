# Binance P2P

Парсер Binance P2P, отображает информацию в Google Sheets.
Пример таблицы - [Binance P2P](https://docs.google.com/spreadsheets/d/1sB_bMqjbK5SyAGA3aSW3kooQ1-ZNoEK7ASLVZBrKZJw/edit?usp=sharing)
### Отображаемая информация
 - Цены P2P (data/banks.json)
 - Цены маркета (data/spread.json)
 - Спреды Банк -> Банк
 - Спреды Банк -> Коин -> Банк

### В таблице можно менять
 - Цену от которой рассматривать ордера
 - Сумма которая будет в них учавствовать
 - Отображение данных в рублях или процентах

### Создание профиля для взаимодейстия с Google API
1) Выполнить шаги из пункта [Authorize credentials for a desktop application](https://developers.google.com/sheets/api/quickstart/python)
(подключить [Google Drive API](https://console.cloud.google.com/marketplace/product/google/drive.googleapis.com?q=search&referrer=search&project=tests-367711), [Google Sheets API](https://console.cloud.google.com/marketplace/product/google/sheets.googleapis.com?q=search&referrer=search&project=tests-367711)). 
2) В настройках доступа таблицы добавить созданный профиль в роли Редактора.

### Запуск
1) Создать директорию "creds"
2) Добавить файл авторизации в "creds".
3) Создать файл .env
```
cp .env_pub .env
```
4) Отредактировать .env
```
SHEET_ID=1a1a1a1a
CREDENTIALS_FILE=creds/credentials.json
```
5) Установить зависимости
```
python3 -m pip install -r requirements.txt
```
6) Запустить
```
python3 main.py
```

Предложения и пожелания писать в Telegram [@offliny](https://t.me/offliny)