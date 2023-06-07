import json


class Vacancy:
    """
    Класс для взаимодействия с выгруженными вакансиями
    """

    def __init__(self, name_vac, url, salary=int, area=None):
        self.wage = None
        self.__name_vac = name_vac
        self.url = url
        if salary == 0:
            self.salary = 0
            self.wage = 'не указана'
        elif salary is None:
            self.salary = 0
            self.wage = 'не указана'
        else:
            self.salary = salary
            self.wage = self.salary
        self.area = area
        self.vacancy = None

    def __repr__(self):
        return f"Название вакансии: {self.__name_vac}\n" \
               f"Заработная плата: {self.wage}\n" \
               f"Ссылка на вакансию: {str(self.url)}\n" \
               f"Местоположения: {str(self.area)}\n"

    def to_dict(self):
        """
        Функция возвращающая шаблон словаря для загрузки данных в файл
        """
        return {
            'Название вакансии': self.__name_vac,
            'Ссылка на вакансию': self.url,
            'Заработная плата': self.wage,
            'Местоположения': self.area,
        }

    @staticmethod
    def filter_vacancies(salary, file_vac='all_vacancy.json'):
        """
        Функция для фильтрации данных из файла по заработной плате
        """
        filtered_vacancies = []
        with open(file_vac, 'r', encoding='utf-8') as file:
            data = json.load(file)
        while True:
            for i in data:
                info_vac = (
                    f"Название вакансии: {i['Название вакансии']}\n"
                    f"Ссылка на вакансию: {i['Ссылка на вакансию']}\n"
                    f"Заработная плата: {i['Заработная плата']}\n"
                    f"Местоположения: {i['Местоположения']}\n")
                try:
                    if i['Заработная плата'] >= salary:
                        filtered_vacancies.append(info_vac)
                except TypeError:
                    pass
            return filtered_vacancies
