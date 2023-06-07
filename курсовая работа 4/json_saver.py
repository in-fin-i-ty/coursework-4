import json


class JSONSaver:
    """
    Класс для работы с Json файлом
    """

    @staticmethod
    def save_vacancies(vacs, file='all_vacancy.json'):
        """
        Функция для сохранения данных в файле
        """
        with open(file, 'w', encoding='utf-8') as f:
            json.dump([i.to_dict() for i in vacs], f, ensure_ascii=False, indent='\t')

    @classmethod
    def file_vacancy_clear(cls):
        """
        Функция для очистки файла
        """
        try:
            with open('all_vacancy.json', 'w', encoding='utf-8'):
                pass
        except FileNotFoundError:
            pass