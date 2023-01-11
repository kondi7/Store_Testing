from playwright.sync_api import Page, Locator


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def add_to_cart(self) -> Locator:
        return self.page.locator('button:near(.inventory_item)')

    @property
    def number_of_all_items_in_cart(self) -> int:
        return self.add_to_cart.count()

    @property
    def cart(self) -> Locator:
        return self.page.locator(f"a:has-text(\"{self.number_of_all_items_in_cart - 1}\")")

    def add_all_items_to_cart(self) -> None:
        for i in range(self.number_of_all_items_in_cart):
            self.add_to_cart.nth(i).click()
        self.cart.click()
