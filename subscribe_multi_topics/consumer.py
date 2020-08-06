import pulsar
from _pulsar import ConsumerType
from multiprocessing import Process
 
 
def consumer_data(partitions, process_index):
    client = pulsar.Client('pulsar://localhost:6650')
    consumer = client.subscribe(partitions, 'my-subscription', consumer_type=ConsumerType.KeyShared)
    while True:
        msg = consumer.receive(timeout_millis=30000)
        print("Process {} Received message '{}' id='{}' partition={}".format(process_index, msg.data(), msg.message_id(), msg.topic_name()))
        consumer.acknowledge(msg)
 
 
if __name__ == "__main__":
    p1 = Process(target=consumer_data, args=(["test-partition-0", "test-partition-1"], "p1",))
    p2 = Process(target=consumer_data, args=(["test-partition-2", "test-partition-3"], "p2",))
    p1.start()
    p2.start()