# Web Automation with Selenium WebDriver and Python

[Udemy Link](https://udemy.com/course/web-automation-with-selenium-webdriver-and-python/learn/)

## Overview

Course curriculum

- Locating page elements

  - Using CSS
  - Using XPath

- Page navigation
- Filling in forms

  - Text boxes
  - Dropdowns
  - Radio buttons

- Waits in Selenium

  - Explicit and implicit

- Page Object Model (POM)
- Using the POM for web testing

Requirements

- Python
- Basic Python Knowledge
- Visual Studio Code
- Jupyter notebook
- Google Chrome

Environments setup

- Python `3.8.10`
- Goolge Chrome 109.0 (make sure your `ChromeDriver` matches your Chrome version)
- Package requirements

Download drivers

- Chrome: [link](https://chromedriver.chromium.org/downloads)

The `settings.py` file

- URLs used in course
- Path to the chromedriver executable
- Other useful/shared information

Setup environments

- Create folder `selenium-udemy`
- Create venv `python -m venv venv`
- Active new env: `source venv/bin/activate`
- Deactive env: `deactivate`
- Requirements file: `pip install -r requirements.txt`
- Settings file: `settings.py`
- Env file: `config.env`

Requirements.txt

```txt
argon2-cffi==21.3.0
argon2-cffi-bindings==21.2.0
asttokens==2.0.8
async-generator==1.10
attrs==22.1.0
backcall==0.2.0
beautifulsoup4==4.11.1
bleach==5.0.1
certifi==2022.6.15.1
cffi==1.15.1
colorama==0.4.5
debugpy==1.6.3
decorator==5.1.1
defusedxml==0.7.1
entrypoints==0.4
executing==1.0.0
fastjsonschema==2.16.1
h11==0.13.0
idna==3.3
importlib-metadata==4.12.0
importlib-resources==5.9.0
ipykernel==6.15.2
ipython==8.5.0
ipython-genutils==0.2.0
ipywidgets==8.0.2
jedi==0.18.1
Jinja2==3.1.2
jsonschema==4.16.0
jupyter==1.0.0
jupyter-console==6.4.4
jupyter-core==4.11.1
jupyter_client==7.3.5
jupyterlab-pygments==0.2.2
jupyterlab-widgets==3.0.3
lxml==4.9.1
MarkupSafe==2.1.1
matplotlib-inline==0.1.6
mistune==2.0.4
nbclient==0.6.8
nbconvert==7.0.0
nbformat==5.4.0
nest-asyncio==1.5.5
notebook==6.4.12
outcome==1.2.0
packaging==21.3
pandocfilters==1.5.0
parso==0.8.3
pexpect==4.8.0
pickleshare==0.7.5
pkgutil_resolve_name==1.3.10
prometheus-client==0.14.1
prompt-toolkit==3.0.31
psutil==5.9.2
ptyprocess==0.7.0
pure-eval==0.2.2
pycparser==2.21
Pygments==2.13.0
pyparsing==3.0.9
pyrsistent==0.18.1
PySocks==1.7.1
python-dateutil==2.8.2
python-dotenv==0.21.0
pyzmq==23.2.1
qtconsole==5.3.2
QtPy==2.2.0
selenium==4.4.3
Send2Trash==1.8.0
six==1.16.0
sniffio==1.3.0
sortedcontainers==2.4.0
soupsieve==2.3.2.post1
stack-data==0.5.0
terminado==0.15.0
tinycss2==1.1.1
tornado==6.2
traitlets==5.3.0
trio==0.21.0
trio-websocket==0.9.2
urllib3==1.26.12
wcwidth==0.2.5
webencodings==0.5.1
widgetsnbextension==4.0.3
wsproto==1.2.0
zipp==3.8.1
```

Driver path: `/Users/dalatcoder/Documents/GitHub/learn-python/web-automation-selenium-2023/selenium-udemy`

Wayback machine: [web archive](https://web.archive.org)

```py
from settings import CHROMEDRIVER_PATH
from selenium import webdriver
```

Selenium use cases in this course

- A web scraper for Wikipedia data
- A form fillter for a band booking form
- A python unit test for testing a booking form

### Chrome Dev Tools

What is chrome devtools?

- A set of web developer tools built directly in the Google
  Chrome Browser
- Makes your life easier

- Elements tab: Inspect DOM and DOM elements
- Console tab: View logged messages or run JS
- Application tab: veiw and edit storage variables, cookies

### Selenium

What is Selenium?

- Selenium automates browsers. that's it
- [Selenium docs](https://www.selenium.dev)
- [Selenium Python docs](https://selenium-python.readthedocs.io/index.html)

Uses cases

- Web scraping/data collection
- Screenshots/captures
- Website testing and automation
- Automation of browser-based tasks

Selenium enables browser automation via a `WebDriver`.
The Web driver is basically the interface between your
Selenium API and the browser.

`Python` -> `Selenium` -> `ChromeDriver` -> `Chrome`

To use Selenium, we need the following installed

- Python
- Selenium package - python - selenium
- Browser-specific WebDriver
- Browser (matching WebDriver)

Note: browser software and version should match:
`Chrome v104 != ChromeDriver v105`

Steps to start Selenium session

- Import `webdriver`
- Import service for specific browser
- Instantiate service object using file path to WebDriver
- Instantiate WebDriver using browser/service
- Get URL using WebDriver
- Quite WebDriver

```py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Driver setup
service = Service(executable_path='path/to/driver')
driver = webdriver.Chrome(service=service)
driver.get('https://someurl.com')
driver.quit()
```
