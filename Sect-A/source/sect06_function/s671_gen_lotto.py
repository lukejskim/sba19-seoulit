import random

def get_lotto():
    lotto_num = set()

    while True:
        pick_num = random.randint(1,46)
        lotto_num.add(pick_num)

        if len(lotto_num)==6:
            break

    lotto_num = sorted(list(lotto_num))

    return lotto_num

lotto_numbers = get_lotto()
print( lotto_numbers )

