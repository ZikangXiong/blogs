from utils import get_root
import markdown as md


def md_to_html(readme):
    with open(readme, "r") as f:
        content = md.markdown(f.read())

    return content


def fill_template(template_path, tag, content) -> str:
    with open(template_path, "r") as f:
        ret = f.read()
        ret = ret.replace(tag, content)
    return ret


def generate_index():
    readme = f"{get_root()}/README.md"
    template = f"{get_root()}/generator/assets/template.html"
    output = f"{get_root()}/index.html"

    blog_tag = "{% blog-list %}"
    content = md_to_html(readme)
    index = fill_template(template, blog_tag, content)

    with open(output, "wb") as f:
        f.write(index.encode(encoding='UTF-8'))


if __name__ == '__main__':
    generate_index()
