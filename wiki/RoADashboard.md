# RoA Dashboard (Rise of Atlantis)

Streamlit analytics dashboard for the Rise of Atlantis game server. Connects to a live database built from hourly automated backups of server data.

## Architecture
- **Frontend**: Streamlit (Python), 16 tabs
- **Data source**: Private GitHub repo (`RoaRealmData`) — CSVs parsed from hourly server backups
- **Auth**: JWT-based login, hashed passwords in Streamlit secrets
- **Caching**: Custom `CacheManager` keyed on data signature (date + row count)

## Tabs
Overview, Daily Report, Player Count, Resources, Power, Speedups, Items, Troops, Buildings, Skins, Quests & Research, Protected Resources (ceasefire), Map, Alliance, PDD, Purchases

## Data model (per snapshot)
- Player count, power, resources (gold/lumber/stone/metal/food/ruby)
- Troops JSON, items JSON, buildings data
- Ceasefire / active effects
- Alliance membership
- Player creation dates → cumulative growth curve

## Current status
- Working well after database cleanup (May 2026)
- Next: reinforce tracking — how players are being reinforced by others, troop source in JSON

## Wiki context
- Member of Rise of Atlantis community team since January 2026
- Helping with community management, game balance spreadsheets (costs, ratios), game direction
- Source code: `junk_drawer/github/RoADashboard/`

## Related
- [[github-projects]]
- [[github-code]]
