# replace "mc" with the screen of the mc name
# if needed, adjust the path to the cahbot.py
psres=$(python3 ./cahbot.py)
screen -S mc -X stuff "say $psres \n"