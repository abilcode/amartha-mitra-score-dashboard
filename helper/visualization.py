import pandas as pd
import plotly.graph_objects as go


def visualize_bar_chart(data, x, y):
    fig = go.Figure(
        data=[go.Bar(
            x=data[x],
            y=data[y],
            marker=dict(color=data[x], colorbar=dict(title=x)),
        )],

        layout=dict(
            xaxis=dict(title=x),
            yaxis=dict(title="% bad loan ratio"),
            title=dict(text=f"mitra score vs bad loan ratio")
        )
    )

    return fig