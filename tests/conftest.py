import pytest

from pathlib import Path


@pytest.fixture
def fixtures_dir() -> Path:
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def godot3_dir(fixtures_dir: Path) -> Path:
    return fixtures_dir / "godot3"


@pytest.fixture
def godot4_dir(fixtures_dir: Path) -> Path:
    return fixtures_dir / "godot4"
