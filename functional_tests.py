from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\Users\Ninja\PycharmProjects\geckodriver.exe')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
