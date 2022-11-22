cd app &&

echo "#######################################################################"
        echo "|LOGIN - CHANGE_PASSWORD| MAKE WANTED CHANGES SAVE AND EXIT"
        echo "#######################################################################"
        sleep 3s       
        nano main.py

cd core &&

 echo "#######################################################################"
        echo "|APPSECRET - CHANGE_KEY| MAKE WANTED CHANGES SAVE AND EXIT"
        echo "#######################################################################"     
        sleep 3s       
        nano config.py

cd .. &&
cd ..