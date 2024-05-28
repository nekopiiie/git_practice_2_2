#Импортирую библиотеку
import telebot
from telebot import types
#Создаем бота в BotFather, копирую токен и всталяю в переменную. С помощью BotFather добавляю аватарку
#и приветствие
bot = telebot.TeleBot('6798268342:AAH246AonsFk87r-Q-4kR54Udh5aPqf3YMc')
#С помощью этого хэндлера мы принимаем сообщение пользователя и добавляем реакцию на него
@bot.message_handler (commands=['start'])
def start(message):
    #Тут мы добавляем первую клавиатуру и кнопки в клавиатуру. Эта клавиатура появляется после нажатия
    #кнопки start
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn = types.InlineKeyboardButton(text='Список маршрутов', callback_data='btn1')
    btn1 = types.InlineKeyboardButton(text='О команде CatStep', callback_data= 'btn2')
    kb.add(btn, btn1)
    bot.send_message(message.chat.id, 'Привет! Я Степа - ваш спутник по Санкт-Петербургу! Я помогу вам выбрать интересный маршрут по городу, чтобы отлично провести время! Мяу?', reply_markup=kb)
#С помощью этого хэндлера бот обрабатывает нажатие кнопки и реагирует на него
@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    # Добавляем реакцию на нажатие кнопки "Список маршрутов"
    if callback.data == 'btn1':
            marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn = types.KeyboardButton(text='Подворотни Санкт-Петербурга')
            btn1 = types.KeyboardButton(text='Здесь был Брат')
            btn2 = types.KeyboardButton(text='Санкт-Петербург Достоевского')
            btn3 = types.KeyboardButton(text='В Питере - жить')
            btn4 = types.KeyboardButton(text='В Питере - пить')
            btn5 = types.KeyboardButton(text='Вернуться в меню')
            marcup.add(btn, btn1,btn2,btn3,btn4,btn5)
            bot.send_message(callback.message.chat.id,'Выбери маршрут',reply_markup=marcup)
    #Добавляем реакцию на нажатие кнопки "О нас"
    elif callback.data == "btn2":
        bot.send_photo(callback.message.chat.id,r'https://psv4.userapi.com/c909618/u537061732/docs/d53/db5cedfa382e/my.jpg?extra=Hs80Nz8F4QBneBP9ob16Kz_HKAkJW9qZ0emAS3VVoQKMQAGU7iLaMZNeSD_D7pSZCtvc4lNK93WMKGn-gW3LTyy9V7kfY6zyp-OvsjQ1WOJE_8CRE35SSdf-PyUVQMvsSeguJwQWGNoiKuflpkMJp1w')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton(text='Вернуться в меню')
        marcup.add(btn5)
        bot.send_message(callback.message.chat.id, 'Мы студентки 2-го курса по направлению «Информационные технологии в дизайне» РГПУ им. Герцена создали этот бот по дисциплине «Технологии программирования».',reply_markup=marcup)

#Этот хэндлер обрабатывает сообщение пользователя
@bot.message_handler(content_types=['text'])
def get_text(message):
    #Добавляем реакцию на каждое сообщение, полученное при нажатии кнопки
    if message.text == 'Подворотни Санкт-Петербурга':
        #Добавляем фото
        bot.send_photo(message.chat.id,r'https://psv4.userapi.com/c237131/u537061732/docs/d47/5966f3211b82/1.jpg?extra=do2LiYFnFUaAozUYZeS13mi7p6gNDJZFjs1ZbEiNiFAZSMSNevLP_lEob7_875sjBL3GIWudVAR8tJN5YNBXeKjgkfXkbuAKXoRLX5ZKRa5emi_GF2tc_oM6SuKXIL2yc779tSxl6V3Zwyx0p8k_nFI','Подворотни Санкт-Петербурга - отдельный, тайный и многогранный мир. Маршрут “Подворотни Санкт-Петербурга” - это сборник уникальных мест, где каждый шаг может привести к неожиданному открытию. Вдруг, повернув за угол, вы найдете старинный дворик, где время словно остановилось: белье висит на верёвках, раскинутых между окнами старинных домов, а в уединённом углу могут играть дети или отдыхать на скамейке пожилые соседи. А за неприметными дверьми  и в подвалах необычных арт-объектов, крошечных музеев или частных галерей, где художники выставляют свои творения. Не упускайте возможность соприкоснуться с другой стороной истории Санкт-Петербурга!')
        #Добавляем клавиатуру
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Подворотня Джона Леннона')
        btn1 = types.KeyboardButton(text='Подворотня ресторанного дворика')
        btn2 = types.KeyboardButton(text='Подворотни Толстовского дома')
        btn3 = types.KeyboardButton(text='Подворотни из к/ф "Брат" ')
        btn4 = types.KeyboardButton(text='Подворотня Литейного проспекта')
        btn5 = types.KeyboardButton(text='Вернуться в меню')
        btn6 = types.KeyboardButton(text='Назад к маршрутам')
        marcup.add(btn, btn1, btn2, btn3, btn4, btn5,btn6)
        bot.send_message(message.chat.id, 'Выбери место, о котором хочешь узнать подробнее', reply_markup=marcup)

    elif message.text== 'Здесь был Брат':
       bot.send_photo(message.chat.id,r'https://psv4.userapi.com/c909418/u537061732/docs/d14/5d69f1543284/2.jpg?extra=ztxF6NPz4A6Gfn_tZYJDZ_RQmTRoFM7WiHy6KD_gjy17cFvmCeFuNCtN4BUFcWMeqV0X-MTumZXnTwlke-f92rB_vo3htt8s5ul0zcU8Fi5H4ZlB-pvb0gWB7kNZbI1cEkeNSt3UV-Zc1AxZuRvKEp4','Санкт-Петербург прославился красотами своей архитектуры: именно поэтому на его улицах так часто снимались известнейшие киноленты. Фильм, который знает каждый - “Брат”, режиссёра Алексея Балабанова. Пройдитесь по следам Сергея Бодрова-младшего, исполнившего роль главного героя, и погрузитесь в атмосферу 90-х, которую настолько тщательно и достоверно воссоздал режиссер. Маршрут "Здесь был брат" позволит вам проследить путь персонажа по городу, который стал не просто фоном для событий, но и полноценным участником сюжета.')
       marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
       btn = types.KeyboardButton(text='Тучков переулок')
       btn1 = types.KeyboardButton(text='Музыкальный магазин "Рок Остров" ')
       btn2 = types.KeyboardButton(text='Троицкий мост')
       btn3 = types.KeyboardButton(text='Дом Адамини')
       btn4 = types.KeyboardButton(text='Склеп Александра фон Бекмана')
       btn5 = types.KeyboardButton(text='Вернуться в меню')
       btn6 = types.KeyboardButton(text='Назад к маршрутам')
       marcup.add(btn, btn1, btn2, btn3, btn4, btn5, btn6)
       bot.send_message(message.chat.id, 'Выбери место, о котором хочешь узнать подробнее', reply_markup=marcup)

    elif message.text == 'Санкт-Петербург Достоевского':
        bot.send_photo(message.chat.id,r'https://psv4.userapi.com/c237331/u537061732/docs/d25/354262ee93aa/3.jpg?extra=lcc5Rx9Uj6bFio0U3D_fdN2zJCnVuNm7NUOCFBhDqdYfdjIONkJ-q4imYYBOUE146mwyxpV7zTNb_HN9aaMfY1Asp3fbFE1aCiSvQgFed2TjHrHCmVzH6uM036F9pHE_jAciqnfGgeEAp_wCBT2PJJ8','Жизнь и творчество Федора Михайловича Достоевского неотделимы от Петербурга. В своем творчестве писатель постоянно обращается к образу города, описывая его как мрачное, угрюмое место, враждебное человеку. Созданные им персонажи блуждают по узким, дождливым улицам, сталкиваясь с собственными страхами и искушениями, что делает городской пейзаж не просто фоном, но и активным участником литературной драмы.')#@bot.callback_query_handler(func=lambda callback: callback.data)
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Литературно-мемориальный музей Достоевского')
        btn1 = types.KeyboardButton(text='Памятник Достоевскому')
        btn2 = types.KeyboardButton(text='Сенная площадь')
        btn3 = types.KeyboardButton(text='Дом Раскольникова')
        btn4 = types.KeyboardButton(text='Дом старухи-процентщицы')
        btn5 = types.KeyboardButton(text='Вернуться в меню')
        btn6 = types.KeyboardButton(text='Назад к маршрутам')
        marcup.add(btn, btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, 'Выбери место, о котором хочешь узнать подробнее', reply_markup=marcup)

    elif message.text == 'В Питере - пить':
        bot.send_photo(message.chat.id,r'https://sun9-59.userapi.com/c237231/u537061732/docs/d50/f720d7009951/4.jpg?extra=OjcNIFFikI5c_IG0zDMorzIgcwpkTMvQkkYFo_vsjD4x-hftZWKncGcCtIrsI862WeMnwxmg3PesWmiqQtjVqBcg3rH8uRoM_XFjyC-Kq7sW36eUTj-J50NwMJB_0Kbb3_eJ33HCvtjnJipfggyZGHI',
                         'Петербург — столица баров и рюмочных, задающая тренды алкогольной культуры в России. Сказывается близость к Прибалтике и скандинавским странам. Именно здесь впервые начали возникать креативные пространства и клубы, где подача напитков стала настоящим искусством. Маршрут "В Питере - пить" предлагает погрузиться в мир петербургской ночной жизни, познакомиться с самыми необычными и стильными барами города, которые удивляют своими оригинальными коктейлями и уникальными интерьерами.')  # @bot.callback_query_handler(func=lambda callback: callback.data)
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text=' «Угрюмочная»')
        btn1 = types.KeyboardButton(text='Бар «812»')
        btn2 = types.KeyboardButton(text=' Бар «Анонимное общество усердных дегустаторов»')
        btn3 = types.KeyboardButton(text='Бар “El Copitas”')
        btn4 = types.KeyboardButton(text='Бар «Синий Пушкин»')
        btn5 = types.KeyboardButton(text='Вернуться в меню')
        btn6 = types.KeyboardButton(text='Назад к маршрутам')
        marcup.add(btn, btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, 'Выбери место, о котором хочешь узнать подробнее', reply_markup=marcup)

    elif message.text == 'В Питере - жить':
        bot.send_photo(message.chat.id,r'https://psv4.userapi.com/c909218/u537061732/docs/d32/79390d012ccf/5.jpg?extra=mmCp_7_3uFrHNAtu4Q2d2fYj57Z0-8JfepIe0MhJ4g1jWkQHYSnH1-DzBYny6fTk33p79vnROtzxmH1rB2eH4s4L0uj4oTNsPYqWiLhjTOeFxfwe8yJiNjRqJEQnQXpOyxX2ZSt_iAP68hETx9-v0Ak','Добро пожаловать в маршрут "В Питере - жить", где каждый шаг открывает новую страницу культурной жизни Санкт-Петербурга, предназначенный для молодых и творческих личностей, жаждущих вдохновения и новых впечатлений.')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Бертгольд центр')
        btn1 = types.KeyboardButton(text='Кафе Aster')
        btn2 = types.KeyboardButton(text='Оранжерея Таврического сада')
        btn3 = types.KeyboardButton(text='Севкабель порт')
        btn4 = types.KeyboardButton(text='Музей-фотосалон имени Карла Буллы')
        btn5 = types.KeyboardButton(text='Вернуться в меню')
        btn6 = types.KeyboardButton(text='Назад к маршрутам')
        marcup.add(btn, btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, 'Выбери место, о котором хочешь узнать подробнее', reply_markup=marcup)

    elif message.text == 'Вернуться в меню':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn = types.InlineKeyboardButton(text='Список маршрутов', callback_data='btn1')
        btn1 = types.InlineKeyboardButton(text='О команде CatStep', callback_data='btn2')
        kb.add(btn, btn1)
        bot.send_message(message.chat.id,
                         'Привет! Я Степа - ваш спутник по Санкт-Петербургу! Я помогу вам выбрать интересный маршрут по городу, чтобы отлично провести время! Мяу?',
                         reply_markup=kb)
    elif message.text=='Назад к маршрутам':
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Подворотни Санкт-Петербурга')
        btn1 = types.KeyboardButton(text='Здесь был Брат')
        btn2 = types.KeyboardButton(text='Санкт-Петербург Достоевского')
        btn3 = types.KeyboardButton(text='В Питере - жить')
        btn4 = types.KeyboardButton(text='В Питере - пить')
        btn5 = types.KeyboardButton(text='Вернуться в меню')
        marcup.add(btn, btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'Выбери маршрут', reply_markup=marcup)
    elif message.text == 'Назад к маршруту 1':
        bot.send_photo(message.chat.id,
                       r'https://psv4.userapi.com/c237131/u537061732/docs/d47/5966f3211b82/1.jpg?extra=do2LiYFnFUaAozUYZeS13mi7p6gNDJZFjs1ZbEiNiFAZSMSNevLP_lEob7_875sjBL3GIWudVAR8tJN5YNBXeKjgkfXkbuAKXoRLX5ZKRa5emi_GF2tc_oM6SuKXIL2yc779tSxl6V3Zwyx0p8k_nFI',
                       'Подворотни Санкт-Петербурга - отдельный, тайный и многогранный мир. Маршрут “Подворотни Санкт-Петербурга” - это сборник уникальных мест, где каждый шаг может привести к неожиданному открытию. Вдруг, повернув за угол, вы найдете старинный дворик, где время словно остановилось: белье висит на верёвках, раскинутых между окнами старинных домов, а в уединённом углу могут играть дети или отдыхать на скамейке пожилые соседи. А за неприметными дверьми  и в подвалах необычных арт-объектов, крошечных музеев или частных галерей, где художники выставляют свои творения. Не упускайте возможность соприкоснуться с другой стороной истории Санкт-Петербурга!')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Подворотня Джона Леннона')
        btn1 = types.KeyboardButton(text='Подворотня ресторанного дворика')
        btn2 = types.KeyboardButton(text='Подворотни Толстовского дома')
        btn3 = types.KeyboardButton(text='Подворотни из к/ф "Брат" ')
        btn4 = types.KeyboardButton(text='Подворотня Литейного проспекта')
        btn5 = types.KeyboardButton(text='Вернуться в меню')
        btn6 = types.KeyboardButton(text='Назад к маршрутам')
        marcup.add(btn, btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, 'Выбери место, о котором хочешь узнать подробнее', reply_markup=marcup)

    elif message.text == 'Назад к маршруту 2':
        bot.send_photo(message.chat.id,
                       r'https://psv4.userapi.com/c909418/u537061732/docs/d14/5d69f1543284/2.jpg?extra=ztxF6NPz4A6Gfn_tZYJDZ_RQmTRoFM7WiHy6KD_gjy17cFvmCeFuNCtN4BUFcWMeqV0X-MTumZXnTwlke-f92rB_vo3htt8s5ul0zcU8Fi5H4ZlB-pvb0gWB7kNZbI1cEkeNSt3UV-Zc1AxZuRvKEp4',
                       'Санкт-Петербург прославился красотами своей архитектуры: именно поэтому на его улицах так часто снимались известнейшие киноленты. Фильм, который знает каждый - “Брат”, режиссёра Алексея Балабанова. Пройдитесь по следам Сергея Бодрова-младшего, исполнившего роль главного героя, и погрузитесь в атмосферу 90-х, которую настолько тщательно и достоверно воссоздал режиссер. Маршрут "Здесь был брат" позволит вам проследить путь персонажа по городу, который стал не просто фоном для событий, но и полноценным участником сюжета.')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Тучков переулок')
        btn1 = types.KeyboardButton(text='Музыкальный магазин "Рок остров" ')
        btn2 = types.KeyboardButton(text='Троицкий мост')
        btn3 = types.KeyboardButton(text='Дом Адамини')
        btn4 = types.KeyboardButton(text='Склеп Александра фон Бекмана')
        btn5 = types.KeyboardButton(text='Вернуться в меню')
        btn6 = types.KeyboardButton(text='Назад к маршрутам')
        marcup.add(btn, btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, 'Выбери место, о котором хочешь узнать подробнее', reply_markup=marcup)

    elif message.text == 'Назад к маршруту 3':
        bot.send_photo(message.chat.id,
                       r'https://psv4.userapi.com/c237331/u537061732/docs/d25/354262ee93aa/3.jpg?extra=lcc5Rx9Uj6bFio0U3D_fdN2zJCnVuNm7NUOCFBhDqdYfdjIONkJ-q4imYYBOUE146mwyxpV7zTNb_HN9aaMfY1Asp3fbFE1aCiSvQgFed2TjHrHCmVzH6uM036F9pHE_jAciqnfGgeEAp_wCBT2PJJ8',
                       'Жизнь и творчество Федора Михайловича Достоевского неотделимы от Петербурга. В своем творчестве писатель постоянно обращается к образу города, описывая его как мрачное, угрюмое место, враждебное человеку. Созданные им персонажи блуждают по узким, дождливым улицам, сталкиваясь с собственными страхами и искушениями, что делает городской пейзаж не просто фоном, но и активным участником литературной драмы.')  # @bot.callback_query_handler(func=lambda callback: callback.data)
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Литературно-мемориальный музей Достоевского')
        btn1 = types.KeyboardButton(text='Памятник Достоевскому')
        btn2 = types.KeyboardButton(text='Сенная площадь')
        btn3 = types.KeyboardButton(text='Дом Раскольникова')
        btn4 = types.KeyboardButton(text='Дом старухи-процентщицы')
        btn5 = types.KeyboardButton(text='Вернуться в меню')
        btn6 = types.KeyboardButton(text='Назад к маршрутам')
        marcup.add(btn, btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, 'Выбери место, о котором хочешь узнать подробнее', reply_markup=marcup)

    elif message.text == 'Назад к маршруту 4':
        bot.send_photo(message.chat.id,
                       r'https://psv4.userapi.com/c909218/u537061732/docs/d32/79390d012ccf/5.jpg?extra=mmCp_7_3uFrHNAtu4Q2d2fYj57Z0-8JfepIe0MhJ4g1jWkQHYSnH1-DzBYny6fTk33p79vnROtzxmH1rB2eH4s4L0uj4oTNsPYqWiLhjTOeFxfwe8yJiNjRqJEQnQXpOyxX2ZSt_iAP68hETx9-v0Ak',
                       'Добро пожаловать в маршрут "В Питере - жить", где каждый шаг открывает новую страницу культурной жизни Санкт-Петербурга, предназначенный для молодых и творческих личностей, жаждущих вдохновения и новых впечатлений.')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Бертгольд центр')
        btn1 = types.KeyboardButton(text='Кафе Aster')
        btn2 = types.KeyboardButton(text='Оранжерея Таврического сада')
        btn3 = types.KeyboardButton(text='Севкабель порт')
        btn4 = types.KeyboardButton(text='Музей-фотосалон имени Карла Буллы')
        btn5 = types.KeyboardButton(text='Вернуться в меню')
        btn6 = types.KeyboardButton(text='Назад к маршрутам')
        marcup.add(btn, btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, 'Выбери место, о котором хочешь узнать подробнее', reply_markup=marcup)

    elif message.text == 'Назад к маршруту 5':
        bot.send_photo(message.chat.id,
                       r'https://sun9-59.userapi.com/c237231/u537061732/docs/d50/f720d7009951/4.jpg?extra=OjcNIFFikI5c_IG0zDMorzIgcwpkTMvQkkYFo_vsjD4x-hftZWKncGcCtIrsI862WeMnwxmg3PesWmiqQtjVqBcg3rH8uRoM_XFjyC-Kq7sW36eUTj-J50NwMJB_0Kbb3_eJ33HCvtjnJipfggyZGHI',
                       'Петербург — столица баров и рюмочных, задающая тренды алкогольной культуры в России. Сказывается близость к Прибалтике и скандинавским странам. Именно здесь впервые начали возникать креативные пространства и клубы, где подача напитков стала настоящим искусством. Маршрут "В Питере - пить" предлагает погрузиться в мир петербургской ночной жизни, познакомиться с самыми необычными и стильными барами города, которые удивляют своими оригинальными коктейлями и уникальными интерьерами.')  # @bot.callback_query_handler(func=lambda callback: callback.data)
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text=' «Угрюмочная»')
        btn1 = types.KeyboardButton(text='Бар «812»')
        btn2 = types.KeyboardButton(text=' Бар «Анонимное общество усердных дегустаторов»')
        btn3 = types.KeyboardButton(text='Бар “El Copitas”')
        btn4 = types.KeyboardButton(text='Бар «Синий Пушкин»')
        btn5 = types.KeyboardButton(text='Вернуться в меню')
        btn6 = types.KeyboardButton(text='Назад к маршрутам')
        marcup.add(btn, btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, 'Выбери место, о котором хочешь узнать подробнее', reply_markup=marcup)

    elif message.text=='Подворотня Джона Леннона':
        bot.send_photo(message.chat.id,r'https://psv4.userapi.com/c237131/u537061732/docs/d43/ba4025f54198/1-1.jpg?extra=PfcTBKbtOJAgths9-BV29lRrOafFVtajMxtYMAiMZm_rlNjh41kf4xrqXjV17AFSJwYQ_noT_06a22Y33cvpBx4Ef8fxoVrsOFxPJukdeBX74m-DzW7EeRI-LDWxXC9JZFHY4MxSJQbZNocMqHcSZjA', 'Подворотня Джона Леннона - одна из самых известных подворотен Петербурга, которая посвящена творчеству легендарной группы The Beatles и её создателю Джону Леннону. Не посетить это место  - не побывать в Петербурге!Эта подворотня украшена граффити с портретами музыкантов, цитатами из их песен и разнообразными арт-объектами, вдохновленными эпохой хиппи и творчеством «ливерпульской четверки». Это место стало своеобразным алтарем для поклонения и вдохновения, где фанаты могут оставлять послания и мемориальные знаки. Атмосфера места наполнена ностальгией и теплом, притягивая не только старшие поколения, но и молодежь, желающую прикоснуться к легенде.Посещение такой подворотни оставит неизгладимое впечатление и добавит особый оттенок в переживания от пребывания в городе. И хотя времена The Beatles далеко позади, подворотня стала живым свидетельством того, как их творчество продолжает вдохновлять новые поколения. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 1')
        marcup.add(btn)
        bot.send_message(message.chat.id,'Чтобы вернуться к маршруту, нажми кнопку',reply_markup=marcup)

    elif message.text=='Подворотня ресторанного дворика':
        bot.send_photo(message.chat.id,r'https://psv4.userapi.com/c237131/u537061732/docs/d56/2b241938e145/1-2.jpg?extra=-c7qdUZZn-MbfBpSKnsDdL4a6A13PHX4DHfhc-0wXOxuVvDM2rFnx3k5RKSB1AEGUevXsYUXo3V3yMTzGzpW4Sj9Iy4f-_pDHGWVjWL_RuHKJ2Ki4aneTcTQzXb_SpvV5IE2Qfs8KXfQpl-qd5Uvsko','На Лиговском проспекте, в нескольких метрах от арки на улицу Пушкинская (Джона Леннона) ближе к Невскому проспекту, есть вход в так называемый «ресторанный дворик», который соединён с проспектом необычной подворотней со своей уникальной атмосферой. Эта подворотня, переливающаяся разнообразием стилей и эпох, представляет собой узкую, но живописную аллею, по бокам которой расположены милые ресторанчики, кафе и бистро. Стены, украшенные уличным искусством, отражают дух современного города, в то время как каждый заведение вносит свою изюминку в общую картину.')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 1')
        marcup.add(btn)
        bot.send_message(message.chat.id,'Чтобы вернуться к маршруту, нажми кнопку',reply_markup=marcup)
    elif message.text=='Подворотни Толстовского дома':
        bot.send_photo(message.chat.id,r'https://psv4.userapi.com/c237131/u537061732/docs/d8/0719fd2d9b6d/1-3.jpg?extra=dk50i5xFsecvvauRDnTGgyeIx4R5I_H8L3SUxAPn10XzyiDfLCyjMh33nmLhI0Fs0HkdKO4GOqys4vBUHoGrYMbMuM7aS2zQl7OSBI0__rttUTBItUbUhF1CF07VtgEO_0OxAyNRZ5ulS19CQ-bPUqM','Всем любителям неформального Петербурга знаком величественный дом Толстова с его сквозными арками, уходящими в высоту на несколько метров. Дом Толстова — огромное, статное и благородное 6-этажное здание, постренное в начале XX века в стиле модерн. Это архитектурный шедевр, который притягивает взгляды как туристов, так и жителей города. Сохранив свою первозданную красоту и украшения, дом Толстова является свидетельством роскошной эпохи и мастерства архитекторов того времени.')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 1')
        marcup.add(btn)
        bot.send_message(message.chat.id,'Чтобы вернуться к маршруту, нажми кнопку',reply_markup=marcup)
    elif message.text=='Подворотни из к/ф "Брат"':
        bot.send_photo(message.chat.id,r'https://psv4.userapi.com/c237131/u537061732/docs/d25/5bfb53643162/1-4.jpg?extra=O6dvSdvpawgeyZFw3Kow8AzQRGS_xcuEl0KA-eiTLdrWPZZkREuGJC1RuVdLzHqS6Bdxbfe7XKxM_pJGiugDbjT3iXARf18EtMne7X_BUg52PtwdasKwpBKmVELp77uJvJx5IqbnU51oOsYfPoBJYMs','Кинофильм «Брат» – истинное олицетворение Петербурга 90-х годов. Проникнуться атмосферой петербуржского криминала и бандитизма можно, заглянув на Тучков переулок. Именно в этих дворах снималась одна из сцен фильма, когда главный герой, Данила Багров, играемый Сергеем Бодровым-младшим, идёт по темным и мрачным улицам, отражающим суровую реальность того времени. Заброшенные здания и старая брусчатка Тучкова переулка создают неповторимый фон, который выражает тяжелую атмосферу постсоветской России.')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 1')
        marcup.add(btn)
        bot.send_message(message.chat.id,'Чтобы вернуться к маршруту, нажми кнопку',reply_markup=marcup)
    elif message.text=='Подворотня Литейного проспекта':
        bot.send_photo(message.chat.id,'https://psv4.userapi.com/c237131/u537061732/docs/d18/9df4ad13a274/1-5.jpg?extra=ZU5kZ9bCkg12rmpmLuIA6yI3l4_IaAtFhWXHCvCqrPT6IQIXLCbHrUu7DO44LrnWRX0-MwR61ubYXmDSvVpTQb7OuyCPQVyCXFBVInvvtv_qxptquWU2QmevS1nAjVv0PCF9OTn2_cd33sGyR_CZaf0','В отличие от знакомого питерского «колодца» граффити-двор на Литейном – настоящая художественная галерея современного уличного искусства! В 2007 году во дворе прошёл фестиваль Montana Jam – первый граффити фестиваль в Санкт-Петербурге, который собрал талантливых художников со всего мира. Тогда и началась история этого необычного места, которое постепенно превратилось в открытую платформу для самовыражения и экспериментов в области граффити и стрит-арта. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 1')
        marcup.add(btn)
        bot.send_message(message.chat.id,'Чтобы вернуться к маршруту, нажми кнопку',reply_markup=marcup)
    elif message.text=='Тучков переулок':
        bot.send_photo(message.chat.id,'https://psv4.userapi.com/c909418/u537061732/docs/d53/2dc263952755/2-1.jpg?extra=NsOEoCz9oFUYoVOqo0PoMCXibQcHO1GRbxBZEVPK0itaJpBXXPnzvm0SD6A3_Af0b3TJ87pUA1aNsOJGnrdzmgdyC5m0z-acTWkbqPrj5E4MtMiJHxqMsqSgcLYQw4oRxX7PCgbf2OBRrgEbQR-HA6s','Кинофильм «Брат» – истинное олицетворение Петербурга 90-х годов. Проникнуться атмосферой петербуржского криминала и бандитизма можно, заглянув на Тучков переулок. Именно в этих дворах снималась одна из сцен фильма, когда главный герой, Данила Багров, играемый Сергеем Бодровым-младшим, идёт по темным и мрачным улицам, отражающим суровую реальность того времени. Заброшенные здания и старая брусчатка Тучкова переулка создают неповторимый фон, который выражает тяжелую атмосферу постсоветской России. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 2')
        marcup.add(btn)
        bot.send_message(message.chat.id,'Чтобы вернуться к маршруту, нажми кнопку',reply_markup=marcup)
    elif message.text=='Музыкальный магазин "Рок остров"':
        bot.send_photo(message.chat.id,'https://psv4.userapi.com/c909418/u537061732/docs/d43/204a12a5e6b0/2-2.jpg?extra=69G_d5fRE99_DhQQna4ubcZ1DEoRpfIoBwxFEZyBjxBzmCINb3RDtnyq0GYHmxd6jtU4F8JnTST-8mpYNMhAdGG8IUZC55T7n8CcVtFKOKUEBtMKbP1OQW1o46e-H4IZ9Zjm3Od_7Ox2X7aQLqkpf90','Музыкальный магазин «Рок Остров», в который Данила заходил за дисками группы «Наутилус Помпилиус», существует до сих пор (правда, интерьер изменился). Магазин открылся в 1992 году, пережил взлёт и падение формата CD, а теперь представляет собой не просто розничную точку, но и своеобразный культурный центр для меломанов и коллекционеров. В «Рок Острове» можно найти не только классические CD и виниловые пластинки, но и эксклюзивные музыкальные издания, раритетные записи и атрибутику любимых групп. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 2')
        marcup.add(btn)
        bot.send_message(message.chat.id,'Чтобы вернуться к маршруту, нажми кнопку',reply_markup=marcup)
    elif message.text=='Троицкий мост':
        bot.send_photo(message.chat.id,'https://psv4.userapi.com/c909418/u537061732/docs/d6/1b7172dbcf73/2-3.jpg?extra=ohFW4vmMskwvR6WdxqCvbmF_IpTFZsjbDchuSM-hm67afOUKnUCM7Ga7HZ_o8AdSQJE3-EsJ_RrzCWxUfyf041OugiiM67Qolbt0lOoQjZEH7LdS30lKQRiT6AV3UvFXoEa-Xjd5ay0JlOfPVuD4DgU','В первый день в городе Данила обходит главные достопримечательности. Мы видим его переходящим по мосту Зимнюю канавку, задирающим голову перед Медным всадником, возле Исаакиевского и Казанского соборов. Самые яркие впечатления, однако, он получает, оказавшись на Троицком мосту. Этот мост является одним из символов Санкт-Петербурга и открывает великолепные виды на город. Пройдя по мостовой, Данила погружается в размышления, наблюдая за бесконечным потоком Невы, которая несёт свои воды мимо грандиозных архитектурных ансамблей. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 2')
        marcup.add(btn)
        bot.send_message(message.chat.id,'Чтобы вернуться к маршруту, нажми кнопку',reply_markup=marcup)
    elif message.text=='Дом Адамини':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c909418/u537061732/docs/d56/f5f0d7fcdb6b/2-4.jpg?extra=P3o0R1vy2o2J4XJPHAxNTiVWJJVHTaKJvXj88UDgx82IqRd3t5PIwO_sd7yigjpearL2vqu-Nn15_YrwHi4CYXg1sOrac63rMWodeBdZIutoxy2oMp0JkSIPDqtbKSwcUHXmt5XUkpDFdM-a7Iywt_U',
                       'Мы точно знаем, где поселился брат Данилы Багрова, став «большим человеком в Ленинграде». Этот адрес называет Данила: «Я брата ищу… Мне мать его адрес дала: Мойка, 1, квартира 8». Дом, в котором живёт (с видом на Спас-на-крови), является одним из знаменитых архитектурных памятников Санкт-Петербурга. Дом Адамини, расположенный на реке Мойке, — это выдающийся образец классической архитектуры, возведенный в начале 19 века. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 2')
        marcup.add(btn)
        bot.send_message(message.chat.id,'Чтобы вернуться к маршруту, нажми кнопку',reply_markup=marcup)

    elif message.text=='Литературно-мемориальный музей Достоевского':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c237331/u537061732/docs/d13/bc52494d40e4/3-1.jpg?extra=uDsojjeY2XwDrgf8YA5ap3dciIokpfPzbqC-D7hWacopMuLeyIS11rTYThFRNlxKHFQaShotKVr5Pvop60FJKNw0FHVJVeXLap0a6a2VWb1VzM-Xi5VjIhwJHYTqfRvEXQjzLIcNls5Aj9yzlVv0YotNow',
                        'Музей разместился в доме, где писатель жил в 1846 г. и с 1878 года до самой смерти(1881).  Мемориальная квартира Достоевского воссоздана по воспоминаниям современников. Литературная экспозиция посвящена жизни и творчеству писателя, рассказывает о важнейших событиях его биографии и ключевых моментах его литературной деятельности. В музее представлены личные вещи Достоевского, его рукописи, первые издания произведений, портреты и фотографии. Посетители могут увидеть рабочий стол писателя, на котором он работал над "Братьями Карамазовыми", и его личную библиотеку, где хранятся издания, которые он читал и цитировал. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 3')
        marcup.add(btn)
        bot.send_message(message.chat.id,'Чтобы вернуться к маршруту, нажми кнопку',reply_markup=marcup)

    elif message.text=='Склеп Александра фон Бекмана':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c909418/u537061732/docs/d38/09a986bd1030/2-5.jpg?extra=UVni-6CMwDR7eiIArAwQiH1pn-Z57BJKSXMvKSe2SOia1zw-T7ecmeVhD_NP5x_s0cKJL30HZOuQynBJ3qzDwLlhAfCrPFPVFWaMm5p6rFbupagZMjUYD_GKCFrrbSiQDh2VMlnu6BI598BnPECUp4M',
                       'Немец ведёт Данилу к себе домой на Смоленское лютеранское кладбище. Здесь похоронены предки Немца и здесь живёт он сам. Железная беседка, в которой собираются бездомные, — склеп, возведённый в 1880-е для генерал-майора Александра фон Бекмана. Этот склеп в фильме превратился в своеобразное жилище для Немца, отражающее его особнякость и отрешенность от обыденной жизни. Стены склепа покрыты мхом и лишены былого великолепия, но все еще хранят тягостное величие и тишину, свойственную месту последнего упокоения.')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 2')
        marcup.add(btn)
        bot.send_message(message.chat.id,'Чтобы вернуться к маршруту, нажми кнопку',reply_markup=marcup)

    elif message.text == 'Памятник Достоевскому':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c237331/u537061732/docs/d60/07bd15f6257d/3-2.jpg?extra=0Xh5RUgALgNOzf9mDaLBdIAJf_3ZcxwMVhGxYFeuTZ_FcDtJB4nRswLQZTiucWhxHpadvsL1rutLeNoVyQUGpLWBceJaPJsltfFW-w7TTJDgRbTRCG_h8Xj8tE6vPDNvMpT7DjR-JV_b0ysm9_fj6F6ZNw',
                        'Открыт 30 мая 1997г., скульпторы Л. М. Холина, П. П. Игнатьев, арх. В. Л. Спиридонов. На полутораметровом постаменте из розового полированного гранита изображен задумчиво сидящим и чуть сгорбившимся писатель и мыслитель, погруженный в свои раздумья. Федор Михайлович Достоевский предстает перед зрителями в момент творческой работы, окруженный неотъемлемыми атрибутами своего времени и личной жизни. Памятник расположен в непосредственной близости от места, где писатель провел последние годы своей жизни, и где сейчас находится литературно-мемориальный музей Достоевского.')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 3')
        marcup.add(btn)
        bot.send_message(message.chat.id, 'Чтобы вернуться к маршруту, нажми кнопку', reply_markup=marcup)
    elif message.text == 'Сенная площадь':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c237331/u537061732/docs/d44/1952e0ec2cb3/3-3.jpg?extra=28otZKXPkYH78GgPeBrYP2CFlprgmfE3yzXgzNg6Kj3haXKezRBGsfYxvb6EX7RfhHhkXiA_c3V_7PrdreGVN87o6degxL21pOblYwlnl9BDNBL59W0fM-IhSfP85Vge_mA84SINPT-kzRip_wyz2zNv4A',
                        'Все места, где происходило действие романа “Преступление и наказание”, сгруппированы вокруг Сенной площади. Во времена Достоевского здесь находился самый дешёвый в городе рынок, где торговали сеном, соломой и дровами. Сенная площадь и окрестные улицы были известны своей бедностью и переполненностью, что создавало плодородную почву для социального неравенства и преступности — темы, активно исследованные Достоевским в его произведениях. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 3')
        marcup.add(btn)
        bot.send_message(message.chat.id, 'Чтобы вернуться к маршруту, нажми кнопку', reply_markup=marcup)

    elif message.text == 'Дом Раскольникова':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c237331/u537061732/docs/d58/e5364af1737e/3-4.jpg?extra=-6wkUg0MtXd9CjeF3qoORLfOvY8xTebqXWjxnB4wdaRPX1Q1V9tc-la-SLO9ELDELSaujVo3BhASXYxObbUTMt92HAhQb2hccOjSYfDKR4x3ARDDJVRyL2XRurAO3pOCL_tGotalut0GnFjWvEnqunpHeg',
                        'Дом на пересечении Гражданской улицы и Столярного переулка по праву называют “началом начал”: именно здесь начинается действие романа “Преступление и наказание”. Каморка Раскольникова находилась под самой крышей этого дома, и именно отсюда он отправляется на свои мрачные раздумья и совершает роковой поступок. Достоевский с такой точностью описывает маршруты своего героя, что читатели и сегодня могут воспроизвести его путь, пройдясь по улицам, которые мало изменились с тех пор.')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 3')
        marcup.add(btn)
        bot.send_message(message.chat.id, 'Чтобы вернуться к маршруту, нажми кнопку', reply_markup=marcup)
    elif message.text == 'Дом старухи-процентщицы':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c237331/u537061732/docs/d7/d234edfbd7a2/3-5.jpg?extra=SQTA944MaEjTluX5jghmkzNa6N7_kGKIYkcP7upvrDcw2XXDu4ocUvNUKXnNePGW3GnjsvM0NLjU2dmKko4PpyXYhlfpGnkKHbXITWKUM9IVXnkaVhKACMjQFZ-t-MkK9tlfldUTvAWbC9wBBUlTsP6E1w',
                        'Ровно 730 шагов насчитал Раскольников от своих ворот до двери старухи-процентщицы. Алёна Ивановна с сестрой занимала две комнаты в простом доходном доме: квартиры тут сдавались мелким чиновникам, ремесленникам, кухаркам. Этот маршрут, пройденный Раскольниковым в состоянии внутреннего напряжения и тревоги перед совершением преступления, стал одной из ключевых сцен в романе. Дом, где жила старуха-процентщица, в романе описывается как типичное для того времени жилище, расположенное в переполненном и не самом благополучном районе города. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 3')
        marcup.add(btn)
        bot.send_message(message.chat.id, 'Чтобы вернуться к маршруту, нажми кнопку', reply_markup=marcup)
    elif message.text == 'Бертгольд центр':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c909218/u537061732/docs/d44/db5e3929740a/5-1.jpg?extra=k5e1iVR5NxI7C0BHo7Q5baXCdgu7TUmeBBBG2wflGzAZhIFtba_i50hkVOduKIad3WadjvjnDLJueGpApoOYXyteoWsgg7lfvJbVoNz4JrXdqM9r8QCjuxjHFnNm45ITgINNtyBddXjlDZpoJNY3vz-j1w',
                        'Место представляет собой целый публичный арт-кластер с множеством мини-баров, кофеен и досуговых мест, также есть множество магазинчиков крафтовых сувениров. Много посадочных мест на улице - летние веранд от каи ресторанов приглашают гостей насладиться напитками и блюдами на свежем воздухе, наслаждаясь видами города и наблюдая за местной жизнью. Посетители могут ожидать увидеть здесь живые выступления уличных музыкантов, которые добавляют атмосферы и динамизма. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 4')
        marcup.add(btn)
        bot.send_message(message.chat.id, 'Чтобы вернуться к маршруту, нажми кнопку', reply_markup=marcup)
    elif message.text == 'Кафе Aster':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c909218/u537061732/docs/d38/db9aff296076/5-2.jpg?extra=5xMO-naA9rFMy7R51s_sK48kwWT3IiavfMkeKkzHer6zgkypc-6Pk02kLkT-vPsZNxkiGeyLyHcgeRMtTwFvX1KJf-JM3vPoFGwh1mdYw-7iv2fjsG7xXDs5X4MkqHtih4XMZT9MjTejG4aQH3K5dvU0fw',
                        'Молодое городское кафе с основательными завтраками, мощной кофейной картой и собственной пекарней. Фанатичный подход к кофе - дело рук энтузиаста Ирины Шариповой. Поэтому на брю-баре предлагают целых пять блендов под воронку, миксы с колдбрю и каскарой. В "Aster" каждый кофейный напиток — это результат тщательной работы и подбора оптимальных сочетаний зерен, обжарки и метода заваривания, что позволяет открывать новые грани привычного вкуса. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 4')
        marcup.add(btn)
        bot.send_message(message.chat.id, 'Чтобы вернуться к маршруту, нажми кнопку', reply_markup=marcup)
    elif message.text == 'Оранжерея Таврического сада':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c909218/u537061732/docs/d18/bb21e2fcd31e/5-3.jpg?extra=sc1Oxh_9VsPEw93jd20be1OwxPMjgcRA2aZTtHaClEGSETjBaxBIgZ0t01rxe3f3kivOCo0XBG8JYzuEWoutbnpQ9P5_1CJwIENl3SHu5-I5IcFjFnI62zhe0CaRJ6fIJGXvhZtiWv7obG9ZUYTbJRVrsQ',
                        'Оранжерея Таврического сада - царство лета, тропических цветов и величественных деревьев. Оранжерея спроектирована английским мастером садоводства Уильямом Гульдом по личному распоряжению императрицы Екатерины Великой и является одной из доминантных архитектурных структур в саду. Это место, где можно найти убежище от холодных петербургских зим, окунувшись в теплую атмосферу вечнозелёных растений. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 4')
        marcup.add(btn)
        bot.send_message(message.chat.id, 'Чтобы вернуться к маршруту, нажми кнопку', reply_markup=marcup)
    elif message.text == 'Севкабель порт':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c909218/u537061732/docs/d37/b65e0ea292f0/5-4.jpg?extra=3AGFJsv74Cj378SXIcL-d5FjNCJ_I4VEfT3IQ_NMOPt6N0eVWspv4Y4BFXZfWg2GQFZFtE-hZ-J68dAZ2QQ0KRS0o9lycg66OHdNz5qz97vOnnjnYhTG4LyWyjDIDg5_gO-hFecqTBcHurlU-gIP9OaROg',
                        'Общественное пространство «Севкабель Порт» открылось в Санкт-Петербурге в 2018 году и сразу завоевало огромную любовь местных жителей и туристов. Еще бы! Здесь необычно все: и местоположение, и архитектура, и атмосфера. Располагается «Севкабель Порт» прямо у Финского залива, на окраине Васильевского острова. Именно здесь можно полюбоваться морскими закатами, которые являются одними из самых живописных в городе. Архитектурный ансамбль «Севкабель Порта» сочетает в себе исторические здания бывшего кабельного завода с современными элементами и арт-объектами, создавая неповторимое индустриальное пространство для отдыха и творчества. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 4')
        marcup.add(btn)
        bot.send_message(message.chat.id, 'Чтобы вернуться к маршруту, нажми кнопку', reply_markup=marcup)
    elif message.text == 'Музей-фотосалон имени Карла Буллы':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c909218/u537061732/docs/d21/5afdc7b57920/5-5.jpg?extra=_0D_Tx5EKSD5BBaSZ8sJ9axQMvBReJEw1sJARhsqiI-MTe2Ocl3Vf9whT2ND3LX1Lm_dy0bBJuTHOg85qL9kGoQA3Tr11PzX4-MkYeIAe-oYSA8sJaYQttJhDK2A1kAhS69VngcIdN6YiRD4j_ZBz81e5A',
                        'Фотосалон-музей имени Карла Буллы - это одно из старейших фотоателье Санкт-Петербурга. Сегодня здесь располагается фотосалон, музей и фонд исторической фотографии. Имеется смотровая площадка, с которой отрывается отличный вид на городские крыши и улицы, позволяющий посетителям ощутить атмосферу старого Петербурга. Основанный Карлом Буллой, фотографом, получившим известность благодаря своим портретам выдающихся личностей и бытовым снимкам городской жизни, фотосалон и по сей день хранит его наследие. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 4')
        marcup.add(btn)
        bot.send_message(message.chat.id, 'Чтобы вернуться к маршруту, нажми кнопку', reply_markup=marcup)

    elif message.text == '«Угрюмочная»':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c237231/u537061732/docs/d58/3c65b09d8203/4-1.jpg?extra=v__BV6oSARM90FepmK5TyR6wOMLuivXg-AWNLKg85W7XGIk143Te8QBZLH_e0A1Pbn-Zi0E28buSDj0A0zmVaWtW7WNpK-OrYLVesO6EvLb3KwLYpmdYayx2-t1xKT-_xleroOSPJWdxvGwGG8KaShPvCg',
                        'Пересекаем Невский проспект и направляемся в сторону улиц Жуковского, Маяковского, Некрасова и Белинского, где сосредоточились жемчужины алкогольной карты Петербурга. По дороге несложно заметить вывеску «Угрюмочная», где подают десятки видов разливного пива и закусок к нему, создавая атмосферу настоящего питерского паба. Улицы Жуковского и Маяковского известны своими барами и клубами, которые работают до рассвета, предлагая гостям поистине бесконечное разнообразие досуга. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 5')
        marcup.add(btn)
        bot.send_message(message.chat.id, 'Чтобы вернуться к маршруту, нажми кнопку', reply_markup=marcup)
    elif message.text == 'Бар «812»':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c237231/u537061732/docs/d21/63c50164b34d/4-2.jpg?extra=z_EbOE5cNRD48-nm0r4rKwzV36GMQecuRY8axJpY94MbnGtB3f0AqbYv0vVHOxMLgAhnXVtyxcJUNsxuugnL0ChSmqXGstTiGvBdPOgvHRyIWhk-SsNsIUg3N04oXYuzQ0lAIH5I6bXo6Q9b_gS7pRgv9A',
                        'Это один из самых креативных коктейль-баров в Петербурге, который прославился своими вкусными авторскими коктейлями и веселой профессиональной командой барменов. Камерная обстановка, простой интерьер, красивые светильники и мягкая музыка создают расслабленную атмосферу, где каждый посетитель может почувствовать себя как дома. Бар предлагает не только классические коктейли, но и смелые эксперименты с необычными ингредиентами, которые удивят даже опытных любителей миксологии.')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 5')
        marcup.add(btn)
        bot.send_message(message.chat.id, 'Чтобы вернуться к маршруту, нажми кнопку', reply_markup=marcup)
    elif message.text == 'Бар «Анонимное общество усердных дегустаторов»':
        bot.send_photo(message.chat.id,
                       'https://sun9-44.userapi.com/c237231/u537061732/docs/d37/ac174bf1d1ba/4-3.jpg?extra=QVw-j1op-UAMTMQeYVzJSd4uV-uiEzbs-C0eGh69UsECGb7FDbey4LvigVSUTUiq0eKcm8a3DJavJcG0xet927s9BSjD-8BlIuLsZ7QdLtFaCcyvSLFosBiXyFMti8pi0k--T7roYQKIOaorJelyr1CBEg',
                        'Добравшись до улицы Рубинштейна, нужно непременно заглянуть в эту эстетскую рюмочную. Бар «Анонимных дегустаторов» (сокращенно — АД) визуально и идеологически разделен на две зоны: на темной стороне расположена рюмочная с широким выбором самых разных видов водки и настоек, где вы можете попробовать классические русские закуски, такие как соленые огурцы и сельдь под шубой. Освещение здесь приглушенное, создавая интригующую атмосферу, которая приглашает гостей к более интимному и сосредоточенному вкусовому опыту. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 5')
        marcup.add(btn)
        bot.send_message(message.chat.id, 'Чтобы вернуться к маршруту, нажми кнопку', reply_markup=marcup)
    elif message.text == 'Бар “El Copitas”':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c237231/u537061732/docs/d50/74b127887a5e/4-4.jpg?extra=wSwAF-x-gG-Vm1mZQrZheO19_--CJf8XLiYB16v8T-EAmPqzIpk3GGdFH3Y9H24ZsDh3kZhjlf7YV6dQn6yvg7mEtVSKxCzk4WrhoheqrrKSLqNYECT01GodOlsmW0IX3Ww2TZZG0wDMbVGIyPbaft6swQ',
                        'Этот бар известен на весь Петербург как «лучший бар страны». Звание это — нисколько не преувеличение: в 2018 году «El Сopitas» занял 39-е место в рейтинге пятидесяти лучших баров мира. Попасть сюда можно только по предварительной записи, что делает визит еще более эксклюзивным. Интерьер «El Copitas» выполнен в стиле мексиканской кантины, а в меню представлены оригинальные коктейли, вдохновленные латиноамериканскими традициями. Здесь подают аутентичные мексиканские закуски, которые идеально сочетаются с сильными и ароматными напитками. ')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 5')
        marcup.add(btn)
        bot.send_message(message.chat.id, 'Чтобы вернуться к маршруту, нажми кнопку', reply_markup=marcup)
    elif message.text == 'Бар «Синий Пушкин»':
        bot.send_photo(message.chat.id,
                       'https://psv4.userapi.com/c237231/u537061732/docs/d28/4b2034ea77b4/4-5.jpg?extra=3Ay4N0ARy0ba9BnJXpfO7RpbQ9aH3QKTm-ihW-O65YbnY0Ure5F5LdJ9JvMDewtargvafET-kDApiE6dwkAdEqMpWri4gT-gWq_yajXU5EFow3BArYLgeI5VeNManI7t3M6ddSj5aoYwMeG8tqwvL-dLJg',
                        'Свернув на Жуковского, заходим в бар «Синий Пушкин», заказываем «ассорти настоек», выпиваем их (желательно не все в одного — иначе ваша барная прогулка закончится ранее ожидаемого) и двигаемся дальше. В этом месте царит уют и домашняя атмосфера, а «ассорти настоек» предлагает широкий выбор вкусов — от классических ягодных вариантов до более экзотических, с травами и специями. Сидя за старинными деревянными столами, можно почувствовать себя частью некой литературной сцены, вдохновленной творчеством великих русских писателей.')
        marcup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton(text='Назад к маршруту 5')
        marcup.add(btn)
        bot.send_message(message.chat.id, 'Чтобы вернуться к маршруту, нажми кнопку', reply_markup=marcup)

bot.polling()