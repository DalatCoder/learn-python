# Web Automation with Selenium WebDriver and Python

[Udemy Link](https://udemy.com/course/web-automation-with-selenium-webdriver-and-python/learn/)

Table of contents

- [Web Automation with Selenium WebDriver and Python](#web-automation-with-selenium-webdriver-and-python)
  - [1. Overview](#1-overview)
    - [1.1. Chrome Dev Tools](#11-chrome-dev-tools)
    - [1.2. Selenium](#12-selenium)
  - [2. Locating Page Elements](#2-locating-page-elements)
    - [2.1. Locating by CSS Selector](#21-locating-by-css-selector)
    - [2.2. Locating by ID](#22-locating-by-id)
    - [2.3. Locating by Name](#23-locating-by-name)
    - [2.4. Locating by Tag Name](#24-locating-by-tag-name)
    - [2.5. Locating by XPath](#25-locating-by-xpath)
    - [2.6. Locating by Link Text](#26-locating-by-link-text)
    - [2.7. Chaining locators](#27-chaining-locators)
    - [2.8. Useful web element methods and attributes](#28-useful-web-element-methods-and-attributes)
  - [3. Note for setup](#3-note-for-setup)
  - [4. Project: Wikipedia Scraper](#4-project-wikipedia-scraper)
  - [5. Page Navigation](#5-page-navigation)
    - [5.1. Opening and Closing Windows](#51-opening-and-closing-windows)
    - [5.2. Opening and Closing Tabs](#52-opening-and-closing-tabs)
    - [5.3. Navigating iFrames](#53-navigating-iframes)
    - [5.4. Browser History](#54-browser-history)
    - [5.5. Alerts](#55-alerts)
    - [5.6. Cookies and Storage](#56-cookies-and-storage)
    - [5.7. Resizing Windows](#57-resizing-windows)
  - [6. Automation of filling in Forms](#6-automation-of-filling-in-forms)
    - [6.1. Buttons](#61-buttons)
    - [6.2. Input Elements](#62-input-elements)
    - [6.3. Radio Buttons and checkboxes](#63-radio-buttons-and-checkboxes)
    - [6.4. Dropdown Menus](#64-dropdown-menus)
    - [6.5. Calendar Picker](#65-calendar-picker)
    - [6.6. File upload and Download](#66-file-upload-and-download)
    - [6.7. Drag and Drop](#67-drag-and-drop)
    - [6.8. Sliders](#68-sliders)
    - [6.9. Keyboard Actions](#69-keyboard-actions)
  - [7. Project: Form Filler](#7-project-form-filler)
  - [8. Wait](#8-wait)
    - [8.1. Implicit Waits](#81-implicit-waits)
    - [8.2. Explicit Waits](#82-explicit-waits)
    - [8.3. Adjusting Network Settings](#83-adjusting-network-settings)

## 1. Overview

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

### 1.1. Chrome Dev Tools

What is chrome devtools?

- A set of web developer tools built directly in the Google
  Chrome Browser
- Makes your life easier

- Elements tab: Inspect DOM and DOM elements
- Console tab: View logged messages or run JS
- Application tab: veiw and edit storage variables, cookies

### 1.2. Selenium

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

## 2. Locating Page Elements

### 2.1. Locating by CSS Selector

All ways of locating page elements with Selenium depend on 2 parts

- By: how do you want to find elements?
- String: what string tells us what to find?

Two WebDriver methods to find element(s)

- `find_element()`: find one (or first) element satisfying locator conditions
- `find_elements()`: find all elements satisfying locator conditions

### 2.2. Locating by ID

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

### 2.3. Locating by Name

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

### 2.4. Locating by Tag Name

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

### 2.5. Locating by XPath

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

### 2.6. Locating by Link Text

`<a>` tags will usually have user-visible text showing on
a web page. Useful when you know some or all of the link text
withinn the anchor `<a>` tag.

Selenium lets us search with exact link text `By.LINK_TEXT`
or by partial match `By.PARTIAL_LINK_TEXT`

### 2.7. Chaining locators

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

### 2.8. Useful web element methods and attributes

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

## 3. Note for setup

Move `chromedriver` executable to home directory at:
`/Users/dalatcoder/bin` (create `bin` folder for organization)

Change `CHROMEDRIVER_PATH` in `config.env` to `CHROMEDRIVER_PATH=/Users/dalatcoder/bin/chromedriver`

Give permissions to the executable with

- `xattr -d com.apple.quarantine chromedriver`
- `spctl --add --label 'Approved' chromedriver`

## 4. Project: Wikipedia Scraper

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

## 5. Page Navigation

### 5.1. Opening and Closing Windows

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

### 5.2. Opening and Closing Tabs

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

### 5.3. Navigating iFrames

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

### 5.4. Browser History

Selenium does not allow access to browser history. However, you
can execute common browser history commands like `forward`
and `back`

```py
driver.get('first')
driver.get('second')

driver.back()
driver.forward()
```

### 5.5. Alerts

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

### 5.6. Cookies and Storage

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

### 5.7. Resizing Windows

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

## 6. Automation of filling in Forms

### 6.1. Buttons

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

### 6.2. Input Elements

You'll usually want to fill out a form field or clear it

- `input_element.clear()`
- `input_element.send_keys('text')`

```py
input_element.clear()
input_element.send_keys('Filling forms is cool')
```

### 6.3. Radio Buttons and checkboxes

Work similarly to buttons in Selenium

- `click()` - click element
- `is_selected()` - check if element is selected

Checkboxes can be selected/deselected with a click;
radio buttons cannot.

```py
checkbox = driver.find_element(By.ID, 'id')

# check selected status
checkbox.is_selected()

# select via click
checkbox.click()
```

### 6.4. Dropdown Menus

Dropdown menus are `<select>` elements in HTML. Options
for the dropdown are contained in `<option>` tags.

You can interact with the elements using the methods
we've learned so far (selecting, click, etc.)

Or, you can use a `Select` object

`Select` objects in Selenium are objects that provide
nice wrappers for dealing with select elements

- `options` - show options
- `select_by_index()`
- `select_by_visible_text()`
- `select_by_value()`

Also can work with multiple-select menus - adds deselect methods

```py
from selenium.webdriver.support.ui import Select

select_element = driver.find_element(By.ID, 'id')
select = Select(select_element)

# options
select.options

# selecting
select.select_by_index(2)
select.select_by_value('value1')

# deselects - only for multi-selects
select.deselect_by_index(2)
select.deselect_all()
```

### 6.5. Calendar Picker

Calendar pickers are a common form element in many
websites these days (think of an airline booking site)

They're generally composed of three components of interest

- An input field
- JS/jQuery to make calendar popup
- The calendar itself (i.i. a `<table>`)

These components provide the outline of how to interact
with calendar pickers

- Find the calendar input element
- Activate the JS/jQuery - e.g. with a click
- Select date of interest from table

You can also use `send_keys()` to simply fill out the date
rather than picking it. Note that this method may still
activate the calendar

### 6.6. File upload and Download

File uploads involve sending text/keys to an input element.
However, note that the path sent to the input element
must be a real path and satisfy any upload restrictions (e.g.
only `.png` files). Otherwise, you'll trigger an error

File downloads tent to be straightforward: click on the
element or download button of interest to activate the
download. We can also change the download directory with
`ChromeOptions()`

Setting directory with ChromeOptions

```py
options = webdriver.ChromeOptions()
options.add_experimental_options('prefs', {
  'download.default_directory': 'path/to/directory'
})

driver = webdriver.Chrome(service=service, options=options)
```

For upload

```py
upload_element = driver.find_element(By.ID, 'upload')
upload_element.send_keys('/Users/dalatcoder/downloads/test.png')
```

### 6.7. Drag and Drop

Since drag and drops are essentially mouse actions - and
really involve a combination of different actions - we'll
need to use `ActionChains` again

We can use a pure drag and drop with a source and target
element. Or we can use a drag and drop with offset, starting
at a source element

```py
src = driver.find_element(By.ID, 'src')
dest = driver.find_element(By.ID, 'dest')

actions.drag_and_drop(src, dest).perform()
```

### 6.8. Sliders

Sliders are an interesting form item, because they can be
interacted with in two ways

- Click
- ActionChains

Within ActionChains, you can use:

- `move_to_element_with_offset()`
- `drag_and_drop_by_offset()`

```py
action = ActionChains(driver=driver)

X = 40 # X offset
Y = 0 # Y offset

action.move_to_element_with_offset(slider_element,X,Y).click().perform()
action.drag_and_drop_by_offset(slider_element,X,Y).perform()
```

### 6.9. Keyboard Actions

As mentioned before, ActionChains enable us to
automate basic user interactions in the browser.

This includes key combinatioins that may be used as shortcuts - think of the keyboard shortcuts in Gmail.

To use this functionality with special keys like Esc, Ctrl, etc., we'll need to import the Keys class.

We need ActionChains to send keys to the browser, as
opposed to a specific element, and to mimic key
combos (e.g. Ctrl + P)

We can use the methods `key_down()`, `key_up()`, and
`release()` methods from ActionChains to mimic the key
combos.

```py
from selenium.webdriver.common.keys import Keys

# Emulate Ctrl + D
action.key_down(Keys.CONTROL).send_keys('d').release().perform()
```

## 7. Project: Form Filler

Goal: fill out and submit the booking request form at
`https://www.thegoldbugs.com/`

- Text fields
- Radio buttons
- Checkboxes
- Dropdowns

- Use what we've learned about identifying elements to select
  form fields.
- Use what we've learned about filling in forms to interact
- with the elements (e.g. clicking, selecting, checking, etc.)
- Submit the form
- Everything we do applies to other forms in real life - booking forms, surveys, searches, etc.

## 8. Wait

### 8.1. Implicit Waits

Modern web pages may have elements that load at different times.

This can cause problems if we try to find elements that
don't yet exist on the page (but will in a second!)

Selenium gives us a way to address this problem with `waits`.
Waits can be

- `Explicit`
- `Implicit`

Implit waits are a session setting during the life of your
`WebDriver` object

An implicit wait tells Selenium to continually check the
DOM for some set amount of time for any element not found
immediately.

Generally, explicit waits are more useful than implicit
waits or using `time.sleep()`.

With explicit waits, you only wait as long as you have to - your program will run faster.

Implicit waits don't provide information on `why/when` we're
waiting.

You can set implicit waits with the `implicitly_wait(seconds)`
method.

Set implicit waits

```py
# set implicit wait for the session
driver.implicitly_wait(10)
```

It's generally better to use explicit waits instead of implicit waits.

### 8.2. Explicit Waits

AS mentioned before, explicit waits in Selenium are more
useful than implicit waits.

Explicit waits sepcify conditions that need met before
proceeding in the code. Ex: wait for form to load before
filling it in.

Setting explicit waits involves two objects:

- A `WebDriverWait`
- An `expected condition`

Selenium provides a number of methods for expected conditions

- `title_is`
- `visibility_of_element_located`
- `element_to_be_clickable`
- and more!

Explicit waits are a characteristic of better/more
maintainable Selenium code.

Explicit waits are more robuts againts network conditions than
the typical alternative, `time.sleep()`. You may also want
to put your explicit waits inside `try-catch-finally` blocks.

Explicit waits imports

```py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Explicit wait for element
element = WebDriverWait(driver,5).until(
  EC.element_to_be_clickable((By.ID, 'btn-id'))
)

# Compare to code without wait
element = driver.find_element(By.ID, 'btn-id')
```

Practice with vanilla Python script

```py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from settings import CHROMEDRIVER_PATH, SELENIUM_DOCS_SEARCH_URL

service = Service(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get(SELENIUM_DOCS_SEARCH_URL)

input_element = driver.find_element(By.NAME, 'q')
input_element.send_keys('explicit wait')
input_element.submit()

LINK_XPATH = '//*[@id="search-results"]/ul/li[1]/a'

# fail, result element does not exist yet!
result_element = driver.find_element(By.XPATH, LINK_XPATH)
print(result_element.text)

driver.quit()
```

Using explicit waits

```py
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException

from settings import CHROMEDRIVER_PATH, SELENIUM_DOCS_SEARCH_URL

service = Service(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get(SELENIUM_DOCS_SEARCH_URL)

# noive way using time.sleep()
time.sleep(3)
input_element = driver.find_element(By.NAME, 'q')
time.sleep(3)
input_element.send_keys('explicit wait')
time.sleep(3)
input_element.submit()

LINK_XPATH = '//*[@id="search-results"]/ul/li[1]/a'

try:
  result_element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH, LINK_XPATH))
  )
  print(result_element.text)
except ElementNotVisibleException:
  print('Element not visible')
finally:
  time.sleep(4)
  driver.quit()
```

### 8.3. Adjusting Network Settings

Sometimes you may want to emulate slower network speeds to
better understand user experience of your site.

Chrome DevTools does provide a Network Throttling setting in
the Network tab. You can also automate it with the `set_network_conditions()` method

`set_network_conditions()` has several parameters

- Offline
- Latency - in `ms`
- Download throughput - in `bps`
- Upload throughput - in `bps`

By adding latency, lowering download throughput, etc. you
can emulate slow networks.
