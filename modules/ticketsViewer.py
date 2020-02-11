import streamlit as st
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='UserForDBViewerOnStreamlit',
    password='123',
    db='DBForDBViewerOnStreamlit'
)


def main(connection=connection):

    def all_table_elements(TableName):

        with connection:
            query = 'SELECT * FROM ' + TableName
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query)
            rowsList = cursor.fetchall()
            return rowsList

    def filtered_tickets(userID):

        with connection:
            query = 'SELECT * FROM Tickets WHERE UserID IN (' + userID + ')'
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query)
            userTickets = cursor.fetchall()
            return userTickets

    usersList = all_table_elements('Users')
    st.title('Список пользователей и их заявок')
    st.dataframe(usersList)

    listToDisplay = []
    for i in range(len(usersList)):
        listToDisplay.append(
            str(usersList[i]['UserID']) + ' ' + usersList[i]['UserName'])

    filterBox = st.checkbox('Фильтр по пользователю')
    if filterBox:
        choice = st.selectbox(
            'Выберите пользователя для просмотра его заявок', listToDisplay)
        if choice is not None:
            userTickets = filtered_tickets(choice.split(' ')[0])
            st.dataframe(userTickets)
    else:
        st.dataframe(all_table_elements('Tickets'))


if __name__ == "__main__":
    main()
