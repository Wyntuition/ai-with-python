docker build -t flask-chatterbot ./chatterbot/web-app

docker run -d --restart=always -p 5000:5000 -t flask-chatterbot