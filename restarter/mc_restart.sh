# replace "mc" with the screen of the mc name
# if needed, adjust the path to the cahbot.py
screen -S mc -X stuff "say server restarts in 5 minutes \n"
sleep 240
screen -S mc -X stuff "say server restarts in 1 minute \n"
sleep 30
screen -S mc -X stuff "say server restarts in 30 seconds \n"
sleep 20
screen -S mc -X stuff "say 10 \n"
sleep 1
screen -S mc -X stuff "say 9 \n"
sleep 1
screen -S mc -X stuff "say 8 \n"
sleep 1
screen -S mc -X stuff "say 7 \n"
sleep 1
screen -S mc -X stuff "say 6 \n"
sleep 1
screen -S mc -X stuff "say 5 \n"
sleep 1
screen -S mc -X stuff "say 4 \n"
sleep 1
screen -S mc -X stuff "say 3 \n"
sleep 1
screen -S mc -X stuff "say 2 \n"
sleep 1
screen -S mc -X stuff "say 1 \n"
sleep 1
screen -S mc -X stuff "stop\n"
sleep 30
screen -S mc -X stuff "./start.sh\n"