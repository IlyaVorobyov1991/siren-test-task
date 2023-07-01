import pytest
from selenium import webdriver

from test.pages.form_confirm_your_number_page import FormConfirmPhoneNumberPage
from test.pages.form_fullname_email_page import FormFullnameEmailPage
from test.pages.form_homeowner_page import FormHomeownerPage
from test.pages.form_kind_of_siding_page import FormKindOfSidingPage
from test.pages.form_phone_number_page import FormPhoneNumberPage
from test.pages.form_sorry_page import FormSorryPage
from test.pages.form_square_feet_page import FormSquareFeetPage
from test.pages.form_stories_house_page import FormStoriesHousePage
from test.pages.form_thank_you_page import FormThankYouPage
from test.pages.index_page import IndexPage
from test.pages.form_type_of_project_page import FormTypeOfProjectPage
from faker import Faker


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    index_page = IndexPage(driver, 'https://hb-eta.stage.sirenltd.dev/siding')
    index_page.open()
    yield driver
    driver.quit()


class TestTask:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.index_page = IndexPage(driver, driver.current_url)
        self.form_type_of_project_page = FormTypeOfProjectPage(driver, driver.current_url)
        self.form_kind_of_siding_page = FormKindOfSidingPage(driver, driver.current_url)
        self.form_square_feet_page = FormSquareFeetPage(driver, driver.current_url)
        self.form_stories_house_page = FormStoriesHousePage(driver, driver.current_url)
        self.form_homeowner_page = FormHomeownerPage(driver, driver.current_url)
        self.form_fullname_email = FormFullnameEmailPage(driver, driver.current_url)
        self.form_phone_number = FormPhoneNumberPage(driver, driver.current_url)
        self.form_confirm_phone_number = FormConfirmPhoneNumberPage(driver, driver.current_url)
        self.form_thank_you = FormThankYouPage(driver, driver.current_url)
        self.form_sorry_page = FormSorryPage(driver, driver.current_url)

        self.fake = Faker()
        self.first_name = self.fake.first_name()
        self.last_name = self.fake.last_name()
        self.email = self.fake.email()

    def test_fill_out_form(self):
        self.text_thanks = f'Thank you {self.first_name}, your contractor QA Customer will call soon!'
        self.index_page.enter_zip_code("09090")
        self.index_page.click_zip_code_button()

        # next What type of project is this?
        self.form_type_of_project_page.button_next_disabled_visible()
        self.form_type_of_project_page.count_type_of_project_icons(5)
        self.form_type_of_project_page.click_first_type_of_project_icon()
        self.form_type_of_project_page.button_next_click()

        # next What kind of siding do you want?
        self.form_kind_of_siding_page.button_next_disabled_visible()
        self.form_kind_of_siding_page.count_kind_of_siding_icons(5)
        self.form_kind_of_siding_page.click_first_kind_of_siding_icon()
        self.form_kind_of_siding_page.button_next_click()

        # next Approximately how many square feet will be covered with new siding?
        self.form_square_feet_page.button_next_disabled_visible()
        self.form_square_feet_page.enter_square_feet(40)
        self.form_square_feet_page.button_next_click()

        # next How many stories is your house?
        self.form_stories_house_page.button_next_disabled_visible()
        self.form_stories_house_page.count_stories_icons(4)
        self.form_stories_house_page.click_first_count_stories_icon()
        self.form_stories_house_page.button_next_click()

        # next Are you the homeowner or authorized to make property changes?
        self.form_homeowner_page.button_next_disabled_visible()
        self.form_homeowner_page.count_yes_and_no_icons(2)
        self.form_homeowner_page.click_icon()
        self.form_homeowner_page.button_next_click()

        # next Who should I prepare this estimate for?
        self.form_fullname_email.enter_full_name(str(self.first_name + ' ' + self.last_name))
        self.form_fullname_email.enter_email(self.email)
        self.form_fullname_email.button_next_click()

        # next What is your phone number?
        self.form_phone_number.enter_phone_number('0000000000')
        self.form_phone_number.click_submit_button()

        # next Please confirm your phone number.
        self.form_confirm_phone_number.click_submit_correct_button()

        # next Thank you
        self.form_thank_you.for_thanks_icon_visible()
        self.form_thank_you.assert_thank_you_message(self.text_thanks)

    def test_incorrect_zip_code(self):
        self.index_page.enter_zip_code("9999")
        self.index_page.click_zip_code_button()
        self.index_page.assert_zip_caption_visible()

    def test_valid_zip_code_check_mark(self):
        self.index_page.enter_zip_code("09090")
        self.index_page.assert_check_mark_visible()

    def test_repair_section_answer_is_no_and_sorry_page(self):
        self.sorry_text1 = 'Sorry to see you go!'
        self.sorry_text2 = 'Check out the other services that we offer.'
        self.index_page.enter_zip_code("09090")
        self.index_page.click_zip_code_button()
        self.form_type_of_project_page.click_repair_section_icon()
        self.form_type_of_project_page.click_no_button()
        self.form_sorry_page.assert_go_homepage_button_visible()
        self.form_sorry_page.assert_sorry_img_visible()
        self.form_sorry_page.assert_text1(self.sorry_text1)
        self.form_sorry_page.assert_text2(self.sorry_text2)
