class UrlError(Exception):
    """Класс ошибки при работе с URL"""
    pass


class Vacancies:
    """
    Класс для создания экземпляров вакансий и работы с ними
    """

    __slots__ = {'title', 'link', 'salary_from', 'salary_to', 'city', 'company'}

    def __init__(self, title: str, link: str, salary_from: int, salary_to: int, city: str, company: str):
        self.title = title
        if not isinstance(self.title, str):
            raise TypeError("Название вакансии должно быть типа 'str'")
        self.link = link
        if self.link[:8] != 'https://':
            raise UrlError("Ссылка должна начинаться с https://")
        self.salary_from = salary_from
        if self.salary_from is None or self.salary_from == 0:
            # raise AttributeError('Поле не может быть пустым')
            self.salary_from = '-'
        self.salary_to = salary_to
        if self.salary_to is None or self.salary_to == 0:
            # raise AttributeError('Поле не может быть пустым')
            self.salary_to = '-'
        self.city = city
        if self.city is None:
            raise AttributeError('Поле не может быть пустым')
        self.company = company
        if self.company is None:
            raise AttributeError('Поле не может быть пустым')

    # def __str__(self):
    #     if self.description == 'по договоренности':
    #         return f"Вакансия: {self.title}, ссылка: {self.url}, город: {self.city}, зарплата: {self.description}"
    #     elif self.salary_from == '0':
    #         return f"Вакансия: {self.title}, ссылка: {self.url}, город: {self.city}, зарплата: до {self.salary_to}"
    #     elif self.salary_from == self.salary_to:
    #         return f"Вакансия: {self.title}, ссылка: {self.url}, город: {self.city}, зарплата: {self.salary_to}"
    #     else:
    #         return f"Вакансия: {self.title}, ссылка: {self.url}, город: {self.city}, зарплата: от {self.salary_from} до {self.salary_to}"

    def __str__(self):
        return f'Название вакансии - {self.title}\n' \
               f'Компания - {self.company}\n' \
               f'Ссылка - {self.link}\n' \
               f'Город - {self.city}\n' \
               f'З/п: от {self.salary_from} до {self.salary_to} руб.\n'

    def __lt__(self, other):
        return self.salary_from < other.salary

    def __eq__(self, other):
        return self.salary_from == other.salary

    def __ne__(self, other):
        return self.salary_from != other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from

    def __ge__(self, other):
        return self.salary_from >= other.salary_from
