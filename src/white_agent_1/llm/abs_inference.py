from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod
    async def call(self, prompt: str, config: dict) -> str:
        pass