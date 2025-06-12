from flask import Flask, request
import json
import os
from google.cloud import pubsub_v1

app = Flask(__name__)
publisher = pubsub_v1.PublisherClient()
project_id = os.environ.get("GCP_PROJECT")
topic_id = os.environ.get("TOPIC_ID")

@app.route("/", methods=["POST"])
def index():
    event = request.get_json()
    name = event.get("name", "unknown")
    size = event.get("size", "unknown")
    format_ = name.split(".")[-1] if "." in name else "unknown"

    message = {
        "file_name": name,
        "file_size": size,
        "file_format": format_
    }

    topic_path = publisher.topic_path(project_id, topic_id)
    publisher.publish(topic_path, json.dumps(message).encode("utf-8"))

    print("Published:", message)
    return "OK", 200
