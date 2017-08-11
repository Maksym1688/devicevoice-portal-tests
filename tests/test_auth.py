def login(driver, variables):
    driver.get(variables['url'])
    el = driver.find_element_by_css_selector('input[type="email"][formcontrolname="username"]')
    el.send_keys(variables['auth']['login'])

    el = driver.find_element_by_css_selector('input[type="password"][formcontrolname="password"]')
    el.send_keys(variables['auth']['password'])

    el = driver.find_element_by_css_selector('button[type="submit"]')
    assert el.text == 'Login'
    el.click()

    assert driver.find_element_by_css_selector('li.dv-user-profile')


def test_auth_success(driver, variables):
    login(driver, variables)


def test_auth_failed(driver, variables):
    driver.get(variables['url'])
    el = driver.find_element_by_css_selector('input[type="email"][formcontrolname="username"]')
    el.send_keys('dsfsdf')

    el = driver.find_element_by_css_selector('input[type="password"][formcontrolname="password"]')
    el.send_keys(variables['auth']['password'])

    el = driver.find_element_by_css_selector('button[type="submit"]')
    assert el.text == 'Login'
    el.click()

    if driver.find_elements_by_css_selector('li.dv-user-profile'):
        raise AssertionError()
    el = driver.find_element_by_css_selector('p.help-block')
    assert el.text == 'Username must be a valid email address'
