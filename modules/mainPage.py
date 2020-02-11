import streamlit as st
from PIL import Image


def main():

    st.title('Добро пожаловать в просмотрщик базы даных')
    st.write('Вас приветствует простое приложение для работы с бд')

    image = Image.open('./media/image.png')
    st.image(image, use_column_width=True)


if __name__ == "__main__":
    main()
