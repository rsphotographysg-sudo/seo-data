# -*- coding: utf-8 -*-
"""Crew schedule, week of 05th to 11th October 2026.
Crew as booked in the RS MS 2026 master schedule; details from the calendar."""

DAYS = [
    ("2026-10-05", "*05th October 2026, Monday*"),
    ("2026-10-06", "*06th October 2026, Tuesday*"),
    ("2026-10-07", "*07th October 2026, Wednesday*"),
    ("2026-10-08", "*08th October 2026, Thursday*"),
    ("2026-10-09", "*09th October 2026, Friday*"),
    ("2026-10-10", "*10th October 2026, Saturday*"),
    ("2026-10-11", "*11th October 2026, Sunday*"),
]

ROSTER = ["Ken", "Alvin", "Gerald", "Bryant", "Wing", "Pierre", "Mifzal", "Evelyn"]

# What a person does on a day with no booking
STANDBY = ["Clear Photo", "TBC", "Standby"]
DEFAULTS = {
    "Ken": STANDBY, "Gerald": STANDBY, "Bryant": STANDBY, "Wing": STANDBY,
    "Alvin": ["TBC", "Standby"],
    "Pierre": ["Clear Photo / Video", "TBC", "Standby"],
    "Mifzal": ["Come in to the Office at 10am", "Clear Video"],
    "Evelyn": ["Clear Video"],
}

LUNCH = ("*Company Lunch*", [
    "Date: 05th October 2026, Monday",
    "Time: 12pm to 2.30pm",
    "Venue: Atrium Restaurant (Level 4), Holiday Inn Singapore Atrium (317 Outram Rd S169075)",
    "*Reservation under Kit Yee.",
])

# --- DAYS Summit, 06 Oct: five crew, one block each in their own role --------
_DAYS_BASE = [
    "Name: Gabriele Samsonovaite, +41 78 253 8160",
    "Event: Digital Asset Yield Summit (DAYS) Singapore",
    "Date: 06th October 2026, Tuesday",
]
_DAYS_TAIL = [
    "Venue: Raffles Hotel Singapore",
    "PG 1: Ken",
    "PG 2: Gerald",
    "Editor: Wing",
    "Roving VG: Mifzal",
    "Static VG: Bryant",
    "Attire: Formal",
    "*Refer to the floor plan",
    "*Static VG: two cameras + clean audio feed + backup recorder",
    "*DAYS highlight (1.5-2 min) + Hyperliquid highlight (1-1.5 min) within 48 hours",
    "*Raw footage delivered synced session by session (no editing)",
]
def _days(report):
    return _DAYS_BASE + [
        f"Session 1: 8am to 5pm (9 Hours) – Report at {report}",
        "Session 2: 5pm to 8pm (3 Hours)",
    ] + _DAYS_TAIL

# --- NLB Donors' Night stock shoot, 06 Oct: Alvin & Pierre -------------------
_STOCK_NLB = [
    "Name: Kamal Hakim, 81129652",
    "POC: Hui Ying, 96924805",
    "Event: Donors’ Appreciation Night",
    "Date: 06th October 2026, Tuesday",
    "Time: 10am to 4pm (6 Hours) – Report at 9.30am",
    "Venue: NL Building, Level 16 (100 Victoria Street S188064)",
    "PG 1: Alvin",
    "PG 2: Pierre",
    "*Take shots of the donated artefacts – one to take the top-down photos, the other the stylised shots.",
    "*Rename the files with the correct artefact name before delivery.",
    "*Indoor",
    "*Full set of final photos to be delivered within 3 working days.",
]

# --- SPICE, 06 Oct: Alvin PG, Pierre VG -------------------------------------
_SPICE = [
    "Name: Bear Kaewsa, +64 22 170 9546",
    "Event: OFF-MENU",
    "Date: 06th October 2026, Tuesday",
    "Time: 7pm to 9pm (2 Hours) – Report at 6.30pm",
    "Venue: La Maison du Whiskey (80 Mohamed Sultan Rd #01-10 S239013)",
    "PG: Alvin",
    "VG: Pierre",
]

# --- DZE Asia, 07 Oct: Gerald PG, Mifzal VG ---------------------------------
_DZE = [
    "Name: Silvia Sambugaro, 94997724",
    "Event: Art Exhibition Opening",
    "Date: 07th October 2026, Wednesday",
    "Time: 5.30pm to 8.30pm (3 Hours) – Report at 5pm",
    "Venue: The Arts House (1 Old Parliament Lane S179429)",
    "PG: Gerald",
    "VG: Mifzal",
    "*Shots of the art pieces, the audience during the opening speeches, the speakers and the artists during the vernissage",
    "*VG: 1 x Event Highlight Video, up to 2 minutes; up to 3 rounds of revision",
]

# --- More & More @ Suntec, 08 Oct: Ken PG cum Static, Bryant VG cum Static --
_MORE_BASE = [
    "Name: Tal Mor, +972 53 827 3287",
    "Event: Agentic Finance Summit & The Odds: Prediction Markets Live",
    "Date: 08th October 2026, Thursday",
]
_MORE_TAIL = [
    "Venue: Suntec Singapore, Nicoll 2 & Nicoll 3",
    "PG cum Static (Main Operator): Ken – 1pm to 7.45pm",
    "VG cum Static (Second Operator): Bryant – 2.30pm to 5.50pm",
    "*2 x Unmanned Static",
    "*Main stage: locked-off cam, continuous 1080p, 3-layer audio (AV feed + backup recorder + on-board), dual cards, mains + battery",
    "*The Odds room: locked-off cam 2.30pm to 5.50pm",
    "*Roving stills + handheld video + soundbite interviews (lapel/handheld mic)",
    "*10 social photos during the event, ~30 same-night selects, 100-150 edited by 9 Oct 6pm",
    "*Organiser provides crew passes + AV-desk line-out in both rooms (AV: Trina, Unearthed Productions)",
]

# --- SAF Chevrons, 08 Oct: Alvin I.Print, Mifzal VG -------------------------
_CHEVRONS = [
    "Name: Winson Khoo, 98353977",
    "Event: Graduation Ceremony Media Coverage 2026",
    "Date: 08th October 2026, Thursday",
]
_CHEVRONS_TAIL = [
    "Venue: The Chevrons, Level 3 Rose Room",
    "I.Print: Alvin",
    "Printing Assistant: TBC",
    "VG: Mifzal",
]

# --- AD Eric, 10 Oct: Ken PG, Bryant VG -------------------------------------
_AD_BASE = [
    "Groom & Bride: Toh Huang En, 92978178 / Samantha Chang, 94669122",
    "Date: 10th October 2026, Saturday",
]
_AD_TAIL = [
    "Venue: Bride’s home (AM), Sembawang & Jurong, Raffles Marina (Lighthouse shoot & dinner)",
    "PG: Ken",
    "VG: Bryant",
    "*SDE",
    "*Refer to the full rundown in the group chat.",
    "*AM: picking up of bride (intimate, traditional); tea ceremony; kua photoshoot (fun, less rigid). Capture the roast pig transfer, morning hair combing (video the auspicious words), tea ceremony prep and auspicious words.",
    "*PM: Lighthouse shoot (dreamy/elegant vs fun casual); reception; 1st march-in (Groom grand, Bride elegant); 2nd march-in (dynamic, fun).",
    "*Photo: VIP table right after cake cutting; stairs shot right before 2nd march-in; full-colour photos preferred.",
    "*Video: both march-ins, cake cutting, games, 2nd march-in pre-video (guest reactions), champagne, yum seng, thank-you speech, lucky draw, table photos.",
]

# --- PAHQ KKSB 2026, 11 Oct (TBC): two pairs of VG --------------------------
_PAHQ_BASE = [
    "Name: Nurul Huda, 80536755",
    "Event: Kasih Keluarga Sihat Bersama (KKSB) 2026",
    "Date: 11th October 2026, Sunday",
]
_PAHQ_TAIL = [
    "*SDE",
    "*1 x Highlight Video up to 3 mins per location, final edit same day (up to 3 revisions)",
    "*All raw footage delivered same day",
]
_PAHQ_L1 = _PAHQ_BASE + [
    "Location 1: 8am to 11am (3 Hours) – Report at 7am to set-up",
    "Venue: Woodlands (M³+ @ Marsiling Yew Tee)",
    "VG 1: Bryant",
    "VG 2: Wing",
] + _PAHQ_TAIL
_PAHQ_L2 = _PAHQ_BASE + [
    "Location 2: 10am to 12pm (2 Hours) – Report at 9am to set-up",
    "Venue: The Anchor @ Marine Parade",
    "VG 1: Mifzal",
    "VG 2: Pierre",
] + _PAHQ_TAIL

JOBS = [
 # --- Monday 05 Oct -------------------------------------------------------
] + [("2026-10-05", "1200", LUNCH[0], LUNCH[1], who)
     for who in ("Ken", "Alvin", "Gerald", "Bryant", "Wing", "Pierre", "Mifzal")] + [
 ("2026-10-05", "1600", "*Stock PG + Event PG*", [
    "Name: Kamal Hakim, 81129652",
    "POC: Sabrina, 98484647",
    "Event: Snoopy Pop-Up Library",
    "Day 1: 05th October 2026, Monday",
    "Stock: 4pm to 6pm (2 Hours) – Report at 3.30pm",
    "Event: 6pm to 7pm (1 Hour)",
    "Venue: Plaza Singapura L3",
    "*Indoors.",
    "*To retrieve all photos after the shoot.",
    "*Full set of final photos to be delivered within 3 working days.",
 ], "Ken"),

 # --- Tuesday 06 Oct ------------------------------------------------------
 ("2026-10-06", "0800", "*Event PG*",       _days("7.30am"),               "Ken"),
 ("2026-10-06", "0800", "*Event PG*",       _days("7.30am"),               "Gerald"),
 ("2026-10-06", "0800", "*On-site Editor*", _days("7.30am"),               "Wing"),
 ("2026-10-06", "0800", "*Event VG (Roving)*", _days("7am to set-up"),     "Mifzal"),
 ("2026-10-06", "0800", "*Static VG*",      _days("7am to set-up"),        "Bryant"),
 ("2026-10-06", "1000", "*Stock PG*", _STOCK_NLB, "Alvin"),
 ("2026-10-06", "1000", "*Stock PG*", _STOCK_NLB, "Pierre"),
 ("2026-10-06", "1900", "*Event PG*", _SPICE, "Alvin"),
 ("2026-10-06", "1900", "*Event VG*", _SPICE, "Pierre"),

 # --- Wednesday 07 Oct ----------------------------------------------------
 ("2026-10-07", "0630", "*Booth PG* (TBC)", [
    "Name: Maria, WhatsApp +7 910 420-31-31",
    "Event: TOKEN2049 Singapore – Exhibition Stand Photography",
    "Date: 07th October 2026, Wednesday",
    "Time: 6.30am to 8.30am (2 Hours) – Report at 6am",
    "Venue: Marina Bay Sands, Sands Expo and Convention Centre",
    "*1 exhibition stand, clean shots before visitors enter (hall opens 8am)",
    "*Stand wide + angles, branding, signage, screen and product details",
    "*~10 selects the same afternoon, 30-40 edited within 48 hours",
    "*Client to arrange the exhibitor/contractor pass for 6.30am hall access",
    "*Stand number and hall TBC",
 ], "Ken"),
 ("2026-10-07", "1000", "*Photo Booth*", [
    "Name: Edwyn Yeo, 97532495",
    "Event: TOE for 4 SAB ORD Milestone Ceremony",
    "Date: 07th October 2026, Wednesday",
    "Time: 10am to 12pm (2 Hours) – Report at 9am to set-up and test print",
    "Venue: Sungei Gedong Camp, 4 SAB (Blk 252)",
    "*18pcs x 4R sized photo frames",
 ], "Alvin"),
 ("2026-10-07", "1515", "*Social Media PG cum VG*", [
    "Name: Leon, 86699600 / Elin, 96757293",
    "Event: Social Media PG cum VG for Taste Ipoh",
    "Date: 07th October 2026, Wednesday",
    "Time: 3.15pm to 5.15pm (2 Hours) – Report at 2.45pm",
    "Venue: Taste Ipoh at Raffles City Shopping Centre (252 N Bridge Rd #B1-81 S179103)",
    "*Pending storyboard.",
    "*Return raw footages to client after the event.",
    "*Photos to be edited.",
    "*Bring tripod.",
 ], "Bryant"),
 ("2026-10-07", "1730", "*Event PG*", _DZE, "Gerald"),
 ("2026-10-07", "1730", "*Event VG*", _DZE, "Mifzal"),
 ("2026-10-07", "0000", "Off", ["*Pierre Request"], "Pierre"),

 # --- Thursday 08 Oct -----------------------------------------------------
 ("2026-10-08", "0000", "Logistic", ["Oversee Operation"], "Alvin"),
 ("2026-10-08", "1000", "*Event PG*", [
    "Name: Wei Guang, 93676797",
    "Event: Singapore Hack Season Conference",
    "Date: 08th October 2026, Thursday",
    "Time: 10am to 6pm (8 Hours) – Report at 9.30am",
    "Venue: Fairmont Hotel Ballroom",
 ], "Gerald"),
 ("2026-10-08", "1300", "*Event PG cum Static VG*", _MORE_BASE + [
    "Time: 1pm to 7.45pm (6 Hours 45 Minutes) – Report at 12.30pm to set-up",
    "*1pm set-up, coverage 2.20pm to 7.40pm, pack-down 8pm – main stage",
 ] + _MORE_TAIL, "Ken"),
 ("2026-10-08", "1430", "*Event VG cum Static VG*", _MORE_BASE + [
    "Time: 2.30pm to 5.50pm (3 Hours 20 Minutes) – Report at 2pm to set-up",
    "*Roving both rooms + networking",
 ] + _MORE_TAIL, "Bryant"),
 ("2026-10-08", "1700", "*Instant Print*", _CHEVRONS + [
    "Time: 5pm to 9pm (4 Hours) – Report at 4pm to set-up and test print",
 ] + _CHEVRONS_TAIL + ["*Bring along tripod"], "Alvin"),
 ("2026-10-08", "1700", "*Event VG*", _CHEVRONS + [
    "Time: 5pm to 9pm (4 Hours) – Report at 4.30pm to set-up",
 ] + _CHEVRONS_TAIL, "Mifzal"),
 ("2026-10-08", "1800", "*Photo Booth* (TBC)", [
    "Name: Owenn, 87799821",
    "Event: Kaffir End of Mono Event",
    "Date: 08th October 2026, Thursday",
    "Time: 6pm to 10pm (4 Hours) – Report at 5pm to set-up and test print",
    "Venue: 11 Slim Barracks Rise #03-03/3A (and #03-01/02) S138664.",
    "*200pax",
 ], "Wing"),
 ("2026-10-08", "2000", "*Event PG + 4R Print*", [
    "Name: Niven Tham, 98595027",
    "Event: House Visit",
    "Date: 08th October 2026, Thursday",
    "Time: 8pm to 9.30pm (1.5 Hours) – Report at 7pm to set-up and test print",
    "Venue: Blk 38B Eunos Road 2",
    "*Canon Selphy Printer",
 ], "Pierre"),

 # --- Friday 09 Oct -------------------------------------------------------
 ("2026-10-09", "0900", "*Event PG*", [
    "Name: Jasvindar, 91181682",
    "POC: Vera, 90184191 / Alvin Sim, 82681234",
    "Event: SST ChangeMakers InnoFest",
    "Date: 09th October 2026, Friday",
    "Time: 9am to 11am (2 Hours) – Report at 8.30am",
    "Venue: SST, Atrium, Block A (beside General Office) (1 Technology Drive S138572)",
    "*Main focus is to capture students in action, presenting to staff and visitors.",
    "*Inform the client of the PG’s details (including vehicle plate) before the event.",
 ], "Gerald"),
 ("2026-10-09", "0930", "*Event PG*", [
    "Name: Kamal Hakim, 81129652",
    "POC: Sabrina, 98484647",
    "Event: Snoopy Pop-Up Library",
    "Day 2: 09th October 2026, Friday",
    "Time: 9.30am to 11.30am (2 Hours) – Report at 9am",
    "Venue: Plaza Singapura L3",
    "*Indoors.",
    "*To retrieve all photos after the shoot.",
    "*Full set of final photos to be delivered within 3 working days.",
 ], "Ken"),
 ("2026-10-09", "1000", "*Deliver A4 Photo*", [
    "POC: Nancy, 96561714",
    "Event: Deliver A4 Photo – SAF Studio Portrait",
    "Date: 09th October 2026, Friday",
    "Venue: SAFTI MI, Blk 60, GKS CSC (500 Upper Jurong Road S638364)",
    "*Call 96561714 or 93850001 on arrival; Nancy or her colleague will collect.",
 ], "Alvin"),

 # --- Saturday 10 Oct -----------------------------------------------------
 ("2026-10-10", "0800", "*AD PG*", _AD_BASE + [
    "PG (AM): 8am to 1pm (5 Hours) – Report at 7.30am",
    "PG (PM): 4pm to 10pm (6 Hours)",
 ] + _AD_TAIL, "Ken"),
 ("2026-10-10", "0800", "*AD VG*", _AD_BASE + [
    "VG (AM): 8am to 12pm (4 Hours) – Report at 7am to set-up",
    "VG (PM): 6pm to 10pm (4 Hours)",
 ] + _AD_TAIL, "Bryant"),
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
 ], "Wing"),

 # --- Sunday 11 Oct -------------------------------------------------------
 ("2026-10-11", "0000", "Appointment", [], "Ken"),
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
 ("2026-10-11", "0800", "*Event VG* (TBC)", _PAHQ_L1, "Bryant"),
 ("2026-10-11", "0800", "*Event VG* (TBC)", _PAHQ_L1, "Wing"),
 ("2026-10-11", "1000", "*Event VG* (TBC)", _PAHQ_L2, "Mifzal"),
 ("2026-10-11", "1000", "*Event VG* (TBC)", _PAHQ_L2, "Pierre"),
]

NOTES = [
 ("*06th October 2026, Tuesday*", []),
 ("(TBC) 2 x VG + PG – The Capital Summit x Asia Stablecoin Conference", [
    "POC: Taehee (The Capital Summit / Cap Rate Labs LLC), WhatsApp +82 10-3005-3638",
    "Time: Breakfast 10am to 11.30am, main event 1pm to 5.30pm",
    "Venue: Conrad Singapore Orchard (same room both parts)",
    "*Full video recording, 16 sessions each as a separate edited video + breakfast highlights; 2 cams; desk audio + own wireless mics",
    "*1 PG full day: speakers, stage, attendees, networking, 300+ edited photos",
    "*Crew not booked – all 7 are on DAYS / NLB that day; needs freelancers if confirmed",
 ]),
 ("*SP Water Turn-on Appointment*", ["Date: 06th October 2026, Tuesday"]),
 ("*EL / CL Oral*", [
    "08th October 2026, Thursday – 4pm (Chinese)",
    "09th October 2026, Friday – 3.25pm (English)",
 ]),
]
