from pages.form_fields_page import FormFieldsPage


def test_fill_form(driver):
    page = FormFieldsPage(driver)
    page.open_page()

    page.enter_name("Amir")
    page.enter_password("1234qwer")
    page.select_drinks(["Milk", "Coffee"])
    page.select_color("Yellow")
    page.select_automation_option("yes")
    page.enter_email("molibdenum@mail.ru")
    page.enter_message("Hello Hi")
    page.submit_form()

    alert_text = page.get_alert_text_and_accept()
    assert alert_text == "Message received!"