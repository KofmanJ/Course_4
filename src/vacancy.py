class Vacancy:
    """
    "Класс для хранения информации о вакансии"
    """

    def __init__(self, job_id, job_url, name, salary_from, salary_to, city):
        self.job_id = job_id
        self.job_url = job_url
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.city = city

    def __str__(self):
        return f'id: {self.job_id}\n' \
               f'Ссылка: {self.job_url}\n' \
               f'Профессия: {self.name}\n' \
               f'Зарплата от: {self.salary_from}\n' \
               f'Зарплата до: {self.salary_to}\n' \
               f'Город: {self.city}\n'

    def __eq__(self, other):
        return self.salary_from == other.salary_from

    def __ne__(self, other):
        return self.salary_from != other.salary_from

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from

    def __ge__(self, other):
        return self.salary_from >= other.salary_from

    def to_dict(self):
        """
        Функция для представления вакансии в виде словаря
        """
        return {
            'job_id': self.job_id,
            'job_url': self.job_url,
            'name': self.name,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'city': self.city
        }

    @staticmethod
    def from_dict(vacancy_dict):
        """Cтатический метод для перевода словаря в вакансию"""
        return Vacancy(
            vacancy_dict['job_id'],
            vacancy_dict['job_url'],
            vacancy_dict['name'],
            vacancy_dict['salary_from'],
            vacancy_dict['salary_to'],
            vacancy_dict['city']
        )


class Vacancies:
    """Класс для хранения данных о вакансиях и их обработки"""

    def __init__(self):
        self.__all_vacancies = []

    def add_vacancies(self, new_vacancies):
        """
        Метод для добавления вакансий
        """
        self.__all_vacancies += new_vacancies

    def delete_vacancies(self, old_vacancies):
        """
        Удаление вакансий
        """
        for i in old_vacancies:
            self.__all_vacancies.remove(i)

    def sort_vacancies_by_salary(self):
        """
        Сортировка вакансий по зарплате
        """
        self.__all_vacancies.sort(reverse=True)

    @property
    def all_vacancies(self):
        """
        Возвращает все вакансии
        """
        return self.__all_vacancies

    def to_list_dict(self):
        """
        Метод для перевода вакансий в список словарей
        """
        a = []
        for i in self.__all_vacancies:
            a.append(i.to_dict())
        return a
