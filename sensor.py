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
Sensor, that feeds currently random level data to the queue
"""

import pika
from random import randint
import sys
import time

sensor_id = 'AR%d' % randint(90000, 100000)
sample_time = 1
queue_name = 'sensor-incoming'
queue_server = 'localhost'

# Make a connection to the message queue
connection = pika.BlockingConnection(pika.ConnectionParameters(
                                     queue_server))
channel = connection.channel(())
channel.queue_declare(queue=queue_name, durable=True)


def get_level():
    """
    This method defines the level of the water.
    """
    return randint(0, 175)


def main():
    while True:
        message = "[%s] Level: %s" % (sensor_id, get_level())
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body=message)
        print " Sent %s" % message
        time.sleep(sample_time)

    connection.close()

if __name__ == "__main__":
    sys.exit(main())
