from time import sleep
import emoji
for c in range(10, -1, -1):
    print(c)
    sleep(0.3)
print('\033[1;33mBANG!\033[m', end=" ")
print(emoji.emojize(':boom:' * 10, use_aliases=True))