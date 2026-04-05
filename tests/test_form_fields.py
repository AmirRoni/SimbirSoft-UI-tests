from pages.form_fields_page import FormFieldsPage


def test_fill_form(driver):
    page = FormFieldsPage(driver)
    message = page.open_page().build_message_from_automation_tools()

    (
        page.enter_name("Amir")
        .enter_password("1234qwer")
        .select_drinks(["Milk", "Coffee"])
        .select_color("Yellow")
        .select_automation_option("yes")
        .enter_email("molibdenum@mail.ru")
        .enter_message(message)
        .submit_form()
    )

    alert_text = page.get_alert_text_and_accept()
    assert alert_text == "Message received!"


def test_form_requires_name(driver):
    page = FormFieldsPage(driver)
    message = page.open_page().build_message_from_automation_tools()

    (
        page.enter_password("1234qwer")
        .select_drinks(["Milk", "Coffee"])
        .select_color("Yellow")
        .select_automation_option("yes")
        .enter_email("molibdenum@mail.ru")
        .enter_message(message)
        .submit_form()
    )

    assert not page.is_alert_present(timeout=2)
    assert page.get_name_validation_message() != ""
