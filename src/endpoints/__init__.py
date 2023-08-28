from fastapi import APIRouter

from . import get_consumer_configuration
from . import publish_to_topic

router = APIRouter()

router.include_router(get_consumer_configuration.router)
router.include_router(publish_to_topic.router)

__all__ = ["router"]
