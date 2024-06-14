import random


ru_alpha = 'абвгдежзиклмнопрстуфхцчшщэюя'.upper()

REGION_MSK = 'msk'
REGION_SPB = 'spb'

# https://www.autonews.ru/news/633febdb9a79473e43223d37
msk_regions: tuple[int, ...] = (
    77, 97, 99, 177, 197, 199, 777, 797, 799,  # Москва
    50, 90, 150, 190, 750,  # Лен. обл.
)
spb_regions: tuple[int, ...] = (
    78, 98, 178, 198, # Питер
    47, 147,  # Лен. обл.
)


def generate_car_id(location: str) -> str:
    result: list[str] = []
    result.append(random.choice(ru_alpha))  # 1st alpha
    result.append(str(random.randrange(1, 999)).ljust(3, '0'))  # 3 digits
    result.append(''.join(random.choices(ru_alpha, k=2)))  # 2 alpha

    region: int
    if location == REGION_MSK:
        region = random.choice(msk_regions)
    elif location == REGION_SPB:
        region = random.choice(spb_regions)
    else:
        raise ValueError('incorrect')
    result.append(str(region))  # region number

    return ''.join(result)
