from gdatlas.analyze.dependency import analyze_dependencies
from gdatlas.model.script import Script

from .common import AnalyzeContext


def analyze_script(ctx: AnalyzeContext, script: Script) -> None:
    analyze_dependencies(ctx, script)
