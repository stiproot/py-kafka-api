from fastapi import APIRouter

router = APIRouter()


@router.get("/topic/{topic_name}/consumer/configuration")
async def get_consumer_configuration(topic_name: str):
    pass
