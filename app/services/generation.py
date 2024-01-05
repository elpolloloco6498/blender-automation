import os
import requests

url_webhook = "https://n8n.ishamletenoux.com/webhook-test/a71824cc-ea70-47e9-b482-2741df9faae8"


async def render_template(text):
    render_path = os.path.abspath("./generation/renders")
    template_path = os.path.abspath("./generation/templates/scene1.blend")
    print(render_path)

    os.system(f'blender.exe --python services/scripts/automation_blender.py -- --render_path "{render_path}" --template_path "{template_path}" --text "{text}"')
    # upload image to bucket and retrieve url, send url in the hook call
    send_render_completion_notification(url_webhook)


def send_render_completion_notification(url_webhook):
    filepath = os.path.abspath("./generation/renders/test.png")
    with open(filepath, "rb") as file:
        binary_data = file.read()
    data = {
        "file": binary_data,
        "status": "file is rendered"
    }
    # "json_data": json.dumps(json_data)
    requests.post(url_webhook, data=data, headers={'Content-Type': 'application/octet-stream'})
