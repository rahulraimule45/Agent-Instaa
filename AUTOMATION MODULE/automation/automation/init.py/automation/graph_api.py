"""Instagram Graph API wrapper (minimal, safe). Uses dry-run by default."""
import os
import requests
from urllib.parse import urljoin

GRAPH_BASE = "https://graph.facebook.com/"

class GraphAPIError(Exception):
    pass

class InstagramGraphClient:
    def __init__(self, access_token=None, ig_account_id=None, api_version=None, dry_run=True):
        self.access_token = access_token or os.getenv('IG_ACCESS_TOKEN')
        self.ig_account_id = ig_account_id or os.getenv('IG_ACCOUNT_ID')
        self.api_version = api_version or os.getenv('GRAPH_API_VERSION', 'v17.0')
        self.dry_run = dry_run

    def _endpoint(self, path):
        return urljoin(GRAPH_BASE, f"{self.api_version}/{path}")

    def create_media_container(self, image_url, caption):
        if self.dry_run:
            return {"id": "mock_container_" + str(abs(hash(image_url)) % 100000), "status": "dry_run"}
        if not all([self.access_token, self.ig_account_id]):
            raise GraphAPIError("Missing credentials")

        url = self._endpoint(f"{self.ig_account_id}/media")
        params = {"image_url": image_url, "caption": caption, "access_token": self.access_token}
        resp = requests.post(url, params=params, timeout=10)

        if resp.status_code != 200:
            raise GraphAPIError(resp.text)
        return resp.json()

    def publish_container(self, creation_id):
        if self.dry_run:
            return {"id": "mock_media_" + str(abs(hash(creation_id)) % 100000), "status": "dry_run"}

        if not all([self.access_token, self.ig_account_id]):
            raise GraphAPIError("Missing credentials")

        url = self._endpoint(f"{self.ig_account_id}/media_publish")
        params = {"creation_id": creation_id, "access_token": self.access_token}
        resp = requests.post(url, params=params, timeout=10)

        if resp.status_code != 200:
            raise GraphAPIError(resp.text)
        return resp.json()
