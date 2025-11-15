"""Simple scheduler for automated Instagram posting."""
import click
import threading
from automation.post_example import schedule_post

@click.command()
@click.option("--image", required=True)
@click.option("--caption", default="Scheduled post")
@click.option("--delay", default=0)
@click.option("--dry-run", is_flag=True, default=True)
def cli_schedule(image, caption, delay, dry_run):
    def worker():
        schedule_post(image, caption, publish_after=delay, dry_run=dry_run)

    t = threading.Thread(target=worker)
    t.start()
    print(f"Post scheduled in {delay}s")

if __name__ == "__main__":
    cli_schedule()
