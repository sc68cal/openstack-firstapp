# Copyright 2014 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""
Worker that consums sensor information from the queue.
Currently just prints whatever it receives to STDout
"""


import pika
from random import randint
import sys
import time

poll_time = 1
queue_name = 'sensor-incoming'
queue_server = 'localhost'

# Make a connection to the message queue
connection = pika.BlockingConnection(pika.ConnectionParameters(
                                     queue_server))
channel = connection.channel(())
channel.queue_declare(queue=queue_name, durable=True)


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep(poll_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,
                          queue=queue_name)

    channel.start_consuming()
    connection.close()

if __name__ == "__main__":
    sys.exit(main())
