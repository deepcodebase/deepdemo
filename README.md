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

Assume the ip of your server is `10.61.2.216`

```
http://10.61.2.216:9000/api/score?t1=hello%20world&t2=ni%20hao
```
