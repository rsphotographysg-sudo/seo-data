# -*- coding: utf-8 -*-
"""Crew schedule, week of 05th to 11th October 2026.
Crew follows the RS MS 2026 master schedule for this week (see week_2026-10-05.py)."""

DAYS = [
    ("2026-10-05", "*05th October 2026, Monday*"),
    ("2026-10-06", "*06th October 2026, Tuesday*"),
    ("2026-10-07", "*07th October 2026, Wednesday*"),
    ("2026-10-08", "*08th October 2026, Thursday*"),
    ("2026-10-09", "*09th October 2026, Friday*"),
    ("2026-10-10", "*10th October 2026, Saturday*"),
    ("2026-10-11", "*11th October 2026, Sunday*"),
]

ROSTER = ["Siang", "Alvin", "Gerald", "Bryant", "Wing", "Pierre", "Mifzal", "Evelyn"]

DAYS_NLB = [
    "Name: Kamal Hakim, 81129652",
    "POC: Sabrina, 98484647",
    "Event: Snoopy Pop-Up Library",
]

_DAYS_SUMMIT = [
    "Name: Gabriele Samsonovaite",
    "Event: DAYS Singapore",
    "Date: 06th October 2026, Tuesday",
    "Session 1: 8am to 5pm (9 Hours) – Report at 7.30am",
    "Session 2: 5pm to 8pm (3 Hours)",
    "Venue: Raffles Hotel Singapore",
    "Event PG: Gerald (Roving) & Bryant (Static)",
    "Event VG: Pierre (Roving) & Mifzal (Static)",
    "On-site Editor: Wing",
    "*Refer to the floor plan",
    "*Static VG: two cameras + clean audio feed + backup recorder",
    "*DAYS highlight (1.5-2 min) + Hyperliquid highlight (1-1.5 min) within 48 hours",
    "*Raw footage delivered synced session by session (no editing)",
]

_STOCK_NLB = DAYS_NLB[:1] + [
    "POC: Hui Ying, 96924805",
    "Event: Donors’ Appreciation Night",
    "Date: 06th October 2026, Tuesday",
    "Time: 10am to 4pm (6 Hours) – Report at 9.30am",
    "Venue: NL Building, Level 16 (100 Victoria Street S188064)",
    "Stock PG: Siang & Alvin",
    "*One to take the top-down photos, the other the stylised shots.",
    "*Rename the files with the correct artefact name before delivery.",
    "*Indoor",
    "*Full set of final photos to be delivered within 3 working days.",
]

_DZE = [
    "Name: Silvia Sambugaro, 94997724",
    "Event: Art Exhibition Opening",
    "Date: 07th October 2026, Wednesday",
    "Time: 5.30pm to 8.30pm (3 Hours) – Report at 5pm",
    "Venue: The Arts House (1 Old Parliament Lane S179429)",
    "Event PG: Pierre",
    "Event VG: Mifzal",
    "*Coverage of the art pieces, opening speeches, speakers, audience and artists",
    "*1 x Event Highlight Video, up to 2 minutes",
    "*Up to 2 rounds of revision; subsequent revisions chargeable",
]

_MORE = [
    "Name: Tal Mor (More & More)",
    "Event: Agentic Finance Summit & The Odds: Prediction Markets Live",
    "Date: 08th October 2026, Thursday",
    "Main operator (VG cum PG): set-up 1pm, coverage 2.20pm to 7.30pm, pack-down 7.45pm – Report at 12.30pm",
    "Second operator (VG cum PG): 2.30pm to 5.50pm – Report at 2pm",
    "Venue: Suntec Singapore, Nicoll 3 (Agentic Finance) & Nicoll 2 (The Odds)",
    "Main operator: Mifzal",
    "Second operator: Pierre",
    "*Nicoll 3 locked-off cam, continuous 1080p, 3-layer audio, dual cards, mains + battery",
    "*Roving stills + handheld video + soundbite interviews (lapel/handheld mic)",
    "*10 social photos during the event, ~30 same-night selects, 100-150 edited by 9 Oct 6pm",
    "*Organiser provides crew passes + AV-desk line-out in both rooms",
]

_CHEVRONS = [
    "Name: Winson Khoo, 98353977",
    "Event: Graduation Ceremony Media Coverage 2026",
    "Date: 08th October 2026, Thursday",
    "Event PG cum Instant Print: 5pm to 9pm (4 Hours) – Report at 4pm to set-up and test print",
    "Videography: 5pm to 9pm (4 Hours) – Report at 4.30pm",
    "Venue: The Chevrons, Level 3 Rose Room",
    "Event PG cum I.Print: Wing",
    "Event VG: Bryant",
]

_AD_ERIC = [
    "Groom: Toh Huang En / Bride: Samantha",
    "Event: Actual Day – Eric",
    "Date: 10th October 2026, Saturday",
    "1st 4 Hours: am – venue TBC",
    "2nd 4 Hours: Raffles Marina – time TBC",
    "AD PG: Wing",
    "AD VG: Bryant",
    "*8 hours photography + 8 hours videography",
    "*Need SDE",
]

def _etoro(day, date_label):
    return [
        "Name: Liran, 91619124",
        "Event: eToro Client Event",
        f"Day {day}: {date_label}",
        "Time: 12pm to 3pm (3 Hours) – Report at 11.30am",
        "Venue: WAKUDA, Marina Bay Sands",
        "Event PG: Pierre",
        "Event VG: Mifzal",
        "*Photography + 1 x social media video reel (45-60 seconds)",
    ]

JOBS = [
 # --- Monday 05 Oct -------------------------------------------------------
] + [("2026-10-05", "0000", "*Company Lunch*", [], who)
     for who in ("Siang", "Alvin", "Gerald", "Bryant", "Wing", "Pierre", "Mifzal")] + [
 ("2026-10-05", "1600", "*Stock PG + Event PG*", DAYS_NLB + [
    "Day 1: 05th October 2026, Monday",
    "Stock: 4pm to 6pm (2 Hours) – Report at 3.30pm",
    "Event: 6pm to 7pm (1 Hour)",
    "Venue: Plaza Singapura L3",
    "*Indoors.",
    "*To retrieve all photos after the shoot.",
    "*Full set of final photos to be delivered within 3 working days.",
 ], "Bryant"),

 # --- Tuesday 06 Oct ------------------------------------------------------
 ("2026-10-06", "0800", "*2 x Event PG + 2 x VG + Editor*", _DAYS_SUMMIT, "Gerald"),
 ("2026-10-06", "0800", "*2 x Event PG + 2 x VG + Editor*", _DAYS_SUMMIT, "Bryant"),
 ("2026-10-06", "0800", "*2 x Event PG + 2 x VG + Editor*", _DAYS_SUMMIT, "Pierre"),
 ("2026-10-06", "0800", "*2 x Event PG + 2 x VG + Editor*", _DAYS_SUMMIT, "Mifzal"),
 ("2026-10-06", "0800", "*2 x Event PG + 2 x VG + Editor*", _DAYS_SUMMIT, "Wing"),
 ("2026-10-06", "1000", "*2 x Stock PG*", _STOCK_NLB, "Siang"),
 ("2026-10-06", "1000", "*2 x Stock PG*", _STOCK_NLB, "Alvin"),
 ("2026-10-06", "1900", "*Event PG + VG* (TBC)", [
    "Name: Bear Kaewsa, +64 221709546",
    "Event: OFF-MENU",
    "Date: 06th October 2026, Tuesday",
    "Time: 7pm to 9pm (2 Hours) – Report at 6.30pm",
    "Venue: La Maison du Whiskey (80 Mohamed Sultan Rd #01-10 S239013)",
    "PG cum VG: Siang",
 ], "Siang"),

 # --- Wednesday 07 Oct ----------------------------------------------------
 ("2026-10-07", "0630", "*Booth PG* (TBC)", [
    "Name: Maria, +7 910 420-31-31",
    "Event: TOKEN2049 Singapore – exhibition stand photography",
    "Date: 07th October 2026, Wednesday",
    "Time: 6.30am to 8.30am (2 Hours) – Report at 6am",
    "Venue: Marina Bay Sands, Sands Expo and Convention Centre",
    "*1 exhibition stand, clean shots before visitors enter (hall opens 8am)",
    "*Stand wide + angles, branding, signage, screen and product details",
    "*~10 selects the same afternoon, 30-40 edited within 48 hours",
    "*Client to arrange the exhibitor pass for 6.30am hall access",
    "*Stand number and hall TBC",
 ], "Siang"),
 ("2026-10-07", "1000", "*Photo Booth*", [
    "Name: Edwyn Yeo, 97532495",
    "Event: TOE for 4 SAB ORD Milestone Ceremony",
    "Date: 07th October 2026, Wednesday",
    "Time: 10am to 12pm (2 Hours) – Report at 9am to set-up and test print",
    "Venue: Sungei Gedong Camp, 4 SAB (Blk 252)",
    "*18pcs x 4R sized photo frames",
 ], "Alvin"),
 ("2026-10-07", "1730", "*Event PG + VG* (TBC)", _DZE, "Pierre"),
 ("2026-10-07", "1730", "*Event PG + VG* (TBC)", _DZE, "Mifzal"),

 # --- Thursday 08 Oct -----------------------------------------------------
 ("2026-10-08", "0800", "*Event PG*", [
    "Name: Wei Guang, 93676797",
    "Event: Singapore Hack Season Conference",
    "Date: 08th October 2026, Thursday",
    "Time: 8am to 6pm (10 Hours) – Report at 7.30am",
    "Venue: Fairmont Hotel Ballroom",
 ], "Gerald"),
 ("2026-10-08", "1300", "*Static VG + Event VG cum PG*", _MORE, "Mifzal"),
 ("2026-10-08", "1430", "*Static VG + Event VG cum PG*", _MORE, "Pierre"),
 ("2026-10-08", "1700", "*Event PG cum Instant Print + VG*", _CHEVRONS, "Wing"),
 ("2026-10-08", "1700", "*Event PG cum Instant Print + VG*", _CHEVRONS, "Bryant"),
 ("2026-10-08", "1800", "*Photo Booth* (TBC)", [
    "Name: Owenn, 87799821",
    "Event: KAFFIR END OF MONO EVENT",
    "Date: 08th October 2026, Thursday",
    "Time: 6pm to 10pm (4 Hours) – Report at 5pm to set-up and test print",
    "Venue: 11 Slim Barracks Rise #03-03/3A (and #03-01/02) Singapore 138664",
    "*200pax",
 ], "Alvin"),

 # --- Friday 09 Oct -------------------------------------------------------
 ("2026-10-09", "0900", "*Deliver A4 Photo*", [
    "POC: Nancy, 96561714",
    "Event: Deliver A4 Photo – SAF Studio Portrait",
    "Date: 09th October 2026, Friday",
    "Venue: SAFTI MI, Blk 60, GKS CSC (500 Upper Jurong Road S638364)",
    "*Call 96561714 or 93850001 on arrival; Nancy or her colleague will collect.",
 ], "Alvin"),
 ("2026-10-09", "0930", "*Event PG*", DAYS_NLB + [
    "Day 2: 09th October 2026, Friday",
    "Time: 9.30am to 11.30am (2 Hours) – Report at 9am",
    "Venue: Plaza Singapura L3",
    "*Indoors.",
    "*To retrieve all photos after the shoot.",
 ], "Bryant"),

 # --- Saturday 10 Oct -----------------------------------------------------
 ("2026-10-10", "0800", "*AD PG + VG*", _AD_ERIC, "Wing"),
 ("2026-10-10", "0800", "*AD PG + VG*", _AD_ERIC, "Bryant"),
 ("2026-10-10", "1200", "*Event PG + VG* (TBC)", _etoro(1, "10th October 2026, Saturday"), "Pierre"),
 ("2026-10-10", "1200", "*Event PG + VG* (TBC)", _etoro(1, "10th October 2026, Saturday"), "Mifzal"),
 ("2026-10-10", "1830", "*Event PG*", [
    "Name: Chermaine Goh, 92250053",
    "Event: Yishun Orchid RN Halloween Party",
    "Date: 10th October 2026, Saturday",
    "Time: 6.30pm to 9pm (2.5 Hours) – Report at 6pm",
    "Venue: Blk 349 Yishun Ave 11 Void Deck",
 ], "Gerald"),
 ("2026-10-10", "1830", "*Photo Booth*", [
    "Name: Jennie, 90606002",
    "Event: 40th Anniversary Sua Annual Dinner 2026",
    "Date: 10th October 2026, Saturday",
    "Time: 6.30pm to 9.30pm (3 Hours) – Report at 5.30pm to set-up and test print",
    "Venue: Horizon Pavilion, Level 5, Rasa Sentosa",
 ], "Alvin"),

 # --- Sunday 11 Oct -------------------------------------------------------
 ("2026-10-11", "0000", "Appointment", [], "Siang"),
 ("2026-10-11", "0815", "*Event PG*", [
    "Name: Ms Indhu, 93286269 / Micheal, 80138360",
    "Event: Breakfast with Love",
    "Date: 11th October 2026, Sunday",
    "Time: 8.15am to 10am (1 Hour 45 Minutes) – Report at 7.45am",
    "Venue: Jalan Besar CC Level 1",
 ], "Gerald"),
 ("2026-10-11", "1430", "*Event PG*", [
    "POC: Lawrence Yeo, 81960996",
    "Event: Water Carnival @ Sturdee Residences",
    "Date: 11th October 2026, Sunday",
    "Time: 2.30pm to 5.30pm (3 Hours) – Report at 2pm",
    "Venue: Sturdee Residences Pool (10 Beatty Road S209955)",
 ], "Gerald"),
 ("2026-10-11", "1200", "*Event PG + VG* (TBC)", _etoro(2, "11th October 2026, Sunday"), "Pierre"),
 ("2026-10-11", "1200", "*Event PG + VG* (TBC)", _etoro(2, "11th October 2026, Sunday"), "Mifzal"),
]

NOTES = []
