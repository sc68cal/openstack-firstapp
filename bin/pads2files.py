#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import hashlib
import json
import logging
import os
import requests
import sys
import yaml

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
logging.getLogger("requests").setLevel(logging.WARNING)

CONFIG = yaml.load(open("pads2files.yaml"))


class PadNotFound(Exception):
    pass


def get_content_from_pad(padname):
    logging.debug("fetching content from pad '%s'" % padname)
    payload = {
        "apikey": CONFIG['secret'],
        "padID": padname
    }
    url = "http://%s/api/1/getText" % CONFIG['server']
    r = requests.get(url, params=payload)
    data = json.loads(r.text)

    if data['code'] == 1:
        raise PadNotFound

    return data['data']['text']


def write_content_to_file(padname):
    try:
        content = get_content_from_pad(padname)
        filename = os.path.join(CONFIG['target'], "%s%s" %
                                (padname, CONFIG['suffix']))

        write = True
        if os.path.isfile(filename):
            cfile = hashlib.md5(open(filename, 'rb').read()).hexdigest()
            ccontent = hashlib.md5(content).hexdigest()
            if cfile == ccontent:
                write = False

        if write:
            logging.info("writing content from pad '%s' to file '%s'" %
                         (padname, filename))
            with open(filename, 'w') as fp:
                fp.write(content)
    except PadNotFound:
        logging.error("pad with name '%s' not found" % padname)

if __name__ == "__main__":
    if not os.path.isdir(CONFIG['target']):
        logging.debug("creating target directory '%s'" % CONFIG['target'])
        os.makedirs(CONFIG['target'])

    pads = get_content_from_pad(CONFIG['index'])
    for padname in pads.splitlines():
        if len(padname) > 0:
            write_content_to_file(padname)
