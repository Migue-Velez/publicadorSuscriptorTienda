package com.mycompany.susciptor1;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.DeliverCallback;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;

 class Susciptor1 {
     
    private static final String password = "VSVBaYPVsR3zhbeVWffbUCKqw0QpCoUf";
     
    public static void main(String[] argv) throws Exception {
      ConnectionFactory factory = new ConnectionFactory();
      factory.setUri("amqps://qoypinry:" + password + "@moose.rmq.cloudamqp.com/qoypinry");
      Connection connection = factory.newConnection();
      Channel channel = connection.createChannel();

      channel.exchangeDeclare("productos.agregar", "topic", true);
      String queueName = "suscriptor1";
      channel.queueDeclare(queueName, true, false, false, null);
      channel.queueBind(queueName, "productos.agregar", "producto");

      System.out.println(" [*] Esperando mensajes para: suscriptor1");

      DeliverCallback deliverCallback = (consumerTag, delivery) -> {
          String message = new String(delivery.getBody(), "UTF-8");
          System.out.println(" [x] Recibido '" + message + "'");
          saveText(message);
      };
      channel.basicConsume(queueName, true, deliverCallback, consumerTag -> { });
    }
    
    public static void saveText(String message) {        
        String path = "C:\\Users\\migue\\Documents\\Universidad\\Semestre VII\\Arquitectura\\seguimiento II\\message.txt";
        File messages = new File(path);
        BufferedWriter bw;
        try {
            messages.getParentFile().mkdirs();
            if (!messages.exists()){
                messages.createNewFile();
            } else {
                System.out.println("Ya existe el archivo.");
            }
            bw = new BufferedWriter(new FileWriter(messages, true));
            while (message != "") {
                bw.write(message);
            bw.newLine();
            bw.close();
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
