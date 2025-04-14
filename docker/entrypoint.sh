echo "Start database migrates"
python3 manage.py migrate
echo "Successfully migrated database"
echo "Start collect static"
python3 manage.py collectstatic --noinput
echo "Successfully collected static"
echo "Start server"
python3 manage.py runserver 0.0.0.0:8080
