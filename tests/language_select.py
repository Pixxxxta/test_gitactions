import time

from pages.start_page import StartPage
from pages.account.accaunt_page import AccountPage


class TestPage:
    def test_language_selection(self, appium_driver):
        start_page = StartPage(appium_driver)
        account_page = AccountPage(appium_driver)

        start_page.go_to_account()
        time.sleep(1)
        account_page.go_to_saved_docs('Паспорта (не РФ)')
        time.sleep(1)
        account_page.click_saved_doc(doc_type='Паспорт',doc_num='FA6169954')
        time.sleep(3)

