# Qtile workspaces

from libqtile.config import Key, Group
from libqtile.command import lazy
from settings.keys import mod, keys


group_names=[   "WWW",
                "DEV",
                "SYS",
                "DOC",
                "MUS"
            ]

groups = [Group(name) for name in group_names]

for i, group in enumerate(groups, 1):
    actual_key = str(i)
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], actual_key, lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
        #    desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
         Key([mod, "shift"], actual_key, lazy.window.togroup(group.name),
             desc="move focused window to group {}".format(group.name)),
    ])