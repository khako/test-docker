import paho.mqtt.client as mqtt
import time

username = "Khako"&nbsp;
mqttc = mqtt.Client(username)
mqttc.connect("mqtt.frugalprototype.com", 1883, 60)

while mqttc.loop() == 0:
    mqttc.publish("frugal/tutorial","Bonjour, je suis " + username + " et je test monit")
    time.sleep(600)