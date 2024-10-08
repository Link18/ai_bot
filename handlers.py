from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
import ai
from aiogram.fsm.context import FSMContext
import keybords


router = Router()

class Questions(StatesGroup):
    chatBot=State()
    flBpot=State()
    image_gen=State()
    gpt=State()

@router.message(CommandStart())
async def start(messege:Message):
    await messege.answer(text="Добро пожпловать в демонстрационный AI бот!\n Он работает с моделями Chat_GPT и Mistral AI \n Если хотите заказать подобного бота или любого другого, то переходите на мою страницу\n Kwork:https://kwork.ru/user/_arteam_ ",
                         reply_markup=keybords.start_menu)
    
@router.message(F.text == 'чат бот')
async def chat(messege:Message):
    await messege.answer(text="Turn AI model",reply_markup=keybords.chat_menu)
    
#images
    
@router.message(F.text == 'создать картинку')
async def image(m:Message,state:FSMContext):
    await m.answer(text='Прошу прощение но Chat_GPT сейчас не доступен: количество токенов 0')
    
@router.message(Questions.image_gen)
async def ansver(messege:Message,state:FSMContext):
    if messege.text == 'стоп':
        await state.clear()
        await messege.answer(text="вы закончили диалог",reply_markup=keybords.start_menu)
    else:
        response=await ai.gpt_image(messege.text)
        await messege.answer_photo(photo=response)
    
    
# ai mistral

@router.callback_query(F.data == 'mistral')
async def generate(cb:CallbackQuery):
    await cb.message.edit_text(text='выберите режим',reply_markup=keybords.mistral_keybord)
    
    
@router.callback_query(F.data == 'chat-bot')
async def generate(cb:CallbackQuery,state:FSMContext):
    await cb.message.answer(text='введите запрос',reply_markup=keybords.stop_button)
    await state.set_state(Questions.chatBot)
    
@router.message(Questions.chatBot)
async def ansver(messege:Message,state:FSMContext):
    if messege.text == 'стоп':
        await state.clear()
        await messege.answer(text="вы закончили диалог",reply_markup=keybords.start_menu)
    else:
        response=await ai.mistral_ai(messege.text)
        await messege.answer(text=response.choices[0].message.content)


#ai_gpt

@router.callback_query(F.data == 'openai')
async def generate(cb:CallbackQuery,state:FSMContext):
    await cb.message.answer(text='Прошу прощение но Chat_GPT сейчас не доступен: количество токенов 0')
    
    
@router.message(Questions.gpt)
async def ansver(messege:Message,state:FSMContext):
    if messege.text == 'стоп':
        await state.clear()
        await messege.answer(text="вы закончили диалог",reply_markup=keybords.start_menu)
    else:
        response=await ai.gpt(messege.text)
        await messege.answer(text=response.choices[0].message.content)

    
# @router.message(Questions.quest,F.text == 'стоп')  
# async def stop(messege:Message,state:FSMContext):
#     await messege.answer(text='диалог закончен')
#     await state.clear()
    
    
# @router.message(F.text)
# async def state_ans(messege:Message):
#     await messege.answer("WEIT") 
    
# @router.message(F.text)
# async def generate(messege:Message,state:FSMContext):
#     await state.set_state(generate.text)
#     response=await gpt(messege.text)
#     await messege.answer(response.choices[0].message.content)
#     await state.clear()