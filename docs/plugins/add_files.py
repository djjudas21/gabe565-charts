import os

from mkdocs.config.base import Config
from mkdocs.structure.files import File, Files


def main(files: Files, config: Config):
    files.append(readme_file(config))

    charts = []
    for root, dirs, dirFiles in os.walk("../charts"):
        for file in dirFiles:
            if file.endswith(".md"):
                charts.append(os.path.join(root, file))
    charts.sort()
    for path in charts:
        files.append(chart_file(path, config))

    return files


def readme_file(config: Config):
    return File(
        path="README.md",
        src_dir="..",
        dest_dir=config.site_dir,
        use_directory_urls=config.use_directory_urls
    )


def chart_file(src_path: str, config: Config):
    src_dir = os.path.dirname(src_path)
    chart_name = os.path.basename(src_dir)
    f = File(
        path=os.path.join("charts", chart_name + ".md"),
        src_dir=src_dir,
        dest_dir=config.site_dir,
        use_directory_urls=config.use_directory_urls
    )
    f.abs_src_path = src_path
    return f
