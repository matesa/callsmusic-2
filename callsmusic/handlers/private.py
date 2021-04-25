# Calls Music 2 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Merhaba🥳 {message.from_user.first_name}!
Ben GoodVibes🎧 Bot, Telegram gruplarınızda müzik çalmanıza izin veren bir botum. 
Sahibim @Poyraz2103 
Hakkımda daha fazla şey öğrenmek için aşağıdaki düğmeleri kullanın.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Komutlar", url="https://t.me/Fmsarkilar",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Grup", url="https://t.me/Fmsarkilar"
                    ),
                    InlineKeyboardButton(
                      "📢Support Kanal", url="https://t.me/Fmsarkilar"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥Support Grup", url="https://t.me/Fmsarkilar"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💻 YouTube videosu aramak istiyor musunuz??",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Evet", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Hayır ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
