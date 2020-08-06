import pulsar
import time
from multiprocessing import Process
 
 
def produce_test(partition, key, message):
    client = pulsar.Client('pulsar://localhost:6650')
    producer = client.create_producer(partition)
    for i in range(240):
        time.sleep(2)
        message_mix = str(int(i)) + message
        print(message_mix)
        producer.send((message_mix).encode('utf-8'), partition_key=key)
    time.sleep(1000)
    client.close()
 
 
if __name__ == "__main__":
    p1 = Process(target=produce_test, args=("test", "10000", "aaaa",))
    p2 = Process(target=produce_test, args=("test", "20000", "bbbb",))
    p3 = Process(target=produce_test, args=("test", "30000", "cccc",))
    p4 = Process(target=produce_test, args=("test", "40000", "dddd",))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
