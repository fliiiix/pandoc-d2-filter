import os
import re
import subprocess
from pathlib import Path

__TEST_BASE_DIR__ = Path(os.path.dirname(__file__)) / "testdata"


def extract_images(json):
    pattern = r"\[\"d2-images\/.*.[png|svg]\""
    return re.findall(pattern, json)


def test_basic_diagram():
    input_file = str(__TEST_BASE_DIR__ / "default.md")
    cmd = subprocess.run(
        ["pandoc", "-t", "json", "--filter", "pandoc-d2", input_file], capture_output=True, text=True, check=False
    )
    assert cmd.returncode == 0

    assert len(extract_images(cmd.stdout)) == 1


def test_theme_number_diagram():
    input_file = str(__TEST_BASE_DIR__ / "theme_number.md")
    cmd = subprocess.run(
        ["pandoc", "-t", "json", "--filter", "pandoc-d2", input_file], capture_output=True, text=True, check=False
    )
    assert cmd.returncode == 0

    assert len(extract_images(cmd.stdout)) == 1
    assert '["theme","1"]' in cmd.stdout


def test_theme_number_invalid_diagram():
    input_file = str(__TEST_BASE_DIR__ / "invalid_theme_number.md")
    cmd = subprocess.run(
        ["pandoc", "-t", "json", "--filter", "pandoc-d2", input_file], capture_output=True, text=True, check=False
    )
    assert cmd.returncode == 0

    assert len(extract_images(cmd.stdout)) == 1
    assert "not found" in cmd.stderr


def test_theme_name_diagram():
    input_file = str(__TEST_BASE_DIR__ / "theme_name.md")
    cmd = subprocess.run(
        ["pandoc", "-t", "json", "--filter", "pandoc-d2", input_file], capture_output=True, text=True, check=False
    )
    assert cmd.returncode == 0

    assert len(extract_images(cmd.stdout)) == 1
    assert '["theme","Grape soda"]' in cmd.stdout


def test_theme_name_invalid_diagram():
    input_file = str(__TEST_BASE_DIR__ / "invalid_theme_name.md")
    cmd = subprocess.run(
        ["pandoc", "-t", "json", "--filter", "pandoc-d2", input_file], capture_output=True, text=True, check=False
    )
    assert cmd.returncode == 0

    assert len(extract_images(cmd.stdout)) == 1
    assert "not found" in cmd.stderr
