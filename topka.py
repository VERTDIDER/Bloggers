# def loveRate(user_id, user_info, count_of_posts) -> float:
#     user_followers_pk = cl.user_followers(user_id).keys()
#     followers_count = user_info.follower_count
#     medias = cl.user_medias(user_id, count_of_posts)
#     loverate_set: List[float] = list()
#     for media in medias:
#         count = 0
#         who_like = cl.media_likers(media.id)
#         who_like_pk = list()
#         for whois in who_like:
#             who_like_pk.append(whois.pk)
#         for item in who_like_pk:
#             if item in user_followers_pk:
#                 count += 1
#         x = float('{:.4}'.format(count / followers_count))
#         loverate_set.append(x)
#         print("done")
#     print(loverate_set)
#     return mean(loverate_set)


# def loveRate_v1(user_id, who_like_pk, followers_count: int):
#     # likes = media.like_count
#     user_followers_pk = cl.user_followers(user_id).keys()
#     count = 0
#     for item in who_like_pk:
#         if item in user_followers_pk:
#             count += 1
#     return '{:.1%}'.format(count / followers_count)

# def con():
#     try:
#         # Подключение к существующей базе данных
#         connection = psycopg2.connect(user="ilagorbacev",
#                                       # пароль, который указали при установке PostgreSQL
#                                       host="localhost",
#                                       port="5432",
#                                       database="ploshadka")
#
#         # Курсор для выполнения операций с базой данных
#         cursor = connection.cursor()
#         # Распечатать сведения о PostgreSQL
#         print("Информация о сервере PostgreSQL")
#         print(connection.get_dsn_parameters(), "\n")
#         # Выполнение SQL-запроса
#         cursor.execute("SELECT version();")
#         # Получить результат
#         record = cursor.fetchone()
#         print("Вы подключены к - ", record, "\n")
#
#     except (Exception, Error) as error:
#         print("Ошибка при работе с PostgreSQL", error)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#             print("Соединение с PostgreSQL закрыто")
