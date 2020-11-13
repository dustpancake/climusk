import motor.motor_asyncio
import os

MONGO_DETAILS = os.environ["MONGO_DETAILS"]
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# probably wont be changing this from development ever,
# so won't make this easier to change
database = client.development
