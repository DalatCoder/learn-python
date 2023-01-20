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

## Locating Page Elements

### Locating by CSS Selector

All ways of locating page elements with Selenium depend on 2 parts

- By: how do you want to find elements?
- String: what string tells us what to find?

Two WebDriver methods to find element(s)

- `find_element()`: find one (or first) element satisfying locator conditions
- `find_elements()`: find all elements satisfying locator conditions

### Locating by ID

ID is unique, so very useful for selecting elements in Selenium

```py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Driver setup
service = Service(executable_path='path/to/driver')
driver = webdriver.Chrome(serivce=service)

# Get URL
driver.get('https://someurl.com/')

# Find element by ID
element1 = driver.find_element(By.ID, 'id')
element1.get_attribute('innerHTML')
element1.get_attribute('data-name')

# Find all elements by class name
all_elements = driver.find_elements(By.CSS_SELECTOR, '.class')
all_elements = driver.find_elements(By.CSS_SELECTOR, '#id')
```

### Locating by Name

Some elements will have a `name` attribute associated with
their HTML tag.

Mostly seen with buttons, forms, form elements, etc.

Unlike ID, not guaranteed to be unique within the page.

The `name` attribute is mostly relevant for HTTP requests
to the server.

```py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Driver setup
service = Service(executable_path='path/to/driver')
driver = webdriver.Chrome(serivce=service)

# Get URL
driver.get('https://someurl.com/')

# Find element by Name
elements = driver.find_elements(By.NAME, 'title')
elements[0].get_attribute('innerHTML')
elements[0].get_attribute('data-name')

element = driver.find_element(By.CSS_SELECTOR, 'input[name="title"]')
```

### Locating by Tag Name

HTML tags are the basic unit of web page setup

Selenium lets us locate elements by their HTML tag name

Usually more useful for finding all elements, find all links with `a` tag

```py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Driver setup
service = Service(executable_path='path/to/driver')
driver = webdriver.Chrome(serivce=service)

# Get URL
driver.get('https://someurl.com/')

# Find element by TagName
elements = driver.find_elements(By.TAG_NAME, 'a')
elements[0].get_attribute('innerHTML')
elements[0].get_attribute('data-name')
```

### Locating by XPath

XPath is th elanguage for locating nodes in an XML document

HTML can be an implementation of XML - this means we can use
XPath to locate elements

Very useful for navigating when element of interest doesn't
have id or name attribute

Can search in relative (advised) or absolute (not advised) terms.

Example syntax

- `/html/body/input[1]`: Absolute path
- `//input[1]` - first input on page
- `//input[@id='search-box']` - input with ID of 'search-box'
- `//a[@title="Title"]/../div` - div one parent above link
  with the title `Title`

Chrome DevTools lets us copy the XPath from `sources` tab.

```py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Driver setup
service = Service(executable_path='path/to/driver')
driver = webdriver.Chrome(serivce=service)

# Get URL
driver.get('https://someurl.com/')

# Find element by XPath
elements = driver.find_elements(By.XPATH, '//input')
elements[0].get_attribute('innerHTML')
elements[0].get_attribute('data-name')
```

Test XPath with Chrome Devtools

```js
$x("//a");
$x("//a[@title]");
```

### Locating by Link Text

`<a>` tags will usually have user-visible text showing on
a web page. Useful when you know some or all of the link text
withinn the anchor `<a>` tag.

Selenium lets us search with exact link text `By.LINK_TEXT`
or by partial match `By.PARTIAL_LINK_TEXT`

### Chaining locators

- All the locators we've reviewed can be chained together
- Useful for navigating parent/child elements
- Might be more readable than using XPath in certain cases

```py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Driver setup
service = Service(executable_path='path/to/driver')
driver = webdriver.Chrome(serivce=service)

# Get URL
driver.get('https://someurl.com/')

# Find element by XPath
element1 = driver.find_element(By.ID, 'id')
element1[0].get_attribute('innerHTML')
element1[0].get_attribute('data-name')

element2 = element1.find_element(By.CSS_SELECTOR, '.class')
```

### Useful web element methods and attributes

The elements you find on the page are `WebElement` objects
in Selenium. It's useful to know some of the more common
attributes and methods associated with `WebElement` objects.

See documentatioin for complete list.

Attributes

- `text`
- `tag_name`
- `size`
- `is_displayed()`
- `is_enabled()`
- `is_selected()`

Methods

- `screenshot()`
- `find_element()`
- `find_elements()`
- `get_dom_attribute()`
- `get_attribute()`
- `get_property()`
- `value_of_css_property()`

`get_dom_attribute()` - gets attribute from underlying HTML (can change with JS)

`get_property()` - get current state of attribute that might
change (text in text box)

`get_attribute()` - gets initial content element of attribute
that might change (initial value of text in text box)

## Note for setup

Move `chromedriver` executable to home directory at:
`/Users/dalatcoder/bin` (create `bin` folder for organization)

Change `CHROMEDRIVER_PATH` in `config.env` to `CHROMEDRIVER_PATH=/Users/dalatcoder/bin/chromedriver`

Give permissions to the executable with

- `xattr -d com.apple.quarantine chromedriver`
- `spctl --add --label 'Approved' chromedriver`

## Project: Wikipedia Scraper

Goal: Scrape link information from 4 main div sections
on Wikipedia

- From today's featuerd article
- In the news
- Did you know...
- On this day

And then,

- Use what we've learned about element locators to construct a dictionary of links by div section
- Store information on each link: title, text and href
- Dictionary structure will look like:

```py
result = {
    'div identifier': [
        {
            title: '',
            text: '',
            href: ''
        }
    ]
}
```

See notebook [Notebook](./selenium-udemy/proj1.ipynb)

## Page Navigation

### Opening and Closing Windows

In older versioins of Selenium, we had to
instantiate a new webdriver in order to open a new window or new tab.

Now, we can switch more easily with:
`driver.switch_to.new_window('window')`

And close secondary/active windows with

- `driver.close()`
- The above method doesn't work if only 1 window active

```py
driver.get('first_url')
dirver.switch_to.new_window('window')
driver.get('second_url')

# close the second window
driver.close()
```

### Opening and Closing Tabs

Opening and closing tabs works like windows

- `driver.switch_to.new_window('tab')`
- `driver.close()` only when more than 1 tab

To switch between tabs, we can use `window handles`, unique
IDs for windows/tabs

- `driver.current_window_handle`
- `driver.window_handles` - list all window handles from
  session
- `driver.switch_to.window('window_handle')`

Old method - executing Javascript:
`driver.execute_script('window.open("url")')`

```py
driver.get('first_url')
dirver.switch_to.new_window('tab')
driver.get('second_url')

# close the second tab
driver.close()
```

To switch between tabs

```py
handles = driver.window_handles
driver.switch_to.window(handles[1])
driver.switch_to.window(handles[0])

print(driver.current_window_handle)

# close tab
driver.close()
```

### Navigating iFrames

iFrames or inline frame load other HTML elements inside a
web page.

Kind of link `HTML within HTML`

Elements inside an iFrame `can't` be selected directyly with
Selenium.

Instead, you have to switch from the `main` HTML into the
`iFrame`

Same problem in reverse - main HTML not accessible within iFrame

Steps:

- Find iFrame element
- Switch to iFrame - `driver.switch_to.frame(WebElement)`
- Find element of interest within iFrame
- Switch back to main HTML - `driver.switch_to.default_content()`

```py
driver.get('url')
iframe = driver.find_element(By.ID, 'iframe')

driver.switch_to.frame(iframe)
driver.find_element(By.ID, 'inside-iframe')
driver.switch_to.default_content()
```

### Browser History

Selenium does not allow access to browser history. However, you
can execute common browser history commands like `forward`
and `back`

```py
driver.get('first')
driver.get('second')

driver.back()
driver.forward()
```

### Alerts

Web pages sometimes have alerts or pop-up dialogs that
show up. In order to interact with them, we should
switch to them like tabs or iFrames.

Alert objects have methods for accepting, dismissing, etc.

```py
driver.get('url')
alert = driver.switch_to.alert
driver.execute_script('alert("Hey!")')

alert.text
alert.accept()
alert.dismiss()
```

### Cookies and Storage

Selenium provides nice methods for interacting with cookies
on a web page

- `driver.get_cookies()`
- `driver.add_cookie()`

However, there's no built-in method for interacting with
local or session storage.

Instead, we have to rely on executing JavaScript
`driver.execute_script()`

Working with Cookies

```py
driver.get('url')

driver.get_cookies()
driver.add_cookie({
    'name': 'c_name',
    'value': 'c_value'
})
```

Working with LocalStorage

````py
driver.execute_script(
    ```
        window.localStorage.setItem('key', 'value')
    ```
)
driver.execute_script(
    ```
    return window.localStorage.getItem('key')
    ```
)
````

Working with Session Storage

````py
driver.execute_script(
    ```
        window.sessionStorage.setItem('key', 'value')
    ```
)
driver.execute_script(
    ```
    return window.sessionStorage.getItem('key')
    ```
)
````

### Resizing Windows

Changing window size could be useful for testing website
accessibility, mobile, etc.

Useful methods in Selenium for window size and position:

- `driver.get_window_size()`: get size
- `driver.get_window_position()`: get position
- `driver.get_window_rect()`: get size & position

Useful methods in Selenium for window size and position

- `driver.set_window_size()`
- `driver.set_window_position()`
- `driver.set_window_rect()`
- `driver.minimize_window()`
- `driver.maximize_window()`

## Automation of filling in Forms

### Buttons

You can interact with buttons by:

- clicking - `button.click()`
- context clicking, i.e. right-click
- click and hold/release

For things like click and hold, we need to use `ActionChains`

ActionChains chain specific user actions together, such as

- Moving the mouse
- Clicking mouse buttons
- Pressing keys
- Drag and drops
- Sliders
- And more!

```py
button = driver.find_element(By.CSS_SELECTOR, 'button#id')
button.click()
```

Or ActionChains

```py
import selenium.webdriver.common.action_chains import ActionChains

action = ActionChains(driver=driver)

action.context_click(element).preform()
action.click_and_hold(element).perform()
action.release().perform()
```

### Input Elements

You'll usually want to fill out a form field or clear it

- `input_element.clear()`
- `input_element.send_keys('text')`

```py
input_element.clear()
input_element.send_keys('Filling forms is cool')
```
