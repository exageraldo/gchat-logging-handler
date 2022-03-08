import argparse

from gchat_logging_handler import GChatHandler


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'GChat Logging Handler',
        description='Test the google chat messaging function'
    )
    parser.add_argument('webhook')
    parser.add_argument('message', default="Just testing!")

    args = parser.parse_args()
    webhook = args.webhook
    message = args.message

    gchat_handler = GChatHandler(webhook)
    gchat_handler.send_to_gchat(message)
