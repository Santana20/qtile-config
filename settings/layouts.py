from libqtile import layout
from libqtile.config import Match
from settings.theme import colors


layout_theme = {"border_width": 2,
                "margin": 4,
                "border_focus": colors['urgent'][0],
                "border_normal": "1D2330"
                }

layouts = [
    layout.Max(),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Matrix(columns=2, **layout_theme),
    layout.RatioTile(**layout_theme),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=colors["color4"][0]
)