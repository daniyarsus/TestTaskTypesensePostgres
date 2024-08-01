from abc import ABC, abstractmethod
from typing import NoReturn


class ImporterServiceInterface(ABC):
    @abstractmethod
    async def process_data(self, dto) -> NoReturn:
        raise NotImplementedError("<process_data> method must be implemented!")
