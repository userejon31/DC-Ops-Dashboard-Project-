import plotly.express as px
import plotly.graph_objects as go


# Modern cyberpunk color palette (matches redesigned app)
PALETTE = {
    "primary": "#00d4ff",      # Cyan
    "secondary": "#ff006e",    # Magenta
    "accent": "#ffbe0b",       # Yellow
    "success": "#06d6a0",      # Green
    "dark": "#0a0e27",
    "text": "#e8e9f3",
}


def line_chart(df, x, y, title):
    fig = px.line(df, x=x, y=y, markers=True, title=title)
    fig.update_traces(
        line_color=PALETTE["primary"],
        marker_color=PALETTE["accent"],
        line_width=3
    )
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=PALETTE["text"]),
        title_font=dict(size=18, color=PALETTE["primary"])
    )
    return fig


def grouped_bar(df, x, ys, title):
    fig = go.Figure()
    colors = [PALETTE["primary"], PALETTE["secondary"], PALETTE["success"]]
    for idx, col in enumerate(ys):
        fig.add_bar(
            name=col,
            x=df[x],
            y=df[col],
            marker_color=colors[idx % len(colors)]
        )
    fig.update_layout(
        barmode="group",
        title=title,
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=PALETTE["text"]),
        title_font=dict(size=18, color=PALETTE["primary"])
    )
    return fig


def donut_chart(df, names, values, title):
    colors = [PALETTE["primary"], PALETTE["secondary"], PALETTE["accent"], PALETTE["success"]]
    fig = px.pie(df, names=names, values=values, hole=0.55, title=title)
    fig.update_traces(marker=dict(colors=colors, line=dict(color=PALETTE["dark"], width=2)))
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=PALETTE["text"]),
        title_font=dict(size=18, color=PALETTE["primary"])
    )
    return fig


def scatter_radar(df, x, y, color, title):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        text="Technology",
        size=[22] * len(df),
        title=title,
        color_discrete_sequence=[PALETTE["primary"], PALETTE["secondary"], PALETTE["accent"], PALETTE["success"]]
    )
    fig.update_traces(textposition="top center")
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=PALETTE["text"]),
        title_font=dict(size=18, color=PALETTE["primary"])
    )
    return fig
