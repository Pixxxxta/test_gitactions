# Автотесты для приложения Росмигрант

## Зависимости

1. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
## Запуск тестов

1. Запуск всех тестов:
   ```bash
   pytest -v tests --alluredir=allure-results
   ```
   Генерация отчёта
   ```bash
   allure generate allure-results -o allure-report --clean
   ```
   Открыть отчёт
   ```bash
   allure open allure-report
   ```
2. Запуск отдельных тестов
   1. Запуск тестов для оплаты патента
      ```bash
      pytest tests\test_payment_patent.py -v
      ```
      Запуск отдельных тестов:
      1. Запуск теста для оплаты патента без сохранённого документа
      ```bash
      pytest tests\test_payment_patent.py::TestPaymentPatent::test_payment_patent_without_saved_doc -v
      ```
      2. Запуск теста для оплаты патента через сохранённый документ
      ```bash
      pytest tests\test_payment_patent.py::TestPaymentPatent::test_payment_patent_with_saved_doc -v
      ```
   2. Запуск тестов для оплаты госпошлины
      ```bash
      pytest tests\test_payment_state_duty.py -v
      ```
      Запуск отдельных тестов:
      1. Запуск теста для оплаты гос пошлины в Москве
      ```bash
      pytest tests\test_payment_state_duty.py::TestPaymentStateDuty::test_search_state_duty_moscow_city -v
      ```
      2. Запуск теста для оплаты гос пошлины в Казани
      ```bash
      pytest tests\test_payment_state_duty.py::TestPaymentStateDuty::test_search_state_duty_kazan_city -v
      ```
      3. Запуск теста для оплаты гос пошлины в Санкт-Петербурге
      ```bash
      pytest tests\test_payment_state_duty.py::TestPaymentStateDuty::test_search_state_duty_spb_city -v
      ```
      4. Запуск теста для оплаты гос пошлины в Нижнем Новгороде
      ```bash
      pytest tests\test_payment_state_duty.py::TestPaymentStateDuty::test_search_state_duty_nn_city -v
      ```
      5. Запуск теста для оплаты гос пошлины в Самаре
      ```bash
      pytest tests\test_payment_state_duty.py::TestPaymentStateDuty::test_search_state_duty_samara_city -v
      ```
      6. Запуск теста для оплаты гос пошлины в другом городе
      ```bash
      pytest tests\test_payment_state_duty.py::TestPaymentStateDuty::test_search_state_duty_another_city -v
      ```
   3. Запуск тестов для проверки штрафов МВД
      ```bash
      pytest tests\test_fines_mvd.py -v
      ```
      Запуск отдельных тестов:
      1. Запуск теста для проверки без штрафов
      ```bash
      pytest tests\test_fines_mvd.py::TestSearchFinesMVD::test_no_fines -v
      ```
      2. Запуск теста для проверки со штрафами
      ```bash
      pytest tests\test_fines_mvd.py::TestSearchFinesMVD::test_have_fines -v
      ```
   4. Запуск тестов для проверки штрафов ГИБДД
      ```bash
      pytest tests\test_fines_gibdd.py -v
      ```
      Запуск отдельных тестов:
      1. Запуск теста для проверки по номеру машины без штрафов
      ```bash
      pytest tests\test_fines_gibdd.py::TestSearchFinesGIBDD::test_no_fines_car_number -v
      ```
      2. Запуск теста для проверки по номеру машины со штрафами
      ```bash
      pytest tests\test_fines_gibdd.py::TestSearchFinesGIBDD::test_have_fines_car_number -v
      ```
      3. Запуск теста для проверки по водительскому удостоверению без штрафов
      ```bash
      pytest tests\test_fines_gibdd.py::TestSearchFinesGIBDD::test_no_fines_driver_num -v
      ```
      4. Запуск теста для проверки по водительскому удостоверению со штрафами
      ```bash
      pytest tests\test_fines_gibdd.py::TestSearchFinesGIBDD::test_have_fines_driver_num -v
      ```
      5. Запуск теста для проверки по УИН без штрафов
      ```bash
      pytest tests\test_fines_gibdd.py::TestSearchFinesGIBDD::test_no_fines_UIN -v
      ```
      6. Запуск теста для проверки по УИН со штрафами
      ```bash
      pytest tests\test_fines_gibdd.py::TestSearchFinesGIBDD::test_have_fines_UIN -v
      ```
    5. Запуск тестов для оплаты налогов
      ```bash
      pytest tests\test_payment_taxes.py -v
      ```
      Запуск отдельных тестов:
   
      1. Запуск теста для оплаты по ИНН без штрафов
      ```bash
      pytest tests\test_payment_taxes.py::TestTaxes::test_payment_taxes_page_inn_no_arrears -v
      ```
      2. Запуск теста для оплаты по ИНН со штрафом
      ```bash
      pytest tests\test_payment_taxes.py::TestTaxes::test_payment_taxes_page_inn_have_arrears -v
      ```
      3. Запуск теста для оплаты по УИН без штрафов
      ```bash
      pytest tests\test_payment_taxes.py::TestTaxes::test_payment_taxes_page_uin_no_arrears -v
      ```
      4. Запуск теста для оплаты по УИН со штрафом(пока нет реквизитов)
      ```bash
      pytest tests\test_payment_taxes.py::TestTaxes::test_payment_taxes_page_uin_have_arrears -v
      ```
   6. Запуск тестов для проверки судебных задолженностей
      ```bash
      pytest tests\test_courts_debts.py -v
      ```
      Запуск отдельных тестов:
      1. Запуск теста для проверки без штрафов
      ```bash
      pytest tests\test_courts_debts.py::TestCourtsDebts::test_payment_courts_debts_page_no_arrears -v
      ```
      2. Запуск теста для проверки со штрафами
      ```bash
      pytest tests\test_courts_debts.py::TestCourtsDebts::test_payment_courts_debts_page_have_arrears -v
      ```