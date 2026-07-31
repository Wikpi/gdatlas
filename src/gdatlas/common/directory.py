from gdatlas.model.directory import Directory


def get_directory_depth(directory: Directory) -> int:
    depth: int = 0

    if not directory.directories:
        return depth

    for new_directory in directory.directories.values():
        if not new_directory:
            continue

        new_depth = get_directory_depth(new_directory) + 1
        if new_depth <= depth:
            continue
        depth = new_depth

    return depth
