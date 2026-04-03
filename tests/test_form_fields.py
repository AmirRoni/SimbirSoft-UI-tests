from pages.form_fields_page import FormFieldsPage


def test_fill_form(driver):
    page = FormFieldsPage(driver)

    page.open_page()

    page.enter_name("Amir")

    page.enter_password("1234qwer")

    page.select_milk()

    page.select_coffee()

    page.select_yellow()

    page.select_automation_yes()

    page.enter_email("molibdenum@mail.ru")

    page.enter_message("Hello Hi")

    page.submit_form()
