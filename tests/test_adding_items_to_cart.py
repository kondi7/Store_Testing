from playwright.sync_api import Playwright
from pages.main_page import MainPage
from pages.inventory_page import InventoryPage
from settings.fixtures import user_data


def test_adding_items_to_cart(user_data: dict, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    main_page = MainPage(page)
    main_page.navigate()
    page.pause()
    inventory_page = InventoryPage(page)
    main_page.login_to_store(user_data)
    inventory_page.add_all_items_to_cart()
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()
