import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

# Название
# Описание
st.title("Fill the blanks")
st.sidebar.write("Upload your dataframe and fill the blanks")


## Шаг 1 Загрузка данных
uploaded_file=st.sidebar.file_uploader('Drag and drop your file here or click to upload',type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df.head(5))
else:
    st.stop()

## Шаг 2 Проверка наличия пропусков в файле
missed_values=df.isna().sum()
missed_values=missed_values[missed_values>0]
# st.write(missed_values)

if len(missed_values)>0:
    fig,ax=plt.subplots()
    sns.barplot(x=missed_values.index,y=missed_values.values)
    ax.set_title('Blanks in columns')
    ax.set_ylabel("Quantity of blanks")
    ax.set_xlabel("Name of columns with blanks")
    st.pyplot(fig)
    if len(missed_values)>0:
        button=st.button("fill the blanks")
        if button:
    ## Шаг 3 Заполните пропуски

            df_filled=df[missed_values.index].copy()
            
            for col in missed_values.index:
                if df_filled[col].dtype=='object':
                    df_filled[col]=df_filled[col].fillna(df_filled[col].mode()[0])
                else:
                    df_filled[col]=df_filled[col].fillna(df_filled[col].mean())
            st.write(df_filled)

    ## Шаг 4 Выгрузить заполненный от пропусков scv-файл

            download_but=st.download_button("Download CSV",data=df_filled.to_csv(),file_name="filled_file")
else:
    st.write("Нет пропусков данных")
    st.stop()
