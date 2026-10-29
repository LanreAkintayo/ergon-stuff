"""
The Ultimate Norsk Hydro Core Log Practice Pack Generator (All 23 Files)
Includes:
- 10 Baseline Files (varied DPIs 100-300, Portrait, Landscape, 90° Sideways)
- 4 Inconsistent Height Files (Tall 16-cores, Shifted Down, Header Bloat, Short Sheet)
- 2 Landscape Centered Files (Floating in center of wide screen)
- 2 Multi-Page Files (Target on Page 2 or Page 3)
- 5 Elite Curveball Files (Split-column, Handwritten corrections, Microfiche negative, Borderless, 180° upside-down)
- Complete Ground Truth CSVs for Cores and Metadata.
"""

import os
import csv
import random
from PIL import Image, ImageDraw, ImageFont, ImageOps

OUT_DIR = "norsk_hydro_practice_pack"
os.makedirs(OUT_DIR, exist_ok=True)

# 23 Complete Well Datasets
WELL_DATASETS = [
    # --- 10 BASELINE FILES (01 - 10) ---
    {
        "filename": "norsk_hydro_01_portrait_150dpi.pdf",
        "orientation": "portrait", "dpi": 150,
        "well_name": "6406/3-2", "date": "", "scale": "1 : 200",
        "group_formation": "FANGST/BÅT-GP.", "age": "Tidlig -midt Jura",
        "country": "Norway", "licence": "PL091", "field": "",
        "owners": "Statoil, Mobil, Saga", "coordinates_geo": "N 64° 51' 46.78\"\nE 06° 49' 51.87\"",
        "elevation_kb": "", "water_depth": "300m", "td_driller": "4523m", "td_logger": "4527.5m",
        "formation_at_td": "Åre fm.", "loggers_depth_diff": "Cores 1-8: 5m, Cores 9-11: 5.5m",
        "geologists": "J.Gj., J.F.B., T.D.", "comments": "", "stamp": "", "skew": 0.2,
        "cores": [
            ("1", "3930 - 3934", "73.5"), ("2", "3935 - 3952", "100"), ("3", "3952 - 3964.2", "94"),
            ("4", "3965 - 3981.5", "91.7"), ("5", "3983 - 4001.3", "100"), ("6", "4001 - 4027", "98 (+2)"),
            ("7", "4027.5 - 4048", "100"), ("8", "4048 - 4056.5", "100"), ("9", "4067 - 4094", "100"),
            ("10", "4094 - 4119.8", "95.6"), ("11", "4121 - 4148.2", "100")
        ]
    },
    {
        "filename": "norsk_hydro_02_portrait_200dpi.pdf",
        "orientation": "portrait", "dpi": 200,
        "well_name": "6406/3-3", "date": "April 1989", "scale": "1 : 200",
        "group_formation": "", "age": "",
        "country": "Norge", "licence": "PL094/091", "field": "",
        "owners": "Statoil/Agip/Arco/Tenneco/Norsk Hydro/Saga", "coordinates_geo": "N 64° 59' 49.18\"\nE 06° 53' 26.64\"",
        "elevation_kb": "29m", "water_depth": "302", "td_driller": "", "td_logger": "4416m",
        "formation_at_td": "Åre fm.", "loggers_depth_diff": "",
        "geologists": "J.G, J.F.B", "comments": "", "stamp": "", "skew": -0.3,
        "cores": [("1", "3938.00 - 3952.45", ""), ("2", "3956.00 - 3972.24", "")]
    },
    {
        "filename": "norsk_hydro_03_landscape_150dpi.pdf",
        "orientation": "landscape", "dpi": 150,
        "well_name": "6407/1-3", "date": "30/9-87, revised 06-89", "scale": "1 : 200",
        "group_formation": "", "age": "",
        "country": "Norway", "licence": "073", "field": "Tyrihans",
        "owners": "Statoil, Amoco, Conoco, Norsk Hydro", "coordinates_geo": "N 64° 52' 25.48\"\nE 07° 02' 53.47\"",
        "elevation_kb": "29", "water_depth": "286", "td_driller": "4469", "td_logger": "4469",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "C1: -1.7m, C2: -1.7m, C3: -1.25, C4: -1.3m, C5: 1.0m, C6: 1m, C7: -0.5m",
        "geologists": "J.Gj., T.D.", "comments": "", "stamp": "Poor Quality Original", "skew": 0.5,
        "cores": [
            ("1", "3619 - 3619.70", ""), ("2", "3624 - 3638.12", ""), ("3", "3639 - 3656.75", ""),
            ("4", "3657 - 3684", ""), ("5", "3684 - 3719.40", ""), ("6", "3711 - 3716.20", ""),
            ("7", "3748 - 3758", "")
        ]
    },
    {
        "filename": "norsk_hydro_04_portrait_100dpi.pdf",
        "orientation": "portrait", "dpi": 100,
        "well_name": "6506/12-4", "date": "1986, revidert 06.89", "scale": "1 : 200",
        "group_formation": "Lysing Fm., Garn Fm.", "age": "Kritt, Jura",
        "country": "Norge", "licence": "PL094", "field": "Smørbukk",
        "owners": "Statoil, Mobil, Agip, Arco, Tenneco, Norsk Hydro", "coordinates_geo": "N 65° 12' 46.97\"\nE 06° 43' 30.37\"",
        "elevation_kb": "25m", "water_depth": "257m", "td_driller": "", "td_logger": "4457m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "Core 1: 0m",
        "geologists": "J.F. Bockelie, J. Gjelberg", "comments": "", "stamp": "", "skew": -0.8,
        "cores": [("1", "3129 - 3150.9", "100%"), ("2", "3972 - 3980", ""), ("3", "3980 - 4008.5", "")]
    },
    {
        "filename": "norsk_hydro_05_landscape_sideways_200dpi.pdf",
        "orientation": "landscape_sideways", "dpi": 200,
        "well_name": "6407/2-2", "date": "April 1989", "scale": "1 : 200",
        "group_formation": "Fangst Gp., Båt Gp.", "age": "Tidlig - midtre Jura",
        "country": "Norge", "licence": "PL074", "field": "",
        "owners": "Saga, Statoil, Mobil, Agip, Arco, Deminex", "coordinates_geo": "N 64° 58' 01.09\"\nE 07° 58' 49.54\"",
        "elevation_kb": "29m", "water_depth": "260m", "td_driller": "", "td_logger": "4268m",
        "formation_at_td": "Åre Fm. / Trias", "loggers_depth_diff": "Cores 1-8: 0.5m, Core 9: 2m",
        "geologists": "J.Gjelberg, J.F.Bockelie", "comments": "", "stamp": "", "skew": 0.0,
        "cores": [
            ("1", "2418 - 2436.5", ""), ("2", "2444.4 - 2473.0", ""), ("3", "2476.3 - 2502.5", ""),
            ("4", "2502.5 - 2511", ""), ("5", "2511 - 2538.7", ""), ("6", "2538.6 - 2555.0", ""),
            ("7", "2557 - 2559", ""), ("8", "2559 - 2577.70", ""), ("9", "2741 - 2769", "")
        ]
    },
    {
        "filename": "norsk_hydro_06_portrait_300dpi.pdf",
        "orientation": "portrait", "dpi": 300,
        "well_name": "6407/9-1", "date": "15/11-1984, rev. 05-89", "scale": "1 : 200",
        "group_formation": "Garn Fm., Not Fm., Ile Fm.", "age": "Mellom Jura",
        "country": "Norway", "licence": "PL093", "field": "Draugen",
        "owners": "A/S Norske Shell, Statoil, Agip", "coordinates_geo": "N 64° 17' 38.12\"\nE 07° 44' 12.35\"",
        "elevation_kb": "25m", "water_depth": "251m", "td_driller": "1720m", "td_logger": "1719m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "C1-C5: 0.8m",
        "geologists": "K.O. Heum, J.F.B.", "comments": "Rannoch / Etive equivalent sands", "stamp": "", "skew": 0.4,
        "cores": [
            ("1", "1605.0 - 1622.5", "98.5"), ("2", "1622.5 - 1640.0", "100"),
            ("3", "1640.0 - 1658.2", "96.2"), ("4", "1658.2 - 1675.0", "92.0"), ("5", "1675.0 - 1690.4", "99.0")
        ]
    },
    {
        "filename": "norsk_hydro_07_landscape_120dpi.pdf",
        "orientation": "landscape", "dpi": 120,
        "well_name": "6507/7-1", "date": "August 1985, rev. 1989", "scale": "1 : 200",
        "group_formation": "Garn / Tilje Fm.", "age": "Tidlig - Mellom Jura",
        "country": "Norway", "licence": "PL095", "field": "Heidrun",
        "owners": "Conoco, Statoil, Tenneco", "coordinates_geo": "N 65° 19' 24.18\"\nE 07° 18' 33.10\"",
        "elevation_kb": "28m", "water_depth": "345m", "td_driller": "2600m", "td_logger": "2598m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "Core 1-6: 1.2m",
        "geologists": "T.D., J.Gj.", "comments": "", "stamp": "", "skew": -0.5,
        "cores": [
            ("1", "2450.0 - 2468.2", "100"), ("2", "2468.2 - 2486.0", "95.5"),
            ("3", "2486.0 - 2504.5", "91.0"), ("4", "2504.5 - 2522.0", "100"),
            ("5", "2522.0 - 2539.8", "88.5"), ("6", "2539.8 - 2555.0", "94.0")
        ]
    },
    {
        "filename": "norsk_hydro_08_portrait_150dpi.pdf",
        "orientation": "portrait", "dpi": 150,
        "well_name": "6406/2-1", "date": "1988, rev. 06-89", "scale": "1 : 200",
        "group_formation": "Tomma / Halten Gp.", "age": "Jura",
        "country": "Norway", "licence": "PL094", "field": "Kristin",
        "owners": "Saga Petroleum, Statoil, Total", "coordinates_geo": "N 64° 55' 12.05\"\nE 06° 31' 44.20\"",
        "elevation_kb": "30m", "water_depth": "360m", "td_driller": "4800m", "td_logger": "4812m",
        "formation_at_td": "Trias Fm.", "loggers_depth_diff": "Cores 1-8: 0m",
        "geologists": "J.F.B., H.M.", "comments": "High pressure / high temperature reservoir", "stamp": "", "skew": 1.5,
        "cores": [
            ("1", "4510.0 - 4522.5", "85.0"), ("2", "4522.5 - 4538.0", "92.0"),
            ("3", "4538.0 - 4554.2", "100"), ("4", "4554.2 - 4571.0", "97.5"),
            ("5", "4571.0 - 4589.5", "100"), ("6", "4589.5 - 4608.0", "99.0"),
            ("7", "4608.0 - 4625.5", "94.0"), ("8", "4625.5 - 4642.0", "100")
        ]
    },
    {
        "filename": "norsk_hydro_09_landscape_sideways_150dpi.pdf",
        "orientation": "landscape_sideways", "dpi": 150,
        "well_name": "6506/11-1", "date": "10/05-1987", "scale": "1 : 200",
        "group_formation": "Garn Fm.", "age": "Mellom Jura",
        "country": "Norway", "licence": "PL134", "field": "",
        "owners": "Statoil, Norsk Hydro, Total", "coordinates_geo": "N 65° 08' 22.80\"\nE 06° 24' 15.10\"",
        "elevation_kb": "26m", "water_depth": "290m", "td_driller": "4150m", "td_logger": "4152m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "C1-4: 0.5m",
        "geologists": "J.Gj.", "comments": "", "stamp": "Poor Quality Original", "skew": -0.6,
        "cores": [
            ("1", "3800.0 - 3818.5", "100"), ("2", "3818.5 - 3836.0", "96.0"),
            ("3", "3836.0 - 3854.2", "89.5"), ("4", "3854.2 - 3870.0", "100")
        ]
    },
    {
        "filename": "norsk_hydro_10_portrait_200dpi.pdf",
        "orientation": "portrait", "dpi": 200,
        "well_name": "6407/6-1", "date": "12/10-1988, rev. 1989", "scale": "1 : 200",
        "group_formation": "Båt Gp., Fangst Gp.", "age": "Jura",
        "country": "Norway", "licence": "PL092", "field": "Mikkel",
        "owners": "Mobil, Statoil, Agip", "coordinates_geo": "N 64° 39' 18.50\"\nE 07° 05' 42.12\"",
        "elevation_kb": "29m", "water_depth": "230m", "td_driller": "3200m", "td_logger": "3196m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "C1-C10: 1.0m",
        "geologists": "T.D., J.F.B.", "comments": "Gas condensate reservoir", "stamp": "", "skew": 0.3,
        "cores": [
            ("1", "2750.0 - 2765.0", "100"), ("2", "2765.0 - 2780.5", "98.0"),
            ("3", "2780.5 - 2795.0", "100"), ("4", "2795.0 - 2812.0", "95.0"),
            ("5", "2812.0 - 2828.5", "100"), ("6", "2828.5 - 2845.0", "92.5"),
            ("7", "2845.0 - 2860.0", "100"), ("8", "2860.0 - 2876.5", "100"),
            ("9", "2876.5 - 2892.0", "97.0"), ("10", "2892.0 - 2908.0", "100")
        ]
    },

    # --- 4 INCONSISTENT HEIGHT FILES (11 - 14) ---
    {
        "filename": "norsk_hydro_11_tall_16_cores_150dpi.pdf",
        "orientation": "portrait", "dpi": 150,
        "well_name": "6507/8-1", "date": "14/06-1986, rev. 1989", "scale": "1 : 200",
        "group_formation": "Fangst Gp., Garn Fm., Ile Fm.", "age": "Mellom Jura",
        "country": "Norway", "licence": "PL124", "field": "Heidrun Sør",
        "owners": "Statoil, Conoco, Tenneco, Norsk Hydro", "coordinates_geo": "N 65° 14' 18.22\"\nE 07° 26' 45.10\"",
        "elevation_kb": "29m", "water_depth": "310m", "td_driller": "2850m", "td_logger": "2852m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "Cores 1-16: 0.5m",
        "geologists": "J.F.B., T.D., K.O.H.", "comments": "Deep appraisal coring sequence", "stamp": "", "skew": 0.2,
        "table_rows_count": 20,
        "cores": [
            ("1", "2400.0 - 2415.5", "100"), ("2", "2415.5 - 2432.0", "98.5"),
            ("3", "2432.0 - 2448.5", "96.0"), ("4", "2448.5 - 2465.0", "100"),
            ("5", "2465.0 - 2482.2", "94.5"), ("6", "2482.2 - 2499.0", "100"),
            ("7", "2499.0 - 2516.5", "99.0"), ("8", "2516.5 - 2533.0", "92.0"),
            ("9", "2533.0 - 2550.0", "100"), ("10", "2550.0 - 2567.5", "97.0"),
            ("11", "2567.5 - 2584.0", "95.5"), ("12", "2584.0 - 2601.2", "100"),
            ("13", "2601.2 - 2618.0", "88.0"), ("14", "2618.0 - 2635.5", "96.5"),
            ("15", "2635.5 - 2652.0", "100"), ("16", "2652.0 - 2668.5", "94.0")
        ]
    },
    {
        "filename": "norsk_hydro_12_shifted_down_200dpi.pdf",
        "orientation": "portrait", "dpi": 200,
        "well_name": "6406/1-1", "date": "08/1987", "scale": "1 : 200",
        "group_formation": "Båt Gp.", "age": "Tidlig Jura",
        "country": "Norway", "licence": "PL094", "field": "Tyrihans Nord",
        "owners": "Statoil, Agip, Total", "coordinates_geo": "N 64° 56' 32.10\"\nE 06° 42' 19.80\"",
        "elevation_kb": "28m", "water_depth": "295m", "td_driller": "4320m", "td_logger": "4318m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "Cores 1-3: 1m",
        "geologists": "J.Gj.", "comments": "", "stamp": "", "skew": -0.4,
        "top_shift_px": 80, "table_rows_count": 8,
        "cores": [("1", "4100.0 - 4118.5", "97.0"), ("2", "4118.5 - 4136.0", "100"), ("3", "4136.0 - 4154.2", "91.5")]
    },
    {
        "filename": "norsk_hydro_13_header_bloat_pushed_down_150dpi.pdf",
        "orientation": "portrait", "dpi": 150,
        "well_name": "6406/2-2", "date": "22/04-1988, rev. 06-89", "scale": "1 : 200",
        "group_formation": "Fangst Gp., Båt Gp., Tilje Fm., Tofte Fm., Ror Fm., Ile Fm., Garn Fm.",
        "age": "Mellom til Tidlig Jura (Toarcian - Aalenian - Bajocian)",
        "country": "Norway", "licence": "PL199", "field": "Lavrans",
        "owners": "Saga Petroleum, Statoil, Mobil, Total, Deminex, Agip, Norsk Hydro, Arco",
        "coordinates_geo": "N 64° 50' 11.45\"\nE 06° 25' 58.12\"",
        "elevation_kb": "31m", "water_depth": "285m", "td_driller": "4750m", "td_logger": "4762m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "C1-C7: -1.2m",
        "geologists": "J.F. Bockelie, J. Gjelberg, T. Dahl, K.O. Heum",
        "comments": "Condensate discovery, thick reservoir column", "stamp": "", "skew": 0.5,
        "header_bloat_extra": 35, "table_rows_count": 12,
        "cores": [
            ("1", "4305.0 - 4322.5", "100"), ("2", "4322.5 - 4340.0", "96.5"),
            ("3", "4340.0 - 4358.0", "94.0"), ("4", "4358.0 - 4376.2", "99.0"),
            ("5", "4376.2 - 4394.0", "100"), ("6", "4394.0 - 4412.5", "92.0"), ("7", "4412.5 - 4430.0", "100")
        ]
    },
    {
        "filename": "norsk_hydro_14_compact_short_sheet_120dpi.pdf",
        "orientation": "portrait", "dpi": 120, "page_height_ratio": 0.85, "top_margin_tight": 10,
        "well_name": "6506/12-1", "date": "1985, rev. 1989", "scale": "1 : 200",
        "group_formation": "Garn Fm.", "age": "Mellom Jura",
        "country": "Norge", "licence": "PL094", "field": "Smørbukk Hoved",
        "owners": "Statoil, Mobil, Agip, Arco, Tenneco, Norsk Hydro",
        "coordinates_geo": "N 65° 10' 12.00\"\nE 06° 45' 18.00\"",
        "elevation_kb": "25m", "water_depth": "262m", "td_driller": "4200m", "td_logger": "4205m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "C1-C4: 0m",
        "geologists": "J.F.B.", "comments": "", "stamp": "", "skew": -0.3, "table_rows_count": 8,
        "cores": [
            ("1", "3900.0 - 3918.0", "100"), ("2", "3918.0 - 3935.5", "95.0"),
            ("3", "3935.5 - 3953.0", "98.0"), ("4", "3953.0 - 3970.5", "100")
        ]
    },

    # --- 2 LANDSCAPE CENTERED FILES (15 - 16) ---
    {
        "filename": "norsk_hydro_15_landscape_centered_150dpi.pdf",
        "orientation": "landscape", "dpi": 150,
        "is_wide_banner": True,
        "well_name": "6406/2-3", "date": "28/11-1986, rev. 1989", "scale": "1 : 200",
        "group_formation": "Tomma Gp., Halten Gp.", "age": "Jura",
        "country": "Norway", "licence": "PL094", "field": "Smørbukk Sør",
        "owners": "Statoil, Agip, Mobil, Deminex", "coordinates_geo": "N 64° 53' 44.18\"\nE 06° 39' 12.50\"",
        "elevation_kb": "29m", "water_depth": "304m", "td_driller": "4600m", "td_logger": "4595m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "Cores 1-6: 0.8m",
        "geologists": "T.D., J.Gj.", "comments": "Wide horizontal banner centered across sheet", "stamp": "", "skew": 0.2,
        "vertical_center": True, "table_rows_count": 8,
        "cores": [
            ("1", "3980.0 - 3995.5", "96.0"), ("2", "3995.5 - 4012.0", "100"),
            ("3", "4012.0 - 4028.5", "94.5"), ("4", "4028.5 - 4045.0", "98.0"),
            ("5", "4045.0 - 4062.2", "100"), ("6", "4062.2 - 4078.0", "92.5")
        ]
    },
    {
        "filename": "norsk_hydro_16_landscape_centered_200dpi.pdf",
        "orientation": "landscape", "dpi": 200,
        "is_transposed_table": True,
        "well_name": "6406/1-2", "date": "15/05-1988", "scale": "1 : 200",
        "group_formation": "Garn / Not Fm.", "age": "Mellom Jura",
        "country": "Norway", "licence": "PL094", "field": "Beta Vest",
        "owners": "Statoil, Total, Arco, Norsk Hydro", "coordinates_geo": "N 64° 58' 22.10\"\nE 06° 35' 18.40\"",
        "elevation_kb": "30m", "water_depth": "315m", "td_driller": "4400m", "td_logger": "4392m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "C1-C5: 0.5m",
        "geologists": "J.F.B., K.O.H.", "comments": "Transposed horizontal core table centered on sheet", "stamp": "", "skew": -0.3,
        "vertical_center": True, "table_rows_count": 6,
        "cores": [
            ("1", "3710.0 - 3728.5", "100"), ("2", "3728.5 - 3746.0", "97.5"),
            ("3", "3746.0 - 3764.0", "100"), ("4", "3764.0 - 3782.2", "91.0"),
            ("5", "3782.2 - 3800.0", "98.5")
        ]
    },

    # --- 2 MULTI-PAGE FILES (17 - 18) ---
    # File 17: 2-Page PDF (Page 1 = Drilling Summary, Page 2 = TARGET Core Log!)
    {
        "filename": "norsk_hydro_17_multipage_target_page2_150dpi.pdf",
        "is_multipage": True, "target_page": 2, "total_pages": 2,
        "orientation": "portrait", "dpi": 150,
        "well_name": "6407/7-2", "date": "10/08-1987, rev. 1989", "scale": "1 : 200",
        "group_formation": "Tilje / Åre Fm.", "age": "Tidlig Jura",
        "country": "Norway", "licence": "PL107", "field": "Njård",
        "owners": "Norsk Hydro, Statoil, Mobil", "coordinates_geo": "N 64° 24' 15.10\"\nE 07° 11' 22.40\"",
        "elevation_kb": "27m", "water_depth": "330m", "td_driller": "3650m", "td_logger": "3645m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "C1-C8: 0.8m",
        "geologists": "T.D., J.Gj.", "comments": "Target table is on Page 2!", "stamp": "", "skew": 0.3,
        "cores": [
            ("1", "3150.0 - 3165.5", "98.0"), ("2", "3165.5 - 3182.0", "100"),
            ("3", "3182.0 - 3198.5", "95.5"), ("4", "3198.5 - 3215.0", "92.0"),
            ("5", "3215.0 - 3232.0", "100"), ("6", "3232.0 - 3248.5", "97.5"),
            ("7", "3248.5 - 3265.0", "100"), ("8", "3265.0 - 3280.0", "96.0")
        ]
    },

    # File 18: 3-Page PDF (Page 1 = Mud Log, Page 2 = Bit Record, Page 3 = TARGET Core Log!)
    {
        "filename": "norsk_hydro_18_multipage_target_page3_150dpi.pdf",
        "is_multipage": True, "target_page": 3, "total_pages": 3,
        "orientation": "portrait", "dpi": 150,
        "well_name": "6506/12-3", "date": "05/1986, rev. 06-89", "scale": "1 : 200",
        "group_formation": "Garn / Ile Fm.", "age": "Mellom Jura",
        "country": "Norge", "licence": "PL094", "field": "Smørbukk Sør",
        "owners": "Statoil, Agip, Total, Norsk Hydro", "coordinates_geo": "N 65° 11' 40.12\"\nE 06° 48' 22.05\"",
        "elevation_kb": "26m", "water_depth": "275m", "td_driller": "4300m", "td_logger": "4296m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "C1-C7: 1.0m",
        "geologists": "J.F.B., T.D.", "comments": "Target table is on Page 3!", "stamp": "", "skew": -0.4,
        "cores": [
            ("1", "3850.0 - 3868.5", "100"), ("2", "3868.5 - 3886.0", "94.0"),
            ("3", "3886.0 - 3904.2", "99.0"), ("4", "3904.2 - 3922.0", "97.5"),
            ("5", "3922.0 - 3940.0", "100"), ("6", "3940.0 - 3957.5", "93.0"),
            ("7", "3957.5 - 3975.0", "100")
        ]
    },

    # --- 5 ELITE CURVEBALL FILES (19 - 23) ---

    # File 19: SPLIT-COLUMN TABLE (Side-by-side core columns!)
    {
        "filename": "norsk_hydro_19_split_column_table_150dpi.pdf",
        "is_split_column": True,
        "orientation": "portrait", "dpi": 150,
        "well_name": "6407/7-1", "date": "18/09-1985, rev. 1989", "scale": "1 : 200",
        "group_formation": "Tilje / Åre Gp.", "age": "Tidlig Jura",
        "country": "Norway", "licence": "PL107", "field": "Njård",
        "owners": "Norsk Hydro, Conoco, Statoil", "coordinates_geo": "N 64° 26' 02.18\"\nE 07° 08' 35.10\"",
        "elevation_kb": "28m", "water_depth": "320m", "td_driller": "3500m", "td_logger": "3495m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "C1-C14: 0.5m",
        "geologists": "K.O.H., J.F.B.", "comments": "Side-by-side split core table layout", "stamp": "", "skew": 0.2,
        "cores": [
            ("1", "3050.0 - 3065.0", "100"), ("2", "3065.0 - 3080.5", "98.0"),
            ("3", "3080.5 - 3096.0", "95.5"), ("4", "3096.0 - 3112.0", "100"),
            ("5", "3112.0 - 3128.5", "92.0"), ("6", "3128.5 - 3145.0", "100"),
            ("7", "3145.0 - 3160.0", "96.5"),
            # Column 2 (Right side):
            ("8", "3160.0 - 3176.5", "100"), ("9", "3176.5 - 3192.0", "94.0"),
            ("10", "3192.0 - 3208.0", "99.0"), ("11", "3208.0 - 3225.5", "100"),
            ("12", "3225.5 - 3242.0", "91.5"), ("13", "3242.0 - 3258.0", "97.0"),
            ("14", "3258.0 - 3274.5", "100")
        ]
    },

    # File 20: HANDWRITTEN CORRECTIONS (Pen strike-throughs on typed numbers with handwritten replacements)
    {
        "filename": "norsk_hydro_20_handwritten_corrections_200dpi.pdf",
        "has_handwritten_corrections": True,
        "orientation": "portrait", "dpi": 200,
        "well_name": "6406/3-1", "date": "14/08-1984, rev. 1989", "scale": "1 : 200",
        "group_formation": "Tomma Gp.", "age": "Jura",
        "country": "Norway", "licence": "PL091", "field": "Smørbukk",
        "owners": "Statoil, Mobil, Saga, Norsk Hydro", "coordinates_geo": "N 64° 55' 08.12\"\nE 06° 52' 14.80\"",
        "elevation_kb": "29m", "water_depth": "298m", "td_driller": "4450m", "td_logger": "4445m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "C1-C5: 1.0m",
        "geologists": "J.Gj., T.D.", "comments": "Handwritten pen corrections on core 2 & 4 depths", "stamp": "", "skew": 0.4,
        # Note: Core 2 typed 3968.0 crossed out, handwritten 3969.5! Core 4 recovery handwritten 95%!
        "cores": [
            ("1", "3935.0 - 3950.0", "100"),
            ("2", "3950.0 - 3969.5", "96.0"), # Corrected ground truth!
            ("3", "3970.0 - 3986.5", "98.5"),
            ("4", "3986.5 - 4004.0", "95.0"), # Corrected ground truth!
            ("5", "4004.0 - 4022.0", "100")
        ]
    },

    # File 21: MICROFICHE / NEGATIVE SCAN (White text on black background!)
    {
        "filename": "norsk_hydro_21_microfiche_negative_scan_150dpi.pdf",
        "is_negative": True, # Inverted colors!
        "orientation": "portrait", "dpi": 150,
        "well_name": "6407/1-2", "date": "1983, rev. 1989", "scale": "1 : 200",
        "group_formation": "Garn Fm.", "age": "Mellom Jura",
        "country": "Norway", "licence": "073", "field": "Tyrihans",
        "owners": "Statoil, Conoco, Norsk Hydro", "coordinates_geo": "N 64° 50' 18.20\"\nE 07° 00' 45.10\"",
        "elevation_kb": "28m", "water_depth": "280m", "td_driller": "4100m", "td_logger": "4095m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "C1-C4: 0.5m",
        "geologists": "J.F.B.", "comments": "Microfiche archival film negative", "stamp": "MICROFICHE ARCHIVE", "skew": -0.5,
        "cores": [
            ("1", "3640.0 - 3658.0", "98.0"), ("2", "3658.0 - 3675.5", "100"),
            ("3", "3675.5 - 3692.0", "94.5"), ("4", "3692.0 - 3708.5", "100")
        ]
    },

    # File 22: FRAMELESS / BORDERLESS TABLE (Typewriter tabbed columns with no vertical gridlines!)
    {
        "filename": "norsk_hydro_22_borderless_table_150dpi.pdf",
        "is_borderless": True, # No vertical grid lines!
        "orientation": "portrait", "dpi": 150,
        "well_name": "6507/7-2", "date": "11/1986", "scale": "1 : 200",
        "group_formation": "Tilje Fm.", "age": "Tidlig Jura",
        "country": "Norway", "licence": "PL095", "field": "Heidrun",
        "owners": "Conoco, Statoil, Tenneco", "coordinates_geo": "N 65° 21' 10.15\"\nE 07° 15' 40.20\"",
        "elevation_kb": "29m", "water_depth": "350m", "td_driller": "2700m", "td_logger": "2695m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "Cores 1-5: 0.8m",
        "geologists": "T.D.", "comments": "Borderless typewriter tabbed sheet", "stamp": "", "skew": 0.3,
        "cores": [
            ("1", "2480.0 - 2496.5", "100"), ("2", "2496.5 - 2514.0", "97.0"),
            ("3", "2514.0 - 2530.5", "100"), ("4", "2530.5 - 2548.0", "93.5"),
            ("5", "2548.0 - 2565.0", "98.0")
        ]
    },

    # File 23: 180° UPSIDE DOWN (Completely inverted document feeder error!)
    {
        "filename": "norsk_hydro_23_upside_down_180deg_150dpi.pdf",
        "is_upside_down": True, # Rotated 180 degrees!
        "orientation": "portrait", "dpi": 150,
        "well_name": "6407/9-2", "date": "04/1985, rev. 1989", "scale": "1 : 200",
        "group_formation": "Garn Fm.", "age": "Mellom Jura",
        "country": "Norway", "licence": "PL093", "field": "Draugen",
        "owners": "A/S Norske Shell, Statoil", "coordinates_geo": "N 64° 19' 22.10\"\nE 07° 46' 18.40\"",
        "elevation_kb": "25m", "water_depth": "255m", "td_driller": "1780m", "td_logger": "1778m",
        "formation_at_td": "Åre Fm.", "loggers_depth_diff": "Cores 1-4: 0.5m",
        "geologists": "K.O.H.", "comments": "Scanned upside-down 180 degrees", "stamp": "", "skew": 0.2,
        "cores": [
            ("1", "1630.0 - 1648.0", "100"), ("2", "1648.0 - 1665.5", "96.5"),
            ("3", "1665.5 - 1682.0", "100"), ("4", "1682.0 - 1700.0", "94.0")
        ]
    }
]

# Standard authentic Diskos naming convention:
# WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_1.pdf ... ENCL_23.pdf
for idx, ds in enumerate(WELL_DATASETS, 1):
    ds["filename"] = f"WB_MULTIPLE_WELLS_ROCK_AND_CORE_CORE_DESC_REPORT_4_ENCL_{idx}.pdf"



def draw_viking_logo(draw, x, y, scale=1.0, color=(0, 0, 0)):
    """Draw the classic Norsk Hydro Viking ship logo."""
    for i in range(3):
        sx = x + int(i * 14 * scale)
        sy = y
        draw.arc([sx, sy, sx + int(12 * scale), sy + int(24 * scale)], start=270, end=90, fill=color, width=max(1, int(2 * scale)))
    hx1 = x - int(4 * scale)
    hy1 = y + int(22 * scale)
    hx2 = x + int(46 * scale)
    hy2 = y + int(30 * scale)
    draw.rectangle([hx1, hy1, hx2, hy2], fill=color)
    draw.line([hx1 - int(2 * scale), hy2 + int(3 * scale), hx2 + int(2 * scale), hy2 + int(3 * scale)], fill=color, width=max(1, int(1.5 * scale)))


def finalize_page_effects(img, ds, dpi, margin, w, h):
    """Apply authentic scan grain, noise, skew, rotation, negative inversion, or 180 flip."""
    # Grain & Noise
    tint = Image.new("RGB", img.size, (253, 252, 248))
    img = Image.blend(img, tint, alpha=0.06)
    draw_noise = ImageDraw.Draw(img)
    num_specks = int(120 * (dpi / 150.0))
    for _ in range(num_specks):
        rx = random.randint(margin, w - margin)
        ry = random.randint(margin, h - margin)
        draw_noise.point((rx, ry), fill=(random.randint(140, 220), random.randint(140, 220), random.randint(140, 220)))

    # Skew
    if abs(ds.get("skew", 0.0)) > 0.01:
        img = img.rotate(ds["skew"], resample=Image.Resampling.BICUBIC, expand=False, fillcolor=(255, 255, 255))

    # Sideways
    if ds.get("orientation") == "landscape_sideways":
        img = img.rotate(-90, expand=True)

    # Negative Scan (Microfiche Inversion)
    if ds.get("is_negative"):
        img = ImageOps.invert(img)

    # 180 Degree Upside Down
    if ds.get("is_upside_down"):
        img = img.rotate(180)

    return img


def render_transposed_table_layout(draw, ds, w, h, s, margin, font_header, font_title, font_sub, font_body, font_body_bold, font_small):
    """Render File 16: Transposed horizontal core table in center of sheet."""
    block_h = int(320 * s)
    box_top = max(margin, (h - block_h) // 2)
    box_bottom = min(h - margin, box_top + block_h)

    # Double outer black border
    draw.rectangle([margin, box_top, w - margin, box_bottom], outline=(0, 0, 0), width=max(1, int(3 * s)))
    draw.rectangle([margin + int(4 * s), box_top + int(4 * s), w - margin - int(4 * s), box_bottom - int(4 * s)], outline=(0, 0, 0), width=max(1, int(1 * s)))

    # Header
    logo_x = margin + int(25 * s)
    logo_y = box_top + int(12 * s)
    draw.rectangle([logo_x, logo_y, logo_x + int(180 * s), logo_y + int(42 * s)], outline=(0, 0, 0), width=max(1, int(1.5 * s)))
    draw_viking_logo(draw, logo_x + int(8 * s), logo_y + int(5 * s), scale=s)
    draw.text((logo_x + int(65 * s), logo_y + int(10 * s)), "Norsk Hydro", font=font_header, fill=(0, 0, 0))

    draw.text((w // 2 - int(75 * s), box_top + int(10 * s)), "CORE LOG", font=font_title, fill=(0, 0, 0))
    draw.text((w // 2 - int(45 * s), box_top + int(36 * s)), f"SCALE: {ds['scale']}", font=font_sub, fill=(0, 0, 0))

    draw.text((w // 2 - int(75 * s), box_top + int(56 * s)), f"WELL : {ds['well_name']}", font=font_header, fill=(0, 0, 0))
    if ds.get('date'):
        draw.text((w - margin - int(240 * s), box_top + int(56 * s)), f"DATE : {ds['date']}", font=font_sub, fill=(0, 0, 0))

    div_y = box_top + int(82 * s)
    draw.line([margin + int(10 * s), div_y, w - margin - int(10 * s), div_y], fill=(0, 0, 0), width=max(1, int(2 * s)))

    # Metadata Grid (horizontal rows)
    m_y1 = div_y + int(8 * s)
    draw.text((margin + int(25 * s), m_y1), f"COUNTRY: {ds['country']}", font=font_small, fill=(0, 0, 0))
    draw.text((margin + int(200 * s), m_y1), f"LICENCE: {ds['licence']}", font=font_small, fill=(0, 0, 0))
    draw.text((margin + int(380 * s), m_y1), f"FIELD: {ds['field']}", font=font_small, fill=(0, 0, 0))
    draw.text((margin + int(580 * s), m_y1), f"ELEVATION KB: {ds['elevation_kb']}", font=font_small, fill=(0, 0, 0))
    draw.text((margin + int(780 * s), m_y1), f"WATER DEPTH: {ds['water_depth']}", font=font_small, fill=(0, 0, 0))
    draw.text((margin + int(980 * s), m_y1), f"TOTAL DEPTH (LOGGER): {ds['td_logger']}", font=font_small, fill=(0, 0, 0))
    draw.text((margin + int(1280 * s), m_y1), f"FORMATION AT TD: {ds['formation_at_td']}", font=font_small, fill=(0, 0, 0))

    m_y2 = m_y1 + int(16 * s)
    draw.text((margin + int(25 * s), m_y2), f"OWNERS: {ds['owners']}", font=font_small, fill=(0, 0, 0))
    coords = ds.get('coordinates_geo', '').replace('\n', '  ')
    draw.text((margin + int(460 * s), m_y2), f"COORDINATES: {coords}", font=font_small, fill=(0, 0, 0))
    draw.text((margin + int(900 * s), m_y2), f"LOGGERS DEPTH - DRILLERS DEPTH: {ds.get('loggers_depth_diff', '')}", font=font_small, fill=(0, 0, 0))
    draw.text((margin + int(1300 * s), m_y2), f"GEOLOGISTS: {ds.get('geologists', '')}", font=font_small, fill=(0, 0, 0))

    div_y2 = m_y2 + int(16 * s)
    draw.line([margin + int(10 * s), div_y2, w - margin - int(10 * s), div_y2], fill=(0, 0, 0), width=max(1, int(1.5 * s)))

    # TRANSPOSED HORIZONTAL TABLE
    t_title_y = div_y2 + int(8 * s)
    draw.text((margin + int(25 * s), t_title_y), "CORES DESCRIBED IN THIS LOG (TRANSPOSED HORIZONTAL CORE INTERVALS)", font=font_small, fill=(0, 0, 0))

    t_top = t_title_y + int(18 * s)
    t_left = margin + int(25 * s)
    t_right = w - margin - int(25 * s)
    hdr_w = int(140 * s)
    num_c = len(ds["cores"])
    core_w = int((t_right - t_left - hdr_w) / num_c)
    row_h = int(24 * s)
    t_h = 3 * row_h

    # Table Outer Box
    draw.rectangle([t_left, t_top, t_left + hdr_w + num_c * core_w, t_top + t_h], outline=(0, 0, 0), width=max(1, int(1.5 * s)))

    # Horizontal divider lines
    draw.line([t_left, t_top + row_h, t_left + hdr_w + num_c * core_w, t_top + row_h], fill=(0, 0, 0), width=1)
    draw.line([t_left, t_top + 2 * row_h, t_left + hdr_w + num_c * core_w, t_top + 2 * row_h], fill=(0, 0, 0), width=1)

    # Vertical divider after header
    draw.line([t_left + hdr_w, t_top, t_left + hdr_w, t_top + t_h], fill=(0, 0, 0), width=max(1, int(1.5 * s)))

    # Vertical divider for each core
    for i in range(1, num_c):
        cx = t_left + hdr_w + i * core_w
        draw.line([cx, t_top, cx, t_top + t_h], fill=(180, 180, 180), width=1)

    # Row 1: CORE NUMBER
    draw.text((t_left + int(10 * s), t_top + int(5 * s)), "CORE NUMBER", font=font_small, fill=(0, 0, 0))
    for i, (c_no, c_int, c_rec) in enumerate(ds["cores"]):
        cx = t_left + hdr_w + i * core_w
        draw.text((cx + int(16 * s), t_top + int(5 * s)), f"CORE {c_no}", font=font_body_bold, fill=(0, 0, 0))

    # Row 2: INTERVAL (m)
    draw.text((t_left + int(10 * s), t_top + row_h + int(5 * s)), "INTERVAL (m)", font=font_small, fill=(0, 0, 0))
    for i, (c_no, c_int, c_rec) in enumerate(ds["cores"]):
        cx = t_left + hdr_w + i * core_w
        draw.text((cx + int(16 * s), t_top + row_h + int(5 * s)), c_int, font=font_body, fill=(0, 0, 0))

    # Row 3: RECOVERY (%)
    draw.text((t_left + int(10 * s), t_top + 2 * row_h + int(5 * s)), "RECOVERY (%)", font=font_small, fill=(0, 0, 0))
    for i, (c_no, c_int, c_rec) in enumerate(ds["cores"]):
        cx = t_left + hdr_w + i * core_w
        draw.text((cx + int(16 * s), t_top + 2 * row_h + int(5 * s)), f"{c_rec}%" if c_rec and "%" not in c_rec else (c_rec or ""), font=font_body, fill=(0, 0, 0))

    # Symbol index
    draw.text((margin + int(25 * s), box_bottom - int(24 * s)), "SYMBOL INDEX :   [■] CLAY / SHALE     [░] SANDSTONE     [▦] SILTSTONE     [▨] LIMESTONE     [▪] COAL", font=font_small, fill=(100, 100, 100))


def render_wide_banner_layout(draw, ds, w, h, s, margin, font_header, font_title, font_sub, font_body, font_body_bold, font_small):
    """Render File 15: Wide horizontal banner in center of landscape sheet."""
    block_h = int(350 * s)
    box_top = max(margin, (h - block_h) // 2)
    box_bottom = min(h - margin, box_top + block_h)

    # Double Border
    draw.rectangle([margin, box_top, w - margin, box_bottom], outline=(0, 0, 0), width=max(1, int(3 * s)))
    draw.rectangle([margin + int(4 * s), box_top + int(4 * s), w - margin - int(4 * s), box_bottom - int(4 * s)], outline=(0, 0, 0), width=max(1, int(1 * s)))

    # Header
    logo_x = margin + int(25 * s)
    logo_y = box_top + int(12 * s)
    draw.rectangle([logo_x, logo_y, logo_x + int(180 * s), logo_y + int(42 * s)], outline=(0, 0, 0), width=max(1, int(1.5 * s)))
    draw_viking_logo(draw, logo_x + int(8 * s), logo_y + int(5 * s), scale=s)
    draw.text((logo_x + int(65 * s), logo_y + int(10 * s)), "Norsk Hydro", font=font_header, fill=(0, 0, 0))

    draw.text((w // 2 - int(75 * s), box_top + int(10 * s)), "CORE LOG", font=font_title, fill=(0, 0, 0))
    draw.text((w // 2 - int(45 * s), box_top + int(36 * s)), f"SCALE: {ds['scale']}", font=font_sub, fill=(0, 0, 0))

    draw.text((w // 2 - int(75 * s), box_top + int(56 * s)), f"WELL : {ds['well_name']}", font=font_header, fill=(0, 0, 0))
    if ds.get('date'):
        draw.text((w - margin - int(240 * s), box_top + int(56 * s)), f"DATE : {ds['date']}", font=font_sub, fill=(0, 0, 0))

    div_y = box_top + int(82 * s)
    draw.line([margin + int(10 * s), div_y, w - margin - int(10 * s), div_y], fill=(0, 0, 0), width=max(1, int(2 * s)))

    # Metadata (Left area)
    meta_x = margin + int(20 * s)
    meta_val_x = meta_x + int(140 * s)
    items = [
        ("COUNTRY", ds['country']), ("LICENCE", ds['licence']), ("FIELD", ds['field']),
        ("OWNERS", ds['owners']), ("COORDINATES", ds['coordinates_geo'].replace('\n', '  ')),
        ("WATER DEPTH", ds['water_depth']), ("TOTAL DEPTH (LOGGER)", ds['td_logger']),
        ("FORMATION AT TD", ds['formation_at_td']), ("GEOLOGISTS", ds['geologists'])
    ]
    cur_y = div_y + int(10 * s)
    for label, val in items:
        draw.text((meta_x, cur_y), label, font=font_small, fill=(0, 0, 0))
        draw.text((meta_val_x, cur_y), str(val), font=font_body, fill=(0, 0, 0))
        cur_y += int(16 * s)

    # Vertical divider
    vdiv_x = margin + int(460 * s)
    draw.line([vdiv_x, div_y, vdiv_x, box_bottom - int(32 * s)], fill=(0, 0, 0), width=max(1, int(1.5 * s)))

    # Tables on Right
    t1_x = vdiv_x + int(15 * s)
    t1_w = int(160 * s)
    t2_x = t1_x + t1_w + int(20 * s)
    t2_w = w - margin - t2_x - int(20 * s)

    draw.text((t1_x, div_y + int(8 * s)), "OTHER CORES IN WELL", font=font_small, fill=(0, 0, 0))
    draw.text((t2_x, div_y + int(8 * s)), "CORES DESCRIBED IN THIS LOG (WIDE HORIZONTAL SECTION)", font=font_small, fill=(0, 0, 0))

    t_top = div_y + int(26 * s)
    row_h = int(18 * s)
    num_rows = max(len(ds["cores"]) + 1, 7)

    # T1 grid
    draw.rectangle([t1_x, t_top, t1_x + t1_w, t_top + num_rows * row_h], outline=(0, 0, 0), width=1)
    draw.line([t1_x + int(35 * s), t_top, t1_x + int(35 * s), t_top + num_rows * row_h], fill=(0, 0, 0), width=1)
    draw.line([t1_x, t_top + row_h, t1_x + t1_w, t_top + row_h], fill=(0, 0, 0), width=1)
    draw.text((t1_x + int(6 * s), t_top + int(3 * s)), "NO", font=font_small, fill=(0, 0, 0))
    draw.text((t1_x + int(42 * s), t_top + int(3 * s)), "GROUP/FORMATION", font=font_small, fill=(0, 0, 0))

    # T2 grid
    c1_w = int(45 * s)
    c2_w = int(220 * s)
    draw.rectangle([t2_x, t_top, t2_x + t2_w, t_top + num_rows * row_h], outline=(0, 0, 0), width=max(1, int(1.5 * s)))
    draw.line([t2_x + c1_w, t_top, t2_x + c1_w, t_top + num_rows * row_h], fill=(0, 0, 0), width=1)
    draw.line([t2_x + c1_w + c2_w, t_top, t2_x + c1_w + c2_w, t_top + num_rows * row_h], fill=(0, 0, 0), width=1)
    draw.line([t2_x, t_top + row_h, t2_x + t2_w, t_top + row_h], fill=(0, 0, 0), width=1)

    draw.text((t2_x + int(8 * s), t_top + int(3 * s)), "NO", font=font_small, fill=(0, 0, 0))
    draw.text((t2_x + c1_w + int(20 * s), t_top + int(3 * s)), "INTERVAL (m)", font=font_small, fill=(0, 0, 0))
    draw.text((t2_x + c1_w + c2_w + int(20 * s), t_top + int(3 * s)), "RECOVERY (%)", font=font_small, fill=(0, 0, 0))

    for r, (c_no, c_int, c_rec) in enumerate(ds["cores"], 1):
        ry = t_top + r * row_h
        draw.line([t2_x, ry, t2_x + t2_w, ry], fill=(180, 180, 180), width=1)
        draw.text((t2_x + int(12 * s), ry + int(3 * s)), c_no, font=font_body_bold, fill=(0, 0, 0))
        draw.text((t2_x + c1_w + int(20 * s), ry + int(3 * s)), c_int, font=font_body, fill=(0, 0, 0))
        draw.text((t2_x + c1_w + c2_w + int(24 * s), ry + int(3 * s)), f"{c_rec}%" if c_rec and "%" not in c_rec else (c_rec or ""), font=font_body, fill=(0, 0, 0))

    # Symbol index
    draw.text((margin + int(20 * s), box_bottom - int(24 * s)), "SYMBOL INDEX :   [■] CLAY / SHALE     [░] SANDSTONE     [▦] SILTSTONE     [▨] LIMESTONE     [▪] COAL", font=font_small, fill=(100, 100, 100))


def render_single_page(ds, is_dummy_cover=False, dummy_page_type=1):
    """Render a single page canvas."""
    dpi = ds["dpi"]
    height_mult = ds.get("page_height_ratio", 1.0)

    if ds["orientation"] == "portrait":
        w = int(8.27 * dpi)
        h = int(11.69 * dpi * height_mult)
    else:
        w = int(11.69 * dpi)
        h = int(8.27 * dpi * height_mult)

    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    s = dpi / 150.0

    # Fonts
    try:
        font_title = ImageFont.truetype("arialbd.ttf", int(24 * s))
        font_header = ImageFont.truetype("arialbd.ttf", int(14 * s))
        font_sub = ImageFont.truetype("arial.ttf", int(11 * s))
        font_body = ImageFont.truetype("cour.ttf", int(10 * s))
        font_body_bold = ImageFont.truetype("courbd.ttf", int(10 * s))
        font_small = ImageFont.truetype("cour.ttf", int(8.5 * s))
        font_script = ImageFont.truetype("segoesc.ttf", int(9.5 * s)) # Handwritten style
    except:
        font_title = ImageFont.load_default()
        font_header = font_title
        font_sub = font_title
        font_body = font_title
        font_body_bold = font_title
        font_small = font_title
        font_script = font_title

    margin = int(ds.get("top_margin_tight", 24) * s)

    # If this is a dummy cover page (for multi-page trap):
    if is_dummy_cover:
        draw.rectangle([margin, margin, w - margin, h - margin], outline=(0, 0, 0), width=max(1, int(2 * s)))
        if dummy_page_type == 1:
            # Drilling Rig Summary Cover
            draw.text((margin + int(40 * s), margin + int(50 * s)), "STATOIL / NORSK HYDRO OFFSHORE OPERATIONS", font=font_header, fill=(0, 0, 0))
            draw.text((margin + int(40 * s), margin + int(80 * s)), f"DRILLING SUMMARY REPORT — WELL: {ds['well_name']}", font=font_title, fill=(0, 0, 0))
            draw.text((margin + int(40 * s), margin + int(120 * s)), f"Rig: Dyvi Delta   |   Licence: {ds['licence']}   |   Field: {ds['field']}", font=font_sub, fill=(0, 0, 0))
            draw.line([margin + int(40 * s), margin + int(150 * s), w - margin - int(40 * s), margin + int(150 * s)], fill=(0, 0, 0), width=2)
            # Dummy operations notes
            draw.text((margin + int(40 * s), margin + int(180 * s)), "SECTION 1: GENERAL DRILLING CHRONOLOGY & BIT PERFORMANCE", font=font_header, fill=(0, 0, 0))
            for i in range(15):
                draw.text((margin + int(40 * s), margin + int(210 * s + i * 20 * s)), f"Day {i+1:02d}: Spudded 36in conductor, drilled to {600 + i*180}m. Mud weight 1.08 SG. No gas peaks.", font=font_body, fill=(50, 50, 50))
            draw.text((margin + int(40 * s), h - margin - int(50 * s)), "CONFIDENTIAL — FOR OPERATORS REVIEW ONLY — PAGE 1 OF 2", font=font_small, fill=(100, 100, 100))
        else:
            # Mud log & casing record
            draw.text((margin + int(40 * s), margin + int(50 * s)), "GEOLOGICAL MUDLOGGING & DRILL BIT PERFORMANCE", font=font_header, fill=(0, 0, 0))
            draw.text((margin + int(40 * s), margin + int(80 * s)), f"CASING AND ANNULAR HYDRAULICS — WELL: {ds['well_name']}", font=font_title, fill=(0, 0, 0))
            draw.line([margin + int(40 * s), margin + int(120 * s), w - margin - int(40 * s), margin + int(120 * s)], fill=(0, 0, 0), width=2)
            for i in range(12):
                draw.text((margin + int(40 * s), margin + int(160 * s + i * 25 * s)), f"Casing String {i+1}: 13-3/8in shoe set at {1200 + i*150}m. FIT tested to 1.75 SG equivalent.", font=font_body, fill=(50, 50, 50))
            draw.text((margin + int(40 * s), h - margin - int(50 * s)), "APPENDIX 2 — OPERATIONS SUMMARY — PAGE 2 OF 3", font=font_small, fill=(100, 100, 100))

        # Add scan noise
        tint = Image.new("RGB", img.size, (253, 252, 248))
        img = Image.blend(img, tint, alpha=0.06)
        return img

    # --- NORMAL NORSK HYDRO CORE LOG PAGE ---
    if ds.get("is_transposed_table"):
        render_transposed_table_layout(draw, ds, w, h, s, margin, font_header, font_title, font_sub, font_body, font_body_bold, font_small)
        return finalize_page_effects(img, ds, dpi, margin, w, h)

    if ds.get("is_wide_banner"):
        render_wide_banner_layout(draw, ds, w, h, s, margin, font_header, font_title, font_sub, font_body, font_body_bold, font_small)
        return finalize_page_effects(img, ds, dpi, margin, w, h)

    num_grid_rows = ds.get("table_rows_count", 15)
    row_h = int(14 * s)
    block_h = int(140 * s) + num_grid_rows * row_h + int(110 * s)

    if ds.get("vertical_center"):
        top_extra = max(0, (h - block_h) // 2 - margin)
    else:
        top_extra = int(ds.get("top_shift_px", 0) * s)

    box_top = margin + top_extra
    box_bottom = min(h - margin, box_top + block_h)

    # 1. Outer Double Black Border
    draw.rectangle([margin, box_top, w - margin, box_bottom], outline=(0, 0, 0), width=max(1, int(3 * s)))
    draw.rectangle([margin + int(4 * s), box_top + int(4 * s), w - margin - int(4 * s), box_bottom - int(4 * s)], outline=(0, 0, 0), width=max(1, int(1 * s)))

    if ds.get("stamp"):
        draw.text((margin + int(10 * s), box_top - int(16 * s)), ds["stamp"], font=font_small, fill=(60, 60, 60))

    # 2. Header
    header_top = box_top + int(18 * s)
    logo_x = margin + int(25 * s)
    logo_y = header_top + int(10 * s)
    draw.rectangle([logo_x, logo_y, logo_x + int(190 * s), logo_y + int(45 * s)], outline=(0, 0, 0), width=max(1, int(1.5 * s)))
    draw_viking_logo(draw, logo_x + int(8 * s), logo_y + int(6 * s), scale=s)
    draw.text((logo_x + int(65 * s), logo_y + int(12 * s)), "Norsk Hydro", font=font_header, fill=(0, 0, 0))

    draw.text((w // 2 - int(75 * s), header_top + int(8 * s)), "CORE LOG", font=font_title, fill=(0, 0, 0))
    draw.text((w // 2 - int(45 * s), header_top + int(42 * s)), f"SCALE: {ds['scale']}", font=font_sub, fill=(0, 0, 0))

    well_line_y = header_top + int(68 * s)
    draw.text((w // 2 - int(75 * s), well_line_y), f"WELL : {ds['well_name']}", font=font_header, fill=(0, 0, 0))
    if ds['date']:
        draw.text((w - margin - int(240 * s), well_line_y + int(2 * s)), f"DATE : {ds['date']}", font=font_sub, fill=(0, 0, 0))

    line_y = well_line_y + int(28 * s)
    draw.line([margin + int(10 * s), line_y, w - margin - int(10 * s), line_y], fill=(0, 0, 0), width=max(1, int(2 * s)))

    sub_y = line_y + int(14 * s)
    bloat_offset = int(ds.get("header_bloat_extra", 0) * s)
    if ds['group_formation']:
        gf_str = f"GROUP/FORMATION:  {ds['group_formation']}"
        draw.text((w // 2 - int(20 * s), sub_y), gf_str[:60], font=font_small, fill=(0, 0, 0))
        if len(gf_str) > 60:
            draw.text((w // 2 + int(100 * s), sub_y + int(12 * s)), gf_str[60:], font=font_small, fill=(0, 0, 0))
    if ds['age']:
        draw.text((w // 2 - int(20 * s), sub_y + int(18 * s) + (int(10 * s) if bloat_offset else 0)), f"AGE:  {ds['age']}", font=font_small, fill=(0, 0, 0))

    col_top = sub_y + int(36 * s) + bloat_offset

    # Left Metadata
    meta_x = margin + int(30 * s)
    meta_val_x = meta_x + int(160 * s)
    cur_y = col_top
    metadata_items = [
        ("COUNTRY", ds['country']), ("LICENCE", ds['licence']), ("FIELD", ds['field']),
        ("OWNERS", ds['owners']), ("COORDINATES", ds['coordinates_geo']),
        ("ELEVATION KB", ds['elevation_kb']), ("WATER DEPTH", ds['water_depth']),
        ("TOTAL DEPTH (DRILLER)", ds['td_driller']), ("TOTAL DEPTH (LOGGER)", ds['td_logger']),
        ("FORMATION AT TOTAL DEPTH", ds['formation_at_td']),
        ("LOGGERS DEPTH - DRILLERS DEPTH", ds['loggers_depth_diff']),
        ("GEOLOGISTS", ds['geologists']), ("COMMENTS", ds['comments']),
    ]
    for label, val in metadata_items:
        draw.text((meta_x, cur_y), label, font=font_small, fill=(0, 0, 0))
        if val:
            lines = val.split("\n")
            for l_idx, line_str in enumerate(lines):
                draw.text((meta_val_x, cur_y + int(l_idx * 11 * s)), line_str, font=font_body, fill=(0, 0, 0))
            cur_y += max(int(16 * s), int(len(lines) * 13 * s))
        else:
            cur_y += int(16 * s)

    # Right Tables
    table_left = w // 2 - int(10 * s) if ds["orientation"] != "portrait" else int(w * 0.48)
    table_mid = table_left + int(150 * s)
    table_y = col_top
    is_borderless = ds.get("is_borderless", False)
    is_split = ds.get("is_split_column", False)

    if is_split:
        # Split column layout: Cores 1-7 in Col A, Cores 8-14 in Col B!
        draw.text((table_left, table_y - int(14 * s)), "CORES DESCRIBED IN THIS LOG (SPLIT COLUMNS)", font=font_small, fill=(0, 0, 0))
        col_w = int(185 * s)
        half_rows = 8
        draw.rectangle([table_left, table_y, table_left + col_w * 2, table_y + half_rows * row_h], outline=(0, 0, 0), width=1)
        draw.line([table_left, table_y + row_h, table_left + col_w * 2, table_y + row_h], fill=(0, 0, 0), width=1)
        draw.line([table_left + col_w, table_y, table_left + col_w, table_y + half_rows * row_h], fill=(0, 0, 0), width=2) # Center divider

        for c_side, offset_x in enumerate([0, col_w]):
            draw.text((table_left + offset_x + int(4 * s), table_y + int(2 * s)), "NO", font=font_small, fill=(0, 0, 0))
            draw.text((table_left + offset_x + int(26 * s), table_y + int(2 * s)), "INTERVAL (m)", font=font_small, fill=(0, 0, 0))
            draw.text((table_left + offset_x + int(130 * s), table_y + int(2 * s)), "REC %", font=font_small, fill=(0, 0, 0))
            draw.line([table_left + offset_x + int(22 * s), table_y, table_left + offset_x + int(22 * s), table_y + half_rows * row_h], fill=(160, 160, 160), width=1)
            draw.line([table_left + offset_x + int(125 * s), table_y, table_left + offset_x + int(125 * s), table_y + half_rows * row_h], fill=(160, 160, 160), width=1)

        for idx, (c_no, c_interval, c_rec) in enumerate(ds["cores"]):
            c_side = 0 if idx < 7 else 1
            r = (idx % 7) + 1
            offset_x = 0 if c_side == 0 else col_w
            ry = table_y + r * row_h
            draw.line([table_left + offset_x, ry, table_left + offset_x + col_w, ry], fill=(180, 180, 180), width=1)
            draw.text((table_left + offset_x + int(6 * s), ry + int(2 * s)), c_no, font=font_body_bold, fill=(0, 0, 0))
            draw.text((table_left + offset_x + int(28 * s), ry + int(2 * s)), c_interval, font=font_body, fill=(0, 0, 0))
            draw.text((table_left + offset_x + int(132 * s), ry + int(2 * s)), c_rec, font=font_body, fill=(0, 0, 0))

    else:
        # Standard or Borderless Twin Tables
        draw.text((table_left + int(10 * s), table_y - int(14 * s)), "OTHER CORES IN WELL", font=font_small, fill=(0, 0, 0))
        draw.text((table_mid + int(10 * s), table_y - int(14 * s)), "CORES DESCRIBED IN THIS LOG", font=font_small, fill=(0, 0, 0))

        # Table 1 Grid
        if not is_borderless:
            draw.rectangle([table_left, table_y, table_left + int(140 * s), table_y + num_grid_rows * row_h], outline=(0, 0, 0), width=max(1, int(1 * s)))
            draw.line([table_left + int(30 * s), table_y, table_left + int(30 * s), table_y + num_grid_rows * row_h], fill=(0, 0, 0), width=max(1, int(1 * s)))
        draw.line([table_left, table_y + row_h, table_left + int(140 * s), table_y + row_h], fill=(0, 0, 0), width=max(1, int(1 * s)))
        draw.text((table_left + int(6 * s), table_y + int(2 * s)), "NO", font=font_small, fill=(0, 0, 0))
        draw.text((table_left + int(36 * s), table_y + int(2 * s)), "GROUP/FORMATION", font=font_small, fill=(0, 0, 0))
        for r in range(1, num_grid_rows):
            ry = table_y + r * row_h
            draw.line([table_left, ry, table_left + int(140 * s), ry], fill=(180, 180, 180), width=1)

        # Table 2 Grid
        t2_w = int(230 * s)
        t2_x = table_mid
        c1_x = t2_x + int(30 * s)
        c2_x = t2_x + int(160 * s)

        if not is_borderless:
            draw.rectangle([t2_x, table_y, t2_x + t2_w, table_y + num_grid_rows * row_h], outline=(0, 0, 0), width=max(1, int(1.2 * s)))
            draw.line([c1_x, table_y, c1_x, table_y + num_grid_rows * row_h], fill=(0, 0, 0), width=max(1, int(1 * s)))
            draw.line([c2_x, table_y, c2_x, table_y + num_grid_rows * row_h], fill=(0, 0, 0), width=max(1, int(1 * s)))

        draw.line([t2_x, table_y + row_h, t2_x + t2_w, table_y + row_h], fill=(0, 0, 0), width=max(1, int(1.2 * s)))
        draw.text((t2_x + int(6 * s), table_y + int(2 * s)), "NO", font=font_small, fill=(0, 0, 0))
        draw.text((c1_x + int(18 * s), table_y + int(2 * s)), "INTERVAL (m)", font=font_small, fill=(0, 0, 0))
        draw.text((c2_x + int(8 * s), table_y + int(2 * s)), "RECOVERY (%)", font=font_small, fill=(0, 0, 0))

        for r in range(1, num_grid_rows):
            ry = table_y + r * row_h
            draw.line([t2_x, ry, t2_x + t2_w, ry], fill=(180, 180, 180), width=1)
            core_idx = r - 1
            if core_idx < len(ds["cores"]):
                c_no, c_interval, c_rec = ds["cores"][core_idx]
                draw.text((t2_x + int(10 * s), ry + int(2 * s)), c_no, font=font_body_bold, fill=(0, 0, 0))

                # Special Handwritten Corrections on File 20
                if ds.get("has_handwritten_corrections") and c_no == "2":
                    # Draw typed text crossed out with red/blue pen line
                    draw.text((c1_x + int(12 * s), ry + int(2 * s)), "3950.0 - 3968.0", font=font_body, fill=(120, 120, 120))
                    draw.line([c1_x + int(80 * s), ry + int(7 * s), c1_x + int(150 * s), ry + int(7 * s)], fill=(20, 30, 180), width=2)
                    draw.text((c1_x + int(85 * s), ry - int(8 * s)), "3969.5", font=font_script, fill=(20, 30, 180)) # Handwritten above!
                    draw.text((c2_x + int(14 * s), ry + int(2 * s)), c_rec, font=font_body, fill=(0, 0, 0))
                elif ds.get("has_handwritten_corrections") and c_no == "4":
                    draw.text((c1_x + int(12 * s), ry + int(2 * s)), c_interval, font=font_body, fill=(0, 0, 0))
                    draw.text((c2_x + int(14 * s), ry + int(2 * s)), "90.0", font=font_body, fill=(120, 120, 120))
                    draw.line([c2_x + int(12 * s), ry + int(7 * s), c2_x + int(45 * s), ry + int(7 * s)], fill=(20, 30, 180), width=2)
                    draw.text((c2_x + int(14 * s), ry - int(8 * s)), "95.0", font=font_script, fill=(20, 30, 180))
                else:
                    draw.text((c1_x + int(12 * s), ry + int(2 * s)), c_interval, font=font_body, fill=(0, 0, 0))
                    if c_rec:
                        draw.text((c2_x + int(14 * s), ry + int(2 * s)), c_rec, font=font_body, fill=(0, 0, 0))

    # Bottom Symbol Index
    index_y = table_y + num_grid_rows * row_h + int(22 * s)
    if index_y + int(70 * s) < box_bottom:
        draw.text((w // 2 - int(70 * s), index_y), "SYMBOL INDEX", font=font_header, fill=(0, 0, 0))
        idx_box_y = index_y + int(20 * s)
        idx_box_h = int(80 * s)
        draw.rectangle([margin + int(20 * s), idx_box_y, w - margin - int(20 * s), idx_box_y + idx_box_h], outline=(0, 0, 0), width=max(1, int(1 * s)))
        legends = ["CLAY / SHALE", "SILTSTONE", "SANDSTONE", "CONGLOMERATE", "COAL", "LIMESTONE", "DOLOMITE", "CHALK"]
        for l_idx, leg in enumerate(legends):
            lx = margin + int(28 * s) + int((l_idx % 4) * (w - 2 * margin - int(40 * s)) / 4)
            ly = idx_box_y + int(10 * s) + int((l_idx // 4) * 30 * s)
            draw.rectangle([lx, ly, lx + int(18 * s), ly + int(12 * s)], outline=(0, 0, 0), fill=(240, 240, 240))
            draw.text((lx + int(24 * s), ly + int(1 * s)), leg, font=font_small, fill=(0, 0, 0))

    return finalize_page_effects(img, ds, dpi, margin, w, h)


def render_well_pdf(ds):
    """Render full PDF for a dataset (single-page or multi-page)."""
    target_pdf = os.path.join(OUT_DIR, ds["filename"])
    dpi = ds["dpi"]

    if ds.get("is_multipage"):
        pages = []
        tot = ds.get("total_pages", 2)
        target_p = ds.get("target_page", 2)

        for p_idx in range(1, tot + 1):
            if p_idx == target_p:
                page_img = render_single_page(ds, is_dummy_cover=False)
            else:
                page_img = render_single_page(ds, is_dummy_cover=True, dummy_page_type=p_idx)
            pages.append(page_img)

        # Save multi-page PDF
        pages[0].save(target_pdf, "PDF", resolution=float(dpi), save_all=True, append_images=pages[1:])
        print(f"Generated Multi-Page PDF: {ds['filename']} ({tot} pages, Target=Page {target_p})")

    else:
        img = render_single_page(ds, is_dummy_cover=False)
        img.save(target_pdf, "PDF", resolution=float(dpi))
        print(f"Generated Single-Page PDF: {ds['filename']} (DPI={dpi})")


def generate_master_ground_truths():
    """Produce comprehensive ground truth CSVs for all 23 wells."""
    cores_csv = os.path.join(OUT_DIR, "ground_truth_cores.csv")
    with open(cores_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["well_name", "source_file", "target_page", "core_no", "top_depth_m", "bottom_depth_m", "recovery_pct", "group_formation"])
        for ds in WELL_DATASETS:
            target_p = ds.get("target_page", 1)
            for c_no, c_interval, c_rec in ds["cores"]:
                parts = c_interval.replace(" ", "").split("-")
                top_d = float(parts[0]) if len(parts) > 0 and parts[0] else None
                bot_d = float(parts[1]) if len(parts) > 1 and parts[1] else None
                rec_val = c_rec.replace("%", "").strip() if c_rec else None
                if rec_val and "(+2)" in rec_val:
                    rec_val = "100.0"
                writer.writerow([ds["well_name"], ds["filename"], target_p, c_no, top_d, bot_d, rec_val, ds["group_formation"]])

    meta_csv = os.path.join(OUT_DIR, "ground_truth_metadata.csv")
    with open(meta_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["well_name", "source_file", "target_page", "date", "licence", "field", "owners", "water_depth", "total_depth_logger", "formation_at_td"])
        for ds in WELL_DATASETS:
            target_p = ds.get("target_page", 1)
            writer.writerow([
                ds["well_name"],
                ds["filename"],
                target_p,
                ds["date"],
                ds["licence"],
                ds["field"],
                ds["owners"],
                ds["water_depth"],
                ds["td_logger"],
                ds["formation_at_td"]
            ])

    print(f"\nGround Truth CSVs updated successfully: {cores_csv} and {meta_csv}")


if __name__ == "__main__":
    for ds in WELL_DATASETS:
        render_well_pdf(ds)
    generate_master_ground_truths()
