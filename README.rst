HTTP API Fuzzer
=========================

Консольная утилита для фаззинга HTTP API


Запуск
------

.. code-block:: bash

    $ python run.py --config="config.json" --report="report.xml" --log="log.txt"


================   =====================================
``config, -c``      Задать конфигурационный файл
``report, -r``      Задать файл отчета
``log, -l``         Задать файл логов
``verbose, -v``     Активировать расширенное логирование
================   =====================================


Конфигурационный файл
---------------------

.. code-block:: javascript

    {
        // [string] API URL
        "api_url": "https://api.vk.com/method/",

        // [int] максимальное количество запросов в секунду
        "rps": 4,

        // [object] заголовки, отправляемые при каждом запросе
        "headers": {
            "Accept": "application/json"
        },

        // [object] параметры, отправляемые при каждом запросе
        "parameters": {
            "access_token": "533bacf01e11f55b536a565b57531ac114461ae8736d6506a3"
        },

        // [object] тестируемые методы API
        "methods": {

            // [string] название тестируемого метода API
            "getProfiles": {

                // [string] HTTP метод (GET', 'DELETE', 'PATCH', 'POST', 'PUT')
                "http_method": "GET",

                // [int] количество запросов
                "count": 10,

                // [object] параметры API метода
                "parameters": {

                    // [string] название параметра
                    "uids": {

                        // [bool] необходимость параметра
                        "required": true,

                        // [string] тип параметра ('string', 'int', 'float')
                        "data_type": "int",

                        // [mixed] значение параметра
                        "value": 1,

                        // [string] действие над значением ('skip', 'generate', 'mutate')
                        "action": "generate"
                    }

                }

            }

        }

    }