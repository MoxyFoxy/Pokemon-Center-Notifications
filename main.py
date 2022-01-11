import datetime
import os
import pyautogui
import PIL
import pytesseract
import random
import signal
import smtplib
import subprocess
import time
from email.mime.text import MIMEText

import config

if __name__ == '__main__':
	images_list   = []
	in_stock_list = []

	# Initial delay, used for scheduling. Comment out if running manually.
	time.sleep(random.randint(config.initial_delay, config.initial_delay_end))

	# Start up SMTP client
	email = smtplib.SMTP('smtp.gmail.com', 587)
	email.starttls()
	email.login(config.email_addr, config.email_pass)

	# Iterate through every link
	for item in config.items:

		# Protects against getting identified as a bot. Adds delay between each request
		time.sleep(random.randint(config.per_item_delay, config.per_item_delay_end))

		firefox = subprocess.Popen(['firefox', item])

		# Sleep for letting the window fully open
		time.sleep(config.per_item_wait)

		# Maximize window
		os.popen('wmctrl -r :ACTIVE: -x "Navigator.Firefox" -b add,maximized_vert,maximized_horz')

		# Sleep for letting it maximize before screenshot
		time.sleep(2)

		images_list.append((item.split('/')[-1]).split('?')[0] + '_' + str(datetime.datetime.now()) + '.png')

		pyautogui.screenshot().save(images_list[-1])

		# Closes Firefox window
		# 
		# This was originally here because I was
		# using os.kill each time since it was annoying
		# to kill otherwise. This will probably still work
		# in the parent scope, but might need a workaround
		# for closing multiple tabs at once.
		os.popen('wmctrl -c "Firefox" -x "Navigator.Firefox"')

	# Iterate through each of the generated items
	for image_name in images_list:
		image = PIL.Image.open(image_name)

		width, height = image.size

		# This cropping is very specific since Tesseract kinda sucks detecting the "ADD TO CART"
		image_cropped = image.crop((width // 2, height // 1.5, width, height - 200))

		text = pytesseract.image_to_string(image_cropped)

		in_stock = True

		if 'OUT OF STOCK' in text:
			in_stock = False

		# This means we probably ran into
		# PokemonCenter's bot detection
		elif 'ADD TO CART' not in text:
			print(str(text))

			msg = MIMEText('We got caught! Bot has been detected.\nTry changing your timings')

			msg['Subject'] = 'PokemonCenter SMTP Bot has been detected'
			msg['From'] = config.email_addr
			msg['To'] = config.to_email

			email.sendmail(config.email_addr, config.to_email, msg.as_string())

			break

		in_stock_list.append(in_stock)

	# Delete all of the images generated
	os.popen('rm *.png')

	# Iterate through each item to see if it's in stock
	for (idx, in_stock) in enumerate(in_stock_list):
		if in_stock:
			msg = MIMEText(f'Item at {config.items[idx]} is in stock!')

			msg['Subject'] = 'PokemonCenter Product In Stock'
			msg['From'] = config.email_addr
			msg['To'] = config.to_email

			email.sendmail(config.email_addr, config.to_email, msg.as_string())

	email.quit()