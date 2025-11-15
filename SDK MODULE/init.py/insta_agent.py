"""InstaAgent SDK wrapper."""
from automation.graph_api import InstagramGraphClient

class InstaAgent:
    def __init__(self, access_token=None, ig_account_id=None, dry_run=True):
        self.client = InstagramGraphClient(access_token, ig_account_id, dry_run=dry_run)

    def post_image(self, image_url, caption):
        container = self.client.create_media_container(image_url, caption)
        creation_id = container.get("id")
        return self.client.publish_container(creation_id)
