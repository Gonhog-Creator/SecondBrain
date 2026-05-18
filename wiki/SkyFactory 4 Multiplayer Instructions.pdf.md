# SkyFactory 4 Multiplayer Instructions.pdf

Source: junk_drawer/SkyFactory 4 Multiplayer Instructions.pdf

Category: [[academic-syllabus]]

## Summary
Multiplayer Instructions: SkyFactory 4 has a ton of great features that translate into multiplayer. There are multiple world types available to all servers, a team system, prestige, and much more. The following information has been provided to help out get running quickly! World Types​: SkyFactory 4 features 30+ world types. Each world type has a unique challenge or environment. To set your server to one of these world types, include the following information into your “server.properties” file b

## Full Content
Multiplayer Instructions:
SkyFactory 4 has a ton of great features that translate into multiplayer. There are multiple
world types available to all servers, a team system, prestige, and much more. The following
information has been provided to help out get running quickly!

World Types​:
SkyFactory 4 features 30+ world types. Each world type has a unique challenge or
environment. To set your server to one of these world types, include the following
information into your “server.properties” file before starting up. For world images and
descriptions, refer to the modpack world creation screen in your client.
★ Sky Factory 4 Classic​:
generator-settings={"Topography-Preset":"Sky Factory 4"}
level-type=DEFAULT
★ Skygrid​:
generator-settings={"Topography-Preset":"Skygrid"}
level-type=skygrid
★ Compactsky​:
The CompactSky world type allows players to each have their own Compact Machine. Players spawn
in a hub and choose which machine they would like. There are 3 settings to have a hub with 16, 64,
or 256 slots available. Choose the world size that best suits your server.
●

16 Machines​:

generator-settings={"Topography-Preset":"Compactsky","schema":"test002","givePSD":false,"size":"S
MALL"}
level-type=compactsky
●

64 Machines​:

generator-settings={"Topography-Preset":"Compactsky","schema":"test002","givePSD":false,"size":"M
EDIUM"}
level-type=compactsky
●

256 Machines​:

generator-settings={"Topography-Preset":"Compactsky","schema":"test002","givePSD":false,"size":"L
ARGE"}
level-type=compactsky

★ Amplified​:
generator-settings={"Topography-Preset":"Amplified"}
level-type=amplified
★ Default​:
generator-settings={"Topography-Preset":"Default"}
level-type=DEFAULT
★ LargeBiomes​:
generator-settings={"Topography-Preset":"LargeBiomes"}
level-type=largeBiomes
★ LargeBiomes​:
generator-settings={"Topography-Preset":"Lostcities"}
level-type=lostcities
★ Flat​:
generator-settings={"Topography-Preset":"Flat"}
level-type=flat
★ SkyFactory Tutorial​:
generator-settings={"Topography-Preset":"SkyFactory Tutorial"}
level-type=DEFAULT
★ Peace Out​:
generator-settings={"Topography-Preset":"Peace Out"}
level-type=DEFAULT
★ Project trEe​:
generator-settings={"Topography-Preset":"Project trEe"}
level-type=DEFAULT
★ Stone Factory​:
generator-settings={"Topography-Preset":"Stone Factory"}
level-type=DEFAULT
★ ObservaTree​:
generator-settings={"Topography-Preset":"ObservaTree"}
level-type=DEFAULT
★ Sky Village​:
generator-settings={"Topography-Preset":"Sky Village"}
level-type=DEFAULT
★ Sea World​:
generator-settings={"Topography-Preset":"Sea World"}
level-type=DEFAULT

★ Lava Factory​:
generator-settings={"Topography-Preset":"Lava Factory"}
level-type=DEFAULT
★ Ender the Sea​:
generator-settings={"Topography-Preset":"Ender the Sea"}
level-type=DEFAULT
★ Bedrock Your World​:
generator-settings={"Topography-Preset":"Bedrock Your World"}
level-type=DEFAULT
★ Between Bedrock and a Hard Place​:
generator-settings={"Topography-Preset":"Between Bedrock and a Hard Place"}
level-type=DEFAULT
★ Rock Bottom​:
generator-settings={"Topography-Preset":"Rock Bottom"}
level-type=DEFAULT
★ Minesweeper​:
generator-settings={"Topography-Preset":"Minesweeper"}
level-type=DEFAULT
★ Lights Out!​:
generator-settings={"Topography-Preset":"Lights Out!"}
level-type=DEFAULT
★ Sticky Situation​:
generator-settings={"Topography-Preset":"Sticky Situation"}
level-type=DEFAULT
★ Cobbled Together​:
generator-settings={"Topography-Preset":"Cobbled Together"}
level-type=DEFAULT
★ Sludgehammer​:
generator-settings={"Topography-Preset":"Sludgehammer"}
level-type=DEFAULT
★ Resonant Sleeper​:
generator-settings={"Topography-Preset":"Resonant Sleeper"}
level-type=DEFAULT
★ Chill Out​:
generator-settings={"Topography-Preset":"Chill Out"}
level-type=DEFAULT

★ Hot Topic​:
generator-settings={"Topography-Preset":"Hot Topic"}
level-type=DEFAULT
★ The Floor is Lava​:
generator-settings={"Topography-Preset":"The Floor is Lava"}
level-type=DEFAULT
★ Seven Seas​:
generator-settings={"Topography-Preset":"Seven Seas"}
level-type=DEFAULT
★ Chunk Norris​:
generator-settings={"Topography-Preset":"Chunk Norris"}
level-type=DEFAULT
★ Skiiiilands​:
generator-settings={"Topography-Preset":"Skiiiilands"}
level-type=DEFAULT
★ Material Girl in a Material World​:
generator-settings={"Topography-Preset":"Material Girl in a Material World"}
level-type=DEFAULT
★ Lava Cake​:
generator-settings={"Topography-Preset":"Lava Cake"}
level-type=DEFAULT
★ Hardcore​:
generator-settings={"Topography-Preset":"Hardcore"}
level-type=DEFAULT
★ Are You Afraid of the Dark​:
generator-settings={"Topography-Preset":"Are You Afraid of the Dark"}
level-type=DEFAULT

Island Creation for players​:
On multiplayer servers you may need to create separate islands for players. Use the
following commands (or setup a command block) to get started:

/topography island <player>

Teams (Together Forever)​:
You may want to team up with other players to share your advancement progress. The
Together Forever mod will allow you to invite players with the following commands:
/tf invite <player>

Prestige Settings​:
Prestige is a new system in SkyFactory. This allows you to enable a progression system
where each player can gain prestige points to unlock items and mods. Prestige is per player
and not shared. Servers and Single Player do not share prestige so any progress you make
on Single Player does not transfer to a server. To enable prestige you will have to enable
the setting in the “prestige.cfg” file to “true”. Keep in mind, certain unlocks one player have
may still be accessible by another player and in most situations this is okay.

Prestige on:
# What is the default value for prestige? [default: true]
B:"Prestige Enabled Default"=true
Prestige off:
# What is the default value for prestige? [default: true]
B:"Prestige Enabled Default"=false

If, for any reason, Prestige is enabled but players are unable to open the window to spend
their prestige points (Default “P”) then the following command will force enable for all
players:
/prestige force enabled
To force disable:

/prestige force disabled



## Metadata
- Source file: junk_drawer/SkyFactory 4 Multiplayer Instructions.pdf
- Extracted: 2026-05-18
- Category: academic-syllabus
