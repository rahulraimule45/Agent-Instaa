"""Example script to schedule and publish a post (dry-run by default)."""
import argparse
import time
from automation.graph_api import InstagramGraphClient

def schedule_post(image_url, caption, publish_after=0, dry_run=True):
    client = InstagramGraphClient(dry_run=dry_run)
    print("[Agent] Creating media container...")
    container = client.create_media_container(image_url, caption)
    print("Container:", container)

    if publish_after > 0:
        print(f"Waiting {publish_after}s...")
        time.sleep(publish_after)

    creation_id = container.get("id")
    print("Publishing:", creation_id)
    resp = client.publish_container(creation_id)
    print("Publish response:", resp)
    return resp

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", default="https://example.com/photo.jpg")
    parser.add_argument("--caption", default="Demo post")
    parser.add_argument("--publish_after", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true", default=True)
    args = parser.parse_args()

    schedule_post(args.image, args.caption, args.publish_after, args.dry_run)
