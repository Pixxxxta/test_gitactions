import time

from pages.start_page import StartPage
from pages.tasks.tasks_page import TasksPage
from pages.tasks.resume_page import ResumePage


class TestResume:
    def test_resume(self, appium_driver):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)
        # Инициализация страницы с резюме
        resume_page = ResumePage(appium_driver)

        start_page.go_to_tasks()
        tasks_page.go_to_resume_page()
        time.sleep(5)

        # 1 этап
        resume_page.set_fio('Емельен Из Такси')
        resume_page.choose_gender('Мужской')
        resume_page.set_age('35')
        resume_page.choose_citizenship('Таджикистан')
        time.sleep(3)
        # resume_page.choose_city('Уфа')
        resume_page.swipe_down()
        resume_page.click_continue_btn()

        # Этап 2
        resume_page.choose_type_of_employment(['Подработка', 'Разовая работа'])
        resume_page.choose_post('Водитель')
        resume_page.click_continue_btn()

        # Этап 3
        resume_page.choose_education('Высшее образование')
        resume_page.choose_work_experience('Нет')
        resume_page.click_continue_btn()

        # Этап 4
        resume_page.set_phone_number('9177329677')
        resume_page.set_email('123@123.com')
        resume_page.choose_ready_for_work('Да')
        resume_page.click_save_btn()

        time.sleep(3)

        assert True
