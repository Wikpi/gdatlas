from gdatlas.analyze.common import AnalyzeContext
from gdatlas.model.directory import Directory


def analyze_directory(ctx: AnalyzeContext) -> None:
    tree: Directory = _build_directory_tree(ctx)

    _add_directory_tree(ctx, tree)


def _build_directory_tree(ctx: AnalyzeContext) -> Directory:
    root = Directory(ctx.project.path)

    for script in ctx.project.scripts:
        current_directory = root

        relative_directory = script.path.parent.relative_to(ctx.project.path)

        for directory_part in relative_directory.parts:
            current_directory = current_directory.directories.setdefault(
                directory_part,
                Directory(current_directory.path / directory_part),
            )

        current_directory.scripts.append(script)

    return root


def _add_directory_tree(ctx: AnalyzeContext, tree: Directory) -> None:
    ctx.project.directory_tree = tree
