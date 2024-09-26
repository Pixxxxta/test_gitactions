import time

from pages.start_page import StartPage
from pages.services.tasks.tasks_page import TasksPage
from pages.services.tasks.entry_ban_page import EntryBanPage


class TestEntryBan:
    def test_have_entry_ban(self, appium_driver):
        # Инициализация стартовой страницы
        start_page = StartPage(appium_driver)
        # Инициализация страницы с задачами
        tasks_page = TasksPage(appium_driver)
        # Инициализация страницы запретом на въезд
        entry_ban_page = EntryBanPage(appium_driver)

        start_page.go_to_tasks()
        tasks_page.go_to_check_entry_ban()
        entry_ban_page.close_rm_window()
        time.sleep(1)
        entry_ban_page.set_last_name('Муминов')
        time.sleep(1)
        entry_ban_page.set_name('Обиджон')
        time.sleep(1)
        entry_ban_page.choose_gender('Мужской')
        time.sleep(1)
        entry_ban_page.set_date('28031990')
        time.sleep(1)
        entry_ban_page.choose_citizenship('Узбекистан')
        time.sleep(1)
        entry_ban_page.choose_doc_type('Национальный паспорт')
        time.sleep(1)
        entry_ban_page.choose_doc_country('Узбекистан')
        time.sleep(1)
        entry_ban_page.set_doc_num('1984119')
        time.sleep(1)
        entry_ban_page.swipe_down()
        time.sleep(1)
        entry_ban_page.set_doc_duration_date('19062029')
        time.sleep(1)
        entry_ban_page.swipe_down()
        time.sleep(30)
        # Ввод капчи пока только руками
        entry_ban_page.click_check_btn()
        time.sleep(5)
        assert entry_ban_page.verify_no_entry_ban(), 'Ошибка при проверке'
