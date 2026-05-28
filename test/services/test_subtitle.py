import unittest

from app.services import subtitle


class TestSubtitleService(unittest.TestCase):
    def test_split_long_lines_splits_thai_subtitle_with_proportional_timing(self):
        srt_text = (
            "1\n"
            "00:00:00,000 --> 00:00:06,000\n"
            "นี่คือข้อความภาษาไทยที่ยาวมาก และควรถูกแบ่งเป็นหลาย subtitle cue\n"
        )

        result = subtitle.split_long_lines(srt_text, max_chars=28)

        self.assertEqual(result.count("-->"), 3)
        self.assertIn("00:00:00,000 --> 00:00:02,000", result)
        self.assertIn("00:00:04,000 --> 00:00:06,000", result)
        self.assertIn("นี่คือข้อความภาษาไทยที่ยาวมาก", result)
        self.assertIn("และควรถูกแบ่งเป็นหลาย", result)


if __name__ == "__main__":
    unittest.main()
