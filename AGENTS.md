# Repository Guidelines

## Project Structure & Module Organization

MoneyPrinterTurbo is a Python app for generating short videos from scripts, TTS, subtitles, and stock or local media. API code lives in `app/`: controllers in `app/controllers/`, business logic in `app/services/`, schemas in `app/models/`, configuration in `app/config/`, and shared helpers in `app/utils/`. `main.py` starts the FastAPI API. The Streamlit UI is in `webui/Main.py` with translations in `webui/i18n/`. Static assets are under `resource/` (`fonts/`, `songs/`, `public/`), docs under `docs/`, and tests under `test/services/`.

## Build, Test, and Development Commands

- `uv sync`: create/update the local virtual environment from `pyproject.toml` and `uv.lock`.
- `uv run python main.py`: run the FastAPI API on the configured host/port, default `0.0.0.0:8080`.
- `uv run streamlit run webui/Main.py`: run the Web UI locally.
- `uv run python -m unittest discover -s test`: run the test suite.
- `docker compose up --build`: run API and Web UI containers with the default compose file.

Legacy `pip install -r requirements.txt` is supported, but `uv.lock` is the preferred reproducible environment.

## Coding Style & Naming Conventions

Use Python 3.11+ and 4-space indentation. Follow existing module style: snake_case functions and variables, PascalCase Pydantic models/classes, and concise service-level helpers. Keep changes scoped to the relevant controller/service/model. Prefer structured path and config helpers from `app.utils` and `app.config` over ad hoc filesystem logic. Avoid logging secrets or absolute host paths returned to clients.

## Testing Guidelines

Tests use `unittest` and live in `test/services/` with names like `test_video.py` and `test_<behavior>`. Add focused regression tests for bug fixes, especially around path handling, queue limits, LLM/TTS fallbacks, and video processing edge cases. External-service tests must be skipped unless required credentials are configured, for example with `unittest.skipUnless`.

## Commit & Pull Request Guidelines

Recent history uses Conventional Commits: `fix: ...`, `feat: ...`, `docs: ...`. Keep commit subjects short and imperative. Pull requests should include a clear problem statement, summary of changes, test results, and linked issue when applicable. Include screenshots or generated sample paths for Web UI/video workflow changes.

## Security & Configuration Tips

Do not commit `config.toml`, `storage/`, generated videos, API keys, or uploaded media. Start from `config.example.toml` and set provider keys locally. Be careful with upload endpoints, task file paths, CORS, and auth-related changes; these affect public API exposure and filesystem safety.
