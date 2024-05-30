# Kafka List Topics

Simple script to list the topics on a Kafka cluster.

## Configuration

1. Add a `.env` file
2. Add an entry for the bootstrap server URL and an entry to indicate if this connection uses TLS, e.g.

```shell
# no tls
BOOTSTRAP_SERVER=localhost:9092
IS_SSL=false
```


```shell
# tls
BOOTSTRAP_SERVER=localhost:9094
IS_SSL=true
```

## Running

1. Initialize the local virtual environment

```shell
python3 -m venv venv
```

2. Activate the virtual environment

```shell
source venv/bin/activate
```

3. Install the required dependencies

```shell
pip install -r requirements.txt
```

4. Run the app

```shell
python3 main.py
```

## Exiting

To stop the virtual environment try either:

```shell
deactivate
```

or

```shell
source deactivate
```