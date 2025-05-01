import pika
import sys
import os
import json
import connection as connectionMongo

def main():

    credentials = pika.PlainCredentials('qoypinry','VSVBaYPVsR3zhbeVWffbUCKqw0QpCoUf')

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='moose-01.rmq.cloudamqp.com',
            virtual_host = 'qoypinry',
            port = 5672,
            credentials = credentials
            ))

    channel = connection.channel()

    channel.exchange_declare(exchange='productos.agregar', exchange_type='topic', durable = True)

    queue_name = "suscriptor2"

    channel.queue_bind(exchange='productos.agregar', queue=queue_name, routing_key = "productos")    

    def callback(ch, method, properties, body):
        message = prepareMessage(body)
        print(message)
        connectionMongo.sendMessage(message)

    print(' [*] Esperando para el/los mensaje/s de suscriptor2. Presione CTRL + C para salir.')

    channel.basic_consume(
        queue=queue_name, 
        on_message_callback=callback, 
        auto_ack=True)

    channel.start_consuming()

def prepareMessage(message):
    messageToProcess = message.decode('utf-8')
    print(messageToProcess)
    
    #messageToProcess = messageToProcess.replace("b", "")
    #messageToProcess = messageToProcess.replace("'", "")
    messageToProcess = messageToProcess.split(';')
        
    dictMessage = {
        "Nombre articulo" : messageToProcess[0].strip(),
        "Cantidad articulos" : messageToProcess[1].strip(),
        "Precio unitario" : messageToProcess[2].strip()
    }
    
    return dictMessage
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo del programa")
        sys.exit(0)
    except SystemExit:
        print("Saliendo del programa")
        os._exit(0)