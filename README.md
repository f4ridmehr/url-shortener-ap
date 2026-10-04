# URL Shortener API

A simple URL shortener REST API built with [FastAPI](https://fastapi.tiangolo.com/).

Send a long URL, get back a short code, and use that code to be redirected to the original address.

## Features

- Create a short link from any valid URL
- Redirect from a short code to the original URL
- Interactive API docs (Swagger UI) out of the box
- Lightweight and easy to extend

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/f4ridmehr/url-shortener-ap.git
cd url-shortener-ap
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Documentation

FastAPI generates interactive docs automatically:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints

| Method | Endpoint       | Description                          |
| ------ | -------------- | ------------------------------------ |
| POST   | `/shorten`     | Create a short URL                   |
| GET    | `/{short_code}`| Redirect to the original URL         |

### Example

**Request**

```bash
curl -X POST http://127.0.0.1:8000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/some/very/long/path"}'
```

**Response**

```json
{
  "short_code": "aB3xYz",
  "short_url": "http://127.0.0.1:8000/aB3xYz",
  "original_url": "https://example.com/some/very/long/path"
}
```

Opening `http://127.0.0.1:8000/aB3xYz` in a browser redirects to the original URL.

## Project Structure

```
url-shortener-ap/
├── main.py
├── requirements.txt
└── README.md
```

## Roadmap

- [ ] Persistent storage (SQLite / PostgreSQL)
- [ ] Custom aliases
- [ ] Link expiration
- [ ] Click statistics
- [ ] Docker support
- [ ] Tests

## Contributing

Issues and pull requests are welcome.

## License

Add a license of your choice (for example, MIT).
