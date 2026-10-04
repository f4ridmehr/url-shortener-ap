import secrets
import string

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl

app = FastAPI(title="URL Shortener API")

# In-memory storage: short_code -> original_url
# (data is lost when the server restarts)
urls: dict[str, str] = {}

ALPHABET = string.ascii_letters + string.digits


class ShortenRequest(BaseModel):
    url: HttpUrl


class ShortenResponse(BaseModel):
    short_code: str
    short_url: str
    original_url: str


def generate_code(length: int = 6) -> str:
    while True:
        code = "".join(secrets.choice(ALPHABET) for _ in range(length))
        if code not in urls:
            return code


@app.post("/shorten", response_model=ShortenResponse)
def shorten(body: ShortenRequest, request: Request):
    original = str(body.url)
    code = generate_code()
    urls[code] = original
    return ShortenResponse(
        short_code=code,
        short_url=str(request.base_url) + code,
        original_url=original,
    )


@app.get("/{short_code}")
def redirect(short_code: str):
    original = urls.get(short_code)
    if original is None:
        raise HTTPException(status_code=404, detail="Short code not found")
    return RedirectResponse(url=original)
