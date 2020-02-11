import streamlit as st
import pymysql
import modules.mainPage
import modules.ticketsViewer
import modules.ticketsMaker
import modules.usersEditor


connection = pymysql.connect(
    host='localhost',
    user='UserForDBViewerOnStreamlit',
    password='123',
    db='DBForDBViewerOnStreamlit'
)

st.sidebar.title('Навигация')
pages = st.sidebar.radio('Страницы', ['Главная',
                                      'Просмотр заявок',
                                      'Создание заявок',
                                      'Управление пользователями']
                         )


def main():

    if pages == 'Главная':
        modules.mainPage.main()
    elif pages == 'Просмотр заявок':
        modules.ticketsViewer.main(connection)
    elif pages == 'Создание заявок':
        modules.ticketsMaker.main(connection)
    elif pages == 'Управление пользователями':
        modules.usersEditor.main(connection)


if __name__ == "__main__":
    main()
