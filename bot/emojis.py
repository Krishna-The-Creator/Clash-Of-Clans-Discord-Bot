import asyncio

import discord

from data.config import Config
from data.secure_folder import Login
from data.useful import Ids, Useful


Emojis = {}


class EmojisBot(discord.Client):
    emojis = {}
    emoji_connected = asyncio.Event()

    def __init__(self):
        super().__init__(intents=discord.Intents.default())

    async def on_ready(self):
        emojis = {}

        # ----- COC TH-BH-Leagues -----
        guild = self.get_guild(Ids["Emojis_coc_th_bh_leagues_server"])
        th_emojis = {}
        for i in range(1, Useful["max_th_lvl"] + 1):
            th_emojis[i] = discord.utils.get(guild.emojis, name=f"TH_{i:02d}")  # Name from TH_01 to TH_14
        emojis["Th_emojis"] = th_emojis

        bh_emojis = {}
        for i in range(1, Useful["max_bh_lvl"] + 1):
            bh_emojis[i] = discord.utils.get(guild.emojis, name=f"BH_{i:02d}")  # Name from BH_01 to BH_09
        emojis["Bh_emojis"] = bh_emojis

        league_emojis = {}
        for league in Useful["league_trophies"].keys():
            emoji = discord.utils.get(guild.emojis, name=league.replace(" ", "_").lower())
            league_emojis[league] = emoji
        emojis["League_emojis"] = league_emojis

        emojis["Barbarian_king"] = discord.utils.get(guild.emojis, name="barbarian_king")
        emojis["Archer_queen"] = discord.utils.get(guild.emojis, name="archer_queen")
        emojis["Grand_warden"] = discord.utils.get(guild.emojis, name="grand_warden")
        emojis["Royal_champion"] = discord.utils.get(guild.emojis, name="royal_champion")
        emojis["Battle_machine"] = discord.utils.get(guild.emojis, name="battle_machine")

        # ----- COC Troops-Spell -----
        guild = self.get_guild(Ids["Emojis_coc_troops_spells_server"])
        emojis["Troop"] = discord.utils.get(guild.emojis, name="TE1")
        troops_emojis = {}
        emoji_to_name = {"TE1": "Barbarian", "TE2": "Archer", "TE3": "Giant", "TE4": "Goblin", "TE5": "Wall Breaker", "TE6": "Balloon", "TE7": "Wizard", "TE8": "Healer", "TE9": "Dragon", "TE10": "P.E.K.K.A", "TE11": "Baby Dragon", "TE12": "Miner", "TE13": "Electro Dragon", "TE14": "Yeti", "TE15": "Dragon Rider", "TD1": "Minion", "TD2": "Hog Rider", "TD3": "Valkyrie", "TD4": "Golem", "TD5": "Witch", "TD6": "Lava Hound", "TD7": "Bowler", "TD8": "Ice Golem", "TD9": "Headhunter", "SE1": "Lightning Spell", "SE2": "Healing Spell", "SE3": "Rage Spell", "SE4": "Jump Spell", "SE5": "Freeze Spell", "SE6": "Clone Spell", "SE7": "Invisibility Spell", "SD1": "Poison Spell", "SD2": "Earthquake Spell", "SD3": "Haste Spell", "SD4": "Skeleton Spell", "SD5": "Bat Spell", "M1": "Wall Wrecker", "M2": "Battle Blimp", "M3": "Stone Slammer", "M4": "Siege Barracks", "M5": "Log Launcher", "M6": "Flame Flinger", "P1": "L.A.S.S.I", "P2": "Electro Owl", "P3": "Mighty Yak", "P4": "Unicorn"}
        for emoji in guild.emojis:
            troops_emojis[emoji_to_name[emoji.name]] = emoji
        emojis["Troops_emojis"] = troops_emojis

        # ----- COC War Leagues -----
        guild = self.get_guild(Ids["Emojis_coc_war_leagues"])
        war_leagues_emojis = {}
        name_to_emoji_name = {"Unranked": "unranked", "Bronze League III": "bronze_league_III", "Bronze League II": "bronze_league_II", "Bronze League I": "bronze_league_I", "Silver League III": "silver_league_III", "Silver League II": "silver_league_II", "Silver League I": "silver_league_I", "Gold League III": "gold_league_III", "Gold League II": "gold_league_II", "Gold League I": "gold_league_I", "Crystal League III": "crystal_league_III", "Crystal League II": "crystal_league_II", "Crystal League I": "crystal_league_I", "Master League III": "master_league_III", "Master League II": "master_league_II", "Master League I": "master_league_I", "Champion League III": "champion_league_III", "Champion League II": "champion_league_II", "Champion League I": "champion_league_I"}
        for name, emoji_name in name_to_emoji_name.items():
            war_leagues_emojis[name] = discord.utils.get(guild.emojis, name=emoji_name)
        emojis["War_leagues"] = war_leagues_emojis

        # ----- COC Main -----
        guild = self.get_guild(Ids["Emojis_coc_main_server"])
        emojis["Exp"] = discord.utils.get(guild.emojis, name="exp")
        emojis["Star"] = discord.utils.get(guild.emojis, name="star")
        emojis["Star_empty"] = discord.utils.get(guild.emojis, name="star_empty")  # NOT USED
        emojis["Star_old"] = discord.utils.get(guild.emojis, name="star_old")  # NOT USED
        emojis["Star_success"] = discord.utils.get(guild.emojis, name="star_success")
        emojis["Trophy"] = discord.utils.get(guild.emojis, name="trophy")
        emojis["Versus_trophy"] = discord.utils.get(guild.emojis, name="versus_trophy")

        # ----- Support Server -----
        guild = self.get_guild(Ids["Support_server"])
        emojis["Bot"] = discord.utils.get(guild.emojis, name="bot")  # NOT USED
        emojis["Bot_certified"] = discord.utils.get(guild.emojis, name="bot_certified")  # NOT USED
        emojis["Clash_info"] = discord.utils.get(guild.emojis, name="ClashINFO")
        emojis["Github"] = discord.utils.get(guild.emojis, name="github")
        emojis["Yes"] = discord.utils.get(guild.emojis, name="yes")
        emojis["No"] = discord.utils.get(guild.emojis, name="no")

        # ----- Discord Main -----
        guild = self.get_guild(Ids["Emojis_discord_main_server"])
        emojis["Add_reaction"] = discord.utils.get(guild.emojis, name="add_reaction")  # NOT USED
        emojis["Channel"] = discord.utils.get(guild.emojis, name="channel")  # NOT USED
        emojis["Channel_locked"] = discord.utils.get(guild.emojis, name="channel_locked")  # NOT USED
        emojis["Channel_nsfw"] = discord.utils.get(guild.emojis, name="channel_nsfw")  # NOT USED
        emojis["Cursor"] = discord.utils.get(guild.emojis, name="cursor")  # NOT USED
        emojis["Deafened"] = discord.utils.get(guild.emojis, name="deafened")  # NOT USED
        emojis["Discord"] = discord.utils.get(guild.emojis, name="discord")
        emojis["Discord_white"] = discord.utils.get(guild.emojis, name="discord_white")
        emojis["Emoji_ghost"] = discord.utils.get(guild.emojis, name="emoji_ghost")  # NOT USED
        emojis["Invite"] = discord.utils.get(guild.emojis, name="invite")
        emojis["Member"] = discord.utils.get(guild.emojis, name="member")
        emojis["Members"] = discord.utils.get(guild.emojis, name="members")
        emojis["Mention"] = discord.utils.get(guild.emojis, name="mention")  # NOT USED
        emojis["Muted"] = discord.utils.get(guild.emojis, name="muted")  # NOT USED
        emojis["News"] = discord.utils.get(guild.emojis, name="news")
        emojis["Nitro"] = discord.utils.get(guild.emojis, name="nitro")  # NOT USED
        emojis["Pin"] = discord.utils.get(guild.emojis, name="pin")
        emojis["Pin_unread"] = discord.utils.get(guild.emojis, name="pin_unread")  # NOT USED
        emojis["Settings"] = discord.utils.get(guild.emojis, name="settings")
        emojis["Slowmode"] = discord.utils.get(guild.emojis, name="slowmode")  # NOT USED
        emojis["Stream"] = discord.utils.get(guild.emojis, name="stream")  # NOT USED
        emojis["Store_tag"] = discord.utils.get(guild.emojis, name="store_tag")  # NOT USED
        emojis["Typing"] = discord.utils.get(guild.emojis, name="typing")  # NOT USED
        emojis["Typing_status"] = discord.utils.get(guild.emojis, name="typing_status")  # NOT USED
        emojis["Undeafened"] = discord.utils.get(guild.emojis, name="undeafened")  # NOT USED
        emojis["Unmuted"] = discord.utils.get(guild.emojis, name="unmuted")  # NOT USED
        emojis["Update"] = discord.utils.get(guild.emojis, name="update")  # NOT USED
        emojis["Updating"] = discord.utils.get(guild.emojis, name="updating")  # NOT USED
        emojis["Voice"] = discord.utils.get(guild.emojis, name="voice")  # NOT USED
        emojis["Voice_locked"] = discord.utils.get(guild.emojis, name="voice_locked")  # NOT USED

        # ----- Discord Badges -----
        guild = self.get_guild(Ids["Emojis_discord_badges_server"])
        emojis["Balance"] = discord.utils.get(guild.emojis, name="balance")  # NOT USED
        emojis["Boost"] = discord.utils.get(guild.emojis, name="boost")  # NOT USED
        emojis["Bravery"] = discord.utils.get(guild.emojis, name="bravery")  # NOT USED
        emojis["Brilliance"] = discord.utils.get(guild.emojis, name="brilliance")  # NOT USED
        emojis["Bug_hunter_lvl1"] = discord.utils.get(guild.emojis, name="bug_hunter_lvl_1")  # NOT USED
        emojis["Bug_hunter_lvl_2"] = discord.utils.get(guild.emojis, name="bug_hunter_lvl_2")  # NOT USED
        emojis["Developer"] = discord.utils.get(guild.emojis, name="developer")  # NOT USED
        emojis["Do_not_disturb"] = discord.utils.get(guild.emojis, name="do_not_disturb")  # NOT USED
        emojis["Early_supporter"] = discord.utils.get(guild.emojis, name="early_supporter")  # NOT USED
        emojis["Idle"] = discord.utils.get(guild.emojis, name="idle")  # NOT USED
        emojis["Hypesquad"] = discord.utils.get(guild.emojis, name="hypesquad")  # NOT USED
        emojis["Hypesquad_events"] = discord.utils.get(guild.emojis, name="hypesquad_events")  # NOT USED
        emojis["Info"] = discord.utils.get(guild.emojis, name="info")  # NOT USED
        emojis["Offline"] = discord.utils.get(guild.emojis, name="offline")  # NOT USED
        emojis["Online"] = discord.utils.get(guild.emojis, name="online")  # NOT USED
        emojis["Owner"] = discord.utils.get(guild.emojis, name="owner")
        emojis["Partner"] = discord.utils.get(guild.emojis, name="partner")  # NOT USED
        emojis["Streaming"] = discord.utils.get(guild.emojis, name="streaming")  # NOT USED

        # ----- General Icons -----
        guild = self.get_guild(Ids["Emojis_general_icons_server"])

        fr_emoji = discord.utils.get(guild.emojis, name="fr")  # NOT USED
        us_uk_emoji = discord.utils.get(guild.emojis, name="us_uk")  # NOT USED
        emojis["Languages_emojis"] = {"English": us_uk_emoji, "French": fr_emoji}  # NOT USED

        emojis["Calendar"] = discord.utils.get(guild.emojis, name="calendar")
        emojis["Delete"] = discord.utils.get(guild.emojis, name="delete")
        emojis["Delete_grey"] = discord.utils.get(guild.emojis, name="delete_grey")
        emojis["Description"] = discord.utils.get(guild.emojis, name="description")
        emojis["Donations"] = discord.utils.get(guild.emojis, name="donations")
        emojis["Id"] = discord.utils.get(guild.emojis, name="id")
        emojis["Language"] = discord.utils.get(guild.emojis, name="language")
        emojis["Received"] = discord.utils.get(guild.emojis, name="received")

        self.emojis = emojis
        await self.close()

    async def on_disconnect(self):
        self.emoji_connected.set()


client = EmojisBot()
loop = asyncio.get_event_loop()


async def login():
    if Config["main_bot"]:
        discord_token = Login["discord"]["main"]
    else:
        discord_token = Login["discord"]["beta"]

    await client.login(discord_token)


loop.run_until_complete(login())


async def wrapped_connect():
    await client.connect()
    global Emojis
    Emojis = client.emojis


loop.create_task(wrapped_connect())


async def check_close():
    futures = [client.emoji_connected.wait()]
    await asyncio.wait(futures)


loop.run_until_complete(check_close())
