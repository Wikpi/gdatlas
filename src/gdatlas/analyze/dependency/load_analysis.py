from gdatlas.analyze.common import AnalyzeContext
from gdatlas.model.dependency import Dependency
from gdatlas.model.script.expressions import Load


def analyze_load(ctx: AnalyzeContext, node: Load) -> Dependency | None:
    if not node:
        return None

    target = ctx.resolve_script_reference(node.path)
    if not target:
        return None

    return Dependency(
        target=target,
        source=node,
    )
