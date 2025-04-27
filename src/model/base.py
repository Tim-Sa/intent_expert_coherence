from pydantic import BaseModel, ConfigDict, Field
from typing import Any, Dict


class BaseModelConfig(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def schema(cls, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        return super().schema(*args, **kwargs)
