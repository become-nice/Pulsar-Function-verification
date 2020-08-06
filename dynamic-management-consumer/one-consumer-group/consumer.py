import pulsar
import time
from _pulsar import ConsumerType, InitialPosition
from multiprocessing import Process
 
 
def consumer_data(topic, process_index, partitions):
    client = pulsar.Client('pulsar://localhost:6650')
    consumer = client.subscribe(topic, "subscription", consumer_type=ConsumerType.KeyShared)
    flag = True
    start_time = int(time.time() * 1000)
    while True:
        if (int(time.time() * 1000) - start_time) > 20000 and process_index is "p1" and flag:
            flag = False
            consumer.close()
            consumer = client.subscribe(partitions, "subscription", consumer_type=ConsumerType.KeyShared)
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        msg = consumer.receive(timeout_millis=30000)
        print(
            "Process {} Received message '{}' id='{}' partition={}".format(process_index, msg.data(), msg.message_id(),
                                                                           msg.topic_name()))
        consumer.acknowledge(msg)
 
 
if __name__ == "__main__":
    p1 = Process(target=consumer_data, args=("test", "p1", ["test-partition-0", "test-partition-1"],))
    p2 = Process(target=consumer_data, args=(["test-partition-2", "test-partition-3"], "p2", "",))
    p1.start()
    time.sleep(10)
    p2.start()