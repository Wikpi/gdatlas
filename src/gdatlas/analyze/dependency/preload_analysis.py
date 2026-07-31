from gdatlas.analyze.common import AnalyzeContext
from gdatlas.model.dependency import Dependency
from gdatlas.model.script.expression import Preload


def analyze_preload(ctx: AnalyzeContext, node: Preload) -> Dependency | None:
    if not node:
        return None

    target = ctx.resolve_script_reference(node.path)
    if not target:
        return None

    return Dependency(
        target=target,
        source=node,
    )
