import asyncio

import aiogram.exceptions
from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from random import *


TOKEN = "7554503970:AAE0H7-FocGi6KnR5Cf9INprp5WE0jDZF4c"
channel_name = "@"

bot = Bot(token=TOKEN)
dp = Dispatcher()

user_data = {}

@dp.message()
async def handle_text(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == '/start':
        await start(message)
    elif 'holat' not in user_data[user_id]:
        await shaharlar(message)
    elif 'shahar' not in user_data[user_id]:
        await menu(message)
    elif message.text == '🛍 Buyurtma berish':
        await buyurtma(message)
    elif message.text == '⬅️ Ortga':
        await menu(message)
    elif message.text == '📖 Buyurtmalar tarixi':
        await tarix(message)
    elif message.text == '🔥 Aksiya':
        await aksiya(message)
    elif message.text == "🙋🏻‍♂️ Jamoamizga qo'shiling":
        await jamoa(message)
    elif message.text == "⚙️Sozlash ℹ️ Ma'lumotlar":
        await sozlama(message)
    elif message.text == '☎️ Les Ailes bilan aloqa':
        await aloqa(message)
    elif message.text == '🏃 Olib ketish':
        await olish(message)
    elif message.text == '🔙Ortga':
        await buyurtma(message)
    elif message.text == '🚙 Yetkazib berish':
        await yetkazish(message)
    elif message.text == "Ismni o'zgartirish":
        await ism(message)
    elif message.text == '👈Ortga':
        await sozlama(message)
    elif message.text == "📱 Raqamni o'zgartirish":
        await raqam(message)
    elif message.text == '👈Ortga':
        await sozlama(message)
    elif message.text == "🏙 Shaharni o'zgartirish":
        await shaharlar(message)
    elif message.text == 'Toshkent':
        await tanlash(message)
    elif message.text == 'Andijon':
        await tanlash(message)
    elif message.text == 'Samarqand':
        await tanlash(message)
    elif message.text == "Farg'ona":
        await tanlash(message)
    elif message.text == 'Buxoro':
        await tanlash(message)
    elif message.text == "Marg'ilon":
        await tanlash(message)
    elif message.text == 'Nukus':
        await tanlash(message)
    elif message.text == 'Xorazm':
        await tanlash(message)
    elif message.text == 'Chirchiq':
        await tanlash(message)
    elif message.text == "Qo'qon":
        await tanlash(message)
    elif message.text == '💬 Biz bilan aloqaga chiqing':
        await boglanish(message)
    elif message.text == "✍️ Fikr bildirish":
        await fikr(message)
        await message.answer("Tanlovingiz uchun rahmat va biz ishimizni 5 balli tizimda baholashingizdan mamnun bo'lamiz.")
    elif message.text == "Bu yerda buyurtma berish 🌐":
        await shu_yerda(message)
    elif message.text == "Filialni tanlang":
        await filial(message)
    elif message.text == "ℹ️ Filallar haqida ma'lumotlar":
        await filial_malumot(message)
    elif message.text == "📄 Ommaviy taklif":
        await taklif(message)
    elif message.text == "🇺🇿 Tilni o'zgartirish":
        await lang(message)
    elif message.text == "🇺🇿 O'zbekcha":
        await message.answer("✅ Tayyor")
        await sozlama(message)
    elif message.text == "🇷🇺 Русский":
        await message.answer("✅ Tayyor")
        await sozlama(message)
    elif message.text == "🇺🇸 English":
        await message.answer("✅ Tayyor")
        await sozlama(message)
    elif message.text in list:
        await lokatsiya_tanlash(message)
    elif message.text == "↖️Ortga":
        await filial(message)
    elif message.text == "↗️Ortga":
        await olish(message)
    elif message.text == "🍱 Setlar" or message.text=="👈🏻Ortga":
        await set(message)
    elif message.text == "⬆️Ortga":
        await back(message)
    elif message.text == "🍗 Tovuq":
        await tovuq(message)
    elif message.text == "🍟 Sneklar":
        await snek(message)
    elif message.text == "🌯 Lesterlar":
        await lester(message)
    elif message.text == "🍔 Burgerlar":
        await burger(message)
    elif message.text == '🌭 Longerlar/Hot-dog':
        await longer_hotdog(message)
    elif message.text == "🥤 Ichimliklar":
        await ichimlik(message)
    elif message.text == "🥗 Salatlar":
        await salat(message)
    elif message.text == "🍩 Ponchiklar":
        await ponchik(message)
    elif message.text == "👶 Bolajonlarga":
        await bolalarga(message)
    elif message.text == "🍅 Souslar":
        await sous(message)
    elif message.text == "Kombo set":
        await kombo(message)
    elif message.text == "1+1 Barbekyu burger":
        await barbeku_burger(message)
    elif message.text == "1+1 Sezar burger":
        await sezar(message)
    elif message.text == "Yangi set":
        await yangi(message)
    elif message.text == "Klassik set":
        await klassik(message)
    elif message.text == "Skul set":
        await skul(message)
    elif message.text == "Do’stlar 1х":
        await dostlar(message)
    elif message.text == "Do’stlar 1х, achchiq":
        await dostlar_achchiq(message)
    elif message.text == "Qiyqiriq set":
        await qiyqiriq(message)
    elif message.text == "Longer rings set":
        await longer_rings(message)
    elif message.text == "Lester set":
        await lester_set(message)
    elif message.text == "Big set":
        await big_set(message)
    elif message.text == "Snek set":
        await snek_set(message)
    elif message.text == "Do’stlar 2х":
        await dostlar_2x(message)
    elif message.text == "Do’stlar 2х, achchiq":
        await dostlar2x_achchiq(message)
    elif message.text == "4 Friends Hot-dog":
        await hot_dog4x(message)
    elif message.text == "4 Friends Klassik burger":
        await burger4x(message)
    elif message.text == "4 Friends Longer chiz":
        await longer4x(message)
    elif message.text == "4 Friends Lester chiz":
        await lester4x(message)
    elif message.text == "Do’stlar 4х":
        await dostlar4x(message)
    elif message.text == "Do’stlar 4х, achchiq":
        await dostlar4x_achchiq(message)
    elif message.text == "Chiken korn":
        await chiken_korn(message)
    elif message.text == "Qanot, 3 dona":
        await qanot3x(message)
    elif message.text == "Achchiq qanot, 3 dona":
        await qanot3x_achchiq(message)
    elif message.text == "Strips, 3 dona":
        await strips3x(message)
    elif message.text == "Achchiq strips, 3 dona":
        await strips3x_achchiq(message)
    elif message.text == "Chizi chiken korn":
        await chizi_chiken(message)
    elif message.text == "Qanot, 7 dona":
        await qanot7x(message)
    elif message.text == "Achchiq qanot, 7 dona":
        await qanot7x_achchiq(message)
    elif message.text == "Strips, 7 dona":
        await strips7x(message)
    elif message.text == "Achchiq strips, 7 dona":
        await strips7x_achchiq(message)
    elif message.text == "Qanot, 17 dona":
        await qanot17x(message)
    elif message.text == "Achchiq qanot, 17 dona":
        await qanot17x_achchiq(message)
    elif message.text == "Strips, 17 dona":
        await strips17x(message)
    elif message.text == "Achchiq strips, 17 dona":
        await strips17x_achchiq(message)
    elif message.text == "Tovuq nagetsi, 3 dona":
        await tovuq_nagets(message)
    elif message.text == 'Chiken stiks, 3 dona':
        await chiken_striks(message)
    elif message.text == "Fri kartoshkasi":
        await fri(message)
    elif message.text == "Pishloqli tovuq sharchalari, 3 dona":
        await tovuq_shar(message)
    elif message.text == "Pishloqli kartoshka sharchalari, 7 dona":
        await kartoshka_shar(message)
    elif message.text == "Jaydari kartoshka":
        await jaydari_fri(message)
    elif message.text == "Tovuq nagetsi, 5 dona":
        await nagets5x(message)
    elif message.text == "Chiken stiks, 5 dona":
        await striks5x(message)
    elif message.text == "Fri basket":
        await fri_basket(message)
    elif message.text == "Pishloqli tovuq sharchalari, 5 dona":
        await tovuq_shar5x(message)
    elif message.text == "Pishloqli kartoshka sharchalari, 11 dona":
        await kartoshka_shar5x(message)
    elif message.text == "Lester sezar":
        await lester_sezar(message)
    elif message.text == "Amerikan lester":
        await american_lester(message)
    elif message.text == "Lester toster":
        await lestre_toster(message)
    elif message.text == "Barbekyu lester":
        await barbeku_lester(message)
    elif message.text == "Lester chili":
        await lester_chili(message)
    elif message.text == "Lester xalapenyo":
        await lester_xalapenyo(message)
    elif message.text == "Lester chiz":
        await lester_chiz(message)
    elif message.text == "Big boks":
        await big_boks(message)
    elif message.text == "Singer":
        await singer(message)
    elif message.text == "Chiken chiz":
        await chiken_chiz(message)
    elif message.text == "Xalapenyo burger":
        await xalapenyo_burger(message)
    elif message.text == "Biger":
        await biger(message)
    elif message.text == "Dabl chiken chiz":
        await dabl_chiken(message)
    elif message.text == "Hot-dog":
        await hotdog(message)
    elif message.text == "Longer":
        await longer(message)
    elif message.text == "Longer rings":
        await longerrings(message)
    elif message.text == "Longer chiz":
        await longerchiz(message)
    elif message.text == "Montella 0.33":
        await montella(message)
    elif message.text == "Qora choy":
        await qora_choy(message)
    elif message.text == "Ko'k choy":
        await kok_choy(message)
    elif message.text == "Limonli qora choy":
        await qora_limon(message)
    elif message.text == "Limonli ko'k choy":
        await kok_limon(message)
    elif message.text == "Espresso":
        await espresso(message)
    elif message.text == "Coca-cola 0.5":
        await cola(message)
    elif message.text == "Fanta 0.5":
        await fanta(message)
    elif message.text == "Sprite 0.5":
        await sprite(message)
    elif message.text == "Les tea!":
        await les_tea(message)
    elif message.text == "Frutea Berry mix":
        await berry(message)
    elif message.text == "Frutea Orange":
        await orange(message)
    elif message.text == "Frutea Strawberry":
        await strawbery(message)
    elif message.text == "Americano":
        await americano(message)
    elif message.text == "Ays kofe":
        await ays(message)
    elif message.text == 'Cappuccino':
        await cappucino(message)
    elif message.text == "Latte":
        await latte(message)
    elif message.text == "Ays kofe milk":
        await ays_milk(message)
    elif message.text == "New Moxito":
        await moxito(message)
    elif message.text == "Berry Moxito":
        await berry_moxito(message)
    elif message.text == "Koulslou":
        await koulslou(message)
    elif message.text == "Sezam":
        await sezam(message)
    elif message.text == "Les Barbekyu":
        await les_barbeku(message)
    elif message.text == "Sezar":
        await sezar_salat(message)
    elif message.text == "Grekcha":
        await grekcha(message)
    elif message.text == "Blueberry donut":
        await blueberry(message)
    elif message.text == "Caramel":
        await caramel(message)
    elif message.text == "Cinnamon":
        await cinnamon(message)
    elif message.text == "Cookies":
        await cookies(message)
    elif message.text == "Nutty cream":
        await nutty_cream(message)
    elif message.text == "Panna cotta":
        await panna_cotta(message)
    elif message.text == "Strawberry":
        await strawbery_donut(message)
    elif message.text == "Kids box longer O'":
        await kids_o(message)
    elif message.text == "Kids box longer Q":
        await kids_q(message)
    elif message.text == "Kids box lester O'":
        await lester_o(message)
    elif message.text == "Kids box lester Q":
        await lester_q(message)
    elif message.text == "Ketchup":
        await ketchup(message)
    elif message.text == "Chili":
        await chili(message)
    elif message.text == "Sezar":
        await sezar_sous(message)
    elif message.text == "Chizi":
        await chizi(message)
    elif message.text == "Mayonez":
        await mayonez(message)
    # elif message.text == "📥 Savat":
        # await view_basket(message)






@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [types.KeyboardButton(text="🇷🇺 Русский"), types.KeyboardButton(text="🇺🇿 O'zbekcha"),
        types.KeyboardButton(text="🇺🇸 English")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Assalomu alaykum! \n Les Ailes yetkazib berish xizmatiga xush kelibsiz.\n\n"
                             "Здравствуйте! Добро пожаловать в службу доставки Les Ailes.\n\n"
                             "Hello! Welcome to Les Ailes delivery service.", reply_markup=keyboard)
    print(user_data)

async def shaharlar(message: types.Message):
    user_id = message.from_user.id
    language = message.text
    user_data[user_id]['holat'] = language
    button = [
        [types.KeyboardButton(text='Toshkent'), types.KeyboardButton(text='Andijon')],
        [types.KeyboardButton(text='Samarqand'), types.KeyboardButton(text="Farg'ona")],
        [types.KeyboardButton(text='Buxoro'), types.KeyboardButton(text="Marg'ilon")],
        [types.KeyboardButton(text='Nukus'), types.KeyboardButton(text='Xorazm')],
        [types.KeyboardButton(text='Chirchiq'), types.KeyboardButton(text="Qo'qon")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Qaysi shaharda yashaysiz? \nIltimos, shaharni tanlang:', reply_markup=keyboard)
    print(user_data)

async def menu(message: types.Message):
    user_id = message.from_user.id
    shahar = message.text
    user_data[user_id]['shahar'] = shahar
    button = [
        [types.KeyboardButton(text='🛍 Buyurtma berish')],
        [types.KeyboardButton(text='📖 Buyurtmalar tarixi')],
        [types.KeyboardButton(text="⚙️Sozlash ℹ️ Ma'lumotlar"), types.KeyboardButton(text="🔥 Aksiya")],
        [types.KeyboardButton(text="🙋🏻‍♂️ Jamoamizga qo'shiling"),
            types.KeyboardButton(text="☎️ Les Ailes bilan aloqa")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Bosh menyu', reply_markup=keyboard)
    print(user_data)

async def buyurtma(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]['holat'] = 'buyurtma'
    button = [
        [types.KeyboardButton(text='🏃 Olib ketish'), types.KeyboardButton(text='🚙 Yetkazib berish')],
        [types.KeyboardButton(text='⬅️ Ortga')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Buyurtmani o'zingiz 🙋‍♂️ olib keting yoki Yetkazib berishni 🚙 tanlang",
                             reply_markup=keyboard)
    print(user_data)

async def tarix(message: types.Message):
    user_id = message.from_user.id
    tarix = message.text
    user_data[user_id]['tarix'] = tarix
    button = [
        [types.KeyboardButton(text="📞Raqamni jo'natish"), types.KeyboardButton(text='⬅️ Ortga')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Avval ro'yxatdan o'ting", )
    await message.answer("Ro'yxatdan o'tish uchun teelfon raqamingizni kiriting!\nMisol uchun, +998xx xxx xx xx",
                             reply_markup=keyboard)
    print(user_data)

async def aksiya(message: types.Message):
    user_id = message.from_user.id
    aksiya = message.text
    user_data[user_id]['aksiya'] = aksiya
    await message.answer("Shahringizda hali aksiyalar mavjud emas")
    print(user_data)



async def jamoa(message: types.Message):
    user_id = message.from_user.id
    jamoa = message.text
    user_data[user_id]['jamoa'] = jamoa
    button = [
        [types.InlineKeyboardButton(text="O'tish",callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    await message.answer("Ahil jamoamizda ishlashga taklif qilamiz! Telegramdan chiqmay, shu yerning o'zida anketani to'ldirish uchun quyidagi tugmani bosing.",reply_markup=keyboard)
    print(user_data)


async def sozlama(message: types.Message):
    user_id = message.from_user.id
    sozlama = message.text
    user_data[user_id]['sozlama'] = sozlama
    button = [
        [types.KeyboardButton(text="Ismni o'zgartirish"), types.KeyboardButton(text="📱 Raqamni o'zgartirish")],
        [types.KeyboardButton(text="🏙 Shaharni o'zgartirish"), types.KeyboardButton(text="🇺🇿 Tilni o'zgartirish")],
        [types.KeyboardButton(text="ℹ️ Filallar haqida ma'lumotlar"), types.KeyboardButton(text="📄 Ommaviy taklif")],
        [types.KeyboardButton(text='⬅️ Ortga')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Harakatni tanlang:', reply_markup=keyboard)
    print(user_data)


async def aloqa(message: types.Message):
    user_id = message.from_user.id
    aloqa = message.text
    user_data[user_id]['aloqa'] = aloqa
    button = [
        [types.KeyboardButton(text="💬 Biz bilan aloqaga chiqing"), types.KeyboardButton(text="✍️ Fikr bildirish")],
        [types.KeyboardButton(text="⬅️ Ortga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Agar siz bizga yozsangiz yoki sharh qoldirmoqchi bo'lsangiz, xursand bo'lamiz.", reply_markup=keyboard)
    print(user_data)


async def olish(message: types.Message):
    user_id = message.from_user.id
    olish = message.text
    user_data[user_id]['olish'] = olish
    button = [
        [types.KeyboardButton(text="🔙Ortga"), types.KeyboardButton(text="📍 Eng yaqin filialni aniqlash")],
        [types.KeyboardButton(text="Bu yerda buyurtma berish 🌐") ,types.KeyboardButton(text="Filialni tanlang")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Qayerdasiz 👀? Agar lokatsiyangizni📍 yuborsangiz, sizga eng yaqin filialni aniqlaymiz",
                         reply_markup=keyboard)
    print(user_data)


async def yetkazish(message: types.Message):
    user_id = message.from_user.id
    yetkazish = message.text
    user_data[user_id]['yetkazish'] = yetkazish
    button = [
        [types.KeyboardButton(text="📍 Eng yaqin filialni aniqlash")],
        [types.KeyboardButton(text="🔙Ortga") ,types.KeyboardButton(text="🗺 Mening manzillarim")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Buyurtmangizni qayerga yetkazib berish kerak 🚙?\n"
    "Agar lokatsiyangizni📍 yuborsangiz, sizga eng yaqin filialni va yetkazib berish xarajatlarini aniqlaymiz 💵",
                         reply_markup=keyboard)
    print(user_data)


async def ism(message: types.Message):
    user_id = message.from_user.id
    ism = message.text
    user_data[user_id]['ism'] = ism
    button = [
        [types.KeyboardButton(text="👈Ortga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Iltimos, ismingiz va familiyangizni kiriting.",
                         reply_markup=keyboard)
    print(user_data)

async def raqam(message: types.Message):
    user_id = message.from_user.id
    raqam = message.text
    user_data[user_id]['raqam'] = raqam
    button = [
        [types.KeyboardButton(text="👈Ortga"), types.KeyboardButton(text="📱 Mening raqamim")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("DeAdpOl_01 ... Raqamni +998 ** *** **** shaklida kiriting yoki yuboring.",
                         reply_markup=keyboard)
    print(user_data)



async def shahar(message: types.Message):
    user_id = message.from_user.id
    shahar = message.text
    user_data[user_id]['shahar'] = shahar
    await message.answer("Qaysi shaharda yashaysiz?\n"
    "Iltimos, shaharni tanlang:")
    print(user_data)

async def tanlash(message: types.Message):
    user_id = message.from_user.id
    tanlash = message.text
    user_data[user_id]['tanlash'] = tanlash
    await message.answer("✅ Tayyor")
    await sozlama(message)
    print(user_data)


async def boglanish(message: types.Message):
    user_id = message.from_user.id
    boglanish = message.text
    user_data[user_id]['boglanish'] = boglanish
    button = [
        [types.InlineKeyboardButton(text="💬 Biz bilan aloqaga chiqing", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    await message.answer("Agar biron-bir savol yoki taklif bo'lsa, bizga aloqaga chiqing.",reply_markup=keyboard)
    print(user_data)


async def fikr(message: types.Message):
    user_id = message.from_user.id
    fikr = message.text
    user_data[user_id]['fikr'] = fikr
    button = [
        [types.InlineKeyboardButton(text=f"Mahsulot", callback_data='text')],
        [types.InlineKeyboardButton(text=f'1 😣', callback_data=f'text'),
         types.InlineKeyboardButton(text=f'2 ☹️', callback_data=f'text'),
         types.InlineKeyboardButton(text=f'3 😐', callback_data=f'text'),
         types.InlineKeyboardButton(text=f'4 😑', callback_data=f'text'),
         types.InlineKeyboardButton(text=f'5 😍', callback_data=f'text')],
        [types.InlineKeyboardButton(text=f"Xizmat", callback_data=f'text')],
        [types.InlineKeyboardButton(text=f'1 👊🏻', callback_data=f'text'),
         types.InlineKeyboardButton(text=f'2 👎🏻', callback_data=f'text'),
         types.InlineKeyboardButton(text=f'3 👌🏻', callback_data=f'text'),
         types.InlineKeyboardButton(text=f'4 🤙🏻', callback_data=f'text'),
         types.InlineKeyboardButton(text=f'5 👍🏻', callback_data=f'text')],
        [types.InlineKeyboardButton(text=f"Yetkazib berish", callback_data=f'text')],
        [types.InlineKeyboardButton(text=f'1 🐌', callback_data=f'text'),
         types.InlineKeyboardButton(text=f'2 🐢', callback_data=f'text'),
         types.InlineKeyboardButton(text=f'3 🛺', callback_data=f'text'),
         types.InlineKeyboardButton(text=f'4 🏎', callback_data=f'text'),
         types.InlineKeyboardButton(text=f'5 🚀', callback_data=f'text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    await message.answer("✅ Les Ailes xizmati sharhi.", reply_markup=keyboard)
    print(user_data)

async def shu_yerda(message: types.Message):
    user_id = message.from_user.id
    shu_yerda = message.text
    user_data[user_id]['shu_yerda'] = shu_yerda
    button = [
        [types.InlineKeyboardButton(text=f"O'tish", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    await message.answer("O'z joylashuvingiz bilan buyurtma bering - https://lesailes.uz/", reply_markup=keyboard)
    print(user_data)



async def filial(message: types.Message):
    user_id = message.from_user.id
    filial = message.text
    user_data[user_id]['filial'] = filial
    button = [
        [types.KeyboardButton(text='Yunusobod'), types.KeyboardButton(text='S. Rahimov')],
        [types.KeyboardButton(text='Atlas'), types.KeyboardButton(text="M-5")],
        [types.KeyboardButton(text='Asia Nukus'), types.KeyboardButton(text="Farhod")],
        [types.KeyboardButton(text="Ko'kcha"), types.KeyboardButton(text='Oybek')],
        [types.KeyboardButton(text='Parus'), types.KeyboardButton(text="Chilonzor")],
        [types.KeyboardButton(text="Buyuk Ipak Yo'li"), types.KeyboardButton(text="Sergeli")],
        [types.KeyboardButton(text="Zenit"), types.KeyboardButton(text='Atlas')],
        [types.KeyboardButton(text='Next'), types.KeyboardButton(text="Samarqand Darvoza savdo markazi")],
        [types.KeyboardButton(text='↗️Ortga')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Qaysi filialdan olib ketishni tanlang', reply_markup=keyboard)
    print(user_data)


async def filial_malumot(message: types.Message):
    user_id = message.from_user.id
    filial_malumot = message.text
    user_data[user_id]['filial_malumot'] = filial_malumot
    button = [
        [types.KeyboardButton(text='Yunusobod'), types.KeyboardButton(text='S. Rahimov')],
        [types.KeyboardButton(text='Atlas'), types.KeyboardButton(text="M-5")],
        [types.KeyboardButton(text='Asia Nukus'), types.KeyboardButton(text="Farhod")],
        [types.KeyboardButton(text="Ko'kcha"), types.KeyboardButton(text='Oybek')],
        [types.KeyboardButton(text='Parus'), types.KeyboardButton(text="Chilonzor")],
        [types.KeyboardButton(text="Buyuk Ipak Yo'li"), types.KeyboardButton(text="Sergeli")],
        [types.KeyboardButton(text="Zenit"), types.KeyboardButton(text='Atlas')],
        [types.KeyboardButton(text='Next'), types.KeyboardButton(text="Samarqand Darvoza savdo markazi")],
        [types.KeyboardButton(text='👈Ortga')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Sizni qaysi filial qiziqtiryapti?', reply_markup=keyboard)
    print(user_data)

async def taklif(message: types.Message):
    user_id = message.from_user.id
    taklif = message.text
    user_data[user_id]['taklif'] = taklif
    await message.answer("https://telegra.ph/Publichnaya-oferta-Chopar-Pizza-05-21")
    print(user_data)

async def lang(message: types.Message):
    user_id = message.from_user.id
    lang = message.text
    user_data[user_id]['lang'] = lang
    button = [
        [types.KeyboardButton(text="🇷🇺 Русский"), types.KeyboardButton(text="🇺🇿 O'zbekcha"),
         types.KeyboardButton(text="🇺🇸 English")],
        [types.KeyboardButton(text="👈Ortga")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Tilni tanlang:', reply_markup=keyboard)
    print(user_data)



list = {
    "Yunusobod":"Yunusobod \n""A. Donish ko‘chasi, 80",
    "S. Rahimov":"S. Rahimov \n""махалля Яккабог, Чиланзарский район, Ташкент",
    "Atlas":"Atlas \n""Afsuski, bu filial yopiq. 😔\n"
    "Buyurtmani ish soatlarida berishga ishonch hosil qiling.\n"
    "Les Ailes yetkazib berish xizmatini tanlaganingiz uchun tashakkur.",
    "M-5":"M-5 \n""Sh. Rashidov shox k. 16A",
    "Asia Nukus":"Asia Nukus \n""MKAD, 19",
    "Farhod":"Farhod \n""Uchtepa t. G9A, 21/2",
    "Ko'kcha":"Ko'kcha \n""Shayxontohur t. \n"
    "Ko‘kcha darvoza 3A",
    "Oybek":"Oybek \n""Shahrisabz ko‘chasi, 10b",
    "Parus":"Parus \n""Parus KSM",
    "Chilonzor":"Chilonzor \n""2-blok, 2-uy",
    "Buyuk Ipak Yo'li":"Buyuk Ipak Yo'li \n""123 Buyuk Ipak Yo'li ko'chasi",
    "Sergeli":"Sergeli \n""Golden life KSM",
    "Zenit":"Zenit \n""7-й квартал, 49, массив Юнусабад, Юнусабадский район, Ташкент",
    "Atlas":"Atlas \n""Afsuski, bu filial yopiq. 😔\n"
    "Buyurtmani ish soatlarida berishga ishonch hosil qiling. \n"
    "Les Ailes yetkazib berish xizmatini tanlaganingiz uchun tashakkur.",
    "Next":"Next \n""Bobur ko‘chasi, 6-uy",
    "Samarqand Darvoza savdo markazi":"Samarqand Darvoza savdo markazi \n""Toshkent shahar, Qoratosh ko'chasi, 5A"
}


async def lokatsiya_tanlash(message: types.Message):
    user_id = message.from_user.id
    lokatsiya_tanlash = message.text
    user_data[user_id]['lokatsiya_tanlash'] = lokatsiya_tanlash
    # if lokatsiya_tanlash == list[lokatsiya_tanlash]:
    button = [
        [types.KeyboardButton(text='↖️Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='🍱 Setlar'), types.KeyboardButton(text="🍗 Tovuq")],
        [types.KeyboardButton(text='🍟 Sneklar'), types.KeyboardButton(text="🌯 Lesterlar")],
        [types.KeyboardButton(text="🍔 Burgerlar"), types.KeyboardButton(text='🌭 Longerlar/Hot-dog')],
        [types.KeyboardButton(text='🥤 Ichimliklar'), types.KeyboardButton(text="🥗 Salatlar")],
        [types.KeyboardButton(text="🍩 Ponchiklar"), types.KeyboardButton(text="👶 Bolajonlarga")],
        [types.KeyboardButton(text="🍅 Souslar")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    loc = list[lokatsiya_tanlash]
    await message.answer(f"{loc}")
    await bot.send_location(chat_id=message.from_user.id,
                            longitude=23.18,
                            latitude=56.17)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)

async def set(message: types.Message):
    user_id = message.from_user.id
    set = message.text
    user_data[user_id]['set'] = set
    button = [
        [types.KeyboardButton(text='⬆️Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Kombo set'), types.KeyboardButton(text="1+1 Barbekyu burger")],
        [types.KeyboardButton(text='1+1 Sezar burger'), types.KeyboardButton(text="Yangi set")],
        [types.KeyboardButton(text="Klassik set"), types.KeyboardButton(text='Skul set')],
        [types.KeyboardButton(text='Do’stlar 1х'), types.KeyboardButton(text="Do’stlar 1х, achchiq")],
        [types.KeyboardButton(text="Qiyqiriq set"), types.KeyboardButton(text="Longer rings set")],
        [types.KeyboardButton(text="Lester set"), types.KeyboardButton(text='Big set')],
        [types.KeyboardButton(text='Snek set'), types.KeyboardButton(text="Do’stlar 2х")],
        [types.KeyboardButton(text="Do’stlar 2х, achchiq"), types.KeyboardButton(text="4 Friends Hot-dog")],
        [types.KeyboardButton(text="4 Friends Klassik burger"), types.KeyboardButton(text='4 Friends Longer chiz')],
        [types.KeyboardButton(text="4 Friends Lester chiz"), types.KeyboardButton(text="Do’stlar 4х")],
        [types.KeyboardButton(text="Do’stlar 4х, achchiq")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)



async def back(message: types.Message):
    user_id = message.from_user.id
    back = message.text
    user_data[user_id]['back'] = back
    button = [
        [types.KeyboardButton(text='↖️Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='🍱 Setlar'), types.KeyboardButton(text="🍗 Tovuq")],
        [types.KeyboardButton(text='🍟 Sneklar'), types.KeyboardButton(text="🌯 Lesterlar")],
        [types.KeyboardButton(text="🍔 Burgerlar"), types.KeyboardButton(text='🌭 Longerlar/Hot-dog')],
        [types.KeyboardButton(text='🥤 Ichimliklar'), types.KeyboardButton(text="🥗 Salatlar")],
        [types.KeyboardButton(text="🍩 Ponchiklar"), types.KeyboardButton(text="👶 Bolajonlarga")],
        [types.KeyboardButton(text="🍅 Souslar")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)


async def tovuq(message: types.Message):
    user_id = message.from_user.id
    tovuq = message.text
    user_data[user_id]['tovuq'] = tovuq
    button = [
        [types.KeyboardButton(text='⬆️Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Chiken korn'), types.KeyboardButton(text="Qanot, 3 dona")],
        [types.KeyboardButton(text='Achchiq qanot, 3 dona'), types.KeyboardButton(text="Strips, 3 dona")],
        [types.KeyboardButton(text="Achchiq strips, 3 dona"), types.KeyboardButton(text='Chizi chiken korn')],
        [types.KeyboardButton(text='Qanot, 7 dona'), types.KeyboardButton(text="Achchiq qanot, 7 dona")],
        [types.KeyboardButton(text="Strips, 7 dona"), types.KeyboardButton(text="Achchiq strips, 7 dona")],
        [types.KeyboardButton(text="Qanot, 17 dona"), types.KeyboardButton(text='Achchiq qanot, 17 dona')],
        [types.KeyboardButton(text='Strips, 17 dona'), types.KeyboardButton(text="Achchiq strips, 17 dona")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)

async def snek(message: types.Message):
    user_id = message.from_user.id
    snek = message.text
    user_data[user_id]['snek'] = snek
    button = [
        [types.KeyboardButton(text='⬆️Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Tovuq nagetsi, 3 dona'), types.KeyboardButton(text="Chiken stiks, 3 dona")],
        [types.KeyboardButton(text='Fri kartoshkasi'), types.KeyboardButton(text="Pishloqli tovuq sharchalari, 3 dona")],
        [types.KeyboardButton(text="Pishloqli kartoshka sharchalari, 7 dona"), types.KeyboardButton(text='Jaydari kartoshka')],
        [types.KeyboardButton(text='Tovuq nagetsi, 5 dona'), types.KeyboardButton(text="Chiken stiks, 5 dona")],
        [types.KeyboardButton(text="Pishloqli tovuq sharchalari, 5 dona"), types.KeyboardButton(text="Pishloqli kartoshka sharchalari, 11 dona")],
        [types.KeyboardButton(text="Fri basket")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)

async def lester(message: types.Message):
    user_id = message.from_user.id
    lester = message.text
    user_data[user_id]['lester'] = lester
    button = [
        [types.KeyboardButton(text='⬆️Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Lester sezar'), types.KeyboardButton(text="Amerikan lester")],
        [types.KeyboardButton(text='Lester toster'), types.KeyboardButton(text="Barbekyu lester")],
        [types.KeyboardButton(text="Lester chili"), types.KeyboardButton(text='Lester xalapenyo')],
        [types.KeyboardButton(text='Lester chiz'), types.KeyboardButton(text="Big boks")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)



async def burger(message: types.Message):
    user_id = message.from_user.id
    burger = message.text
    user_data[user_id]['burger'] = burger
    button = [
        [types.KeyboardButton(text='⬆️Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Klassik'), types.KeyboardButton(text="1+1 Barbekyu burger")],
        [types.KeyboardButton(text='1+1 Sezar burger'), types.KeyboardButton(text="Singer")],
        [types.KeyboardButton(text="Chiken chiz"), types.KeyboardButton(text='Xalapenyo burger')],
        [types.KeyboardButton(text='Biger'), types.KeyboardButton(text="Dabl chiken chiz")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)

async def longer_hotdog(message: types.Message):
    user_id = message.from_user.id
    longer_hotdog = message.text
    user_data[user_id]['longer_hotdog'] = longer_hotdog
    button = [
        [types.KeyboardButton(text='⬆️Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Hot-dog'), types.KeyboardButton(text="Longer")],
        [types.KeyboardButton(text='Longer rings'), types.KeyboardButton(text="Longer chiz")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)

async def ichimlik(message: types.Message):
    user_id = message.from_user.id
    ichimlik = message.text
    user_data[user_id]['ichimlik'] = ichimlik
    button = [
        [types.KeyboardButton(text='⬆️Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Montella 0.33'), types.KeyboardButton(text="Qora choy")],
        [types.KeyboardButton(text="Ko'k choy"), types.KeyboardButton(text="Limonli qora choy")],
        [types.KeyboardButton(text="Limonli ko'k choy"), types.KeyboardButton(text='Espresso')],
        [types.KeyboardButton(text='Coca-cola 0.5'), types.KeyboardButton(text="Fanta 0.5")],
        [types.KeyboardButton(text="Sprite 0.5"), types.KeyboardButton(text="Les tea!")],
        [types.KeyboardButton(text="Frutea Berry mix"), types.KeyboardButton(text='Frutea Orange')],
        [types.KeyboardButton(text='Frutea Strawberry'), types.KeyboardButton(text="Americano")],
        [types.KeyboardButton(text="Ays kofe"), types.KeyboardButton(text="Aysti")],
        [types.KeyboardButton(text="Cappuccino"), types.KeyboardButton(text='Latte')],
        [types.KeyboardButton(text="Ays kofe milk"), types.KeyboardButton(text="New Moxito")],
        [types.KeyboardButton(text="Berry Moxito")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)


async def salat(message: types.Message):
    user_id = message.from_user.id
    salat = message.text
    user_data[user_id]['salat'] = salat
    button = [
        [types.KeyboardButton(text='⬆️Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Koulslou'), types.KeyboardButton(text="Sezam")],
        [types.KeyboardButton(text='Les Barbekyu'), types.KeyboardButton(text="Sezar")],
        [types.KeyboardButton(text='Grekcha')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)



async def ponchik(message: types.Message):
    user_id = message.from_user.id
    ponchik = message.text
    user_data[user_id]['ponchik'] = ponchik
    button = [
        [types.KeyboardButton(text='⬆️Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Blueberry donut'), types.KeyboardButton(text="Caramel")],
        [types.KeyboardButton(text='Cinnamon'), types.KeyboardButton(text="Cookies")],
        [types.KeyboardButton(text="Nutty cream"), types.KeyboardButton(text='Panna cotta')],
        [types.KeyboardButton(text='Strawberry')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)

async def bolalarga(message: types.Message):
    user_id = message.from_user.id
    bolalarga = message.text
    user_data[user_id]['bolalarga'] = bolalarga
    button = [
        [types.KeyboardButton(text='⬆️Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text="Kids box longer O'"), types.KeyboardButton(text="Kids box longer Q")],
        [types.KeyboardButton(text="Kids box lester O'"), types.KeyboardButton(text="Kids box lester Q")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)

async def sous(message: types.Message):
    user_id = message.from_user.id
    sous = message.text
    user_data[user_id]['sous'] = sous
    button = [
        [types.KeyboardButton(text='⬆️Ortga'), types.KeyboardButton(text='📥 Savat')],
        [types.KeyboardButton(text='Ketchup'), types.KeyboardButton(text="Chili")],
        [types.KeyboardButton(text='Sezar'), types.KeyboardButton(text="Chizi")],
        [types.KeyboardButton(text='Mayonez')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer('Nimadan boshlaymiz?', reply_markup=keyboard)
    print(user_data)




async def kombo(message: types.Message):
    user_id = message.from_user.id
    item = message.text
    user_data[user_id]['kombo'] = item
    price = 22000
    button = [
        [types.InlineKeyboardButton(text="-", callback_data=f"minus_{item}"),
         types.InlineKeyboardButton(text="1", callback_data=f"miqdor_{item}"),
         types.InlineKeyboardButton(text="+", callback_data=f"plus_{item}")],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data=f"add_{item}")]
    ]
    buttons = [
        [types.KeyboardButton(text='👈🏻Ortga'), types.KeyboardButton(text="📥 Savatga qo'shish ✅")]
    ]
    keyboards = types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/kombo.jpg"
    caption_text = (f"{item}\n"
                    "Fri kartoshkasi Coca-cola 0.5\n"
                    f"Narxi:{price} so'm")
    await message.answer("Miqdorini belgilang", reply_markup=keyboards)
    await message.reply_photo(caption=caption_text,photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

count = 1
@dp.callback_query(lambda c: c.data.startswith(('plus', 'minus', 'add')))
async def checkcallback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    narx = callback.data
    price = 22000
    name = "Fri kartoshkasiCoca-cola 0.5\n"
    command, item = callback.data.split('_')
    global count
    # global price

    if command == 'plus':
        count += 1
    elif command == 'minus':
        if count > 1:
            count -= 1
    elif command == 'add':
        if 'basket' not in user_data[user_id]:
            user_data[user_id]['basket'] = {item: count}
        else:
            if item in user_data[user_id]['basket']:
                user_data[user_id]['basket'][item] += count
            else:
                user_data[user_id]['basket'][item] = count

        count = 1  # Reset count after adding item to the basket
        await callback.message.answer(f"Mahsulot: {name} savatga muvaffaqiyatli qo'shildi ✅\n"
                                    "Davom etamizmi?")

    print(f"Count:{count}")
    button = [
        [types.InlineKeyboardButton(text=f"-", callback_data=f"minus_{item}"),
         types.InlineKeyboardButton(text=f"{count}", callback_data=f"miqdor_{item}"),
         types.InlineKeyboardButton(text=f"+", callback_data=f"plus_{item}"), ],
        [types.InlineKeyboardButton(text=f"📥Savatga qo'shish✅", callback_data=f"add_{item}"), ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    price = price * count  # Update the price based on count
    try:
        print(user_data)
        await callback.message.edit_caption(
            caption="Kombo set\n\n"
                    f"Nomi: {name}\n"
                    f"Narxi: {price} so'm",
            reply_markup=keyboard
        )
    except aiogram.exceptions.TelegramBadRequest as e:
        if "message is not modified" in str(e):
            print("Xabar o'zgarmaganligi sababli yangilash o'tkazib yuborildi.")
        else:
            print(f"Xato yuz berdi: {e}")




async def barbeku_burger(message: types.Message):
    user_id = message.from_user.id
    barbeku_burger = message.text
    user_data[user_id]['barbeku_burger'] = barbeku_burger
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/barbeku_burger.jpg"
    caption_text = ("1+1 Barbekyu burger\n"
                    "Bittasi narxiga ikkita Barbekyu burger! miqdori chegaralangan\n"
                    "Narxi: 27 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

# Savatni ko'rish funksiyasi
@dp.callback_query(lambda c: c.data == "view_basket")
async def view_basket(callback: types.CallbackQuery):
    user_id = callback.from_user.id  # Foydalanuvchi ID'sini olish

    # Agar foydalanuvchining savati bo'lsa
    if user_id in user_data and 'basket' in user_data[user_id] and user_data[user_id]['basket']:
        basket_items = ""  # Savatdagi mahsulotlarni saqlash uchun bo'sh string
        total_price = 0  # Umumiy narxni boshlang'ich qiymat

        # Savatdagi barcha mahsulotlar va ularning miqdorini olish
        for item, quantity in user_data[user_id]['basket'].items():
            basket_items += f"{item}: {quantity}\n"  # Mahsulot va miqdor
            total_price += quantity * price  # Umumiy narxni hisoblash

        # Foydalanuvchiga savatdagi mahsulotlar va umumiy narxni yuborish
        await callback.message.answer(
            f"Savatdagi mahsulotlar:\n\n{basket_items}\nUmumiy narx: {total_price} so'm"
        )
    else:
        # Agar savat bo'sh bo'lsa
        await callback.message.answer("Savatda hech qanday mahsulot yo'q.")





# user_data[user_id]['basket'] = {item: count}

async def sezar(message: types.Message):
    user_id = message.from_user.id
    sezar = message.text
    user_data[user_id]['sezar'] = sezar
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/sezar.jpg"
    caption_text = ("1+1 Sezar burger\n"
                    "Bittasi narxiga ikkita Sezar burger! miqdori chegaralangan\n"
                    "Narxi: 27 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def yangi(message: types.Message):
    user_id = message.from_user.id
    yangi = message.text
    user_data[user_id]['yangi'] = yangi
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/yangi.jpg"
    caption_text = ("Yangi set\n"
                    "Klassik burgerNagets, 3 donaLes tea!\n"
                    "Narxi: 35 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def klassik(message: types.Message):
    user_id = message.from_user.id
    klassik = message.text
    user_data[user_id]['klassik'] = klassik
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/klassik.jpg"
    caption_text = ("Klassik set\n"
                    "Klassik burgerCoca-cola 0.3 Fri kartoshkasi S\n"
                    "Narxi: 38 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def skul(message: types.Message):
    user_id = message.from_user.id
    skul = message.text
    user_data[user_id]['skul'] = skul
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/skul.jpg"
    caption_text = ("Skul set\n"
                    "Hot-dogCoca-cola 0.3 Fri kartoshkasi SKetchup sousi\n"
                    "Narxi: 41 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def dostlar(message: types.Message):
    user_id = message.from_user.id
    dostlar = message.text
    user_data[user_id]['dostlar'] = dostlar
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/do'stlar.jpg"
    caption_text = ("Do’stlar 1х\n"
                    "Qanotchalar 3Tovuq sharchalari 2 Tovuq nagetsi 2Kartoshka fri SKetchup\n"
                    "Narxi: 47 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def dostlar_achchiq(message: types.Message):
    user_id = message.from_user.id
    dostlar_achchiq = message.text
    user_data[user_id]['dostlar_achchiq'] = dostlar_achchiq
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/do'stlar_achchiq.jpg"
    caption_text = ("Do’stlar 1х, achchiq\n"
                    "Achchiq qanotchalar 3Tovuq sharchalari 2Tovuq nagetsi 2Kartoshka fri SKetchup\n"
                    "Narxi: 47 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def qiyqiriq(message: types.Message):
    user_id = message.from_user.id
    qiyqiriq = message.text
    user_data[user_id]['qiyqiriq'] = qiyqiriq
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/qiyqiriq.jpg"
    caption_text = ("Qiyqiriq set \n"
                    "Barbekyu lesterPishloqli toviq sharchalari, 3 donaAystiJo'shqin salati \n"
                    "Narxi: 49 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def longer_rings(message: types.Message):
    user_id = message.from_user.id
    longer_rings = message.text
    user_data[user_id]['longer_rings'] = longer_rings
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/longer_rings.jpg"
    caption_text = ("Longer rings set\n"
                    "Longer ringsTovuq sharchalari 3Fri kartoshkasi SKetchup\n"
                    "Narxi: 50 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def lester_set(message: types.Message):
    user_id = message.from_user.id
    lester_set = message.text
    user_data[user_id]['lester_set'] = lester_set
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/lester_set.jpg"
    caption_text = ("Lester set\n"
                    "Lester tosterNaggetslar, 3 dona Coca-cola 0.5 Fri kartoshkasi S Ketchup sousi\n"
                    "Narxi: 59 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def big_set(message: types.Message):
    user_id = message.from_user.id
    big_set = message.text
    user_data[user_id]['big_set'] = big_set
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/big_set.jpg"
    caption_text = ("Big set\n"
                    "Big boxChicken cornCoca-cola 0.5Kartoshka fri LKetchup sousi\n"
                    "Narxi: 69 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def snek_set(message: types.Message):
    user_id = message.from_user.id
    snek_set = message.text
    user_data[user_id]['snek_set'] = snek_set
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/snek_set.jpg"
    caption_text = ("Snek set\n"
                    "Pishloqli tovuq sharchalari 5Chiken stiks 5Tovuq nagetsi 5Pishloqli kartoshka sharchalari 5Fri kartoshkasi LKetchup 2 \n"
                    "Narxi: 85 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def dostlar_2x(message: types.Message):
    user_id = message.from_user.id
    dostlar_2x = message.text
    user_data[user_id]['dostlar_2x'] = dostlar_2x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/dostlar_2x.jpg"
    caption_text = ("Do’stlar 2х\n"
                    "Qanotchalar 6Tovuq sharchalari 6Chiken korn Kartoshka fri LKetchup 3\n"
                    "Narxi: 85 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def dostlar2x_achchiq(message: types.Message):
    user_id = message.from_user.id
    dostlar2x_achchiq = message.text
    user_data[user_id]['dostlar2x_achchiq'] = dostlar2x_achchiq
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/dostlar2x_achchiq.jpg"
    caption_text = ("Do’stlar 2х, achchiq\n"
                    "Achchiq qanotchalar 6 Tovuq sharchalari 6 Chiken korn Kartoshka fri LKetchup 3\n"
                    "Narxi: 85 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def hot_dog4x(message: types.Message):
    user_id = message.from_user.id
    hot_dog4x = message.text
    user_data[user_id]['hot_dog4x'] = hot_dog4x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/hot_dog4x.jpg"
    caption_text = ("4 Friends Hot-dog\n"
                    "Hot-dog 4 dona Pishloqli tovuq sharchalari 12 dona \n"
                    "Narxi: 117 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def burger4x(message: types.Message):
    user_id = message.from_user.id
    burger4x = message.text
    user_data[user_id]['burger4x'] = burger4x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/burger4x.jpg"
    caption_text = ("4 Friends Klassik burger\n"
                    "Klassik burger 4 donaPishloqli tovuq sharchalari 12 dona\n"
                    "Narxi: 126 000  soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def longer4x(message: types.Message):
    user_id = message.from_user.id
    longer4x = message.text
    user_data[user_id]['longer4x'] = longer4x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/longer4x.jpg"
    caption_text = ("4 Friends Longer chiz\n"
                    "Longer chiz 4 donaPishloqli tovuq sharchalari 12 dona\n"
                    "Narxi: 126 000  soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def lester4x(message: types.Message):
    user_id = message.from_user.id
    lester4x = message.text
    user_data[user_id]['lester4x'] = lester4x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/lester4x.jpg"
    caption_text = ("4 Friends Lester chiz\n"
                    "Lester chiz 4 donaPishloqli tovuq sharchalari 12 dona\n"
                    "Narxi: 138 000  soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def dostlar4x(message: types.Message):
    user_id = message.from_user.id
    dostlar4x = message.text
    user_data[user_id]['dostlar4x'] = dostlar4x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/dostlar4x.jpg"
    caption_text = ("Do’stlar 4х\n"
                    "Qanotchalar 12 Tovuq sharchalari 4 Chiken korn Kartoshka fri L 2Jaydari kartoshka LKetchup 4\n"
                    "Narxi: 165 000  soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def dostlar4x_achchiq(message: types.Message):
    user_id = message.from_user.id
    dostlar4x_achchiq = message.text
    user_data[user_id]['dostlar4x_achchiq'] = dostlar4x_achchiq
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/dostlar4x_achchiq.jpg"
    caption_text = ("Do’stlar 4х, achchiq\n"
                    "Achchiq qanotchalar 12 Tovuq sharchalari 4 Chiken korn Kartoshka fri L 2Jaydari kartoshka LKetchup 4\n"
                    "Narxi: 165 000  soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def chiken_korn(message: types.Message):
    user_id = message.from_user.id
    chiken_korn = message.text
    user_data[user_id]['chiken_korn'] = chiken_korn
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/chiken_korn.jpg"
    caption_text = ("Chiken korn\n"
                    "Yumshoq tovuq bo'lakchalari\n"
                    "Narxi: 20 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def qanot3x(message: types.Message):
    user_id = message.from_user.id
    qanot3x = message.text
    user_data[user_id]['qanot3x'] = qanot3x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/qanot3x.jpg"
    caption_text = ("Qanot, 3 dona\n"
                    "Maxsus panirovkadagi, tovuqning xushta‘m qanotlari (Halal). 3 dona\n"
                    "Narxi: 24 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def qanot3x_achchiq(message: types.Message):
    user_id = message.from_user.id
    qanot3x_achchiq = message.text
    user_data[user_id]['qanot3x_achchiq'] = qanot3x_achchiq
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/qanot3x_achchiq.jpg"
    caption_text = ("Achchiq qanot, 3 dona\n"
                    "Maxsus panirovkadagi, o‘tkir ziravorli, tovuqning xushta‘m qanotlari (Halal). 3 dona\n"
                    "Narxi: 24 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def strips3x(message: types.Message):
    user_id = message.from_user.id
    strips3x = message.text
    user_data[user_id]['strips3x'] = strips3x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/strips3x.jpg"
    caption_text = ("Strips, 3 dona\n"
                    "Tovuqning maxsus panirovkadagi mayin filesi (Halal). 3 dona\n"
                    "Narxi: 24 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def strips3x_achchiq(message: types.Message):
    user_id = message.from_user.id
    strips3x_achchiq = message.text
    user_data[user_id]['strips3x_achchiq'] = strips3x_achchiq
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/strips3x_achchiq.jpg"
    caption_text = ("Achchiq strips, 3 dona\n"
                    "Maxsus panirovkadagi, o‘tkir ziravorli, tovuqning mayin filesi (Halal). 3 dona\n"
                    "Narxi: 24 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def chizi_chiken(message: types.Message):
    user_id = message.from_user.id
    chizi_chiken = message.text
    user_data[user_id]['chizi_chiken'] = chizi_chiken
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/chizi_chiken.jpg"
    caption_text = ("Chizi chiken korn\n"
                    "Pishloq sousidagi yumshoq tovuq bo'lakchalari\n"
                    "Narxi: 40 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def qanot7x(message: types.Message):
    user_id = message.from_user.id
    qanot7x = message.text
    user_data[user_id]['qanot7x'] = qanot7x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/qanot7x.jpg"
    caption_text = ("Qanot, 7 dona\n"
                    "Maxsus panirovkadagi, tovuqning xushta‘m qanotlari (Halal). 7 dona\n"
                    "Narxi: 48 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def qanot7x_achchiq(message: types.Message):
    user_id = message.from_user.id
    qanot7x_achchiq = message.text
    user_data[user_id]['qanot7x_achchiq'] = qanot7x_achchiq
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/qanot7x_achchiq.jpg"
    caption_text = ("Achchiq qanot, 7 dona\n"
                    "Maxsus panirovkadagi, o‘tkir ziravorli, tovuqning xushta‘m qanotlari (Halal). 7 dona\n"
                    "Narxi: 48 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def strips7x(message: types.Message):
    user_id = message.from_user.id
    strips7x = message.text
    user_data[user_id]['strips7x'] = strips7x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/strips7x.jpg"
    caption_text = ("Strips, 7 dona\n"
                    "Tovuqning maxsus panirovkadagi mayin filesi (Halal). 7 dona\n"
                    "Narxi: 48 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def strips7x_achchiq(message: types.Message):
    user_id = message.from_user.id
    strips7x_achchiq = message.text
    user_data[user_id]['strips7x_achchiq'] = strips7x_achchiq
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/strips7x_achchiq.jpg"
    caption_text = ("Achchiq strips, 7 dona\n"
                    "Maxsus panirovkadagi, o‘tkir ziravorli, tovuqning mayin filesi (Halal). 7 dona\n"
                    "Narxi: 48 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def qanot17x(message: types.Message):
    user_id = message.from_user.id
    qanot17x = message.text
    user_data[user_id]['qanot17x'] = qanot17x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/qanot17x.jpg"
    caption_text = ("Qanot, 17 dona\n"
                    "Maxsus panirovkadagi, tovuqning xushta‘m qanotlari (Halal). 17 dona\n"
                    "Narxi: 108 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def qanot17x_achchiq(message: types.Message):
    user_id = message.from_user.id
    qanot17x_achchiq = message.text
    user_data[user_id]['qanot17x_achchiq'] = qanot17x_achchiq
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/qanot17x_achchiq.jpg"
    caption_text = ("Achchiq qanot, 17 dona\n"
                    "Maxsus panirovkadagi, o‘tkir ziravorli, tovuqning xushta‘m qanotlari (Halal). 17 dona\n"
                    "Narxi: 108 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def strips17x(message: types.Message):
    user_id = message.from_user.id
    strips17x = message.text
    user_data[user_id]['strips17x'] = strips17x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/strips17x.jpg"
    caption_text = ("Strips, 17 dona\n"
                    "Tovuqning maxsus panirovkadagi mayin filesi (Halal). 17 dona\n"
                    "Narxi: 108 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def strips17x_achchiq(message: types.Message):
    user_id = message.from_user.id
    strips17x_achchiq = message.text
    user_data[user_id]['strips17x_achchiq'] = strips17x_achchiq
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/strips17x_achchiq.jpg"
    caption_text = ("Achchiq strips, 17 dona\n"
                    "Maxsus panirovkadagi, o‘tkir ziravorli, tovuqning mayin filesi (Halal). 17 dona\n"
                    "Narxi: 108 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def tovuq_nagets(message: types.Message):
    user_id = message.from_user.id
    tovuq_nagets = message.text
    user_data[user_id]['tovuq_nagets'] = tovuq_nagets
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/tovuq_nagets.jpg"
    caption_text = ("Tovuq nagetsi, 3 dona\n"
                    "Maxsus panirovka bilan qoplangan, tovuq qiymasidan tayyorlangan ishtahaochar naggetslar\n"
                    "Narxi:  15 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def chiken_striks(message: types.Message):
    user_id = message.from_user.id
    chiken_striks = message.text
    user_data[user_id]['chiken_striks'] = chiken_striks
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/chiken_striks.jpg"
    caption_text = ("Chiken stiks, 3 dona\n"
                    "Maxsus panirovka bilan qoplangan, tovuq qiymasidan tayyorlangan ishtahaochar naggetslar (Halal) \n"
                    "Narxi:  15 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def fri(message: types.Message):
    user_id = message.from_user.id
    fri = message.text
    user_data[user_id]['fri'] = fri
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/fri.jpg"
    caption_text = ("Fri kartoshkasi \n"
                    "Ishtahaochar, qarsildoq fri kartoshkasi. \n"
                    "Narxi: 16 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def tovuq_shar(message: types.Message):
    user_id = message.from_user.id
    kartoshka_shar = message.text
    user_data[user_id]['kartoshka_shar'] = kartoshka_shar
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/kartoshka_shar.jpg"
    caption_text = ("Pishloqli kartoshka sharchalari, 7 dona \n"
                    "Maxsus panirovkadagi, pishloqli kartoshka sharchalari. 7 dona \n"
                    "Narxi: 18 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def kartoshka_shar(message: types.Message):
    user_id = message.from_user.id
    kartoshka_shar = message.text
    user_data[user_id]['kartoshka_shar'] = kartoshka_shar
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/kartoshka_shar.jpg"
    caption_text = ("Pishloqli kartoshka sharchalari, 7 dona \n"
                    "Maxsus panirovkadagi, pishloqli kartoshka sharchalari. 7 dona \n"
                    "Narxi: 18 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def jaydari_fri(message: types.Message):
    user_id = message.from_user.id
    jaydari_fri = message.text
    user_data[user_id]['jaydari_fri'] = jaydari_fri
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/jaydari_fri.jpg"
    caption_text = ("Jaydari kartoshka \n"
                    "Ziravorlar bilan qovurilgan, ishtahaochar kartoshka bo'laklari. \n"
                    "Narxi: 18 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def nagets5x(message: types.Message):
    user_id = message.from_user.id
    nagets5x = message.text
    user_data[user_id]['nagets5x'] = nagets5x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/nagets5x.jpg"
    caption_text = ("Tovuq nagetsi, 5 dona \n"
                    "Maxsus panirovka bilan qoplangan, tovuq qiymasidan tayyorlangan ishtahaochar naggetslar. \n"
                    "Narxi: 20 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def striks5x(message: types.Message):
    user_id = message.from_user.id
    striks5x = message.text
    user_data[user_id]['striks5x'] = striks5x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/striks5x.jpg"
    caption_text = ("Chiken stiks, 5 dona \n"
                    "Maxsus panirovka bilan qoplangan, tovuq qiymasidan tayyorlangan ishtahaochar naggetslar (Halal) \n"
                    "Narxi: 20 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def tovuq_shar5x(message: types.Message):
    user_id = message.from_user.id
    tovuq_shar5x = message.text
    user_data[user_id]['tovuq_shar5x'] = tovuq_shar5x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/tovuq_shar5x.jpg"
    caption_text = ("Pishloqli tovuq sharchalari, 5 dona \n"
                    "Maxsus panirovkadagi, yumshoq va mazali, pishloqli tovuq sharchalari (Halol). \n"
                    "Narxi: 23 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def kartoshka_shar5x(message: types.Message):
    user_id = message.from_user.id
    kartoshka_shar5x = message.text
    user_data[user_id]['kartoshka_shar5x'] = kartoshka_shar5x
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/kartoshka_shar5x.jpg"
    caption_text = ("Pishloqli kartoshka sharchalari, 11 dona \n"
                    "Maxsus panirovkadagi, pishloqli kartoshka sharchalari. 11 dona \n"
                    "Narxi: 25 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def fri_basket(message: types.Message):
    user_id = message.from_user.id
    fri_basket = message.text
    user_data[user_id]['fri_basket'] = fri_basket
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/fri_basket.jpg"
    caption_text = ("Fri basket \n"
                    "Yanada ko'proq ishtahaochar, qarsildoq fri kartoshkasi \n"
                    "Narxi:  29 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def lester_sezar(message: types.Message):
    user_id = message.from_user.id
    lester_sezar = message.text
    user_data[user_id]['lester_sezar'] = lester_sezar
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/lester_sezar.jpg"
    caption_text = ("Lester sezar \n"
                    "Lavash, maxsus panirovka bilan qoplangan yumshoq tovuq filesi (Halol), aysberg salati, sezar sousi \n"
                    "Narxi:  27 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def american_lester(message: types.Message):
    user_id = message.from_user.id
    american_lester = message.text
    user_data[user_id]['american_lester'] = american_lester
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/american_lester.jpg"
    caption_text = ("Amerikan lester \n"
                    "Lavash, maxsus panirovka bilan qoplangan yumshoq tovuq filesi (Halol), qovurilgan kartoshka, tuzlangan bodring, piyoz, mayonez va ketchup sousi. \n"
                    "Narxi:  27 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def lestre_toster(message: types.Message):
    user_id = message.from_user.id
    lestre_toster = message.text
    user_data[user_id]['lestre_toster'] = lestre_toster
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/lestre_toster.jpg"
    caption_text = ("Lester toster \n"
                    "Lavash xamiri, maxsus panirovka bilan qoplangan yumshoq tovuq filesi (Halol), sarxil pomidor, tuzlangan bodring, salat bargi, mayonez va ketchup sousi. \n"
                    "Narxi:  27 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def barbeku_lester(message: types.Message):
    user_id = message.from_user.id
    barbeku_lester = message.text
    user_data[user_id]['barbeku_lester'] = barbeku_lester
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/barbeku_lester.jpg"
    caption_text = ("Barbekyu lester \n"
                    "Lavash, maxsus panirovkali yumshoq tovuq filesi (Halol), sarxil pomidor va bodring, salat bargi, mayonez va ishtahaochar BBQ sousi \n"
                    "Narxi:  27 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def lester_chili(message: types.Message):
    user_id = message.from_user.id
    lester_chili = message.text
    user_data[user_id]['lester_chili'] = lester_chili
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/lester_chili.jpg"
    caption_text = ("Lester chili \n"
                    "Lavash xamiri, maxsus panirovka bilan qoplangan yumshoq tovuq filesi (Halol), sarxil pomidor, tuzlangan bodring, salat bargi, mayonez va chili sousi \n"
                    "Narxi: 28 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def lester_xalapenyo(message: types.Message):
    user_id = message.from_user.id
    lester_xalapenyo = message.text
    user_data[user_id]['lester_xalapenyo'] = lester_xalapenyo
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/lester_xalapenyo.jpg"
    caption_text = ("Lester xalapenyo \n"
                    "Lavash xamiri, maxsus panirovka bilan qoplangan yumshoq tovuq filesi (Halol), sarxil pomidor, salat bargi, xalapenyo qalampiri, mayonez va ketchup sousi. \n"
                    "Narxi:  29 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def lester_chiz(message: types.Message):
    user_id = message.from_user.id
    lester_chiz = message.text
    user_data[user_id]['lester_chiz'] = lester_chiz
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/lester_chiz.jpg"
    caption_text = ("Lester chiz \n"
                    "Lavash, maxsus panirovka bilan qoplangan yumshoq tovuq filesi (Halol), Chedder pishlog'i, sarxil pomidor bo'laklari, salat bargi, mayonez va ketchup sousi. \n"
                    "Narxi:  29 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def big_boks(message: types.Message):
    user_id = message.from_user.id
    big_boks = message.text
    user_data[user_id]['big_boks'] = big_boks
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/big_boks.jpg"
    caption_text = ("Big boks \n"
                    "Lavash, maxsus panirovka bilan qoplangan yumshoq tovuq filesi (Halol), kartoshka pyuresi, Chedder pishlog'i, sarxil pomidor bo'laklari, salat bargi, mayonez sousi. \n"
                    "Narxi: 33 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def singer(message: types.Message):
    user_id = message.from_user.id
    singer = message.text
    user_data[user_id]['singer'] = singer
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/singer.jpg"
    caption_text = ("Singer\n"
                    "Yumshoq bulochka, maxsus panirovka bilan qoplangan mayin tovuq filesi (Halol), pomidor bo'laklari, tuzlangan bodring, salat bargi, mayonez va chili sousi \n"
                    "Narxi: 27 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def chiken_chiz(message: types.Message):
    user_id = message.from_user.id
    chiken_chiz = message.text
    user_data[user_id]['chiken_chiz'] = chiken_chiz
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/chiken_chiz.jpg"
    caption_text = ("Chiken chiz \n"
                    "Yumshoq bulochka, sarxil tovuq kotleti (Halol), Chedder pishlog'i, sarxil pomidor bo'laklari, aysberg salati, mayonez va ketchup sousi. \n"
                    "Narxi: 27 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def xalapenyo_burger(message: types.Message):
    user_id = message.from_user.id
    xalapenyo_burger = message.text
    user_data[user_id]['xalapenyo_burger'] = xalapenyo_burger
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/xalapenyo_burger.jpg"
    caption_text = ("Xalapenyo burger \n"
                    "Yumshoq bulochka, maxsus panirovka bilan qoplangan mayin tovuq filesi (Halol), pomidor bo'laklari, tuzlangan bodring, salat bargi, xalapenyo qalampiri, mayonez va ketchup sousi \n"
                    "Narxi: 28 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def biger(message: types.Message):
    user_id = message.from_user.id
    biger = message.text
    user_data[user_id]['biger'] = biger
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/biger.jpg"
    caption_text = ("Biger\n"
                    "Yumshoq bulochka, dudlangan mol go'shti (Halol), maxsus panirovka bilan qoplangan mayin tovuq filesi (Halol), Chedder pishlog'i, pomidor bo'laklari, tuzlangan bodring, salat bargi, mayonez va ketchup souslari \n"
                    "Narxi: 30 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def dabl_chiken(message: types.Message):
    user_id = message.from_user.id
    dabl_chiken = message.text
    user_data[user_id]['dabl_chiken'] = dabl_chiken
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/dabl_chiken.jpg"
    caption_text = ("Dabl chiken chiz \n"
                    "Yumshoqqina bulochka,ikkita shirador tovuq kotleti (Halal), chedder pishlog‘i, yangi pomidor, marinadlangan bodiring, aysberg salat barglari, mayonez va ketchup souslari \n"
                    "Narxi: 34 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def hotdog(message: types.Message):
    user_id = message.from_user.id
    hotdog = message.text
    user_data[user_id]['hotdog'] = hotdog
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/hotdog.jpg"
    caption_text = ("Hot-dog \n"
                    "Mini longer bulochka, Yegerskiye sosiskasi (Halol), tuzlangan bodring, xantal, mayonez va ketchup souslari  \n"
                    "Narxi: 22 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def longer(message: types.Message):
    user_id = message.from_user.id
    longer = message.text
    user_data[user_id]['longer'] = longer
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/longer.jpg"
    caption_text = ("Longer \n"
                    "Yumshoq bulochka, maxsus panirovka bilan qoplangan mayin tovuq filesi (Halol), pomidor bo'laklari, salat bargi, mayonez va ketchup souslari \n"
                    "Narxi: 23 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def longerrings(message: types.Message):
    user_id = message.from_user.id
    longerrings = message.text
    user_data[user_id]['longerrings'] = longerrings
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/longerrings.jpg"
    caption_text = ("Longer rings \n"
                    "Yumshoq bulochka, maxsus panirovka bilan qoplangan mayin aylanalari filesi (Halol), pomidor bo'laklari, tuzlangan bodring, salat bargi, mayonez va ketchup souslari \n"
                    "Narxi: 24 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def longerchiz(message: types.Message):
    user_id = message.from_user.id
    longerchiz = message.text
    user_data[user_id]['longerchiz'] = longerchiz
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/longerchiz.jpg"
    caption_text = ("Longer chiz \n"
                    "Yumshoq bulochka, maxsus panirovka bilan qoplangan mazali tovuq filesi (Halol), Chedder pishlog'i, pomidor bo'laklari, salat bargi, mayonez va ketchup souslari \n"
                    "Narxi: 25 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def montella(message: types.Message):
    user_id = message.from_user.id
    montella = message.text
    user_data[user_id]['montella'] = montella
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/montella.jpg"
    caption_text = ("Montella 0.33 \n\n"
                    "Narxi: 3 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def qora_choy(message: types.Message):
    user_id = message.from_user.id
    qora_choy = message.text
    user_data[user_id]['qora_choy'] = qora_choy
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/qora_choy.jpg"
    caption_text = ("Qora choy \n\n"
                    "Narxi:  5 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def kok_choy(message: types.Message):
    user_id = message.from_user.id
    kok_choy = message.text
    user_data[user_id]['kok_choy'] = kok_choy
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/kok_choy.jpg"
    caption_text = ("Ko'k choy \n\n"
                    "Narxi:  5 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def qora_limon(message: types.Message):
    user_id = message.from_user.id
    qora_limon = message.text
    user_data[user_id]['qora_limon'] = qora_limon
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/qora_limon.jpg"
    caption_text = ("Limonli qora choy \n\n"
                    "Narxi:  7 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def kok_limon(message: types.Message):
    user_id = message.from_user.id
    kok_limon = message.text
    user_data[user_id]['kok_limon'] = kok_limon
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/kok_limon.jpg"
    caption_text = ("Limonli ko'k choy \n\n"
                    "Narxi:  7 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def espresso(message: types.Message):
    user_id = message.from_user.id
    espresso = message.text
    user_data[user_id]['espresso'] = espresso
    await message.answer("Mahsulot hozircha mavjud emas.")
    print(user_data)

async def cola(message: types.Message):
    user_id = message.from_user.id
    cola = message.text
    user_data[user_id]['cola'] = cola
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/cola.jpg"
    caption_text = ("Coca-cola 0.5 \n\n"
                    "Narxi: 11 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def fanta(message: types.Message):
    user_id = message.from_user.id
    fanta = message.text
    user_data[user_id]['fanta'] = fanta
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/fanta.jpg"
    caption_text = ("Fanta 0.5 \n\n"
                    "Narxi: 11 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def sprite(message: types.Message):
    user_id = message.from_user.id
    sprite = message.text
    user_data[user_id]['sprite'] = sprite
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/sprite.jpg"
    caption_text = ("Sprite 0.5 \n\n"
                    "Narxi: 11 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def les_tea(message: types.Message):
    user_id = message.from_user.id
    les_tea = message.text
    user_data[user_id]['les_tea'] = les_tea
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/les_tea.jpg"
    caption_text = ("Les tea! \n"
                    "Apelsin va yalpiz bilan damlangan shakarli, qaynoq karkade choy. 300 ml \n"
                    "Narxi: 13 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def berry(message: types.Message):
    user_id = message.from_user.id
    berry = message.text
    user_data[user_id]['berry'] = berry
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/berry.jpg"
    caption_text = ("Frutea Berry mix \n"
                    "Qaynoq tozalangan ichimlik suvi, malina, smorodina, shakar. 300 ml \n"
                    "Narxi: 14 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def orange(message: types.Message):
    user_id = message.from_user.id
    orange = message.text
    user_data[user_id]['orange'] = orange
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/orange.jpg"
    caption_text = ("Frutea Orange \n"
                    "Qaynoq tozalangan ichimlik suvi, apelsi, zanjabil, asal, shakar. 300 ml \n"
                    "Narxi: 14 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def strawbery(message: types.Message):
    user_id = message.from_user.id
    strawbery = message.text
    user_data[user_id]['strawbery'] = strawbery
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/strawbery.jpg"
    caption_text = ("Frutea Strawberry \n"
                    "Qaynoq, tozalangan ichimlik suvi, qulupnay, rayhon yaproqlari, shakar. 300 ml \n"
                    "Narxi: 14 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def americano(message: types.Message):
    user_id = message.from_user.id
    americano = message.text
    user_data[user_id]['americano'] = americano
    await message.answer("Mahsulot hozircha mavjud emas.")
    print(user_data)

async def ays(message: types.Message):
    user_id = message.from_user.id
    ays = message.text
    user_data[user_id]['ays'] = ays
    await message.answer("Mahsulot hozircha mavjud emas.")
    print(user_data)

async def cappucino(message: types.Message):
    user_id = message.from_user.id
    cappucino = message.text
    user_data[user_id]['cappucino'] = cappucino
    await message.answer("Mahsulot hozircha mavjud emas.")
    print(user_data)

async def latte(message: types.Message):
    user_id = message.from_user.id
    latte = message.text
    user_data[user_id]['latte'] = latte
    await message.answer("Mahsulot hozircha mavjud emas.")
    print(user_data)

async def ays_milk(message: types.Message):
    user_id = message.from_user.id
    ays_milk = message.text
    user_data[user_id]['ays_milk'] = ays_milk
    await message.answer("Mahsulot hozircha mavjud emas.")
    print(user_data)

async def moxito(message: types.Message):
    user_id = message.from_user.id
    moxito = message.text
    user_data[user_id]['moxito'] = moxito
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/moxito.jpg"
    caption_text = ("New Moxito \n"
                    "Tabiiy, muzdek moxitoning yangi, yorqin ta'mi \n"
                    "Narxi: 26 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def berry_moxito(message: types.Message):
    user_id = message.from_user.id
    berry_moxito = message.text
    user_data[user_id]['berry_moxito'] = berry_moxito
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/berry_moxito.jpg"
    caption_text = ("Berry Moxito \n"
                    "Yorqin qulupnay ta'mli moxito \n"
                    "Narxi: 26 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def koulslou(message: types.Message):
    user_id = message.from_user.id
    koulslou = message.text
    user_data[user_id]['koulslou'] = koulslou
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/koulslou.jpg"
    caption_text = ("Koulslou \n"
                    "Oq karam, qizil sabzi, sirka, shakar va mayonez sousi. \n"
                    "Narxi: 11 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def sezam(message: types.Message):
    user_id = message.from_user.id
    sezam = message.text
    user_data[user_id]['sezam'] = sezam
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/sezam.jpg"
    caption_text = ("Sezam\n"
                    "Aysberg salati va yumshoqqina tovuq bo'lakchalari (Halol) solingan, kunjut urug'i sepilgan, ishtahaochar teriyaki sousidagi shirali salat. \n"
                    "Narxi: 25 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def les_barbeku(message: types.Message):
    user_id = message.from_user.id
    les_barbeku = message.text
    user_data[user_id]['les_barbeku'] = les_barbeku
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/les_barbeku.jpg"
    caption_text = ("Les Barbekyu \n"
                    "BBQ tovuq bo'lakchalari, ananas, aysberg salati, bodiring, rukkola va ishtahaochar teriyaki sousi \n"
                    "Narxi: 30 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def sezar_salat(message: types.Message):
    user_id = message.from_user.id
    sezar_salat = message.text
    user_data[user_id]['sezar_salat'] = sezar_salat
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/sezar_salat.jpg"
    caption_text = ("Sezar\n"
                    "Tovuq filesi (Halol), parmesan pishlog'i, cherri pomidori, suxari, aysberg salati, sezar sousi \n"
                    "Narxi: 30 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def grekcha(message: types.Message):
    user_id = message.from_user.id
    grekcha = message.text
    user_data[user_id]['grekcha'] = grekcha
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/grekcha.jpg"
    caption_text = ("Grekcha\n"
                    "Limon va rayhon sousli, salat barglari, pomidor, zaytun, bodring va fetaks pishloqli sarxil salat. \n"
                    "Narxi: 32 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)



async def blueberry(message: types.Message):
    user_id = message.from_user.id
    blueberry = message.text
    user_data[user_id]['blueberry'] = blueberry
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/blueberry.jpg"
    caption_text = ("Blueberry donut \n\n"
                    "Narxi: 17 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def caramel(message: types.Message):
    user_id = message.from_user.id
    caramel = message.text
    user_data[user_id]['caramel'] = caramel
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/caramel.jpg"
    caption_text = ("Caramel \n"
                    "Shirin karamel bilan to'ldirilgan donut\n"
                    "Narxi: 17 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def cinnamon(message: types.Message):
    user_id = message.from_user.id
    cinnamon = message.text
    user_data[user_id]['cinnamon'] = cinnamon
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/cinnamon.jpg"
    caption_text = ("Cinnamon\n\n"
                    "Narxi: 17 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def cookies(message: types.Message):
    user_id = message.from_user.id
    cookies = message.text
    user_data[user_id]['cookies'] = cookies
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/cookies.jpg"
    caption_text = ("Cookies\n\n"
                    "Narxi: 17 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def nutty_cream(message: types.Message):
    user_id = message.from_user.id
    nutty_cream = message.text
    user_data[user_id]['nutty_cream'] = nutty_cream
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/nutty_cream.jpg"
    caption_text = ("Nutty cream \n\n"
                    "Narxi: 17 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def panna_cotta(message: types.Message):
    user_id = message.from_user.id
    panna_cotta = message.text
    user_data[user_id]['panna_cotta'] = panna_cotta
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/panna_cotta.jpg"
    caption_text = ("Panna cotta \n\n"
                    "Narxi: 17 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def strawbery_donut(message: types.Message):
    user_id = message.from_user.id
    strawbery_donut = message.text
    user_data[user_id]['strawbery_donut'] = strawbery_donut
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/strawbery_donut.jpg"
    caption_text = ("Strawberry\n\n"
                    "Narxi: 17 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def kids_o(message: types.Message):
    user_id = message.from_user.id
    kids_o = message.text
    user_data[user_id]['kids_o'] = kids_o
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/kids_o.jpg"
    caption_text = ("Kids box longer O' \n"
                    "Longer-mini, fri kartoshkasi, sharbat 125 ml, o'yinchoq \n"
                    "Narxi: 44 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def kids_q(message: types.Message):
    user_id = message.from_user.id
    kids_q = message.text
    user_data[user_id]['kids_q'] = kids_q
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/kids_q.jpg"
    caption_text = ("Kids box longer Q \n"
                    "Longer-mini, fri kartoshkasi, sharbat 125 ml, o'yinchoq \n"
                    "Narxi: 44 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def lester_o(message: types.Message):
    user_id = message.from_user.id
    lester_o = message.text
    user_data[user_id]['lester_o'] = lester_o
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/lester_o.jpg"
    caption_text = ("Kids box lester O' \n"
                    "Mini lester, fri kartoshkasi, sharbat 125 ml, o'yinchoq \n"
                    "Narxi: 44 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def lester_q(message: types.Message):
    user_id = message.from_user.id
    lester_q = message.text
    user_data[user_id]['lester_q'] = lester_q
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/lester_q.jpg"
    caption_text = ("Kids box lester Q \n"
                    "Mini lester, fri kartoshkasi, sharbat 125 ml, o'yinchoq \n"
                    "Narxi: 44 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def ketchup(message: types.Message):
    user_id = message.from_user.id
    ketchup = message.text
    user_data[user_id]['ketchup'] = ketchup
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/ketchup.jpg"
    caption_text = ("Ketchup\n\n"
                    "Narxi: 4 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)


async def chili(message: types.Message):
    user_id = message.from_user.id
    chili = message.text
    user_data[user_id]['chili'] = chili
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/chili.jpg"
    caption_text = ("Chili\n\n"
                    "Narxi: 4 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def sezar_sous(message: types.Message):
    user_id = message.from_user.id
    sezar_sous = message.text
    user_data[user_id]['sezar_sous'] = sezar_sous
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/sezar_sous.jpg"
    caption_text = ("Sezar\n\n"
                    "Narxi: 4 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def chizi(message: types.Message):
    user_id = message.from_user.id
    chizi = message.text
    user_data[user_id]['chizi'] = chizi
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/chizi.jpg"
    caption_text = ("Chizi\n\n"
                    "Narxi: 4 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)

async def mayonez(message: types.Message):
    user_id = message.from_user.id
    mayonez = message.text
    user_data[user_id]['mayonez'] = mayonez
    button = [
        [types.InlineKeyboardButton(text="-", callback_data='-'),
         types.InlineKeyboardButton(text="1", callback_data='1'),
         types.InlineKeyboardButton(text="+", callback_data='+')],
        [types.InlineKeyboardButton(text="📥 Savatga qo'shish ✅", callback_data='text')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button, resize_keyboard=True)
    file_path = "image/mayonez.jpg"
    caption_text = ("Mayonez\n\n"
                    "Narxi: 4 000 soʻm")
    await message.answer("Miqdorini belgilang")
    await message.reply_photo(caption=caption_text,
        photo=types.FSInputFile(path=file_path), parse_mode='Markdown', reply_markup=keyboard)
    # await message.answer("", reply_markup=keyboard)
    print(user_data)







async def main():
    await dp.start_polling(bot)


print('The bot is running...')
asyncio.run(main())
