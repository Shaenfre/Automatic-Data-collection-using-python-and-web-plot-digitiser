from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from pynput.mouse import Button, Controller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import glob
browser = webdriver.Firefox()
browser.get("https://apps.automeris.io/wpd/")
for file in glob.glob("/Users/shubham/Desktop/untitled folder/*.jpeg"):
#for i in range(len(filename)):
	pyautogui.moveTo(33,116,duration = 0.25)
	#clicking load image button
	browser.find_element_by_css_selector("div.wpd-menu:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1)").click()
	#browsing the file
	filename = str(file)
	browser.find_element_by_css_selector("#fileLoadBox").send_keys(filename)
	#clicking xy plot button
	xyplt = browser.find_element_by_css_selector("#axesList > p:nth-child(5) > input:nth-child(1)")
	xyplt.location_once_scrolled_into_view
	xyplt.click()
	#clicking proceed
	browser.find_element_by_css_selector("#xyAxesInfo > p:nth-child(6) > input:nth-child(1)").click()
	#clicking the four points on graph

	grph_pt1 = browser.find_element_by_css_selector("#topCanvas")
	ac = ActionChains(browser)
	ac.move_to_element(grph_pt1).move_by_offset(-298.5, 157.7).click().perform()
	ac = ActionChains(browser)
	ac.move_to_element(grph_pt1).move_by_offset(289, 157.7).click().perform()
	ac = ActionChains(browser)
	ac.move_to_element(grph_pt1).move_by_offset(-298.5, 157.7).click().perform()
	ac = ActionChains(browser)
	ac.move_to_element(grph_pt1).move_by_offset(-298.5, -260).click().perform()

	#clicking the complete button
	browser.find_element_by_css_selector("#axes-calibration-sidebar > p:nth-child(3) > input:nth-child(1)").click()
	#filling the x coordinate
	x_cord = browser.find_element_by_css_selector("#xmax")
	x_cord.clear()
	x_cord = browser.find_element_by_css_selector("#xmax")
	x_cord.send_keys("8046")
	#filling the y coordinate
	y_cord = browser.find_element_by_css_selector("#ymax")
	y_cord.clear()
	y_cord = browser.find_element_by_css_selector("#ymax")
	y_cord.send_keys("20000")
	#clicking on ok button
	browser.find_element_by_css_selector("#xyAlignment > center:nth-child(4) > p:nth-child(4) > input:nth-child(1)").click()
	#clicking the run button
	browser.find_element_by_css_selector("#acquireDataSidebar > p:nth-child(15) > input:nth-child(1)").click()
	#clicking the view data button
	browser.find_element_by_css_selector("#dataset-item-tree-widget > center:nth-child(2) > p:nth-child(5) > input:nth-child(1)").click()
	#clicking the download csv button
	browser.find_element_by_css_selector("#csvWindow > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > p:nth-child(4) > input:nth-child(2)").click()
	#clicking the save button
	pyautogui.moveTo(774,515, duration = 1.5) 
	pyautogui.click(774,515, button = 'left')
	#closing the acquired data tab
	browser.find_element_by_css_selector("#csvWindow > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > p:nth-child(4) > input:nth-child(4)").click()
	#clicking for changing colour option
	browser.find_element_by_css_selector("#color-button").click()
	#clicking the red color
	browser.find_element_by_css_selector("#color-selection-red").clear()
	browser.find_element_by_css_selector("#color-selection-red").send_keys("243")
	browser.find_element_by_css_selector("#color-selection-green").clear()
	browser.find_element_by_css_selector("#color-selection-green").send_keys("42")
	browser.find_element_by_css_selector("#color-selection-blue").clear()
	browser.find_element_by_css_selector("#color-selection-blue").send_keys("55")
	#clicking done button

	done = browser.find_element_by_css_selector("#color-selection-widget > p:nth-child(10) > input:nth-child(1)")
	browser.execute_script("arguments[0].click();", done)

	#clicking the run button to get data points
	browser.find_element_by_css_selector("#acquireDataSidebar > p:nth-child(15) > input:nth-child(1)").click()
	#clicking the view data button
	browser.find_element_by_css_selector("#dataset-item-tree-widget > center:nth-child(2) > p:nth-child(5) > input:nth-child(1)").click()
	#clicking the download csv button
	browser.find_element_by_css_selector("#csvWindow > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > p:nth-child(4) > input:nth-child(2)").click()
	#clicking the save button
	pyautogui.moveTo(774,515, duration = 1.5)
	pyautogui.click(774,515, button = 'left')
	#clicking the close button
	browser.find_element_by_css_selector("#csvWindow > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > p:nth-child(4) > input:nth-child(4)").click()

