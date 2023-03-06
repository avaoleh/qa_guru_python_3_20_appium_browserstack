from selene import have, be
from selene.support.shared import browser
from allure import step as title


def test_search_wikipedia():
    with title('Type search'):
        browser.element('Search Wikipedia').tap()
        browser.element('#search_src_text').type('BrowserStack')

    with title('Verify content found'):
        browser.all('#page_list_item_title').should(have.size_greater_than(0))
        browser.element('«Software company based in India»').should(be.visible)


def test_search_selene():
    with title('Type search'):
        browser.element('Search Wikipedia').tap()
        browser.element('#search_src_text').type('selene')

    with title('Verify content found'):
        browser.all('#page_list_item_title').should(have.size_greater_than(0))
        browser.element('«Ancient Greek goddess of the Moon»').should(be.visible)


def test_open_article():
    with title("Activate search field"):
        browser.element("Search Wikipedia").tap()
    with title("Type search request"):
        browser.element('#search_src_text').type('appium')
    with title("Click to the first article"):
        browser.all("#page_list_item_container").first.tap()
