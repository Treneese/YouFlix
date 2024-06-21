#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db
from server.config import db
from models import Show, Episode 

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

def seed_data():
    # Clear existing data
    db.session.query(Episode).delete()
    db.session.query(Show).delete()

    # Sample Shows
    shows = [
        Show(
            title="The Beast Family",
            image="https://yt3.googleusercontent.com/Wc-6npXg72-wpERcq6hcaRnkSsdzrCipvmAOmOOm7QnLb6RkDyGPLkY65FPdHt16fZEu5AOG=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="Enjoy a Family channel that does vlogs, pranks, challenges, and funny skits.",
            category="Family Skits",
            subCategory="shows"
        ),
        Show(
            title="official BRODA SHAGGI",
            image="https://yt3.googleusercontent.com/4QXln30ncURDYGU_2wX3u0qDISfpRQTlWdEkPAYSfBjWtynr1V_aBzxiewXDefFKENgY14yqfRE=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="WANNA LAUGH? 😉 You’re welcome 🫶🏽❤️.",
            category="Comedy Nigeria skits",
            subCategory="shows"
        ),
        Show(
            title="The Trench Family",
            image="https://yt3.googleusercontent.com/NoP9U31suFvZoxkTnTR5vuK1JpwYEQw7xeiToODQ23LWHrc0ySdZlW-b6PDRWfSkuZgSRdRB0KY=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="YOU’RE TUNING IN TO THE LITTEST FAMILY ON YOUTUBE!",
            category="Family Skits",
            subCategory="shows"
        ),
          Show(
            title="Dtay Known",
            image="https://yt3.googleusercontent.com/rqpW2pYdqE_uLlUNzi_sKklIyZZd5Qu5Awqywnf2C2dmW1RmfkYz-yiLHK99dZRS0llOZH6M=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="Welcome to my channel! New content is always in the works 🎬🔥.#TeamDtay.",
            category="Comedy Skits",
            subCategory="shows"
        ),
        Show(
            title="Jillian and Addie Laugh",
            image="https://yt3.googleusercontent.com/WsTeNtV0YCncpS9QyKRGXfISb31wtPzUAZQ0CgwDMTRHTUC7GA6JLshN5o5uTa14I2g4GTMouA=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="Jillian and Addie Laugh (formerly Babyteeth More) is a sketch comedy and improv channel where teenager Jillian and her sister Addie do all sorts of silly skits, top 50 lists, anything for a laugh!  Whether they are being chased by a chicken or throwing a dummy down the stairs, if it's funny for teenagers and up, they'll do anything for a laugh!",
            category="Family",
            subCategory="kids"
        ),
          Show(
            title="OmoBerry",
            image="https://yt3.googleusercontent.com/a46oJQfE1-63UUZh-KIITWtoGxQw6LgVxdm0ZSl1eLo2lp8_bhPzpI1MxrKYhNXRSPxOY36tfdc=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="With an aim to entertain, educate and empower the next generation of little digital learners, OmoBerry’s curriculum-based episodes and songs cover topics related to STEM learning, cross-cultural experiences, prosocial skill development, character development and self-esteem building. Each OmoBerry musical adventure will definitely deliver and delight!",
            category="learning",
            subCategory="kids"
        ),
        Show(
            title="Gracie's Corner",
            image="https://yt3.googleusercontent.com/Ga0V14KJ_LTOA33hm5tfXLj6MX-u-eYiynl84UV4WKTm8cJ0km1GR-aX4BZYGBLKhZgDMoUmVZY=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="Gracie's Corner is a YouTube channel for kids. It provides a combination of educational, fun, and encouraging songs for children from diverse backgrounds. Come sing and dance with Gracie as she takes a fun imaginary journey with family and friends!",
            category="Music",
            subCategory="kids"
        ),
         Show(
            title="The Tunies",
            image="https://yt3.googleusercontent.com/_k3zkNrY432bku9FOD2YGuKppt-uABVp45cSFVeu3ualBEBv18KB0V0L-xJHFsVkyqmmBQYviw=w1060-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="At Chasin’ Clouds Daycare, the Tunies’ songs are always educational and contemporary, connecting kids, families, and generations through music and imagination!",
            category="Music",
            subCategory="kids"
        ),
        Show(
            title="Cocomelon - Nursery Rhymes",
            image="https://yt3.googleusercontent.com/iJ9wiqW8duyDAuUOubcIq9m5VdL9yMq3N47UAonmmQmbwS0WtSiBOYeRA1NWyXXrzycCRRsP=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="At CoComelon, our primary goal has always been to engage families with entertaining and educational content that makes universally-relatable preschool moments fun. ",
            category="Music",
            subCategory="kids"
        ),
         Show(
            title="How it Should Have Ended",
            image="https://yt3.googleusercontent.com/CtumYH-JDc3ttS23HRP1LTSOQEfAFJQWO4HjGTgEzOWSlFONvGSzLbK8J3fBs7Hp7KhAsZeFYmw=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="A mockumentary on a group of typical office workers.",
            category="Cartoons about MOVIES!!!",
            subCategory="shows"
        ),
        Show(
            title="Video Game Dunkey",
            image="https://yt3.googleusercontent.com/AqGGWESp1RZqdqjxWvZGDToTLDeACFpvRBK60Ic65SuAEpI7R5SQvcARxES9ziEfiiMm-otd=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="Watch my stupid videos.",
            category="Gaming",
            subCategory="shows"
        ),
         Show(
            title="Mama Myers: The Movie",
            image="https://yt3.googleusercontent.com/rqpW2pYdqE_uLlUNzi_sKklIyZZd5Qu5Awqywnf2C2dmW1RmfkYz-yiLHK99dZRS0llOZH6M=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="Welcome to my channel! New content is always in the works 🎬🔥.#TeamDtay.",
            category="Comedy",
            subCategory="movies"
        ),
        Show(
            title="Squid Game Season 2: THE MOVIE! I hope you all enjoyed :).  ",
            image="https://yt3.googleusercontent.com/rqpW2pYdqE_uLlUNzi_sKklIyZZd5Qu5Awqywnf2C2dmW1RmfkYz-yiLHK99dZRS0llOZH6M=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="Welcome to my channel! New content is always in the works 🎬🔥.#TeamDtay.",
            category="Comedy",
            subCategory="movies"
        ),
         Show(
            title="Stalker Followed Our Adopted Daughter Home…",
            image="https://yt3.googleusercontent.com/NoP9U31suFvZoxkTnTR5vuK1JpwYEQw7xeiToODQ23LWHrc0ySdZlW-b6PDRWfSkuZgSRdRB0KY=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="YOU’RE TUNING IN TO THE LITTEST FAMILY ON YOUTUBE!",
            category="Family",
            subCategory="movies"
        ),
        Show(
            title="Our Adopted Daughter Survived A TORNADO🌪️.  ",
            image="https://yt3.googleusercontent.com/NoP9U31suFvZoxkTnTR5vuK1JpwYEQw7xeiToODQ23LWHrc0ySdZlW-b6PDRWfSkuZgSRdRB0KY=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="YOU’RE TUNING IN TO THE LITTEST FAMILY ON YOUTUBE!",
            category="Family",
            subCategory="movies"
        ),
         Show(
            title="THE STALKER IS BACK.. We Have To MOVE!",
            image="https://yt3.googleusercontent.com/NoP9U31suFvZoxkTnTR5vuK1JpwYEQw7xeiToODQ23LWHrc0ySdZlW-b6PDRWfSkuZgSRdRB0KY=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="YOU’RE TUNING IN TO THE LITTEST FAMILY ON YOUTUBE!",
            category="Family",
            subCategory="movies"
        ),
        Show(
            title="Stalker Won’t Leave The Trench Family Alone (THE MOVIE).  ",
            image="https://yt3.googleusercontent.com/NoP9U31suFvZoxkTnTR5vuK1JpwYEQw7xeiToODQ23LWHrc0ySdZlW-b6PDRWfSkuZgSRdRB0KY=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="YOU’RE TUNING IN TO THE LITTEST FAMILY ON YOUTUBE!",
            category="Family",
            subCategory="movies"
        ),
        Show(
            title="Stalker Finally Got Arrested… (THE MOVIE)",
            image="https://yt3.googleusercontent.com/NoP9U31suFvZoxkTnTR5vuK1JpwYEQw7xeiToODQ23LWHrc0ySdZlW-b6PDRWfSkuZgSRdRB0KY=w1138-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj",
            summary="YOU’RE TUNING IN TO THE LITTEST FAMILY ON YOUTUBE!",
            category="Family",
            subCategory="movies"
        ),
    ]

    # Sample Episodes
    episodes = [
        Episode(
            title="Episode 1",
            summary="This video series is about a young girl who loves her younger brother more than her older brother. The older brother ends up getting jealous and doing something that he terribly regrets. Siblings may not sometimes agree and may even fight but it's important that they always remember that they love each other and life is not promised, so enjoy and cherish each other in every moment. Hope you enjoy it.",
            video="https://www.youtube.com/embed/poVl9oPfILs?si=UeKRP5DdBIGPdHXm",
            show_id=1
        ),
        Episode(
            title="Episode 2",
            summary="Sometimes when people are mad they say things that they eventually regret. In this video, Layla's words prove to be very powerful as she wishes for a new family and her wish actually comes true. Layla learns valuable lessons and realizes that her words can't hurt people and even hurt her. Watch what you say to others because your words hold power and you can use them to uplift others or bring them down.",
            video="https://www.youtube.com/embed/wI3qu4Ajijk?si=WGY9pANiFKwnyXlt",
            show_id=1
        ),
        Episode(
            title="Episode 3",
            summary="Siblings CAN'T GET ALONG, They LIVE TO Regret IT! ",
            video="https://www.youtube.com/embed/TsJ6ozwIDrE?si=tI4aIAMEvlhKm4zA",
            show_id=1
        ),
        Episode(
            title="Episode 4",
            summary="NOT GUILTY Kid GOES TO JAIL, What Happens IS SHOCKING",
            video="https://www.youtube.com/embed/eW18OhhcGyU?si=i-99CPD0CliT-E8B",
            show_id=1
        ),
        Episode(
            title="Episode 5",
            summary="Girl DISRESPECTS Her Mom, What Happens Next Is Shocking! ",
            video="https://www.youtube.com/embed/PvJjdM9ISHE?si=Eqxo7tjrCm1wUGah",
            show_id=1
        ),
        Episode(
            title="Episode 6",
            summary="Layla Meets Stranger!",
            video="https://www.youtube.com/embed/duQs_XQyzCY?si=Bql4XYRWEtoTZwIX",
            show_id=1
        ),
        Episode(
            title="Episode 7",
            summary="Layla and Jujuj think it's easy to become adults and that grown-ups should stop complaining. So in this video, the kids turn 21 but things take an interesting turn when they realize being 21 is not as fun as it seems.",
            video="https://www.youtube.com/embed/UwH8Gqt1c_w",
            show_id=1
        ),
        Episode(
            title="Episode 8",
            summary="Something FOLLOWED Us HOME, What Happens IS SHOCKING! ",
            video="https://www.youtube.com/embed/L-v1t11Hw1Y?si=1-49Y4AgWqIZE7Tt",
            show_id=1
        ),
        Episode(
            title="Episode 9",
            summary="Family BUYS EVIL TOY, What Happens NEXT Is Shocking!",
            video="https://www.youtube.com/embed/dos6AKorcwY?si=z0KPtnDhXsbpAjMf",
            show_id=1
        ),
        Episode(
            title="Episode 10",
            summary="Siblings Get KICKED OUT HOUSE For FIGHTING, What Happens Is SHOCKING ",
            video="https://www.youtube.com/embed/sQP1V5duivA?si=N784KEiSsQxyfTu8",
            show_id=1
        ),
        Episode(
            title="Episode 11",
            summary="Mom BIRTHS 3 KIDS IN ONE MONTH, What Happens Next Is SHOCKING ",
            video="https://www.youtube.com/embed/aEKrnSKW82s?si=tgClHX37A0RBk2Mu",
            show_id=1
        ),
        Episode(
            title="Episode 12",
            summary="Rude DAD IS MEAN To FAMILY, He LIVES TO REGRET IT",
            video="https://www.youtube.com/embed/mc5VZbGcDkM?si=ktH3d2yBkmUZyu1x",
            show_id=1
        ),
        Episode(
            title="Episode 13",
            summary="Family BUYS DREAM HOUSE, They Live TO REGRET IT | SKIBIDI TOILET MOVIE",
            video="https://www.youtube.com/embed/fcpm1uXA1X0?si=fo3A5mpdk33C93tn",
            show_id=1
        ),
        Episode(
            title="Episode 14",
            summary="Siblings CAN'T GET ALONG, They LIVE TO Regret IT! ",
             video="https://www.youtube.com/embed/TsJ6ozwIDrE?si=3-zV7AVQFqhXX1at",
            show_id=1
        ),
        Episode(
            title="Episode 15",
            summary="Layla and Juju think it's easy BEING PARENTS ",
            video="https://www.youtube.com/embed/pavs_nF4InQ?si=nS5ZzpM6wUwFqFGQ",
            show_id=1
        ),
        Episode(
            title="Episode 16",
            summary="Parent CHOOSES FAVORITE CHILD, Family Lives To Regret It ",
            video="https://www.youtube.com/embed/g-AD_j1Zdjk?si=tAISr1iVYsye6mT5",
            show_id=1
        ),
        Episode(
            title="Episode 17",
            summary="Dad TURNS INTO GRIMACE, What Happens Is Shocking ",
            video="https://www.youtube.com/embed/Oc-FCHDTsVk?si=amK2-KAePDC2jl2h",
            show_id=1
        ),
        Episode(
            title="Episode 18",
            summary="SNEAKY Girl KEEPS LYING, She Lives To Regret It",
            video="https://www.youtube.com/embed/a2RHMmyZ9Lo?si=8Gii4c5q3cOaBL_8",
            show_id=1
        ),
        Episode(
            title="Episode 19",
            summary="Dad SURPRISES FAMILY WITH NEW MANSION!",
            video="https://www.youtube.com/embed/D2-7GeWF6xY?si=LJA4HqclAtIvI_s-",
            show_id=1
        ),
        Episode(
            title="Episode 20",
            summary="Kids BREAK EVERY RULE On SUMMER VACATION, What THEY DO IS SHOCKING | THE BEAST FAMILY",
            video="https://www.youtube.com/embed/sWgW3CHNgjg?si=6ZBDTK_Jei5uCR8o",
            show_id=1
        ),
        Episode(
            title="Episode 1",
            summary="Brodashaggi decides to rent his room in Davido's Banana Island House to Charles Okocha",
            video="https://www.youtube.com/embed/qF_EEMt1I_g?si=msZVXbRK8VzCUOmw",
            show_id=2
        ),
        Episode(
            title="Episode 2",
            summary="BRODA SHAGGI FINALLY KISSES DJ CUPPIED",
            video="https://www.youtube.com/embed/_AoBvHjAj64?si=XgmWMwe9xhO2V-IJ",
            show_id=2
        ),
        Episode(
            title="Episode 3",
            summary="The Agent by Broda Shaggi",
            video="https://www.youtube.com/embed/p2w4sijMjdw?si=DwBCOOopc01Lhz1l",
            show_id=2
        ),
        Episode(
            title="Episode 4",
            summary="LAST BUS STOP ",
            video="https://www.youtube.com/embed/xoADlE5p_cc?si=jySCdAriDyeFCtHv",
            show_id=2
        ),
        Episode(
            title="Episode 5",
            summary="WHAT ARE FRIENDS FOR",
            video="https://www.youtube.com/embed/Ph5JpIFKVoE?si=3Zd4suBsWhQ4C7Pp",
            show_id=2
        ),
        Episode(
            title="Episode 6",
            summary="AMERICAN DOLLAR VS NIGERIAN NAIRA",
            video="https://www.youtube.com/embed/xGizoRn3lIY?si=9nuE-u9ja_b23MTl",
            show_id=2
        ),
        Episode(
            title="Episode 7",
            summary="DOCTOR WEREY",
            video="https://www.youtube.com/embed/EGA3cvPRaWc?si=zH6hQvCnBumLQpQo",
            show_id=2
        ),
        Episode(
            title="Episode 8",
            summary="YOU GO KPAI",
            video="https://www.youtube.com/embed/p2jj4wB2hMo?si=dg_XmwtS9ttlzzsk",
            show_id=2
        ),
        Episode(
            title="Episode 9",
            summary="MONEY MISS ROAD",
            video="https://www.youtube.com/embed/1paJnorFDqs?si=ageCIUodLirrqOD8",
            show_id=2
        ),
        Episode(
            title="Episode 10",
            summary="YA SHAGGI THE HOODLUM",
            video="https://www.youtube.com/embed/Y2zXMWJAc10?si=MwMHXKbXqYLIateN",
            show_id=2
        ),
        Episode(
            title="Episode 11",
            summary="THE SWITCH",
            video="https://www.youtube.com/embed/77cB6oztFo4?si=2x0EdeKHihU16YHC",
            show_id=2
        ),
        Episode(
            title="Episode 12",
            summary="THE ITALIAN MAN",
            video="https://www.youtube.com/embed/GcEj9TAZQRQ?si=Bf2P-9nG__4uWMlz",
            show_id=2
        ),
        Episode(
            title="Episode 13",
            summary="AGENT OF DARKNESS",
            video="https://www.youtube.com/embed/pHpZyblXLQc?si=QuGHHfZAgtbyLAE3",
            show_id=2
        ),
        Episode(
            title="Episode 14",
            summary="Shaggi The Driver",
            video="https://www.youtube.com/embed/zbu_JM583hU?si=eSIH71_FcnGAkaOU",
            show_id=2
        ),
        Episode(
            title="Episode 15",
            summary="LIFE OF BRODA SHAGGI",
            video="https://www.youtube.com/embed/7ZFE--vjibg?si=uhvq8ihNxdCAGlXc",
            show_id=2
        ),
        Episode(
            title="Episode 16",
            summary="BRODASHAGGI the LONDONER",
            video="https://www.youtube.com/embed/YySsqgJEjuU?si=KJ4bs7E8mHQoUVLF",
            show_id=2
        ),
        Episode(
            title="Episode 17",
            summary="PROPHET SHAGGI (The Matchmaker)",
            video="https://www.youtube.com/embed/Ir0ZbDiiqyg?si=rAbXjWZzhNyG8BA3",
            show_id=2
        ),
        Episode(
            title="Episode 18",
            summary="BE MY VAL",
            video="https://www.youtube.com/embed/NyDIVkItPPo?si=C3SpY5LDWVJaV8TO",
            show_id=2
        ),
        Episode(
            title="Episode 19",
            summary="SHAGGI GYMNASIUM",
            video="https://www.youtube.com/embed/MAsd6Lrxi_Q?si=4NVCM01KLsAtdXPG",
            show_id=2
        ),
        Episode(
            title="Episode 20",
            summary="THE ROBBERY!!! ",
            video="https://www.youtube.com/embed/GxdY1uQI_3U?si=-Wj39yiFT4GbvpHt",
            show_id=2
        ),
        Episode(
            title="Episode 1",
            summary="We Survived A TORNADO 🌪️",
            video="https://www.youtube.com/embed/nSvrodMY9sM?si=B0KZf0Qj0JjHshGa",
            show_id=3
        ),
        Episode(
            title="Episode 2",
            summary="SOMEONE IS LIVING IN OUR ATTIC…",
            video="https://www.youtube.com/embed/dlYiWDyctUo?si=gPD8LXb3ol5safVG",
            show_id=3
        ),
        Episode(
            title="Episode 3",
            summary="Stalker Came To Our Home At 3AM! *cops called*",
            video="https://www.youtube.com/embed/3zTPKXABhTw?si=J3fot3OnVsiXkoSb",
            show_id=3
        ),
        Episode(
            title="Episode 4",
            summary="Stalker Ruined Zakyius LAST Day Of School…",
            video="https://www.youtube.com/embed/IzHe4PyFF_4?si=T6Yt5PGQ0nwiTM9A",
            show_id=3
        ),
        Episode(
            title="Episode 5",
            summary="Our Daughter AND Son Go MISSING…",
            video="https://www.youtube.com/embed/Zvz2DOkw_IM?si=KRT0ui2P43X2YJvO",
            show_id=3
        ),
        Episode(
            title="Episode 6",
            summary="We ADOPTED a GIRL, But ZAKYIUS Gets JEALOUS!",
            video="https://www.youtube.com/embed/Dbtbdt26T1c?si=mc36xXPLkQLQf22S",
            show_id=3
        ),
        Episode(
            title="Episode 7",
            summary="Zakyius FLOODED Our House",
            video="https://www.youtube.com/embed/uBRhZ61kmHw?si=8mdf_a7NNL2dPWtY",
            show_id=3
        ),
        Episode(
            title="Episode 8",
            summary="Somebody KNOCKED Zakyius Tooth Out At School..",
            video="https://www.youtube.com/embed/SxlYBu8Q8eo?si=4TgSyJT0-wDG9ezn",
            show_id=3
        ),
        Episode(
            title="Episode 9",
            summary="Someone DESTROYED Our House…",
            video="https://www.youtube.com/embed/iDVyTNdqFfo?si=OHoga5cgzYcjKxRz",
            show_id=3
        ),
        Episode(
            title="Episode 10",
            summary="I Snuck Into a Water Park OVERNIGHT!",
            video="https://www.youtube.com/embed/ur40arBEU3g?si=77aetUZ2Eb4ezjn2",
            show_id=3
        ),
        Episode(
            title="Episode 11",
            summary="SAYING YES TO OUR SON ZAKYIUS FOR 24 HOURS STRAIGHT!",
            video="https://www.youtube.com/embed/v7C8TBC1YtI?si=4mTkn7kxh4Vi40jF",
            show_id=3
        ),
        Episode(
            title="Episode 12",
            summary="SOMEONE Keeps RINGING The Doorbell At 3AM!",
            video="https://www.youtube.com/embed/zNRljxaVPWg?si=OsZIKxiKV0m9iIcl",
            show_id=3
        ),
        Episode(
            title="Episode 13",
            summary="HOME ALONE Without Parents *Hidden Cameras*",
            video="https://www.youtube.com/embed/Rxo2-OH3aGU?si=NE6Qp0nAosdD4r1O",
            show_id=3
        ),
        Episode(
            title="Episode 14",
            summary="SPYING ON ZAKYIUS! *He Has A Crush*",
            video="https://www.youtube.com/embed/MdB4_FhBA2M?si=XCkdI3O1Mvu5iwlD",
            show_id=3
        ),
        Episode(
            title="Episode 15",
            summary="Stalker RUINED Zakyius Birthday Party Surprise!",
            video="https://www.youtube.com/embed/lOej_SCPFlg?si=xZ2q35DIRY-I_GFb",
            show_id=3
        ),
        Episode(
            title="Episode 16",
            summary="I Locked My PARENTS Out The House For 24 Hours!",
            video="https://www.youtube.com/embed/HUaYHoMleUI?si=sFzizz_8P_EDqwBk",
            show_id=3
        ),
        Episode(
            title="Episode 17",
            summary="We Found A SECRET Door In Our New House…",
            video="https://www.youtube.com/embed/ATNmUaroe2I?si=8G4LzolhMbFffh3X",
            show_id=3
        ),
        Episode(
            title="Episode 18",
            summary="Zakyius Got Into A Fight While At School..",
            video="https://www.youtube.com/embed/BI4E_Biy9RY?si=LeTnXdhCshZJgdYC",
            show_id=3
        ),
        Episode(
            title="Episode 1",
            summary="Us Parody",
            video="https://www.youtube.com/embed/EaAoPNNApIk?si=45HVRgnEH08NqvgE",
            show_id=4
        ),
        Episode(
            title="Episode 2",
            summary="Different Childhood Sleepovers ",
            video="https://www.youtube.com/embed/Bm1syakZ40g?si=TgOQjI3LEkeCCXQ_",
            show_id=4
        ),
        Episode(
            title="Episode 3",
            summary="Different Childhood Sleepovers (pt.2)",
            video="https://www.youtube.com/embed/zD-QndvujJo?si=h3V4E8Qs_8-AAyNw",
            show_id=4
        ),
        Episode(
            title="Episode 4",
            summary="Different Childhood Sleepovers (pt.3)",
            video="https://www.youtube.com/embed/GWdetYBd1bs?si=kkGGIGtqsZa30ebx",
            show_id=4
        ),
        Episode(
            title="Episode 5",
            summary="Different Childhood Sleepovers (pt.4)",
            video="https://www.youtube.com/embed/rzYxIV12eSM?si=QHOZTfgubzbEhnlR",
            show_id=4
        ),
        Episode(
            title="Episode 6",
            summary="Different Childhood Sleepovers (pt.5) | Ep.1",
            video="https://www.youtube.com/embed/q3FXUUV3hWA?si=Iqd2CU2kayW3hj_4",
            show_id=4
        ),
        Episode(
            title="Episode 7",
            summary="Different Childhood Sleepovers (pt.5) | Ep.2",
            video="https://www.youtube.com/embed/EB1gMxx1o2Q?si=rcmkO2MNZh3MZVMz",
            show_id=4
        ),
        Episode(
            title="Episode 8",
            summary="Different Childhood Sleepovers (pt.5) | Ep.3",
            video="https://www.youtube.com/embed/cRsgfzMTops?si=FRqD2yQbf1Luh0k8",
            show_id=4
        ),
        Episode(
            title="Episode 9",
            summary="The Friend That Can Fix Anything ",
            video="https://www.youtube.com/embed/DCBYbKyJj9c?si=QATPC7PItIB36qcP",
            show_id=4
        ),
        Episode(
            title="Episode 10",
            summary="Parents During Quarantine ",
            video="https://www.youtube.com/embed/gkkMknM6Eu4?si=hjsxdsT_XTKuNbQj",
            show_id=4
        ),
        Episode(
            title="Episode 11",
            summary="A Socially Distanced Thanksgiving ",
            video="https://www.youtube.com/embed/v4Gx1vL8k60?si=4sUjwmaojgI0pCaE",
            show_id=4
        ),
        Episode(
            title="Episode 12",
            summary="Different Types of Uber Drivers",
            video="https://www.youtube.com/embed/sNCmo6WSbKU?si=vtMRNAIDtdeP33Qz",
            show_id=4
        ),
        Episode(
            title="Episode 13",
            summary="Different Types of Uber Drivers 2: The Last Ride",
            video="https://www.youtube.com/embed/uCP3Bg3rflk?si=JsWsD3P49srxRjeQ",
            show_id=4
        ),
        Episode(
            title="Episode 14",
            summary="The Super Clean Uber Driver ",
            video="https://www.youtube.com/embed/LxKFRYTnA8c?si=PSAgx8EysmUcl7cc",
            show_id=4
        ),
        Episode(
            title="Episode 15",
            summary="The Quiet Uber Driver",
            video="https://www.youtube.com/embed/wed70uB3aKE?si=QZKOGkHSL8f1scTQ",
            show_id=4
        ),
        Episode(
            title="Episode 16",
            summary="Different Types of Salesmen",
            video="https://www.youtube.com/embed/NOnXrc5ubgw?si=GZyKPbMPYZ96jTd-",
            show_id=4
        ),
        Episode(
            title="Episode 17",
            summary="Kids During Halloween",
            video="https://www.youtube.com/embed/79JWQ8yg6nE?si=OOkPcmJOEqAW3lOR",
            show_id=4
        ),
        Episode(
            title="Episode 18",
            summary="New Year's Resolutions Be Like...",
            video="https://www.youtube.com/embed/C_7kJ5ikwnM?si=yng9VSSMeXJr3JhN",
            show_id=4
        ),
        Episode(
            title="Episode 19",
            summary="'PAIN' - STAY Parody ",
            video="https://www.youtube.com/embed/RIlRS8tKcpM?si=2wzwwj9jaGbPfgUl",
            show_id=4
        ),
        Episode(
            title="Episode 20",
            summary="'Belt Talk' - Knife Talk Parody",
            video="https://www.youtube.com/embed/oLwpyBYbKcI?si=lsXNSN0Nq9DfoY2A",
            show_id=4
        ),
        # Episode(
        #     title="Episode 1",
        #     summary="This video series is about a young girl who loves her younger brother more than her older brother. The older brother ends up getting jealous and doing something that he terribly regrets. Siblings may not sometimes agree and may even fight but it's important that they always remember that they love each other and life is not promised, so enjoy and cherish each other in every moment. Hope you enjoy it.",
        #     video="https://www.youtube.com/embed/poVl9oPfILs?si=UeKRP5DdBIGPdHXm",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 2",
        #     summary="Sometimes when people are mad they say things that they eventually regret. In this video, Layla's words prove to be very powerful as she wishes for a new family and her wish actually comes true. Layla learns valuable lessons and realizes that her words can't hurt people and even hurt her. Watch what you say to others because your words hold power and you can use them to uplift others or bring them down.",
        #     video="https://www.youtube.com/embed/wI3qu4Ajijk?si=WGY9pANiFKwnyXlt",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 3",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 4",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 5",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 6",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 7",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 8",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 9",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 10",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 11",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 12",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 13",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 14",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 15",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 16",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 17",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 18",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 19",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 20",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=5
        # ),
        # Episode(
        #     title="Episode 1",
        #     summary="This video series is about a young girl who loves her younger brother more than her older brother. The older brother ends up getting jealous and doing something that he terribly regrets. Siblings may not sometimes agree and may even fight but it's important that they always remember that they love each other and life is not promised, so enjoy and cherish each other in every moment. Hope you enjoy it.",
        #     video="https://www.youtube.com/embed/poVl9oPfILs?si=UeKRP5DdBIGPdHXm",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 2",
        #     summary="Sometimes when people are mad they say things that they eventually regret. In this video, Layla's words prove to be very powerful as she wishes for a new family and her wish actually comes true. Layla learns valuable lessons and realizes that her words can't hurt people and even hurt her. Watch what you say to others because your words hold power and you can use them to uplift others or bring them down.",
        #     video="https://www.youtube.com/embed/wI3qu4Ajijk?si=WGY9pANiFKwnyXlt",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 3",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 4",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 5",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 6",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 7",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 8",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 9",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 10",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 11",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 12",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 13",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 14",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 15",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 16",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 17",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 18",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 19",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 20",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=6
        # ),
        # Episode(
        #     title="Episode 1",
        #     summary="This video series is about a young girl who loves her younger brother more than her older brother. The older brother ends up getting jealous and doing something that he terribly regrets. Siblings may not sometimes agree and may even fight but it's important that they always remember that they love each other and life is not promised, so enjoy and cherish each other in every moment. Hope you enjoy it.",
        #     video="https://www.youtube.com/embed/poVl9oPfILs?si=UeKRP5DdBIGPdHXm",
        #     show_id=7
        # ),
        # Episode(
        #     title="Episode 2",
        #     summary="Sometimes when people are mad they say things that they eventually regret. In this video, Layla's words prove to be very powerful as she wishes for a new family and her wish actually comes true. Layla learns valuable lessons and realizes that her words can't hurt people and even hurt her. Watch what you say to others because your words hold power and you can use them to uplift others or bring them down.",
        #     video="https://www.youtube.com/embed/wI3qu4Ajijk?si=WGY9pANiFKwnyXlt",
        #     show_id=7
        # ),
        # Episode(
        #     title="Episode 3",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=7
        # ),
        # Episode(
        #     title="Episode 4",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=7
        # ),
        # Episode(
        #     title="Episode 5",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=7
        # ),
        # Episode(
        #     title="Episode 6",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=7
        # ),
        # Episode(
        #     title="Episode 7",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=7
        # ),
        Episode(
            title="Episode 8",
            summary="Six in the Bed | Counting with Gracie’s Corner | Kids Songs + Nursery Rhymes",
            video="https://www.youtube.com/embed/pY98uZBVL-A?si=6_6gudI5_1BMqxAy",
            show_id=7
        ),
        Episode(
            title="Episode 9",
            summary="Three Little Birds | Gracie’s Corner Cover | Kids Songs + Nursery Rhymes",
            video="https://www.youtube.com/embed/IB2FnOv-718?si=PJ5mMzCyznieYHDn",
            show_id=7
        ),
        Episode(
            title="Episode 10",
            summary="Letter H Song | Letter Recognition + Phonics with Gracie’s Corner | Kids Songs + Nursery Rhymes",
            video="https://www.youtube.com/embed/wQ5PtFuf-V4?si=hMlxUCFeM5DwjZ14",
            show_id=7
        ),
        Episode(
            title="Episode 11",
            summary="Play Outside | An Original Song by Gracie’s Corner | Kids Songs + Nursery Rhymes",
            video="https://www.youtube.com/embed/c1LVM6RgRRc?si=p9g6KM3_1XC8GEbU",
            show_id=7
        ),
        Episode(
            title="Episode 12",
            summary="Skidamarink + More Fun and Educational Kids Songs & Nursery Rhymes | Gracie’s Corner Compilation",
            video="https://www.youtube.com/embed/yXjPx21FkVM?si=mz-NJr0-nOqkVbOi",
            show_id=7
        ),
        Episode(
            title="Episode 13",
            summary="Jamming to “Legacy” with Gracie’s Corner | An Original Song from Barbie",
            video="https://www.youtube.com/embed/2D9SRnht27A?si=TlHtAYfPATT-_aIX",
            show_id=7
        ),
        Episode(
            title="Episode 14",
            summary="Three Blind Mice | Gracie’s Corner | Nursery Rhymes + Kids Songs",
            video="https://www.youtube.com/embed/sVqXCZ_Jbpg?si=G4ZMgsSYnikKL7ej",
            show_id=7
        ),
        Episode(
            title="Episode 15",
            summary="Floor is Lava + More Fun and Educational Kids Songs | Gracie’s Corner Compilation",
            video="https://www.youtube.com/embed/Z_FPggafmNs?si=fx0i848VhLBjNMJ7",
            show_id=7
        ),
        Episode(
            title="Episode 16",
            summary="You’re Happy and You Know It (Remix) | Gracie’s Corner | Nursery Rhymes + Kids Songs",
            video="https://www.youtube.com/embed/KqjkZid9Qe8?si=pPFtDkZs6Mm501ov",
            show_id=7
        ),
        Episode(
            title="Episode 17",
            summary="You Are My Sunshine | Gracie’s Corner | Nursery Rhymes + Kids Songs",
            video="https://www.youtube.com/embed/SE-V86_zHhU?si=ukEBdq4oBRK7jr0n",
            show_id=7
        ),
        Episode(
            title="Episode 18",
            summary="Skip to My Lou | Gracie’s Corner | Nursery Rhymes + Kids Songs",
            video="https://www.youtube.com/embed/kO6WZ9fi7d0?si=aWsKl1ehxpThulsY",
            show_id=7
        ),
        Episode(
            title="Episode 19",
            summary="Dinosaur Song + More Fun and Educational Kids Songs | Gracie’s Corner Compilation",
            video="https://www.youtube.com/embed/FXvj5SNGKks?si=UbheXBkmnb27liDl",
            show_id=7
        ),
        Episode(
            title="Episode 20",
            summary="Deck the Halls with Lyrics | Christmas Song for Kids | Gracie’s Corner Nursery Rhymes + Kids Songs",
            video="https://www.youtube.com/embed/-92o9xsgFyc?si=jsaDb9ELY3C2tBuw",
            show_id=7
        ),
        # Episode(
        #     title="Episode 1",
        #     summary="This video series is about a young girl who loves her younger brother more than her older brother. The older brother ends up getting jealous and doing something that he terribly regrets. Siblings may not sometimes agree and may even fight but it's important that they always remember that they love each other and life is not promised, so enjoy and cherish each other in every moment. Hope you enjoy it.",
        #     video="https://www.youtube.com/embed/poVl9oPfILs?si=UeKRP5DdBIGPdHXm",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 2",
        #     summary="Sometimes when people are mad they say things that they eventually regret. In this video, Layla's words prove to be very powerful as she wishes for a new family and her wish actually comes true. Layla learns valuable lessons and realizes that her words can't hurt people and even hurt her. Watch what you say to others because your words hold power and you can use them to uplift others or bring them down.",
        #     video="https://www.youtube.com/embed/wI3qu4Ajijk?si=WGY9pANiFKwnyXlt",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 3",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 4",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 5",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 6",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 7",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 8",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 9",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 10",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 11",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 12",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 13",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 14",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 15",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 16",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 17",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 18",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 19",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 20",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=8
        # ),
        # Episode(
        #     title="Episode 1",
        #     summary="This video series is about a young girl who loves her younger brother more than her older brother. The older brother ends up getting jealous and doing something that he terribly regrets. Siblings may not sometimes agree and may even fight but it's important that they always remember that they love each other and life is not promised, so enjoy and cherish each other in every moment. Hope you enjoy it.",
        #     video="https://www.youtube.com/embed/poVl9oPfILs?si=UeKRP5DdBIGPdHXm",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 2",
        #     summary="Sometimes when people are mad they say things that they eventually regret. In this video, Layla's words prove to be very powerful as she wishes for a new family and her wish actually comes true. Layla learns valuable lessons and realizes that her words can't hurt people and even hurt her. Watch what you say to others because your words hold power and you can use them to uplift others or bring them down.",
        #     video="https://www.youtube.com/embed/wI3qu4Ajijk?si=WGY9pANiFKwnyXlt",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 3",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 4",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 5",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 6",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 7",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 8",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 9",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 10",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 11",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 12",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 13",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 14",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 15",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 16",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 17",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 18",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 19",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 20",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=9
        # ),
        # Episode(
        #     title="Episode 1",
        #     summary="This video series is about a young girl who loves her younger brother more than her older brother. The older brother ends up getting jealous and doing something that he terribly regrets. Siblings may not sometimes agree and may even fight but it's important that they always remember that they love each other and life is not promised, so enjoy and cherish each other in every moment. Hope you enjoy it.",
        #     video="https://www.youtube.com/embed/poVl9oPfILs?si=UeKRP5DdBIGPdHXm",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 2",
        #     summary="Sometimes when people are mad they say things that they eventually regret. In this video, Layla's words prove to be very powerful as she wishes for a new family and her wish actually comes true. Layla learns valuable lessons and realizes that her words can't hurt people and even hurt her. Watch what you say to others because your words hold power and you can use them to uplift others or bring them down.",
        #     video="https://www.youtube.com/embed/wI3qu4Ajijk?si=WGY9pANiFKwnyXlt",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 3",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 4",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 5",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 6",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 7",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 8",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 9",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 10",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 11",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 12",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 13",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 14",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 15",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 16",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 17",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 18",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 19",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 20",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=10
        # ),
        # Episode(
        #     title="Episode 1",
        #     summary="This video series is about a young girl who loves her younger brother more than her older brother. The older brother ends up getting jealous and doing something that he terribly regrets. Siblings may not sometimes agree and may even fight but it's important that they always remember that they love each other and life is not promised, so enjoy and cherish each other in every moment. Hope you enjoy it.",
        #     video="https://www.youtube.com/embed/poVl9oPfILs?si=UeKRP5DdBIGPdHXm",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 2",
        #     summary="Sometimes when people are mad they say things that they eventually regret. In this video, Layla's words prove to be very powerful as she wishes for a new family and her wish actually comes true. Layla learns valuable lessons and realizes that her words can't hurt people and even hurt her. Watch what you say to others because your words hold power and you can use them to uplift others or bring them down.",
        #     video="https://www.youtube.com/embed/wI3qu4Ajijk?si=WGY9pANiFKwnyXlt",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 3",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 4",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 5",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 6",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 7",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 8",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 9",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 10",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 11",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 12",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 13",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 14",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 15",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 16",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 17",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 18",
        #     summary="Woody and Buzz's first adventure.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 19",
        #     summary="Walter White turns to making meth.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),
        # Episode(
        #     title="Episode 20",
        #     summary="Michael's offensive behavior leads to a diversity training.",
        #     video="https://www.youtube.com/embed/UwH8Gqt1c_w",
        #     show_id=11
        # ),

        Episode(
            title="Mama Myers: The Movie",
            summary="It's a Mama Myers Joint!",
            video="https://www.youtube.com/embed/RJ4El2ztDF0?si=vqL-kGypkG3VKGdg",
            show_id=12
        ),
        Episode(
            title="Squid Game Season 2: THE MOVIE!  ",
            summary="I hope you all enjoyed :).",
            video="https://www.youtube.com/embed/uXw0yIGhjrs?si=NBTM9ERaqFlBaMaL",
            show_id=13
        ),
        Episode(
            title="Stalker Followed Our Adopted Daughter Home…",
            summary="The Movie.",
            video="https://www.youtube.com/embed/1cnkbPZiO24?si=ldBOVf6-VLrvT8i3",
            show_id=14
        ),
        Episode(
            title="Our Adopted Daughter Survived A TORNADO🌪️",
            summary="(THE MOVIE)",
            video="https://www.youtube.com/embed/XNqZD-C97Ag?si=OjdwyNnFrvxOdaZI",
            show_id=15
        ),
        Episode(
            title="THE STALKER IS BACK.. We Have To MOVE!",
            summary="(THE MOVIE).",
            video="https://www.youtube.com/embed/0mkK7g2Sxtw?si=K0TArjBfk2Mx-BXT",
            show_id=16
        ),
        Episode(
            title="Stalker Won’t Leave The Trench Family Alone (THE MOVIE)",
            summary="(THE MOVIE).",
            video="https://www.youtube.com/embed/t0s1Nfzfp8o?si=4Z54YU0e3spwtyjq",
            show_id=17
        ),
        Episode(
            title="Stalker Finally Got Arrested… (THE MOVIE)",
            summary="(THE MOVIE)",
            video="https://www.youtube.com/embed/kdbIjA1KHCs?si=NQPUwLfW4XcjWwbS",
            show_id=18
        ),
    ]

    # Add sample data to session
    db.session.add_all(shows)
    db.session.add_all(episodes)

    # Commit session to database
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():  # Make sure your Flask app context is set up
        seed_data()
        print("Database seeded successfully!")