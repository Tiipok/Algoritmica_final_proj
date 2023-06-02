import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mat


df = pd.read_csv('events.csv')

print(df.info())

# фильтруем данные
df['day'] = df['visit_date'].apply(lambda x: x[0:2]) 

df['month'] = df['visit_date'].apply(lambda x: x[3:5])


def format(url):
    data = url.split('/')

    if len(data) < 5: str_val = 'without format'

    else:

        if data[4] =='': str_val = 'without format'
        else: str_val = data[4]

    return str_val

df['format'] = df['URL_visited'].apply(format)


def material(url):
    data = url.split('/')
    if len(data) < 6:
        str_val = 'without material'
    else:
        if data[5] =='':
            str_val = 'without material'
        else:
            str_val = data[5]
            
    return str_val

df['material'] = df['URL_visited'].apply(material)


def submaterial(url):
    data = url.split('/')
    str_val = 'without material'

    if len(data) == 6:
        str_val = f'the only one lesson({data[5]})'    

    if len(data) == 8:

        if data[7] =='':
            str_val = f'the only one lesson({data[5]})'

        else:
            str_val = f'{data[7]}({data[5]})'

    return str_val

df['submaterial'] = df['URL_visited'].apply(submaterial)


# создаем таблицы
plt1 = df[(df['format']=='courses') & (df['submaterial']!='without material')].groupby(['submaterial'])['user_id'].count().sort_values(ascending=False)

plt2 = df[(df['month']=='02')].groupby('day')['user_id'].count().agg(['min','mean', 'max'])

plt3 = df[(df['month']=='02')].groupby('day')['user_id'].count() 

plt4 = df[df['format']!='without format']['format'].value_counts()

plt5 = df[(df['format']=='courses') & (df['material']!='without material')].groupby(['material'])['user_id'].count().sort_values(ascending=False)

plt6 = df.groupby('month')['user_id'].count().sort_values(ascending=False)

plt7 = df[df['format']=='video'].groupby(['material'])['user_id'].count().sort_values(ascending=False)

plt8 = df[df['format']=='trajectory'].groupby(['material'])['user_id'].count().sort_values(ascending=False)

plt9 = df[df['format']=='category'].groupby(['material'])['user_id'].count().sort_values(ascending=False)


# выводим таблицы
mat.rcParams['figure.subplot.left'] = 0.6
plt1.iloc[0:10].plot(kind='barh', title='Топ 10 самых посещаемых уроков')
plt.show()

mat.rcParams['figure.subplot.left'] = 0.2
plt2.plot(kind='barh', title='Статистика посещений за один день в феврале')
plt.show()

plt3.plot(kind='line', title='Количество посещений по дням за февраль')
plt.grid()
plt.show()

mat.rcParams['figure.subplot.left'] = 0.3
plt4.plot(kind='barh', title='Топ посещаемости по разделам')
plt.show()

mat.rcParams['figure.subplot.left'] = 0.4 
plt5.iloc[0:10].plot(kind='barh', title='Топ 10 самых посещаемых курсов')
plt.show()

mat.rcParams['figure.subplot.left'] = 0.2
plt6.plot(kind='barh', title='Топ месяцев по количеству посещений в месяц')
plt.show()

mat.rcParams['figure.subplot.left'] = 0.2
plt7.iloc[0:10].plot(kind='barh', title='Топ 10 самых посещаемых видео (номера)')
plt.show()

plt8.iloc[0:10].plot(kind='barh', title='Топ 10 самых посещаемых направлений')
plt.show()

plt9.iloc[0:10].plot(kind='barh', title='Топ посещения по категориям')
plt.show()


'''Для полноценного анализа данных о юзерах, которые перестали учиться, мне не хватает информации 
о том, на какие курсы они были записаны и на сколько времени был рассчитан срок их обучения.'''

