from gdatlas.analyze.common import AnalyzeContext
from gdatlas.model.dependency import Dependency
from gdatlas.model.script import Script, ScriptNode
from gdatlas.model.script.element import Class, Constant, Variable
from gdatlas.model.script.metadata import Extends

from .dispatch import ANALYZER_RULES


def analyze_dependency(ctx: AnalyzeContext) -> None:
    for script in ctx.project.scripts:
        _analyze_expressions(ctx, script)
        _analyze_metadata(ctx, script)


def _analyze_expressions(ctx: AnalyzeContext, script: Script) -> None:
    if not script:
        return

    for node in script.elements:
        if not node:
            continue

        expression = None
        if isinstance(node, Constant):
            expression = node.value
        elif isinstance(node, Variable):
            expression = node.default_value

        if not expression:
            continue

        dependency = _resolve_dependency(ctx, expression)
        if not dependency:
            continue

        _add_dependency(script, dependency)


def _analyze_metadata(ctx: AnalyzeContext, script: Script) -> None:
    if not script:
        return

    for node in script.metadata:
        if not node:
            continue

        if not isinstance(node, Extends):
            continue

        dependency = _resolve_dependency(ctx, node)
        if not dependency:
            continue

        _add_dependency(script, dependency)


def _resolve_dependency(ctx: AnalyzeContext, node: ScriptNode) -> Dependency | None:
    for rule in ANALYZER_RULES:
        if not isinstance(node, rule.token):
            continue
        return rule.analyzer(ctx, node)
    return None


def _add_dependency(scope: Script | Class, dependency: Dependency) -> None:
    if not dependency or not scope:
        return
    scope.dependencies.append(dependency)
