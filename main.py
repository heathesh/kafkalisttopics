import os
from kafka.admin import KafkaAdminClient

# from kafka.consumer import KafkaConsumer
from dotenv import load_dotenv

load_dotenv()

boostrap_server_url = os.environ.get("BOOTSTRAP_SERVER")
print(f"Boostrap server URL: {boostrap_server_url}")

is_ssl = os.environ.get("IS_SSL") == "true"
print(f"Is SSL: {is_ssl}")

if is_ssl:
    admin_client = KafkaAdminClient(
        security_protocol="SSL", bootstrap_servers=[boostrap_server_url]
    )
else:
    admin_client = KafkaAdminClient(bootstrap_servers=[boostrap_server_url])

topics = admin_client.list_topics()

for topic in topics:
    print(topic)
