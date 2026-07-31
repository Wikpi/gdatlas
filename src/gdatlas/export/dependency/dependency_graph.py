from pathlib import Path

from graphviz import Digraph

from gdatlas.common.directory import get_directory_depth
from gdatlas.model import Project
from gdatlas.model.directory import Directory
from gdatlas.model.script.expression import Load, Preload
from gdatlas.model.script.metadata import Extends

EDGE_COLORS = {
    Extends: "#4A90E2",
    Preload: "#2ECC71",
    Load: "#F39C12",
}


def export_dependency_graph(project: Project, output_file: str, output_path: Path) -> None:
    graph = _create_new_directed_graph()

    graph = _build_graph(graph, project)

    graph.render(
        filename=output_path / output_file.removesuffix(".svg"),  # TODO: remove hardcoded file format.
        format="svg",
        cleanup=True,
    )


def _build_graph(graph: Digraph, project: Project) -> Digraph:
    _render_subgraphs(graph, project)
    _render_graph_legend(graph)
    _render_graph_edges(graph, project)

    return graph


def _create_new_directed_graph() -> Digraph:
    return Digraph(
        engine="dot",
        graph_attr={
            "label": "Dependency Graph\n\n",  # Graph title
            "rankdir": "TB",  # Graph draw direction
            "splines": "ortho",  # Graph edge draw style
            "nodesep": "1.0",  # Graph horizontal spacing
            "ranksep": "1.5",  # Graph vertical spacing
            "pad": "1",  # Padding around graph
            "margin": "0",  # Graph canvas margin
            "overlap": "false",  # Graph node overlap (engine specific)
            "concentrate": "true",  # Merge parallel graph edges
            "fontname": "Times-Bold",  # Graph title font
            "fontsize": "38",  # Graph title size
            "fontcolor": "black",  # Graph title color
            "labeljust": "c",  # Graph title allignment
            "labelloc": "t",  # Graph title position
            "bgcolor": "white",  # Graph background color
            "dpi": "96",  # Graph output resolution
        },
        node_attr={
            "shape": "box",  # Node shape
            "style": "filled,rounded,bold",  # Node style
            "fillcolor": "lightgrey",  # Node interior color
            "color": "black",  # Node border color
            "penwidth": "1.5",  # Border thickness
            "fontname": "Times-Roman",  # Node text font
            "fontsize": "14",  # Node text size
            "fontcolor": "black",  # Node text color
            "margin": "0.33, 0.22",  # Node margin
            "width": "0.75",  # Node min width
            "height": "0.5",  # Node min height
        },
        edge_attr={
            "arrowhead": "normal",  # Edge head arrow
            "arrowtail": "normal",  # Edge tail arrow
            "dir": "forward",  # Edge arrow direction
            "style": "bold",  # Edge style
            "color": "black",  # Edge color
            "penwidth": "3",  # Edge thickness
            "headlabel": "",  # Text near target
            "taillabel": "",  # Text near source
        },
    )


def _render_subgraphs(graph: Digraph, project: Project) -> None:
    MIN_FILL = 100
    MAX_FILL = 220

    def _render_directory(graph, directory: Directory, depth: int = 0) -> None:
        with graph.subgraph(name=f"cluster_{directory.path}") as cluster:
            fill_color = MAX_FILL - int((MAX_FILL - MIN_FILL) * depth / max(max_depth, 1))

            cluster.attr(
                label=directory.path.name,
                style="rounded,filled",
                color="black",
                fillcolor=f"#{fill_color:02x}{fill_color:02x}{fill_color:02x}",
                margin="50",
            )

            for script in directory.scripts:
                cluster.node(
                    name=str(script.path),
                    label=script.path.name,
                )

            for child in directory.directories.values():
                _render_directory(cluster, child, depth + 1)

    tree = project.directory_tree
    if not tree:
        return graph

    max_depth: int = get_directory_depth(tree)

    _render_directory(graph, tree)


def _render_graph_edges(graph: Digraph, project: Project) -> None:
    for script in project.scripts:
        for dependency in script.dependencies:
            graph.edge(tail_name=str(script.path), head_name=str(dependency.target.path), color=EDGE_COLORS[type(dependency.source)])


def _render_graph_legend(graph: Digraph) -> None:
    rows_html: list[str] = []

    for entry, color in EDGE_COLORS.items():
        rows_html.append(
            f"<TR>"
            f'<TD WIDTH="50" HEIGHT="20" FIXEDSIZE="TRUE" '
            f'BORDER="3" COLOR="{color}" SIDES="B" ALIGN="CENTER" VALIGN="MIDDLE">'
            f"</TD>"
            f'<TD ALIGN="LEFT" VALIGN="MIDDLE" CELLPADDING="6">'
            f'<FONT FACE="Times-Roman" POINT-SIZE="18">{entry.name}</FONT>'
            f"</TD>"
            f"</TR>"
        )

    legend_html = f'<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="12" CELLPADDING="4">{"".join(rows_html)}</TABLE>>'

    with graph.subgraph(name="cluster_legend") as legend:
        legend.attr(
            label="Legend",
            style="rounded",
            color="black",
            margin="0",
            pad="0",
        )
        legend.node(
            name="legend_table",
            label=legend_html,
            shape="none",
            fillcolor="none",
        )
