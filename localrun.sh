if [ -d ".env" ];
then
    echo " '.env' folder found, starting visualisation"
else 
    echo " '.env' folder not found, creating a virtual environment"
    exit N 
fi
. .env/bin/activate
python3 a_star.py
deactivate
