from telethon.sync import TelegramClient, events

async with TelegramClient("@Vijay_Vigneshh", api_id = 10830442, api_hash = "9b34b23bf7eb7ae6b53416c274700083") as client:

    @client.on(events.NewMessage(pattern='(?i).*Hello'))
    async def handler(event):
        await event.reply('Hey!')

    await client.run_until_disconnected()
