from string import ascii_letters
from random import choices
import webbrowser

random_letters = choices(ascii_letters, k=5)

post_id = ''.join(random_letters)
post_id = post_id.lower()

print("Rolling!")
webbrowser.open_new_tab(f'https://redd.it/{post_id}')
