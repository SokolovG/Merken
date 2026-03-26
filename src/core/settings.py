from typing import Self

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    SOURCE_PROVIDER: str = "MOCHI"
    SOURCE_PROVIDER_BASE_URL = ""
    LLM_PROVIDER: str = ""
    LLM_API_KEY: str = ""
    SOURCE_API_KEY: str = ""

    @model_validator(mode="after")
    def validate_required_secrets(self) -> Self:
        required = {
            "LLM_API_KEY": self.LLM_API_KEY,
            "SOURCE_API_KEY": self.SOURCE_API_KEY,
            "LLM_PROVIDER": self.LLM_PROVIDER,
            "SOURCE_PROVIDER_BASE_URL": self.SOURCE_PROVIDER_BASE_URL,
        }
        missing = [k for k, v in required.items() if not v]
        if missing:
            raise ValueError(f"Missing required secrets: {', '.join(missing)}")
        return self


settings = Settings()
