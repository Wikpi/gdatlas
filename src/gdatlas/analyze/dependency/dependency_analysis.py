from gdatlas.analyze.common import AnalyzeContext, AnalyzeRule
from gdatlas.model.dependency import Dependency
from gdatlas.model.script import Script, ScriptNode, expressions, metadata
from gdatlas.model.script.elements import Class, Constant, Variable
from gdatlas.model.script.metadata import Extends

from .extends_analysis import analyze_extends
from .load_analysis import analyze_load
from .preload_analysis import analyze_preload

DEPENDENCY_ANALYZER_RULES: list[AnalyzeRule] = [
    AnalyzeRule(metadata.Extends, analyze_extends),
    AnalyzeRule(expressions.Load, analyze_load),
    AnalyzeRule(expressions.Preload, analyze_preload),
]


def analyze_dependencies(ctx: AnalyzeContext, script: Script) -> None:
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
    for rule in DEPENDENCY_ANALYZER_RULES:
        if not isinstance(node, rule.token):
            continue
        return rule.analyzer(ctx, node)
    return None


def _add_dependency(scope: Script | Class, dependency: Dependency) -> None:
    if not dependency or not scope:
        return
    scope.dependencies.append(dependency)
