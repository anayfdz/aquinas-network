from fastapi import ApiRouter

router = ApiRouter()


@router.get("/users")
async def get_users():
    return {"users"}
@router.post("/users")
async def create_user():
    return {"message","Usuario creado exitosamente."}