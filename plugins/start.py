from pyrogram import Client as neural ,filters
from helpers.buttons import *
@neural.on_message( filters.command("start"))
import asyncio

channelUsername1 = '@MOGATEAM'
channelUsername2 = '-1001928933168'

async def start_command(data, chat_id, bot):
    if data == 'start_command':
        await start_command(chat_id, bot)

async def start_command(chat_id, bot):
    try:
        member1, member2 = await asyncio.gather(
            bot.get_chat_member(channelUsername1, chat_id),
            bot.get_chat_member(channelUsername2, chat_id)
        )

        if (member1.status in ['member', 'administrator', 'creator']) and \
           (member2.status in ['member', 'administrator', 'creator']):
            inline_keyboard = {
                'inline_keyboard': [
                    [
                        {'text': "𝗖𝗥𝗘𝗔𝗧𝗘 𝗔 𝗟𝗜𝗡𝗞🖥️", 'callback_data': "crenew"},
                        contact_us_button,
                    ],
                    [
                        {'text': "𝙃𝙀𝙇𝙋☹️👷", 'callback_data': "alhaiwan"},
                    ],
                ],
            }

            message_options = {
                'reply_markup': json.dumps(inline_keyboard),
            }

            await bot.send_message(
                chat_id,
                ('𝗛𝗲𝗹𝗹𝗼 𝗺𝘆 𝗳𝗿𝗶𝗲𝗻𝗱\n\n𝗜 𝗮𝗺 𝗮 𝘀𝗺𝗮𝗿𝘁 𝗯𝗼𝘁 𝗺𝗮𝗱𝗲 𝗯𝘆 @MOGATEAM. 🤖\n\n🔍 '
                 '𝗬𝗼𝘂 𝗰𝗮𝗻 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁 𝘁𝗼 𝘁𝗿𝗮𝗰𝗸 𝗽𝗲𝗼𝗽𝗹𝗲 𝗯𝘆 𝘀𝗲𝗻𝗱𝗶𝗻𝗴 𝘁𝗵𝗲𝗺 𝗮 𝘀𝗶𝗺𝗽𝗲 𝗹𝗶𝗻𝗸.\n\n'
                 '𝗜𝘁 𝗰𝗮𝗻 𝗰𝗼𝗹𝗹𝗲𝗰𝘁 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗹𝗶𝗸𝗲:-\n\n➊ 𝙇𝙤𝙘𝙖𝙩𝙞𝙤𝙣📍\n➋ 𝘿𝙚𝙫𝙞𝙘𝙚 𝘿𝙚𝙩𝙖𝙞𝙡𝙨📱\n'
                 '➌ 𝘾𝙖𝙢𝙚𝙧𝙖 𝙎𝙣𝙖𝙥𝙨𝙝𝙤𝙩𝙨 📸.\n\n𝗖𝗹𝗶𝗰𝗸 "𝗛𝗘𝗟𝗣" 𝗳𝗼𝗿 𝗺𝗼𝗿𝗲 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 🆘'),
                message_options
            )
        else:
            message_options = {
                'reply_markup': json.dumps({
                    'inline_keyboard': [
                        [join_channel1_button, join_channel2_button],
                        [check_joined_button, contact_us_button],
                    ],
                }),
            }

    except Exception as e:
        print("Error:", e)
