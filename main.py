from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.widget import get_date
from src.widget import mask_account_card

__name__ = "main"

print(get_mask_card_number(7000792289606361))  # 7000 79** **** 6361
print(get_mask_account(73654108430135874305))  # **4305
print(mask_account_card('Счет 64686473678894779589'))
print(get_date("2024-03-11T02:26:18.671407"))
