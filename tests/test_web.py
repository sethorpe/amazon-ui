import pytest

from pages.search import AmazonSearchPage
from pages.result import AmazonResultPage
from pages.product import AmazonProductPage

@pytest.mark.parametrize('item, warranty',
                        [
                            ('Apple Watch', 'Yes'),
                            # ('McVities HobNobs', ''),
                            # ('Pampers', ''),
                            ('Tal Water Bottle', '')
                        ]
)
def test_basic_amazon_search(browser, item, warranty):
    ITEM = item

    # Search for item
    search_page = AmazonSearchPage(browser)
    search_page.load()
    search_page.search(ITEM)

    # Verify that results appear
    result_page = AmazonResultPage(browser)
    assert result_page.search_input_value() == ITEM

    # Find Amazon Choice item on Results page
    result_page.select_choice_item()
    # Add to Cart and Checkout
    product_page = AmazonProductPage(browser)
    product_page.add_to_cart(warranty)