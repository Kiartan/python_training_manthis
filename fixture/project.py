from selenium import webdriver
from fixture.session import SessionHelper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_add_project_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/manage_proj_create_page.php"):
            wd.find_element(By.LINK_TEXT, "Create New Project").click()

    def open_projects_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element(By.XPATH, "//a[@href='/mantisbt-1.2.20/manage_proj_page.php']").click()

    def create(self, project):
        wd = self.app.wd
        # Open page with contacts
        self.app.open_add_project_page()
        # Fill the new project form
        self.fill_new_project_form(project)
        # submitting the form
        wd.find_element(By.XPATH, "//input[@value='Add Project']").click()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def change_dropdown_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            Select(wd.find_element(By.NAME, field_name)).select_by_visible_text(text)

    def fill_new_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_dropdown_value("status", project.status)
        self.change_dropdown_value("view_state", project.status)
        self.change_field_value("description", project.description)

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.project_cache.append(Project(name=text, id=id))
        return list(self.project_cache)

