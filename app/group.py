from app import router
from aiogram import F, Bot
from aiogram.types import CallbackQuery, Message
from app.database.models import User, Group
import app.keyboards as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from config import TOKEN

@router.callback_query(F.data == 'btn_group')