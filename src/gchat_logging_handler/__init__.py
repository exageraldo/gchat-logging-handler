import logging

import httpx


class GChatHandler(logging.Handler):
    def __init__(self, webhook_url: str) -> None:
        logging.Handler.__init__(self)
        if not webhook_url:
            raise ValueError("Webhook url not provided")
        self.webhook_url = webhook_url
        self.http_session = httpx.Client(
            headers={
                'Content-Type': 'application/json; charset=UTF-8'
            }
        )

    def emit(self, record: logging.LogRecord) -> None:
        try:
            self.send_to_gchat(self.format(record))
        except Exception:
            try:
                self.handleError(record)
            except Exception as err:
                print(err)

    def send_to_gchat(self, message: str) -> None:
        self.http_session.post(
            url=self.webhook_url,
            json={"text": message}
        )
