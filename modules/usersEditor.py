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

        if match('^[-0-9A-Za-zA-Яa-яЁё ]*$', string) and not ("\\" in string) and string:
            return True
        else:
            st.text(
                'Некорректный ввод! Строка должно включать русские или английские буквы, цифры или дефис')
            return False

    def all_table_elements(TableName):

        with connection:
            query = 'SELECT * FROM ' + TableName
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query)
            rowsList = cursor.fetchall()
            return rowsList

    def user_add(userName):

        if not string_check(userName):
            return False

        with connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO Users (UserName) VALUES (\'' + userName + '\')')
        return True

    def user_delete(user):

        if not string_check(user):
            return False

        with connection:
            cursor = connection.cursor()
            try:
                cursor.execute(
                    'DELETE FROM Users WHERE UserID IN (' + str(user.split(' ')[0]) + ')')
            except Exception:
                st.text('Польователь \"' + str(user) +
                        '\" отсутствует или не может быть удален!')
                return False
        return True

    st.title('Управление пользоватлями')
    usersList = all_table_elements('Users')
    userName = st.text_input('Введите имя нового пользователя')
    addButton = st.button('Добавить')
    user = st.text_input(
        'Введите ID и полное имя удаляемого пользователя через пробел')
    deleteButton = st.button('Удалить')

    if addButton:
        if user_add(userName):
            st.text('Польователь \"' + userName + '\" успешно добавлен!')
            usersList = all_table_elements('Users')

    if deleteButton:
        if user_delete(user):
            st.text('Польователь \"' + str(user) +
                    '\" удален или отсутствовал!')
            usersList = all_table_elements('Users')
    st.dataframe(usersList)


if __name__ == "__main__":
    main()
