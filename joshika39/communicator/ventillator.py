import zmq
import random
import time


class Ventillator():
    def __init__(self, sender_addr: str, sink_addr: str) -> None:
        print(f"Creating ventillator ({sender_addr}) with the sink ({sink_addr})")
        context = zmq.Context()
        
        self.sender = context.socket(zmq.PUSH)
        self.sender.bind(sender_addr)

        self.sink = context.socket(zmq.PUSH)
        self.sink = self.sink.connect(sink_addr)

    def start(self):
        print("Press Enter when the workers are ready: ")
        _ = input()
        print("Sending tasks to workers...")

        self.sink.send(b'0')

        random.seed()

        total_msec = 0
        for task_nbr in range(100):

            workload = random.randint(1, 100)
            total_msec += workload

            self.sender.send_string(f"{workload}")

        print(f"Total expected cost: {total_msec} msec")

        time.sleep(1)
