import pulsar
from multiprocessing import Process
 
 
def produce_test(partition, key, message):
    client = pulsar.Client('pulsar://localhost:6650')
    producer = client.create_producer(partition)
    for i in range(16):
        message_mix = str(int(i)) + message
        producer.send((message_mix).encode('utf-8'), partition_key=key)
    client.close()
 
 
if __name__ == "__main__":
    p1 = Process(target=produce_test, args=("test", "0", "aaaa",))
    p2 = Process(target=produce_test, args=("test", "1", "bbbb",))
    p3 = Process(target=produce_test, args=("test", "2", "cccc",))
    p4 = Process(target=produce_test, args=("test", "3", "dddd",))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
