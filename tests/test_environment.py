"""Testes de sanidade do ambiente de desenvolvimento."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_supported_python_version() -> None:
    """Confirma que os testes usam Python 3.12."""
    assert sys.version_info[:2] == (3, 12)


def test_required_setup_files_exist() -> None:
    """Confirma a presença dos arquivos essenciais de preparação."""
    required_files = [
        ".env.example",
        ".gitattributes",
        ".gitignore",
        ".python-version",
        "AGENTS.md",
        "README.md",
        "pyproject.toml",
        "requirements-dev.in",
        "requirements-dev.txt",
    ]

    missing_files = [
        relative_path
        for relative_path in required_files
        if not (PROJECT_ROOT / relative_path).is_file()
    ]

    assert not missing_files, f"Arquivos ausentes: {missing_files}"
