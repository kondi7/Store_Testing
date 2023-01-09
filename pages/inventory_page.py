from playwright.sync_api import Page, Locator


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def add_to_cart(self):
        x = 'button'
        if x == "#react-burger-menu-btn":
            return False
        else:
            return self.page.locator(f'{x}')

    @property
    def cart(self) -> Locator:
        return self.page.locator("a:has-text(\"6\")")

    def add_all_items_to_cart(self) -> None:
        buttons = self.add_to_cart.count()
        for i in range(buttons):
            self.add_to_cart.nth(i).click()
        self.cart.click()
