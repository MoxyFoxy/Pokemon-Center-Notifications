# Pokemon Center Notifications
This is a simple bot that will send notifications when a product in PokemonCenter is in stock.

This is **NOT** to be used for scalping/mass purchases. This has no ability to automatically purchase products, nor does it have any other additional functionality other than notifying via email when a product is in stock.

In order to better avoid detection, adjust the timings in the `config.py`. In my testing, even with timing, if you do it in succession, it will trigger the bot detection. I plan to have this run once a day via a cron job on a Raspberry Pi 4 once I can get my hands on one.

Once again, for emphasis, **THIS IS NOT TO BE USED FOR SCALPING!!!** This also has **NO** ability to make automatic purchases.

TL;DR of next few paragraphs in Requirements.

Note this will only work on Linux.

The way this works is really weird since PokemonCenter's bot detection is pretty good. It first loads up the page in Firefox, maximizes it, takes a screenshot of the screen, then closes Firefox. This process has multiple sleeps in between to prevent detection as being a bot.

In order to function properly, this script must have full "control" over the system for some time, meaning nothing else interacting with any windows. This is due to this script requiring Firefox to be in the front of the screen in order to take a screenshot. This may change in the future. It must also be ran in the same directory as the main.py, or have the same working directory, as it cleans up the images using `rm *.png` afterwards. You technically should be able to run it anywhere, but just so no one complains this deleted their images, I'll be putting this as a requirement.

Is this kinda hacky? Yeah, it's literally a <50 LOC script excluding the imports and config file. It's small, easy to understand, and easy to edit and extend.

PRs are welcome.

## Installation
This requires `Tesseract`, `wmctrl`, and `Firefox`.

Instructions for installing `Tesseract` can be found [here](https://github.com/tesseract-ocr/tesseract#installing-tesseract). I personally used the Debian repository [here](https://notesalexp.org/tesseract-ocr/#tesseract_5.x).

`wmctrl` can be installed in apt via `sudo apt install wmctrl`. I do not know about installing these in other distros other than Debian-based ones. Feel free to update this section of the README with your process if you use another Linux distro.

There are a variety of ways to install `Firefox`, the easiest simply being to install it via your browser or package manager. You probably even already have it installed. The script is also easy to edit if you wish to use a different browser, but it may take a bit of tweaking.

## Requirements
- Linux
- Firefox
- Tesseract
- wmctrl
- Must have working directory be the same as the script
- Must not be interacting with the machine while script is running
- Must not be opening windows while script is running

PRs to reduce these requirements would be appreciated.