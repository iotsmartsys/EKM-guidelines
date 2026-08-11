#!/usr/bin/env python3
"""Valida somente regras estruturais objetivas do roteamento EKOM 3.1."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REPORT_FIELDS = (
    "**Classe da fonte:** Relatório",
    "**Papel:**",
    "**Especificação:**",
    "**Revisão confrontada:**",
    "**Estado:**",
)

FORBIDDEN_SPEC_HEADINGS = (
    "análise de implementabilidade",
    "resultado da implementação",
    "evidências da implementação",
    "revisão independente",
    "relatório de implementação",
    "relatório de revisão",
    "validação e decisão do arquiteto",
)


def markdown_files(root: Path, selected: list[str]) -> list[Path]:
    if selected:
        paths = [(root / value).resolve() for value in selected]
        return [path for path in paths if path.suffix.lower() == ".md"]
    return sorted((root / "docs").rglob("*.md"))


def headings(text: str) -> list[str]:
    return [
        match.group(1).strip().lower()
        for match in re.finditer(r"^#{1,6}\s+(.+)$", text, re.MULTILINE)
    ]


def validate_report(path: Path, text: str) -> list[str]:
    if path.name.lower() == "readme.md":
        return []
    return [f"campo obrigatório ausente: {field}" for field in REPORT_FIELDS if field not in text]


def validate_adr(path: Path, text: str) -> list[str]:
    if path.name.lower() == "readme.md":
        return []
    errors: list[str] = []
    if "**Estado:**" not in text:
        errors.append("campo obrigatório ausente: **Estado:**")
    found = headings(text)
    for required in ("contexto", "decis", "consequên"):
        if not any(item.startswith(required) for item in found):
            errors.append(f"seção obrigatória ausente: {required}…")
    return errors


def validate_spec(text: str) -> list[str]:
    found = headings(text)
    return [
        f"seção de relatório não permitida na especificação: {heading}"
        for heading in found
        if any(heading.startswith(prefix) for prefix in FORBIDDEN_SPEC_HEADINGS)
    ]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Valida o roteamento estrutural de documentos EKOM 3.1."
    )
    parser.add_argument("root", nargs="?", default=".", help="raiz do projeto")
    parser.add_argument(
        "files",
        nargs="*",
        help="arquivos relativos; omitir para verificar todos em docs/",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()
    failures: list[str] = []

    for path in markdown_files(root, args.files):
        if not path.exists():
            failures.append(f"{path}: arquivo inexistente")
            continue
        try:
            relative = path.relative_to(root)
        except ValueError:
            failures.append(f"{path}: arquivo fora da raiz")
            continue
        text = path.read_text(encoding="utf-8")
        parts = relative.parts
        errors: list[str] = []
        if len(parts) >= 2 and parts[:2] == ("docs", "reports"):
            errors = validate_report(path, text)
        elif len(parts) >= 2 and parts[:2] == ("docs", "adr"):
            errors = validate_adr(path, text)
        elif len(parts) >= 2 and parts[:2] == ("docs", "specs"):
            errors = validate_spec(text)
        for error in errors:
            failures.append(f"{relative}: {error}")

    if failures:
        print("Roteamento documental EKOM inválido:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Roteamento documental EKOM válido.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
