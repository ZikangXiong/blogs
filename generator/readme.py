from .utils import get_root
import shutil
import json
import os

IGNORE = [".ipynb_checkpoints", "res", "_draft", "data", ".DS_Store"]


def get_title(file_path):
    with open(file_path, "r") as f:
        note = json.load(f)
        title = note["cells"][0]["source"][0][2:]

    return title


def generate_file_path(topic, file_name):
    return f"{get_root()}/notebooks/{topic}/{file_name}"


def generate_link(topic, file_name):
    return f"https://nbviewer.jupyter.org/github/ZikangXiong/blogs/blob/main/notebooks/{topic}/{file_name}"


def read_all_notes():
    topics = os.listdir("notebooks/")
    topics = [t for t in topics if t not in IGNORE]
    topics.sort()

    notes = {}
    for t in topics:
        ipynbs = os.listdir("notebooks/" + t)
        ipynbs = [n for n in ipynbs if n not in IGNORE]
        notes[t] = ipynbs

    return notes


def generate_readme():
    notes = read_all_notes()
    readme = f"{get_root()}/README.md"

    shutil.copy(f"{get_root()}/generator/assets/readme_head.md", readme)

    with open(readme, "a") as f:
        for topic, ipy in notes.items():
            f.write(f"## {topic}\n")
            for file in ipy:
                file_path = generate_file_path(topic, file)
                title = get_title(file_path)
                link = generate_link(topic, file)
                f.write(f"- {title} [note]({link.replace(' ', '%20')})  \n")
