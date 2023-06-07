import os
from abc import ABC, abstractmethod
import requests
from vacancy import Vacancy


class Get_service_API(ABC):
    """
    Абстрактный класс для работы с API
    """

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(Get_service_API):

    def get_vacancies(self, name_vac=None, count=0):
        """
        Функция для взаимодействия с API HeadHunter
        """
        params = {
            'text': name_vac,
            'search_filed': 'name',
            'page': 0,
            'per_page': count
        }
        req = requests.get('https://api.hh.ru/vacancies', params)
        vacs = [Vacancy(
            name_vac=i.get('name'),
            url=i.get('alternate_url'),
            salary=(i.get('salary').get('from', 0) if i.get('salary') else 0),
            area=i.get('area').get('name'),
        ) for i in req.json()['items'] if i]

        return vacs


class SuperJobAPI(Get_service_API):

    @staticmethod
    def get_salary(salary, currency):
        """
        Функция для получения заработной платы
        возвращающая None если заработная плата не указана
        """
        formatted_salary = None
        if salary and salary != 0:
            formatted_salary = salary if currency == 'rub' else salary * 78
        return formatted_salary

    def get_vacancies(self, name_vac=None, count=0):
        """
        Функция для взаимодействия с API SuperJob
        """
        headers = {'X-Api-App-Id': os.getenv('SuperJobAPI')}
        params = {
            "keyword": name_vac,
            "page": 0,
            "count": count
        }
        req = requests.get("https://api.superjob.ru/2.0/vacancies/", params=params, headers=headers)
        vacs = [Vacancy(
            name_vac=i.get('profession'),
            url=i.get('link'),
            salary=self.get_salary(i.get('payment_from'), i.get('currency')),
            area=i.get('town').get('title'))for i in req.json()['objects'] if i]
        return vacs
