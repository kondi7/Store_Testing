from playwright.sync_api import Page, Locator


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    @property
    def add_to_cart_button(self) -> Locator:
        return self.page.locator('button:near(.inventory_item)')

    @property
    def number_of_all_items_in_cart(self) -> int:
        return self.add_to_cart_button.count()

    @property
    def cart(self) -> Locator:
        return self.page.locator(f"a:has-text(\"{self.number_of_all_items_in_cart - 1}\")")

    @property
    def sort_options(self) -> Locator:
        return self.page.locator("[data-test=\"product_sort_container\"]")

    @property
    def items_available(self) -> Locator:
        return self.page.locator('.inventory_item')

    @property
    def item_select(self):
        return self.page.query_selector_all('.inventory_item')

    def add_all_items_to_cart(self) -> None:
        for i in range(self.number_of_all_items_in_cart):
            self.add_to_cart_button.nth(i).click()
        self.cart.click()

    def name_z_to_a_option(self) -> None:
        first_position = self.item_select[0]
        last_position = self.item_select[-1]
        self.sort_options.select_option("za")
        # assert first_position == last_position
