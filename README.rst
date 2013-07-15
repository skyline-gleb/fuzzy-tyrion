HTTP API Fuzzer
=========================

Консольная утилита для фаззинга HTTP API

Формат запуска
--------------

::
    ./python run.py --config="config.json" --report="report.xml" --log="log.txt"

Конфигурационный файл
---------------------

.. code-block:: javascript

    {
        "api_url": "https://api.vk.com/method/",

        "rps": 4,

        "headers": {},

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
                        "action": "generate"
                    }
                }
            }
        }
    }

api_url    - API URL

rps        - максимальное количество запросов в секунду

headers    - заголовки, отправляемые при каждом запросе, например:
::
    {"Accept": "application/json"}

parameters - параметры, отправляемые при каждом запросе, например:
::
    {"api_key": "abc1234"}

methods    - тестируемые методы API