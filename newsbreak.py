import webbrowser
import time

# Change the below to suit your needs

SITE_TO_OPEN = "https://bbc.com"  # The site to open
TIMES_TO_OPEN = 8  # Number of times to open site
INTERVAL = 1  # Number of hours between opening site

# DO NOT CHANGE ANYTHING BELOW THIS LINE
times_opened = 0

print("NewsBreak v1.0 | Started", time.ctime())
while times_opened < TIMES_TO_OPEN:
    time.sleep(INTERVAL*3600)
    webbrowser.open(SITE_TO_OPEN)
    times_opened += 1
