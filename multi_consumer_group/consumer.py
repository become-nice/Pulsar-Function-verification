import pulsar
from _pulsar import ConsumerType
from multiprocessing import Process
 
 
def consumer_data(topic,subscription):
    client = pulsar.Client('pulsar://localhost:6650')
    consumer = client.subscribe(topic, subscription, consumer_type=ConsumerType.Shared)
    while True:
        msg = consumer.receive(timeout_millis=30000)
        print("Received message '{}' id='{}'".format(msg.data(), msg.message_id()))
        consumer.acknowledge(msg)
 
 
if __name__ == "__main__":
    p1 = Process(target=consumer_data, args=("test", "sub1",))
    p2 = Process(target=consumer_data, args=("test", "sub2",))
    p1.start()
    p2.start()