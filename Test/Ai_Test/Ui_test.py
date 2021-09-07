from PageActions.Commonfunctions import Test
from PageObjects.Test_case_xpaths import TestActions
import time
import yaml

c_functions = Test()
f_functions = TestActions()

c_functions.open_browser('https://www.globalsqa.com/demo-site/')
c_functions.page_title()
time.sleep(3)
c_functions.scrolldown()
c_functions.click_on_inputs(f_functions.tab_xpath)
time.sleep(3)
c_functions.switch_to_frame(f_functions.frame1)
time.sleep(3)
c_functions.scrolldown()
c_functions.click_on_inputs(f_functions.sections_path)
c_functions.click_on_inputs(f_functions.sections_3)
c_functions.click_on_inputs(f_functions.sections_4)
c_functions.switch()
time.sleep(3)
c_functions.click_on_inputs(f_functions.resize_path)
c_functions.switch_to_frame(f_functions.frame2)
time.sleep(5)
res = c_functions.click_on_inputs(f_functions.resize)
c_functions.scrolldown()
c_functions.move_element(res, 100, 5)
c_functions.click_on_inputs(f_functions.res_1)
c_functions.click_on_inputs(f_functions.res_2)
c_functions.click_on_inputs(f_functions.res_3)
c_functions.switch()
c_functions.click_on_inputs(f_functions.toggle)
time.sleep(3)
c_functions.switch_to_frame(f_functions.frame3)
time.sleep(2)
c_functions.click_on_inputs(f_functions.toggle_2)
c_functions.click_on_inputs(f_functions.toggle_3)
c_functions.click_on_inputs(f_functions.toggle_4)
c_functions.click_on_inputs(f_functions.toggle_icon)
c_functions.switch()
time.sleep(5)
c_functions.click_on_inputs(f_functions.one_bar)
time.sleep(5)
c_functions.click_on_inputs(f_functions.sort)
time.sleep(5)
c_functions.switch_to_frame(f_functions.frame_4)
time.sleep(3)
c_functions.click_on_inputs(f_functions.column_1)
time.sleep(3)
c_functions.select(f_functions.feed)
