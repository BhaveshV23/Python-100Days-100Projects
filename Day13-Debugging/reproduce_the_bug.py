from random import randint

dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)

print(dice_images[dice_num])

# Debugging method:
# - Reproduced the bug by controlling random range
# - Fixed index error by using valid list indices
