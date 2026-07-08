"""
example_usage.py -- Demonstrates AntiAICopyPurifierClient
"""
from client import AntiAICopyPurifierClient

def main():
    client = AntiAICopyPurifierClient()
    result = client.purify_copy(
        text_copy="Let us delve into this new tool. It is more than just a seamless game changer to elevate your workflow."
    )
    print("[Copy Purifier Result]")
    print(f"Cliche count: {result['ai_cliche_count']}")
    print(f"Purified: {result['purified_text']}")

if __name__ == "__main__":
    main()
