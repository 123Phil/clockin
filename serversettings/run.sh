uwsgi --ini ../serversettings/uwsgi.ini 1>../clock/logs/console_uwsgi.log 2>../clock/logs/uwsgi.log </dev/null &
echo "started."

