from playwright.sync_api import Playwright
from pages.main_page import MainPage
from settings.fixtures import user_data
from pages.inventory_page import InventoryPage


def test_sorting(user_data: dict, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    main_page = MainPage(page)
    main_page.navigate()
    page.pause()
    inventory_page = InventoryPage(page)
    main_page.login_to_store(user_data)
    inventory_page.name_z_to_a_option()
    context.tracing.stop(path='test_results/trace_test_sort_items.zip')
    context.close()
    browser.close()
