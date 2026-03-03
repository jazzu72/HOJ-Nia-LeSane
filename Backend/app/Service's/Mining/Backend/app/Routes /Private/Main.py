from app.routes.private import bird_dog, nft_minting

app.include_router(bird_dog.router, prefix="/api/private/bird-dog", tags=["bird-dog"])
app.include_router(nft_minting.router, prefix="/api/private/nft", tags=["nft"])
