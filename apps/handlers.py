from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import emoji

from config import (
    list,
    fee,
    cashback,
    time,
    safety,
    apathy,
    proceses_first,
    proceses_second,
    action,
    rejectbonus,
    promises,
    biometry,
    useless,
    usefullurl,
)
from config import (
    baml,
    meetings,
    fraud,
    agents,
    applications,
    actualisation,
    facetime,
    transfers,
    limits,
    cardservice,
)
from config import (
    incidents,
    subscriptions,
    pro_subscription,
    regularphrase,
    cover,
    updates,
    creditcardpromotion,
    replenishment,
    withdrawl,
)
from apps import keyboards as kb

router = Router()

CONTENT_MAP = {
    "fee": {"data": fee, "back_btn": "inline_client"},
    "cashback": {"data": cashback, "back_btn": "inline_client"},
    "time": {"data": time, "back_btn": "inline_client"},
    "safety": {"data": safety, "back_btn": "inline_client"},
    "apathy": {"data": apathy, "back_btn": "inline_client"},
    "baml": {"data": baml, "back_btn": "inline_client"},
    "meetings": {"data": meetings, "back_btn": "inline_client"},
    "fraud": {"data": fraud, "back_btn": "inline_client"},
    "agents": {"data": agents, "back_btn": "inline_client"},
    "applications": {"data": applications, "back_btn": "inline_client"},
    "actualisation": {"data": actualisation, "back_btn": "inline_client"},
    "facetime": {"data": facetime, "back_btn": "inline_client"},
    "incidents": {"data": incidents, "back_btn": "inline_client"},
    "subscriptions": {"data": subscriptions, "back_btn": "inline_client"},
    "action": {"data": action, "back_btn": "inline_client"},
    "rejectbonus": {"data": rejectbonus, "back_btn": "inline_client"},
    "promises": {"data": promises, "back_btn": "inline_client"},
    "biometry": {"data": biometry, "back_btn": "inline_client"},
    "cover": {"data": cover, "back_btn": "inline_client"},
    "useless": {"data": useless, "back_btn": "inline_client"},
    "regularphrase": {"data": regularphrase, "back_btn": "inline_client"},
    "usefullurl": {"data": usefullurl, "back_btn": "inline_client"},
    "pro_subscription": {"data": pro_subscription, "back_btn": "inline_back"},
    "creditcardpromotion": {"data": creditcardpromotion, "back_btn": "inline_back"},
    "transfers": {"data": transfers, "back_btn": "inline_back"},
    "limits": {"data": limits, "back_btn": "inline_back"},
    "withdrawl": {"data": withdrawl, "back_btn": "inline_back"},
    "replenishment": {"data": replenishment, "back_btn": "inline_back"},
    "cardservice": {"data": cardservice, "back_btn": "inline_back"},
}


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        text="Обновление 06.06" + emoji.emojize("❗"), reply_markup=await kb.update()
    )
    await message.answer("Основной функционал", reply_markup=kb.main)


@router.message(F.text.in_([item["key"] for item in list]))
async def cmd_help(message: Message):
    key = message.text.lower()
    response = next(
        (item["value"] for item in list if item["key"].lower() == key), "Нинаю:("
    )
    await message.answer(response)


@router.callback_query(F.data.in_(CONTENT_MAP.keys()))
async def show_content(callback: CallbackQuery):
    action_data = CONTENT_MAP.get(callback.data)
    if not action_data:
        return
    raw_data = action_data["data"]
    if isinstance(raw_data[0], dict):
        message_text = "\n".join(
            ["- {} - {}".format(item["key"], item["value"]) for item in raw_data]
        )
    else:
        message_text = "\n".join(raw_data)
    try:
        await callback.message.edit_text(
            text=message_text,
            reply_markup=await getattr(kb, action_data["back_btn"])(),
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )
    except Exception:
        pass


@router.callback_query(F.data == "soft")
async def soft(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выбери категорию софта", reply_markup=await kb.inline_softs()
    )


@router.callback_query(F.data == "abbr")
async def abbr(callback: CallbackQuery):
    new_text = "Напиши аббревиатуру *большими* буквами, а я расшифрую\nТакже можешь посмотреть полный список"
    await callback.message.edit_text(new_text, reply_markup=await kb.inline_abbr())


@router.callback_query(F.data == "fullList")
async def full_list(callback: CallbackQuery):
    message_text = "\n".join(
        ["{} - {}".format(item["key"], item["value"]) for item in list]
    )
    await callback.message.edit_text(
        message_text, reply_markup=await kb.inline_client()
    )


@router.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    await callback.message.edit_text(
        "Чем могу помочь?", reply_markup=await kb.inline_client()
    )


@router.callback_query(F.data == "back2")
async def back2(callback: CallbackQuery):
    await callback.message.edit_text("Основной функционал", reply_markup=kb.main)


@router.callback_query(F.data == "back3")
async def back3(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выбери тему шаблона", reply_markup=await kb.inline_patterns()
    )


@router.callback_query(F.data == "client")
async def client(callback: CallbackQuery):
    await callback.message.edit_text(
        "Тут все, что нужно для работы с клиентами",
        reply_markup=await kb.inline_client(),
        parse_mode="Markdown",
    )


@router.callback_query(F.data == "hide")
async def hide(callback: CallbackQuery):
    await callback.message.edit_text(
        text="Что нового" + emoji.emojize(":red_question_mark:"),
        reply_markup=await kb.update(),
    )


@router.callback_query(F.data == "updates")
async def handle_updates(callback: CallbackQuery):
    message_text = "\n".join(updates)
    await callback.message.edit_text(
        message_text, reply_markup=await kb.hide(), parse_mode="Markdown"
    )


@router.callback_query(F.data == "pattern")
async def pattern(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выбери тему шаблона",
        reply_markup=await kb.inline_patterns(),
        parse_mode="Markdown",
    )


@router.callback_query(F.data == "proc")
async def proceses(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выбери одну из частей процедуры",
        reply_markup=await kb.inline_proc(),
        parse_mode="Markdown",
    )


@router.callback_query(F.data == "firstproc")
async def first_proc(callback: CallbackQuery):
    message_text = "\n".join(
        ["- {} - {}".format(item["key"], item["value"]) for item in proceses_first]
    )
    await callback.message.edit_text(
        message_text, reply_markup=await kb.inline_first_proc(), parse_mode="Markdown"
    )


@router.callback_query(F.data == "secondproc")
async def second_proc(callback: CallbackQuery):
    message_text = "\n".join(
        ["- {} - {}".format(item["key"], item["value"]) for item in proceses_second]
    )
    await callback.message.edit_text(
        message_text, reply_markup=await kb.inline_second_proc(), parse_mode="Markdown"
    )
