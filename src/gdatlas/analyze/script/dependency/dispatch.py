from gdatlas.analyze.common import AnalyzeRule
from gdatlas.model.script import expression, metadata

from .extends_analysis import analyze_extends
from .load_analysis import analyze_load
from .preload_analysis import analyze_preload

ANALYZER_RULES: list[AnalyzeRule] = [
    AnalyzeRule(metadata.Extends, analyze_extends),
    AnalyzeRule(expression.Load, analyze_load),
    AnalyzeRule(expression.Preload, analyze_preload),
]
