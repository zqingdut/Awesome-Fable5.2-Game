#!/usr/bin/env python3
"""Render README.md from data/cases.json using templates/README.md.j2."""
import json

from jinja2 import Environment, FileSystemLoader

CATEGORIES = {
    "racing": "🏎️ 竞速 (Racing)",
    "shooter": "🔫 射击 (Shooter)",
    "casual": "🚲 休闲 (Casual)",
    "moba": "⚔️ MOBA 对战 (MOBA)",
    "action": "🥷 动作 (Action)",
    "rpg": "🗡️ 角色扮演 (RPG)",
    "puzzle": "🧩 益智 (Puzzle)",
    "sports": "⚽ 体育 (Sports)",
    "sandbox": "🏗️ 沙盒 (Sandbox)",
    "other": "🎮 其他 (Other)",
}

CATEGORIES_EN = {
    "racing": "🏎️ Racing",
    "shooter": "🔫 Shooter",
    "casual": "🚲 Casual",
    "moba": "⚔️ MOBA",
    "action": "🥷 Action",
    "rpg": "🗡️ RPG",
    "puzzle": "🧩 Puzzle",
    "sports": "⚽ Sports",
    "sandbox": "🏗️ Sandbox",
    "other": "🎮 Other",
}


def cell(value) -> str:
    """Sanitize a value for use inside a Markdown table cell."""
    if value is None:
        return ""
    return str(value).replace("|", "¦").replace("\n", " ").strip()


def build():
    with open("data/cases.json", "r", encoding="utf-8") as f:
        cases = json.load(f)

    env = Environment(
        loader=FileSystemLoader("templates"),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    env.filters["cell"] = cell
    template = env.get_template("README.md.j2")
    md = template.render(cases=cases, categories=CATEGORIES)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(md)
    print(f"README.md rendered from {len(cases)} cases.")

    template_en = env.get_template("README_EN.md.j2")
    md_en = template_en.render(cases=cases, categories_en=CATEGORIES_EN)
    with open("README_EN.md", "w", encoding="utf-8") as f:
        f.write(md_en)
    print(f"README_EN.md rendered from {len(cases)} cases.")


if __name__ == "__main__":
    build()
