from gdatlas.model.dependency import Dependency
from gdatlas.model.script.metadata import Extends

from ..common import AnalyzeContext


def analyze_extends(ctx: AnalyzeContext, node: Extends) -> Dependency | None:
    if not node:
        return None

    target = ctx.resolve_script_reference(node.value)
    if not target:
        return None

    return Dependency(
        target=target,
        source=node,
    )
