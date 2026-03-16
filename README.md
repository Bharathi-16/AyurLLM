# 🌿 AyurParam AI

Ayurveda-specialized AI assistant powered by a local LLM.

## Quick Start

```bash
# 1. Clone or download this folder
cd ayurparam

# 2. Setup Virtual Environment (Recommended)
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run
python run.py
```

Open **http://localhost:8080** in your browser.

The model downloads automatically on first run (~2-4 GB depending on model).
Loading takes 1-5 minutes depending on your hardware.

## Features

- **Local LLM Chat** — Streaming responses via SSE, no API keys needed
- **Chat History** — Persistent sessions saved to SQLite
- **Multiple Sessions** — Create, switch, delete conversations
- **Stop / Regenerate** — Control generation in real-time
- **Model Settings** — Temperature, top-p, max tokens sliders
- **Presets** — Fast, Balanced, Quality modes
- **System Prompt Editor** — Customize the AI personality
- **Herb Database** — Built-in Ayurvedic herb lookup panel
- **Dark / Light Mode** — Theme toggle with persistence
- **Export Chat** — Download conversations as TXT
- **Device Auto-Detection** — CUDA, Apple MPS, or CPU
- **Tokens/sec Display** — Real-time performance metrics
- **Mobile Responsive** — Works on phone and tablet
- **Medical Disclaimer** — Built-in safety notice

## Project Structure

```
ayurparam/
├── run.py                  ← Entry point (python run.py)
├── requirements.txt        ← Dependencies
├── .env.example            ← Config template
├── app/
│   ├── __init__.py         ← Flask app factory
│   ├── routes/
│   │   ├── main.py         ← Serves the UI
│   │   ├── chat.py         ← /api/chat (SSE streaming)
│   │   ├── history.py      ← /api/sessions (CRUD)
│   │   ├── settings.py     ← /api/settings
│   │   ├── admin.py        ← /api/admin (health, reload, debug)
│   │   └── herbs.py        ← /api/herbs (lookup)
│   ├── services/
│   │   └── inference.py    ← Model loading, generation, streaming
│   └── models/
│       └── database.py     ← SQLite schema, CRUD operations
├── templates/
│   └── index.html          ← Full chat UI
├── static/                 ← CSS, JS, images (optional)
├── data/                   ← SQLite database (auto-created)
└── logs/                   ← Application logs
```

## API Endpoints

| Method | Endpoint                              | Description               |
| ------ | ------------------------------------- | ------------------------- |
| GET    | `/`                                   | Web UI                    |
| GET    | `/api/status`                         | Model loading status      |
| POST   | `/api/chat`                           | Send message (SSE stream) |
| POST   | `/api/chat/stop`                      | Stop generation           |
| POST   | `/api/chat/regenerate`                | Regenerate last response  |
| GET    | `/api/sessions`                       | List chat sessions        |
| POST   | `/api/sessions`                       | Create new session        |
| GET    | `/api/sessions/:id`                   | Get session + messages    |
| PUT    | `/api/sessions/:id`                   | Update session title      |
| DELETE | `/api/sessions/:id`                   | Delete session            |
| GET    | `/api/sessions/:id/export?format=txt` | Export chat               |
| GET    | `/api/settings`                       | Get inference config      |
| PUT    | `/api/settings`                       | Update config             |
| POST   | `/api/settings/reset`                 | Reset to defaults         |
| GET    | `/api/herbs`                          | List/search herbs         |
| GET    | `/api/herbs/:name`                    | Herb detail               |
| GET    | `/api/admin/health`                   | System health check       |
| POST   | `/api/admin/reload`                   | Hot-reload model          |
| GET    | `/api/admin/debug`                    | Debug info                |

## Hardware Requirements

| Device               | RAM       | Speed          |
| -------------------- | --------- | -------------- |
| CUDA GPU (RTX 3060+) | 6GB+ VRAM | Fast           |
| Apple Silicon (M1+)  | 8GB+      | Good           |
| CPU (Intel/AMD)      | 8GB+      | Slow but works |

## Next Steps (from Architecture Doc)

**Phase 2: RAG** — Add PDF upload + ChromaDB for source-cited answers **Phase 3:
Ayurveda** — Prakriti assessment, structured disease format, Dinacharya **Phase
4: Polish** — Voice I/O, multi-language, admin analytics dashboard
