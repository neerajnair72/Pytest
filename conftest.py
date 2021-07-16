import pytest
from os import environ

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.remote_connection import RemoteConnection

@pytest.fixture(scope='function')
def driver(request):

    desired_caps = {}
    browser = {
    "build" : "cc",
    "name" : "your test name",
    "platformName" : "Android",
    "deviceName" : "Galaxy S8",
    "platformVersion" : "7",
      "browserName" :"chrome",
      "name": "v",
      "network": "true",
      "video": "true",
      "visual": "true",
      "console": "true"
    }

    desired_caps.update(browser)
    test_name = request.node.name
    build = environ.get('BUILD', "Sample PY Build")
    tunnel_id = environ.get('TUNNEL', False)
    username = "neerajn"
    access_key = "RVxtO0XHRNG5VqR9pQumcJ5M9CIx6xu6QLFsGqHbrqkoz9N1GG"
    selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)

    desired_caps['build'] = build
    desired_caps['name'] = test_name
    desired_caps['video']= True
    desired_caps['visual']= True
    desired_caps['network']= True
    desired_caps['console']= True

    executor = RemoteConnection(selenium_endpoint, resolve_ip=False)
    browser = webdriver.Remote(
        command_executor=executor,
        desired_capabilities=desired_caps
    )
    yield browser


@pytest.fixture(scope='function')
def driver2(request):

    desired_caps = {}

    browser2 = {
    "build" : "cc",
    "name" : "your test name",
    "platformName" : "Android",
    "deviceName" : "Galaxy Note 10 Plus",
    "platformVersion" : "10",
    "browserName" :"chrome",
    "name": "v1",
    "network": "true",
    "video": "true",
    "visual": "true",
    "console": "true"
    }

    desired_caps.update(browser2)
    test_name = request.node.name
    build = environ.get('BUILD', "Sample PY Build")
    tunnel_id = environ.get('TUNNEL', False)
    username = "neerajn"
    access_key = "RVxtO0XHRNG5VqR9pQumcJ5M9CIx6xu6QLFsGqHbrqkoz9N1GG"

    selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    desired_caps['build'] = build
    desired_caps['name'] = test_name
    desired_caps['video']= True
    desired_caps['visual']= True
    desired_caps['network']= True
    desired_caps['console']= True

    executor = RemoteConnection(selenium_endpoint, resolve_ip=False)
    browser2 = webdriver.Remote(
        command_executor=executor,
        desired_capabilities=desired_caps
    )
    yield browser2

'''

    def fin():
        #browser.execute_script("lambda-status=".format(str(not request.node.rep_call.failed if "passed" else "failed").lower()))
        if request.node.rep_call.failed:
            browser.execute_script("lambda-status=failed")
        else:
            browser.execute_script("lambda-status=passed")
            browser.quit()
    request.addfinalizer(fin)
    
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for LambdaTest reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set an report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
'''
