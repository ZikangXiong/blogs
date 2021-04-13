import os
import datetime
from generator.readme import generate_readme


def deploy():
    os.system("git add .")
    now = datetime.datetime.now()
    t = now.strftime("%Y-%m-%d %H:%M:%S")
    os.system(f'git commit -m "{t}"')
    os.system("git push")


if __name__ == '__main__':
    generate_readme()
    # deploy()
