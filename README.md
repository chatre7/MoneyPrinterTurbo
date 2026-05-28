# MoneyPrinterTurbo

AI short-video generator for creating TikTok, Reels, Shorts, news clips, knowledge videos, and product promos from a topic, script, local media, TTS audio, subtitles, and background music.

This fork is tuned for Thai/English video production. The Web UI now includes practical templates, Thai subtitle fixes, a subtitle editor, and a 10-second preview flow before final rendering.

## What This App Does

- Generates or accepts a video script.
- Creates voice audio with TTS.
- Generates and renders subtitles.
- Combines stock or local video/image materials.
- Adds background music.
- Exports short videos in portrait or landscape format.

Primary use case: quickly produce social short videos while still allowing manual control over subtitles, fonts, audio, and source media.

## Key Features

- Web UI with Thai and English interface languages.
- Templates for:
  - Short News
  - Knowledge
  - Product Promo
  - TikTok/Reels Viral
  - Thai Video
  - No Subtitle
  - Subtitle Clean
  - Subtitle With Background
- Thai subtitle rendering with `NotoSansThai-Regular.ttf` and `NotoSansThai-Bold.ttf`.
- Subtitle background toggle.
- Subtitle draft editor before final export.
- Split long Thai subtitle lines.
- 10-second preview render before final video.
- Local media workflow for testing without stock-video API keys.

## Project Structure

```text
app/                  FastAPI app, services, schemas, video pipeline
webui/                Streamlit Web UI and i18n files
webui/i18n/en.json    English UI text
webui/i18n/th.json    Thai UI text
resource/fonts/       Subtitle fonts
resource/songs/       Background music files
storage/              Generated tasks, temp files, local uploaded media
test/                 Unit tests and test resources
main.py               API server entry point
config.example.toml   Example configuration
config.toml           Local runtime configuration, not for sharing
```

## Requirements

- Python 3.11
- `uv`
- FFmpeg
- ImageMagick
- WSL, Linux, macOS, or Windows

Recommended for WSL:

```bash
uv python install 3.11
uv sync --frozen
```

## Configuration

Copy the example config if `config.toml` does not exist:

```bash
cp config.example.toml config.toml
```

Useful config areas:

- `llm_provider`: AI script provider.
- `openai_api_key`, `gemini_api_key`, `qwen_api_key`, etc.: LLM keys.
- `pexels_api_keys`: stock video search via Pexels.
- `pixabay_api_keys`: stock video search via Pixabay.
- `subtitle_provider`: `edge` or `whisper`.
- `edge_tts_timeout`: timeout for Azure TTS V1 / Edge TTS.

You can avoid most keys while testing by using:

- A manually written script.
- `Video Source = Local file`.
- Uploaded local video/image assets.
- Azure TTS V1 / Edge TTS voices.

You need keys when using AI script generation, Pexels, Pixabay, Azure TTS V2, SiliconFlow TTS, Gemini TTS, or other paid/cloud providers.

## Run Locally

Start the Web UI:

```bash
uv run streamlit run webui/Main.py --server.address 0.0.0.0 --server.port 8501 --browser.gatherUsageStats false
```

Open:

```text
http://localhost:8501
```

Start the API server:

```bash
uv run python main.py
```

Open API docs:

```text
http://localhost:8080/docs
```

## Recommended Workflow

1. Open the Web UI.
2. Select a `Video Template`.
3. Click `Apply Template`.
4. Enter a video subject or script.
5. Use local files for fast testing, or configure Pexels/Pixabay keys.
6. Click `Generate Subtitle Draft`.
7. Edit the SRT in the subtitle editor.
8. Click `Split Long Thai Lines` if Thai subtitles are too long.
9. Click `Preview First 10 Seconds`.
10. If the preview is correct, click `Generate Video`.

Generated files are saved under:

```text
storage/tasks/<task-id>/
```

## Subtitle Notes

Thai subtitles require a font with Thai glyph support. This fork keeps only:

```text
resource/fonts/NotoSansThai-Regular.ttf
resource/fonts/NotoSansThai-Bold.ttf
```

If subtitles look wrong, check:

- Font is `NotoSansThai-Regular.ttf`.
- Subtitle lines are not too long.
- Subtitle background is enabled or disabled as desired.
- The edited SRT has valid time ranges.

## Supported Sources

Currently usable video sources:

- `Local file`
- `Pexels`
- `Pixabay`

The UI may show TikTok, Bilibili, or Xiaohongshu entries, but they are not valid generation sources in the current workflow.

## Testing

Run all tests:

```bash
uv run python -m unittest discover -s test
```

Run focused tests:

```bash
uv run python -m unittest test.services.test_video
uv run python -m unittest test.services.test_voice
uv run python -m unittest test.services.test_subtitle
uv run python -m unittest test.services.test_task
```

Some tests are skipped unless matching cloud API keys are configured.

## Security Notes

- Do not commit real API keys in `config.toml`.
- Prefer local media testing before connecting cloud providers.
- Keep `tls_verify = true` unless you are intentionally using a trusted internal proxy.
- Local media paths are restricted to project storage directories to avoid unsafe file reads.

## License

MIT. See [LICENSE](LICENSE).
