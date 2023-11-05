from src.savers import *
from src.job_api import Api_superjob, Api_hh


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    hh_vacancies = Api_hh()
    superjob_vacancies = Api_superjob()
    print('Добро пожаловать!\n')
    while True:
        user_actions = input(f'Для начала работы с программой выберете порядковый номер действия:\n'
                             f'1. Поиск вакансий\n'
                             f'2. Вывод списка вакансий\n'
                             f'3. Удаление вакансии из списка\n'
                             f'0. Завершение работы с программой\n')
        if user_actions == '1':
            print()
            print(f'Вы выбрали раздел поиска вакансий.\n'
                  f'Для поиска вакансий введите ключевое слово:')
            keyword = input()
            print('Введите количество страниц, по которым будет осуществлен поиск:')
            pages = int(input())
            from_hh_vacancies = hh_vacancies.get_vacancies(keyword, pages)
            from_sj_vacancies = superjob_vacancies.get_vacancies(keyword, pages)
            print('Найденные вакансии на сайте "HeadHunter": \n')
            for vacancy in from_hh_vacancies:
                print(vacancy)
            print('Найденные вакансии на сайте "SuperJob": \n')
            for vacancy in from_sj_vacancies:
                print(vacancy)
            print('Хотите сортировать вакансии? Введите "да" или "нет"')
            user_actions = input()
            if user_actions == 'да' or user_actions == 'yes':
                from_all = JSONSaver()
                from_all.add_vacancies(from_hh_vacancies)
                from_all.add_vacancies(from_sj_vacancies)
                from_all.sort_vacancies_by_salary()
                from_all.save_vacancies()
                print()
            elif user_actions == 'нет' or user_actions == 'no':
                from_all = JSONSaver()
                from_all.add_vacancies(from_hh_vacancies)
                from_all.add_vacancies(from_sj_vacancies)
                from_all.save_vacancies()
            else:
                print('Некорректный ввод')
            print()
        elif user_actions == '2':
            print()
            vacancy_reader = JSONSaver()
            vacancy_reader.read_vacancies()
            print()
        elif user_actions == '3':
            try:
                print()
                vacancy_remover = JSONSaver()
                vacancy_remover.remove_vacancies()
            except ValueError:
                print('Некорректный ввод')
                print()
        elif user_actions == '0':
            print('Завершение работы с программой')
            break
        else:
            print('Некорректный ввод')
            print()


if __name__ == '__main__':
    user_interaction()
