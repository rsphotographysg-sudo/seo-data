# -*- coding: utf-8 -*-
"""Week of 05th to 11th October 2026 — jobs from the calendar, crew picked on
specialisation and location.

Specialisation, counted off the 2026 master schedule:
  Siang   corporate / interior / stock, instant print   (28 corporate, 7 interior)
  Alvin   photo booth and logistics                     (44 booth, 62 logistic)
  Gerald  event PG, government and grassroots           (121 event PG)
  Bryant  event PG, stock PG, static VG, live streaming (12 stock, 3 live stream)
  Wing    event PG, instant print, editor               (17 4R print, 8 editor)
  Pierre  event PG cum VG, MC                           (28 VG, 8 MC)
  Mifzal  videographer                                  (Event VG, 30 clear video)
"""
SHEET = "October 2026"

# (date label as in row 6, lead crew, start time HHMM, lines down the column)
PLAN = [
 # --- Monday 05 Oct -------------------------------------------------------
 ("5th October 2026", "Siang",  1000, ["Company Lunch"]),
 ("5th October 2026", "Alvin",  1000, ["Company Lunch"]),
 ("5th October 2026", "Gerald", 1000, ["Company Lunch"]),
 ("5th October 2026", "Wing",   1000, ["Company Lunch"]),
 ("5th October 2026", "Pierre", 1000, ["Company Lunch"]),
 ("5th October 2026", "Mifzal", 1000, ["Company Lunch"]),
 ("5th October 2026", "Bryant", 1000, ["Company Lunch"]),
 ("5th October 2026", "Bryant", 1600, ["Stock PG + Event PG", "NLB", "Stock: 4pm to 6pm",
                                       "Event: 6pm to 7pm", "Plaza Singapura L3"]),

 # --- Tuesday 06 Oct ------------------------------------------------------
 ("6th October 2026", "Gerald", 1000, ["2 x Event PG + 2 x VG", "DAYS", "S1: 8am to 5pm",
                                       "S2: 5pm to 8pm", "Raffles Hotel",
                                       "PG (Roving): Gerald", "PG (Static): Bryant",
                                       "VG (Roving): Pierre", "Static VG: Mifzal",
                                       "Editor: Wing"]),
 ("6th October 2026", "Siang",  1000, ["2 x Stock PG", "NLB", "10am to 4pm",
                                       "NL Building L16", "Stock PG 1: Siang",
                                       "Stock PG 2: Alvin"]),
 ("6th October 2026", "Siang",  1900, ["(TBC) Event PG + VG", "SPICE", "7pm to 9pm",
                                       "La Maison du Whiskey", "PG cum VG: Siang"]),

 # --- Wednesday 07 Oct ----------------------------------------------------
 ("7th October 2026", "Siang",  1000, ["(TBC) Booth PG", "TOKEN2049", "6.30am to 8.30am",
                                       "MBS Sands Expo", "*Stand no. TBC"]),
 ("7th October 2026", "Alvin",  1000, ["Photo Booth", "SAF", "10am to 12pm",
                                       "Sungei Gedong Camp", "*18pcs 4R frames"]),
 ("7th October 2026", "Pierre", 1730, ["(TBC) Event PG + VG", "DZE Asia", "5.30pm to 8.30pm",
                                       "The Arts House", "Event PG: Pierre",
                                       "Event VG: Mifzal"]),

 # --- Thursday 08 Oct -----------------------------------------------------
 ("8th October 2026", "Gerald", 1000, ["Event PG", "Wei Guang", "8am to 6pm",
                                       "Fairmont Hotel Ballroom"]),
 ("8th October 2026", "Mifzal", 1300, ["Static VG + VG cum PG", "More & More",
                                       "Set-up 1pm", "2.20pm to 7.30pm",
                                       "Suntec Nicoll 3 & 2", "Main: Mifzal",
                                       "2nd (2.30pm to 5.50pm): Pierre"]),
 ("8th October 2026", "Wing",   1700, ["Event PG cum I.Print + VG", "SAF", "5pm to 9pm",
                                       "The Chevrons L3", "I.Print: Wing", "VG: Bryant"]),
 ("8th October 2026", "Alvin",  1800, ["(TBC) Photo Booth", "SAF", "6pm to 10pm",
                                       "11 Slim Barracks Rise", "*200pax"]),

 # --- Friday 09 Oct -------------------------------------------------------
 ("9th October 2026", "Alvin",  1000, ["Deliver A4 Photo", "SAF", "SAFTI MI Blk 60",
                                       "*Call 96561714 on arrival"]),
 ("9th October 2026", "Bryant", 1000, ["Event PG", "NLB", "9.30am to 11.30am",
                                       "Plaza Singapura L3"]),

 # --- Saturday 10 Oct -----------------------------------------------------
 ("10th October 2026", "Wing",  1000, ["AD PG + VG", "Eric", "8 Hours - time TBC",
                                       "Raffles Marina", "AD PG: Wing", "AD VG: Bryant",
                                       "*Need SDE"]),
 ("10th October 2026", "Pierre", 1200, ["(TBC) Event PG + VG", "eToro", "12pm to 3pm",
                                        "WAKUDA, MBS", "Event PG: Pierre",
                                        "Event VG: Mifzal"]),
 ("10th October 2026", "Gerald", 1830, ["Event PG", "Yishun Orchid RN", "6.30pm to 9pm",
                                        "Blk 349 Yishun Ave 11"]),
 ("10th October 2026", "Alvin",  1830, ["Photo Booth", "Jennie (Dinx Boss)",
                                        "6.30pm to 9.30pm", "Rasa Sentosa L5"]),

 # --- Sunday 11 Oct -------------------------------------------------------
 ("11th October 2026", "Siang",  1000, ["Siang Appointment"]),
 ("11th October 2026", "Gerald", 1000, ["Event PG", "King George’s Ave RN",
                                        "8.15am to 10am", "Jalan Besar CC"]),
 ("11th October 2026", "Gerald", 1430, ["Event PG", "Lavender RN", "2.30pm to 5.30pm",
                                        "Sturdee Residences Pool"]),
 ("11th October 2026", "Pierre", 1200, ["(TBC) Event PG + VG", "eToro", "12pm to 3pm",
                                        "WAKUDA, MBS", "Event PG: Pierre",
                                        "Event VG: Mifzal"]),
]
