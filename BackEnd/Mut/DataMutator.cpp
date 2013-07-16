/* 
 * File:   DataMutator.cpp
 * Author: golovin
 * 
 * Created on 16 Июль 2013 г., 11:58
 */

#include "DataMutator.h"
#include <cstdlib>
#include <sstream>
#include <ctime>

DataMutator::DataMutator()
{
    // Инициализация рандома
    std::srand(time(NULL));
}

DataMutator::~DataMutator()
{
}

int DataMutator::mutateInt32(int _value, int _numberOfMutations)
{
    std::string s;
    std::stringstream ss;

    // Инициализация рандома
    //std::srand(time(NULL));

    // Переводим число в строку
    ss << _value;
    s = ss.str();

    // Получаем длину числа
    int n = s.length();

    // Необходимое кол-во раз мутируем число
    for (int i = 0; i < _numberOfMutations; ++i) {
        // Каждая цифра мутирует отдельно
        for (int j = 0; j < n; ++j) {
            // Берем цифру
            int k = s[j] - '0';

            // Мутируем её
            switch (std::rand() % 3) {
            case 1:
                k++;
                break;
            case 2:
                k--;
                break;
            case 0:
            default:
                break;
            }

            // Если цифра стала двузначной, то небольшая фича
            // по превращению в однозначную
            if (k >= 10) {
                if (std::rand() % 2 == 1)
                    k = k % 10;
                else k = k / 10;
            }

            // Изменяем цифру на новую (смутированную)
            s[j] = k + '0';
        }
    }

    // Очистка потока
    ss.str("");
    // Запись в него результата (строковый вид)
    ss << s;
    // Сохраняем результат в имеющуюся свободную переменную
    ss >> n;

    return n;
}
