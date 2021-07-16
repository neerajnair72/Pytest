import pytest
import sys


@pytest.mark.usefixtures('driver')
     
class TestLink:

    def test_check(self, driver):
        """
        Verify click and title of page
        :return: None
        """
        driver.get('https://lambdatest.github.io/sample-todo-app/')
        driver.find_element_by_name("li1").click()
        driver.find_element_by_name("li2").click()

        title = "Sample page - lambdatest.com"
        assert title == driver.title
        driver.quit()


@pytest.mark.usefixtures('driver2')
     
class TestLink2:


    def test_check1(self, driver2):
        """
        Verify item submission
        :return: None
        """
        driver2.get('https://lambdatest.github.io/sample-todo-app/')
        sample_text = "Happy Testing at LambdaTest"
        email_text_field = driver2.find_element_by_id("sampletodotext")
        email_text_field.send_keys(sample_text)

        driver2.find_element_by_id("addbutton").click()
        driver2.quit()
      
       
