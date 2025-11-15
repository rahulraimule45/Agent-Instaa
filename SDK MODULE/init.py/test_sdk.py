"""SDK test runner."""
from sdk.insta_agent import InstaAgent

def main():
    agent = InstaAgent(dry_run=True)
    resp = agent.post_image("https://example.com/img.png", "Hello from SDK test")
    print("SDK response:", resp)

if __name__ == "__main__":
    main()
