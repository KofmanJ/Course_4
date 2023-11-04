import requests
from abc import ABC, abstractmethod
import os
from dotenv import load_dotenv
from vacancies import Vacancies

load_dotenv()


class Api_job(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class Api_superjob(Api_job):
    """
    Класс для работы с вакансиями SuperJob
    """
    def get_vacancies(self):
        """
        Метод через requests.get получает данные в json-формате с сайта superjob
        """

        api_url = 'https://api.superjob.ru/2.0/vacancies'
        headers = {'X-Api-App-Id': os.getenv('API_SUPERJOB')}
        response = requests.get(api_url, headers=headers)
        # return response.json()['objects']
        vacancies_list = []
        if response.status_code == 200:
            for object in response.json()['objects']:
                # if object['candidat'] and object['payment_to'] and object['currency'] == 'rub':
                title = object['profession']
                link = object['link']
                payment_from = object['payment_from']
                payment_to = object['payment_to']
                city = object['town']['title']
                company = object['firm_name']
                vacancy = Vacancies(title, link, payment_from, payment_to, city, company)
                vacancies_list.append(vacancy)
            vacancies = '\n'.join(str(vacancy) for vacancy in vacancies_list)
            return f"Вакансии с сайта SuperJob.ru:\n{vacancies}\n"
        #     return f'Подключение с сайтом SuperJob.ru установлено с кодом: {response.status_code}'
        else:
            return 'Ошибка подключения'

class Api_hh(Api_job):
    """
    Класс для работы с вакансиями HeadHunter
    """
    def get_vacancies(self):
        """
        Метод через requests.get получает данные в json-формате с сайта hh.ru
        """
        api_url = 'https://api.hh.ru/vacancies'
        headers = {'X-Api-App-Id': os.getenv('API_HHRU')}
        response = requests.get(api_url, headers=headers)
        vacancies_list = []
        if response.status_code == 200:
            for item in response.json()['items']:
                title = item['name']
                link = item['alternate_url']
                payment_from = item['salary']['from']
                payment_to = item['salary']['to']
                city = item['area']['name']
                company = item['employer']['name']
                vacancy = Vacancies(title, link, payment_from, payment_to, city, company)
                vacancies_list.append(vacancy)
            vacancies = '\n'.join(str(vacancy) for vacancy in vacancies_list)
            return f"Вакансии с сайта HH.ru:\n{vacancies}\n"
            #     return f'Подключение с сайтом SuperJob.ru установлено с кодом: {response.status_code}'
        else:
            return 'Ошибка подключения'


if __name__ == '__main__':
    ex1 = Api_superjob()
    ex2 = Api_hh()
    print(ex1.get_vacancies())
    print(ex2.get_vacancies())
