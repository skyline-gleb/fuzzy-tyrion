HTTP API Fuzzer
=========================

Консольная утилита для фаззинга HTTP API

Запуск
--------------
::
    python run.py --config="config.json" --report="report.xml" --log="log.txt"

--config, -c  - задать конфигурационный файл
--report, -r  - задать файл отчета
--log, -l     - задать файл логов
--verbose, -v - активировать расширенное логирование

Конфигурационный файл
---------------------

.. code-block:: javascript

    {
        "api_url": "https://api.vk.com/method/",

        "rps": 4,

        "headers": {
            "Accept": "application/json"
        },

        "parameters": {
            "access_token": "533bacf01e11f55b536a565b57531ac114461ae8736d6506a3"
        },

        "methods": {
            "getProfiles": {
                "http_method": "GET",
                "count": 10,
                "parameters": {
                    "uids": {
                        "required": true,
                        "data_type": "int",
                        "value": 1,
                        "action": "generate"
                    },
                    "fields": {
                        "required": false,
                        "data_type": "string",
                        "value": "uid,first_name,last_name",
                        "action": "mutate"
                    }
                }
            }
        }
    }

api_url     - [string] API URL
rps         - [int] максимальное количество запросов в секунду
headers     - [object] заголовки, отправляемые при каждом запросе
parameters  - [object] параметры, отправляемые при каждом запросе
methods     - [object] тестируемые методы API

    http_method - [string] HTTP метод (GET', 'DELETE', 'PATCH', 'POST', 'PUT')
    count       - [int] количество запросов
    parameters  - [object] параметры API метода

        required  - [bool] необходимость параметра
        data_type - [string] тип параметра ('string', 'int', 'float')
        value     - [mixed] значение параметра
        action    - [string] действие над значением ('skip', 'generate', 'mutate')