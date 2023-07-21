from inventory_report.product import Product


def test_create_product() -> None:
    mock_product = Product(
        id="1",
        company_name="company",
        product_name="company product",
        manufacturing_date="2023-06-08",
        expiration_date="2025-10-17",
        serial_number="1234",
        storage_instructions="hgfddgh",
    )

    assert mock_product.id == "1"
    assert mock_product.company_name == "company"
    assert mock_product.product_name == "company product"
    assert mock_product.manufacturing_date == "2023-06-08"
    assert mock_product.expiration_date == "2025-10-17"
    assert mock_product.serial_number == "1234"
    assert mock_product.storage_instructions == "hgfddgh"
