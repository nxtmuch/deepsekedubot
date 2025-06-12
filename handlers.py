from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


from generate import ai_generate

CHANNEL_ID = "-1002624384393"

router = Router()


class Gen(StatesGroup):
    wait = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Я твой личный наставник, готовый помочь тебе лучше разобраться в школьных предметах! Напиши мне предмет и тему, которую ты не понимаешь, и я постараюсь помочь тебе!')


@router.message(Command('about'))
async def cmd_abot(message: Message):
    await message.answer('Данный чат-бот разработал студент 2-го курса магистратуры ШФ ИвГУ Борзов Иван. Чат-бот работает на модели ИИ "Deepseek V3", и следует заранее прописанному промпту (запросу), цель которого - оказывать поддержку в принятии решений. Все запросы пользователей сохраняются!!!')


@router.message()
async def generating(message: Message, state: FSMContext):
    log_message = await message.bot.send_message(chat_id=CHANNEL_ID, text=f"User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) said:\n\n{message.text}", parse_mode='Markdown')
    await state.set_state(Gen.wait)
    response = await ai_generate(message.text)
    await log_message.reply(text=f"Bot answered:\n\n{response}", parse_mode='Markdown')
    await message.answer(response, parse_mode='Markdown')
    await state.clear()
