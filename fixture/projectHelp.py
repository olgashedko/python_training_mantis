import time

from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create_new_project(self, project):
        wd = self.app.wd
        # go to manage project page
    #    self.open_manage_page()
        self.open_project_page_by_link()
        # create new project
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        # fill project parameters
        self.fill_project_data(project)
        # submit project creation
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_page.php")):
            wd.find_element_by_css_selector("span.bracket-link:nth-child(2)").click()

    def open_project_page_by_link(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_page.php")):
            wd.get(self.app.base_url + "/manage_proj_page.php")

    def open_manage_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_overview_page.php")):
            wd.find_element_by_link_text("Manage").click()

    def fill_project_data(self, project):
        wd = self.app.wd
        self.add_text("name", project.project_name)

    def add_text(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page_by_link()
        project_list = []
        count = len(wd.find_elements_by_xpath('//table[@class="width100"][2]//tbody//tr'))
        for n in range(3, count + 1):
            project_id = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td//a').get_attribute('href')
            project_id = str(project_id).split("=")[1]
            project_name = wd.find_element_by_xpath(f'//table[@class="width100"][2]//tbody//tr[{n}]//td//a').text
            project_list.append(Project(project_id=project_id, project_name=project_name))
        print(project_list)
        return project_list

    def delete_project_by_id(self, project):
        wd = self.app.wd
        self.open_project_page_by_link()
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s" % project.project_id).click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        time.sleep(0.5)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
