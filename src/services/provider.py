from http import HTTPMethod
from typing import Protocol

from src.api.client import HTTPClient
from src.core.settings import settings
from src.core.value_objects import Card


class IProviderService(Protocol):
    async def add_card(self, data: Card) -> None: ...
    async def delete_card(self, data: Card) -> None: ...
    async def update_card(self, data: Card) -> None: ...


class MochiService:
    def __init__(self, http_client: HTTPClient) -> None:
        self.client = http_client
        self.base_url = settings.SOURCE_PROVIDER_BASE_URL

    def _get_headers(self) -> dict[str, str]:
        return {
            "Content-Type": "application/json",
            "Authorization": f"Basic {settings.SOURCE_API_KEY}",
        }

    async def add_card(self, data: Card) -> None:
        try:
            body = {"content": "", "deck-id": "", "template-id": ""}
            response = self.client.make_request(
                url=f"{self.base_url}cards",
                data=body,
                method=HTTPMethod.POST,
                headers=self._get_headers(),
            )

        except Exception:
            ...

    async def delete_card(self, data: Card) -> None:
        try:
            card_id = ""
            body = {}
            response = self.client.make_request(
                url=f"{self.base_url}cards/{card_id}",
                data=body,
                method=HTTPMethod.DELETE,
                headers=self._get_headers(),
            )
        except Exception:
            ...

    async def update_card(self, data: Card) -> None:
        try:
            card_id = ""
            body = {"content": ""}
            response = self.client.make_request(
                url=f"{self.base_url}cards/{card_id}",
                data=body,
                method=HTTPMethod.POST,
                headers=self._get_headers(),
            )
        except Exception:
            ...


class AnkiService:
    def __init__(self, http_client: HTTPClient) -> None:
        self.client = http_client

    async def add_card(self, data: Card) -> None: ...
    async def delete_card(self, data: Card) -> None: ...
    async def update_card(self, data: Card) -> None: ...
