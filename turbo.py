import asyncio 
import getpass
import json

import httpx
from colorama import Fore, init

init(autoreset=True)

async def try_vanity(vanity: str, guild: str, token: str, session: httpx.AsyncClient):
    while True:
        resp = await session.patch(
            f"https://discord.com/api/v9/guilds/{guild}/vanity-url",
            data=json.dumps({"code": vanity.casefold()}),
            headers={"Content-Type": "application/json", "Authorization": token},
            
        )
        if resp.json().get("code") == vanity.casefold():
            return print(f"{Fore.LIGHTGREEN_EX}-> {resp.text}")
        else:
            print(f"{Fore.RED}{resp.text}")


async def main():
    token = getpass.getpass("Auth Token -> ").strip()
    vanity = input("Target Vanity -> ").strip()
    guild = input("Recipient Guild ID -> ").strip()
    async with httpx.AsyncClient() as session:
        await try_vanity(vanity, guild, token, session)
        
asyncio.run(main())
