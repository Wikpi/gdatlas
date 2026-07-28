from gdatlas.analyze.common import AnalyzeContext
from gdatlas.analyze.script.dependency import analyze_dependencies
from gdatlas.model.script import Script


def analyze_script(ctx: AnalyzeContext, script: Script) -> None:
    analyze_dependencies(ctx, script)
