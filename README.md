# Install dependencies

```
pip install flask
pip install flask-cors
pip install flask-compress

```

## Launch Server

```
python core.py launch_server --port 9000
```

## Test APIs

Assume the IP of your server is `10.61.2.216`, open the link in your browser:

```
http://10.61.2.216:9000/api/score?t1=hello%20world&t2=ni%20hao
```

## Launch Client

```
python core.py launch_client --port 8000
```

