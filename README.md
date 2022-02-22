# Celery-demo

# install
## install redis
```shell
apt-get install redis-server
```

## install pipenv
```shell
pip install pipenv
```

# How to use
terminal 1
```shell=
celery -A tasks worker -l INFO -c 1 -Q demo
```

terminal 2
```shell
python trigger_add_tasks.py
```

or 
```shell
python trigger_divide_by_zero.py
```