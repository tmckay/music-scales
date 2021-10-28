"""Generates web site with scales"""
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape


_SCALE_IMG_DIR = Path('/images')


def _get_all_scale_images():
    files_in_dir = [ff for ff in _SCALE_IMG_DIR.glob('*') if ff.is_file()]
    return files_in_dir


def main():
    env = Environment(
        loader=FileSystemLoader('/app/music_scales/templates/'),
        autoescape=select_autoescape()
    )
    template = env.get_template('web.html')
    rendered_template = template.render(imgs=_get_all_scale_images())
    print(rendered_template)


if __name__ == '__main__':
    main()
