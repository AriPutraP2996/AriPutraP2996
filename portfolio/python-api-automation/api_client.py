from __future__ import annotations

import json
from urllib.request import Request, urlopen


class ApiClient:
    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    def get_json(self, url: str):
        request = Request(url, headers={"Accept": "application/json", "User-Agent": "portfolio-api-client/1.0"})
        with urlopen(request, timeout=self.timeout) as response:
            if response.status < 200 or response.status >= 300:
                raise RuntimeError(f"Unexpected HTTP status: {response.status}")
            return json.loads(response.read().decode("utf-8"))
