from pydantic import BaseModel, Field


class ProductImportInfo(BaseModel):
    task_id: int = Field(description="Идентификатор задачи импорта.", title="Идентификатор задачи импорта")