import os
import shutil
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

from app.services import task as task_service
from app.utils import utils


class TestTaskService(unittest.TestCase):
    def test_generate_subtitle_accepts_edited_subtitle_inside_task_dir(self):
        task_id = "custom-subtitle-test"
        task_dir = utils.task_dir(task_id)
        subtitle_path = Path(task_dir) / "subtitle-edited.srt"
        subtitle_path.write_text(
            "1\n00:00:00,000 --> 00:00:01,000\nedited text\n",
            encoding="utf-8",
        )
        params = SimpleNamespace(
            subtitle_enabled=True,
            custom_subtitle_file=str(subtitle_path),
        )

        try:
            result = task_service.generate_subtitle(
                task_id, params, "script", sub_maker=None, audio_file=""
            )
        finally:
            shutil.rmtree(task_dir, ignore_errors=True)

        self.assertEqual(result, str(subtitle_path))

    def test_generate_subtitle_rejects_edited_subtitle_outside_task_dir(self):
        task_id = "unsafe-subtitle-test"
        task_dir = utils.task_dir(task_id)
        params = None

        with tempfile.NamedTemporaryFile(suffix=".srt", delete=False) as temp_file:
            temp_file.write(
                b"1\n00:00:00,000 --> 00:00:01,000\noutside\n"
            )
            params = SimpleNamespace(
                subtitle_enabled=True,
                custom_subtitle_file=temp_file.name,
            )

        try:
            result = task_service.generate_subtitle(
                task_id, params, "script", sub_maker=None, audio_file=""
            )
        finally:
            os.remove(params.custom_subtitle_file)
            shutil.rmtree(task_dir, ignore_errors=True)

        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
