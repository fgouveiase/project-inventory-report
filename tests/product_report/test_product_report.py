from inventory_report.product import Product


def test_product_report() -> None:
    mock_product = Product(
        id="1",
        company_name="company",
        product_name="company product",
        manufacturing_date="2023-06-08",
        expiration_date="2025-10-17",
        serial_number="1234",
        storage_instructions="hgfddgh",
    )

    assert str(mock_product) == (
        "The product 1 - company product "
        "with serial number 1234 "
        "manufactured on 2023-06-08 "
        "by the company company "
        "valid until 2025-10-17 "
        "must be stored according to the following instructions: hgfddgh."
    )
