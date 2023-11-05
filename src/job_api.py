from abc import abstractmethod
import requests
from src.vacancy import Vacancy
from dotenv import load_dotenv
import os


class JobAPI:
    """Абстрактный класс для хранения информации из API"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self, name_job):
        pass


class Api_hh(JobAPI):
    "Класс для хранения информации из API с сайта HH"

    def __init__(self):
        super().__init__()
        self.url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, name_job, pages):
        """
        Метод через requests.get получает данные в json-формате с сайта hh.ru
        """
        url = self.url
        vacancies_list = []
        for i in range(pages):
            par = {'text': name_job, 'per_page': '3', 'page': i}
            r = requests.get(url, params=par)
            e = r.json()
            for j in e['items']:
                job_id = str(j['id'])
                job_url = j['alternate_url']
                name = j['name']
                if not ((j['salary'] is None) or (j['salary']['from'] is None)):
                    salary_from = j['salary']['from']
                    salary_to = j['salary']['to']
                else:
                    salary_from = 0
                    salary_to = 0
                if not (j['address'] is None):
                    city = j['address']['city']
                else:
                    city = None
                vacancy = Vacancy(job_id, job_url, name, salary_from, salary_to, city)
                vacancies_list.append(vacancy)
        return vacancies_list


class Api_superjob(JobAPI):
    def __init__(self):
        super().__init__()
        load_dotenv()
        self.url = 'https://api.superjob.ru/2.0/vacancies'
        self.api_key = os.getenv('API_SUPERJOB')

    def get_vacancies(self, name_job, pages):
        """
        Метод через requests.get получает данные в json-формате с сайта superjob
        """
        url = self.url
        vacancies_list = []
        head = {'Host': 'api.superjob.ru',
                'X-Api-App-Id': self.api_key
                }
        for i in range(pages):
            par = {'keyword': name_job, 'count': 3, 'page': i}
            r = requests.get(url, params=par, headers=head)
            e = r.json()
            for j in e['objects']:
                job_id = str(j['id'])
                job_url = j['link']
                name = j['profession']
                salary_from = j['payment_from']
                salary_to = j['payment_to']
                if j['address'] is None:
                    city = None
                else:
                    city = j['address'].split(',')[0]
                vacancy = Vacancy(job_id, job_url, name, salary_from, salary_to, city)
                vacancies_list.append(vacancy)
        return vacancies_list
