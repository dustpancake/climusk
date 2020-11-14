from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from climusk.routes import category_router, user_router, effort_router

app = FastAPI()


# add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# register routers
app.include_router(
    category_router.router,
    prefix="/category", tags=["Category"]
)
app.include_router(
    user_router.router,
    prefix="/user", tags=["User"]
)
app.include_router(
    effort_router.router,
    prefix="/effort", tags=["Effort"]
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"climusk": {
        "test":"message"
        }
    }
