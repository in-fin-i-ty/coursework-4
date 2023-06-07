from vacancy import Vacancy
from api_platforms import HeadHunterAPI, SuperJobAPI
from json_saver import JSONSaver

"""
Файл для взаимодействия с пользователем
"""


def user_interaction():
    api_hh = HeadHunterAPI()
    api_sj = SuperJobAPI()
    saver = JSONSaver()
    saver.file_vacancy_clear()
    vacancies = None
    print("Привет, я помогу вам найти несколько вакансий по вашему запросу")
    search_query = input(f'Ведите специальность для поиска\n')
    top_n = int(input(f'Ведите количество вакансий которое хотите загрузить\n'))
    print("Выбери с какой платформы выгрузить вакансии и введи соответствующий номер")
    print(f"1-HeadHunter\n"
          "2-SuperJob\n"
          "3-Загрузки с 2х платформ сразу")
    while True:
        user_choice = int(input())
        print('Подождите загружаю вакансии...')
        if user_choice == 1:
            vacancies = api_hh.get_vacancies(search_query, top_n)
            break
        elif user_choice == 2:
            vacancies = api_sj.get_vacancies(search_query, top_n)
            break
        elif user_choice == 3:
            vacancies = api_hh.get_vacancies(search_query, top_n)
            vacancies += api_sj.get_vacancies(search_query, top_n)
            break
        else:
            print('Не понимаю вас')
            continue
    if not vacancies:
        print('Нет вакансий по данному запросу!')
        print("Попробуем ещё?(введите соответствующий номер)")
        print(f"1 - да\n"
              f"2 - нет")
        while True:
            user_answer = input()
            if user_answer == "1":
                user_interaction()
            elif user_answer == "2":
                print('Всего хорошего, буду рад вам помочь!')
                exit()
            else:
                print("Не понимаю вас")
                continue
    saver.save_vacancies(vacancies)
    print("Теперь уточним минимальный уровень зарплаты")
    print("Введите сумму")
    user_salary = int(input())
    valid_salary = Vacancy.filter_vacancies(user_salary)
    try:
        for i in valid_salary:
            print(i)
    except TypeError:
        pass
    while True:
        print('Хотите начать заново?(введите соответствующий номер)')
        print(f"1 - да\n"
              f"2 - нет")
        new_vac = input()
        if new_vac.lower() == '1':
            user_interaction()
        elif new_vac.lower() == '2':
            print('До новых встреч!')
            exit()
        else:
            print("Не понимаю вас")
            continue
