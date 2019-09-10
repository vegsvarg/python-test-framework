import os

test_folder = "/Users/jarovit/PycharmProjects/python-test-framework"
driver = "Firefox"
base_url = "http://the-internet.herokuapp.com"
loc_path = "/Users/jarovit/PycharmProjects/python-test-framework"


command_line = "py.test.exe {0} --driver {1} --base-url {2} --variables {3}".format(
                test_folder, driver, base_url, loc_path)

os.system(command_line)
