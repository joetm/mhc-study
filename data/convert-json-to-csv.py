#!/usr/bin/env python

import json
import csv

FILENAME = 'notifications.csv'


with open("sample-notifications-export.json") as fp:
    jsonNotifications = json.load(fp)

    notifications = jsonNotifications['notifications']

    with open(FILENAME, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # header
        header = notifications[0].keys()
        spamwriter.writerow(header)

        for n in notifications:
            spamwriter.writerow([x for x in n.values()])

