from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import list, fee, cashback, time, safety, apathy, proceses_first, proceses_second, action, rejectbonus, promises, biometry, useless,usefullurl
from config import baml, meetings, fraud, agents, applications, actualisation, facetime, transfers, limits, cardservice
from config import incidents, subscriptions, tinkoffpro, regularphrase, cover, updates, creditcardpromotion, replenishment, withdrawl
from aiogram.types import CallbackQuery
from apps import keyboards as kb
import emoji

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    # await message.answer_sticker('CAACAgIAAxkBAAEMK3ZmTv5_JVjPv9qIT_4AAYhvaXWbdhUAAjFIAAKv6nhKzmH7q-Fadwg1BA')
    await message.answer(text='Обновление 06.06' + emoji.emojize("\u2757"), reply_markup=await kb.update())

    await message.answer('Основной функционал', reply_markup=kb.main)

@router.message(F.text.in_([item["key"] for item in list]))
async def cmd_help(message: Message):
    key = message.text.lower()
    try:
        response = next(item["value"] for item in list if item["key"].lower() == key)
    except StopIteration:
        response = 'Нинаю:('
    await message.answer(response)

@router.callback_query(F.data == 'soft')
async def soft(callback: CallbackQuery):
    new_text = 'Выбери категорию софта'
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_softs())

@router.callback_query(F.data == 'abbr')
async def abbr(callback: CallbackQuery):
    new_text = ('Напиши аббревиатуру *большими* буквами, а я расшифрую\n'
                'Также можешь посмотреть полный список')
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_abbr(), parse_mode="Markdown")

@router.callback_query(F.data == 'back')
async def Back(callback: CallbackQuery):
    new_text = 'Чем могу помочь?'
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client())

@router.callback_query(F.data == 'back2')
async def Back(callback: CallbackQuery):
    new_text = 'Основной функционал'
    await callback.message.edit_text(new_text, reply_markup=kb.main)

@router.callback_query(F.data == 'fullList')
async def FullList(callback: CallbackQuery):
    message_text = '\n'.join(['{} - {}'.format(item['key'], item['value']) for item in list])
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client())

@router.callback_query(F.data == 'cashback')
async def Cashback(callback: CallbackQuery):
    message_text = '\n'.join(cashback)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'fee')
async def Fee(callback: CallbackQuery):
    message_text = '\n'.join(fee)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'time')
async def Time(callback: CallbackQuery):
    message_text = '\n'.join(time)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'safety')
async def Safety(callback: CallbackQuery):
    message_text = '\n'.join(safety)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'apathy')
async def Apathy(callback: CallbackQuery):
    message_text = '\n'.join(apathy)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'baml')
async def Baml(callback: CallbackQuery):
    message_text = '\n'.join(baml)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'meetings')
async def Meetings(callback: CallbackQuery):
    message_text = '\n'.join(meetings)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'fraud')
async def Fraud(callback: CallbackQuery):
    message_text = '\n'.join(fraud)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'agents')
async def Agents(callback: CallbackQuery):
    message_text = '\n'.join(agents)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'applications')
async def Applications(callback: CallbackQuery):
    message_text = '\n'.join(applications)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'actualisation')
async def Actualisation(callback: CallbackQuery):
    message_text = '\n'.join(actualisation)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'facetime')
async def Facetime(callback: CallbackQuery):
    message_text = '\n'.join(facetime)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'incidents')
async def Incidents(callback: CallbackQuery):
    message_text = '\n'.join(incidents)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'subscriptions')
async def Subscriptions(callback: CallbackQuery):
    message_text = '\n'.join(subscriptions)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'tinkoffpro')
async def Tinkoffpro(callback: CallbackQuery):
    message_text = '\n'.join(tinkoffpro)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_back(), parse_mode="Markdown")

@router.callback_query(F.data == 'action')
async def Action(callback: CallbackQuery):
    message_text = '\n'.join(action)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'rejectbonus')
async def Rejectbonus(callback: CallbackQuery):
    message_text = '\n'.join(rejectbonus)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'promises')
async def Promises(callback: CallbackQuery):
    message_text = '\n'.join(promises)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'biometry')
async def Biometry(callback: CallbackQuery):
    message_text = '\n'.join(biometry)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'cover')
async def Cover(callback: CallbackQuery):
    message_text = '\n'.join(cover)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'useless')
async def Useless(callback: CallbackQuery):
    message_text = '\n'.join(useless)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'regularphrase')
async def Regularphrase(callback: CallbackQuery):
    message_text = '\n'.join(regularphrase)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'proc')
async def Proceses(callback: CallbackQuery):
    new_text = 'Выбери одну из частей процедуры'
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_proc(), parse_mode="Markdown")


@router.callback_query(F.data == 'firstproc')
async def Proceses(callback: CallbackQuery):
    message_text = '\n'.join(['- {} - {}'.format(item['key'], item['value']) for item in proceses_first])
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_first_proc(), parse_mode="Markdown")

@router.callback_query(F.data == 'secondproc')
async def Proceses(callback: CallbackQuery):
    message_text = '\n'.join(['- {} - {}'.format(item['key'], item['value']) for item in proceses_second])
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_second_proc(), parse_mode="Markdown")

@router.callback_query(F.data == 'usefullurl')
async def Usefullurl(callback: CallbackQuery):
    message_text = '\n'.join(usefullurl)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown", disable_web_page_preview=True)

@router.callback_query(F.data == 'client')
async def Usefullurl(callback: CallbackQuery):
    new_text = 'Тут все, что нужно для работы с клиентами'
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_client(), parse_mode="Markdown")

@router.callback_query(F.data == 'hide')
async def Usefullurl(callback: CallbackQuery):
    new_text = 'Тут все, что нужно для работы с клиентами'
    if new_text != callback.message.text:
        await callback.message.edit_text(text='Что нового' + emoji.emojize(":red_question_mark:"), reply_markup=await kb.update())

@router.callback_query(F.data == 'updates')
async def Handle_updates(callback: CallbackQuery):
    message_text = '\n'.join(updates)
    if message_text != callback.message.text:
        await callback.message.edit_text(message_text, reply_markup=await kb.hide(), parse_mode="Markdown")

@router.callback_query(F.data == 'pattern')
async def Pattern(callback: CallbackQuery):
    # if message_text != callback.message.text:
    await callback.message.edit_text('Выбери тему шаблона',reply_markup=await kb.inline_patterns(), parse_mode="Markdown")


@router.callback_query(F.data == 'creditcardpromotion')
async def CreditcardProm(callback: CallbackQuery):
    message_text = '\n'.join(creditcardpromotion)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_back(), parse_mode="Markdown")

@router.callback_query(F.data == 'back3')
async def Back3(callback: CallbackQuery):
    new_text = 'Выбери тему шаблона'
    await callback.message.edit_text(new_text, reply_markup=await kb.inline_patterns())

@router.callback_query(F.data == 'transfers')
async def Transfers(callback: CallbackQuery):
    message_text = '\n'.join(transfers)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_back(), parse_mode="Markdown")

@router.callback_query(F.data == 'limits')
async def Limits(callback: CallbackQuery):
    message_text = '\n'.join(limits)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_back(), parse_mode="Markdown")

@router.callback_query(F.data == 'withdrawl')
async def Withdrawl(callback: CallbackQuery):
    message_text = '\n'.join(withdrawl)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_back(), parse_mode="Markdown")

@router.callback_query(F.data == 'replenishment')
async def Replenishment(callback: CallbackQuery):
    message_text = '\n'.join(replenishment)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_back(), parse_mode="Markdown")

@router.callback_query(F.data == 'cardservice')
async def Cardservice(callback: CallbackQuery):
    message_text = '\n'.join(cardservice)
    new_text = message_text
    if new_text != callback.message.text:
        await callback.message.edit_text(new_text, reply_markup=await kb.inline_back(), parse_mode="Markdown")