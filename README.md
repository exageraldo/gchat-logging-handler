
# GChat Logging Handler

Logging handler to send the logs to Google Chat (GChat) room/space.

## Installation

Install with pip:

```bash
$ pip install gchat-logging-handler
```

## Features

- Push logs to google chat using the webhook url
- Send a message to google chat using a simple CLI command (also using webhook)

## Usage/Examples

### In code

```python
import logging

from gchat_logging_handler import GChatHandler


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
gchat_handler = GoogleChatHandler(
    webhook_url="https://chat.googleapis.com/v1/spaces/XXXXXXXXX"
)
gchat_handler.setLevel(logging.ERROR)
logger.addHandler(gchat_handler)

logger.debug("DEBUG - not in gchat")
logger.info("INFO - not in gchat")
logger.error("ERROR - in gchat")

```

### CLI Command

```bash
$ python -m gchat_logging_handler \
    "https://chat.googleapis.com/v1/spaces/XXXXXXXXX" \
    "Sending via CLI"
```

## License

[BSD 3-Clause](/LICENSE)
