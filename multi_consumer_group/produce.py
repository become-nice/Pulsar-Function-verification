import pulsar
from multiprocessing import Process
 
 
def produce_test(topic, message):
    client = pulsar.Client('pulsar://localhost:6650')
    producer = client.create_producer(topic)
    for i in range(16):
        producer.send((message).encode('utf-8'))
    time.sleep(1000)
    client.close()
 
 
if __name__ == "__main__":
    p1 = Process(target=produce_test, args=("test", "aaaa",))
    p1.start()