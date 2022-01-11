# Comma-delimited string of URLs.
# 
# Example:
# items = [ 	
#	'https://www.pokemoncenter.com/product/701-29524/vespiquen-sitting-cuties-plush-5-in',
#	'https://www.pokemoncenter.com/product/701-29624/giratina-origin-forme-sitting-cuties-plush-7-in',
#	'https://www.pokemoncenter.com/product/701-29625/giratina-altered-forme-sitting-cuties-plush-9-in',
# ]
# 
# The final comma is optional
# 
# Note that this will ONLY work with
# PokemonCenter links.
items = [
	
]

# Initial delay before the script starts
# Helps prevent system possibly picking up
# on you starting at the same time every day
initial_delay     = 0
initial_delay_end = 3600 # Up to an hour after the scheduled task

# Delay before each item is started
per_item_delay     = 30
per_item_delay_end = 120

# Delay before taking a screenshot
# Necessary to make sure page loads
# properly, and may help prevent detection
per_item_wait = 8

# Email and password of GMAIL account.
# I recommend using an account specifically
# for the bot.
# 
# to_email is your full email. If you want
# to get fancy, you could do something like
# your_email+PokemonCenterBot@gmail.com for
# easy filtering, idk.
# 
# You also need to allow SMTP access in the
# specified GMAIL. Here is a tutorial on
# doing that:
# https://support.google.com/mail/answer/7126229?hl=en#zippy=%2Cstep-check-that-imap-is-turned-on
email_addr = ''
email_pass = ''
to_email   = ''