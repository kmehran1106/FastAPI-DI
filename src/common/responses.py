from pydantic import BaseModel


class ApiResponse(BaseModel):
    status_code: int
