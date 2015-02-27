# -*- coding: utf-8 -*-
import soundcloud

client = soundcloud.Client(client_id=CLIENT_ID)

track = client.get('/resolve', url='http://soundcloud.com/xzayoso/fractales')
print track.id

track = client.get('/tracks/111261789/stream', allow_redirects=False)
print track.location

tracks = client.get('/tracks', limit=10)
for track in tracks:
    print track.title
    print track.id