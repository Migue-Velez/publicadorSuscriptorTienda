import pika

def publishMessage(message):
    credentials = pika.PlainCredentials('qoypinry','VSVBaYPVsR3zhbeVWffbUCKqw0QpCoUf')

    connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host = 'moose-01.rmq.cloudamqp.com',
        virtual_host = 'qoypinry',
        port = 5672,
        credentials = credentials
        ))

    channel = connection.channel()
    exchange = 'productos.agregar'

    channel.exchange_declare(exchange, exchange_type = 'topic', durable=True)
    channel.basic_publish(exchange, routing_key = 'producto', body = message)
    #print(message)
    print(f" [x] Sent {message}")

    connection.close()