"""Generates web site with scales"""
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    env = Environment(
        loader=FileSystemLoader('/app/music_scales/templates/'),
        autoescape=select_autoescape()
    )
    template = env.get_template('web.html')
    rendered_template = template.render()

# (1) Generate all scales in all keys
# (2) Generate pages to present those scales
#      * Organize by key and by scale


if __name__ == '__main__':
    main()
