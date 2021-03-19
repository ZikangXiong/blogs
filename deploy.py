import os
import json
import shutil
import datetime

IGNORE = [".ipynb_checkpoints", "res", "_draft", "data"]


def get_title(file_path):
    with open(file_path, "r") as f:
        note = json.load(f)
        title = note["cells"][0]["source"][0][2:]

    return title


def generate_file_path(topic, file_name):
    return f"notebooks/{topic}/{file_name}"


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
    readme = "README.md"

    shutil.copy("assets/readme_head.md", readme)

    with open(readme, "a") as f:
        for k, ipy in notes.items():
            f.write(f"## {k}\n")
            for file in ipy:
                file_path = generate_file_path(k, file)
                title = get_title(file_path)
                link = generate_link(k, file)
                f.write(f"{title} [note]({link.replace(' ', '%20')})  \n")


def deploy():
    os.system("git add .")
    now = datetime.datetime.now()
    t = now.strftime("%Y-%m-%d %H:%M:%S")
    os.system(f'git commit -m "{t}"')
    os.system("git push")


if __name__ == '__main__':
    generate_readme()
    deploy()
