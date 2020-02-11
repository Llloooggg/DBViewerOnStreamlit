import streamlit as st
import pymysql
from re import match

connection = pymysql.connect(
    host='localhost',
    user='UserForDBViewerOnStreamlit',
    password='123',
    db='DBForDBViewerOnStreamlit'
)


def main(connection=connection):

    def string_check(string):

        if match('^[0-9A-Za-zA-Яa-яЁё -"/_]*$', string) and string:
            return True
        else:
            return False

    def all_table_elements(TableName):

        with connection:
            query = 'SELECT * FROM ' + TableName
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query)
            rowsList = cursor.fetchall()
            return rowsList

    usersList = all_table_elements('Users')

    listToDisplay = []
    for i in range(len(usersList)):
        listToDisplay.append(
            str(usersList[i]['UserID']) + ' ' + usersList[i]['UserName'])

    st.title('Создание заявок')
    choice = st.selectbox('Выберите пользователя', listToDisplay)
    ticketText = st.text_area('Введите текст заявки')
    AddButton = st.button('Создать')

    if AddButton:
        if string_check(ticketText):
            with connection:
                cursor = connection.cursor()
                cursor.execute('INSERT INTO Tickets (TicketText, UserID) VALUES (\'' +
                               ticketText + '\' , \'' + choice.split(' ')[0] + '\')')
            st.text('Заявка создана!')
        else:
            st.text('Некорректный ввод!')


if __name__ == "__main__":
    main()
