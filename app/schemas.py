"""Schemas for the input/output in API."""
from typing import List

from pydantic import BaseModel


class CommonBase(BaseModel):
    """Common schema for both input and output data."""

    sentence: str


class Input(CommonBase):
    """Input schema."""

class Versions(BaseModel):
    """Schema for the versions."""

    api: str
    data: str
    model: str


class Toxicity_score(CommonBase):
    """Schema for the output data."""

    sentence: str
    score: float


class API_output(BaseModel):
    """Schema for the output."""

    data: Toxicity_score
    versions: Versions

