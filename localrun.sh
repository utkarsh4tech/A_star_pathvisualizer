if [ -d ".env" ];
then
    echo " \'.env\' folder found, installing dependencies using pip3"
else 
    echo " \'.env\' folder not found, creating a virtual environment"
    exit N 
fi
. .env/Scripts/activate
python a_star.py
deactivate