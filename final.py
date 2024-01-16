import streamlit as st
import webbrowser
import pandas as pd
import streamlit_pandas as sp
from PIL import Image
import plotly.express as px
import numpy as np
import pickle


# icon = Image.open(r"C:\Users\ADMIN\Downloads\photo_2023-12-15_22-33-02.jpg")
st.set_page_config(page_title="Final_retail_sales_forecast",
                # page_icon= icon,  
                   layout="wide", initial_sidebar_state="auto") 
df=pd.read_csv(r"C:\Users\ADMIN\Videos\capstion_project\final_project\data_analysis.csv")

with st.sidebar:
    st.sidebar.markdown("# :rainbow[Select an option to filter:]")
    selected = st.selectbox("**Menu**", ("Home","Analysis","prediction",'data_frame'))
    
    
if selected=="Home":
    st.markdown('## :green[welcome to Home page:]')
    with st.form(key = 'form',clear_on_submit=False):   
        st.markdown('## :blue[Project Title:]')
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Final_retail_sales_forecast ")
        st.markdown('## :blue[Skills takes away From This project:]')
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Data Wrangling, EDA, Model Building, Model Deployment")
        st.markdown('## :blue[Domain:]')
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Retail_Sales")
        st.markdown('## :blue[Problem:]')
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1. Predict the department-wide sales for each store for the following year.")
        # st.subheader('following year.')
        st.subheader('&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;2. Model the effects of markdowns on holiday weeks.')
        st.subheader('&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;3. Provide recommended actions based on the insights drawn, with prioritization ')
        st.subheader('placed on largest business impact.')

        link="https://github.com/Muthukumar0908/Industrial-Copper-Modeling.git"
        link1='https://www.linkedin.com/in/muthukumar-r-44848416b/'
        colum3,colum4,colum5= st.columns([0.015,0.020,0.1])
        with colum3:
            if st.form_submit_button('GidHub',use_container_width=True):
                webbrowser.open_new_tab(link)
        with colum4:
            if st.form_submit_button("LinkedIn",use_container_width=True):
                webbrowser.open_new_tab(link1)

    
if selected=="Analysis":
    colum3,colum4= st.columns([1,1])
    with colum3:
        data=df.groupby(['year']).sum(['MarkDown']).sort_values("MarkDown")
        # data
        fig = px.bar(data, y='MarkDown', x=data.index,title="total MarkDown in year:",color="MarkDown")
        # fig.show()
        st.plotly_chart(fig,use_container_width=True) 
    with colum4:
        data=df.groupby(['year']).sum(['Weekly_Sales']).sort_values("Weekly_Sales")
        # data
        fig = px.bar(data, y='Weekly_Sales', x=data.index,title="total Weekly_Sales in year:")
        # fig.show()
        st.plotly_chart(fig,use_container_width=True)         
    
    
    
    data=df.groupby(['Date']).sum(['MarkDown']).sort_values("MarkDown")
    # data
    fig = px.line(data, y='MarkDown', x=data.index,title="total MarkDown in weak_wize:")
    # fig.show()
    st.plotly_chart(fig,use_container_width=True) 
    
    
    
    data=df.groupby(['Month']).sum(['MarkDown'])
    # data
    fig = px.line(data, y='MarkDown', x=data.index,title="total MarkDown in month vize line plot:")
    # fig.show()
    st.plotly_chart(fig,use_container_width=True)  
    
    data=df.groupby(['Month']).sum(['Weekly_Sales'])
    # data
    fig = px.line(data, y='Weekly_Sales', x=data.index,title="total Weekly_Sales in month vize line plot:")
    # fig.show()
    st.plotly_chart(fig,use_container_width=True)
    
    colum3,colum4= st.columns([1.5,1])
    with colum3:
        data=df.groupby(['Month']).sum(['Fuel_Price'])
        # data
        fig = px.bar(data, y='Fuel_Price', x=data.index,title="total fule_price in month vize bar plot:",color=data.index)
        # fig.show()
        st.plotly_chart(fig,use_container_width=True) 
    with colum4:
        data=df.groupby(['Month']).sum(['Fuel_Price']).sort_values('Fuel_Price',ascending=False).head(10)
        # data
        fig = px.bar(data, y='Fuel_Price', x=data.index)
        # fig.show()
        st.plotly_chart(fig,use_container_width=True)        
    
    colum3,colum4= st.columns([1,1.5])
    with colum4:
        data=df.groupby(['Month']).sum(['CPI'])
        # data
        fig = px.bar(data, y='CPI', x=data.index,color=data.index)
        # fig.show()
        st.plotly_chart(fig,use_container_width=True)

    with colum3:
        data=df.groupby(['Month']).sum(['CPI']).sort_values('CPI',ascending=False).head(10)
        # data
        fig = px.bar(data, y='CPI', x=data.index,title="total CPI in month vize bar plot:")
        # fig.show()
        st.plotly_chart(fig,use_container_width=True) 
    
    fig=px.scatter(df, x="Weekly_Sales", y="MarkDown", animation_frame="Month", animation_group="Store",
                size="MarkDown", color="Store",log_x=True, size_max=55,range_y=[0,135000],range_x=[5000,145000],
                title="Store vize total_markdown in month:")
    fig1=px.bar(df, x="Store", y="Weekly_Sales", color="Type", 
                    animation_frame="Month", animation_group="Store",range_y=[0,100000],title="type vize total weekly_sales for month:")
    # fig.show()
    # fig1.show()
    st.plotly_chart(fig,use_container_width=True) 
    st.plotly_chart(fig1,use_container_width=True) 
    colum3,colum4= st.columns([1,1])
    with colum3:
        fig = px.histogram(df, x="IsHoliday", y="Weekly_Sales",
                color='Type', barmode='group',title="weekly holiday vize total sales price:"
                )
        fig.show() 
        st.plotly_chart(fig,use_container_width=True)  
    
    with colum4:
        date_calculate=df['weekly_sales_date'].value_counts()
        date_vize_analysis=pd.DataFrame({
            'weakly_dates':date_calculate.index,
            'high_sales_date':date_calculate.values
        }).sort_values('high_sales_date',ascending=False)
        date_vize_analysis['date']=np.nan
        k=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        for i,j in zip(range(0,7),range(0,7)):
        #     print(i,j)
            date_vize_analysis.loc[(date_vize_analysis['weakly_dates']==i),'date'] = k[j]
        # st.dataframe(date_vize_analysis)
        fig=px.bar(date_vize_analysis,x="date",y=date_vize_analysis['high_sales_date'],color='date')
        # fig.show()
        st.plotly_chart(fig,use_container_width=True) 


if selected=="prediction": 
    lis=[]
    with open(r"C:\Users\ADMIN\Videos\capstion_project\final_project\random_regression.pkl",'rb') as file:
        Result = pickle.load(file)
    
    column1,column2 = st.columns([2,2], gap = 'small')
    min_Temperature = df['Temperature_fahr'].min()
    max_Temperature = df['Temperature_fahr'].max()
    min_Fuel_Price = df['Fuel_Price'].min()
    max_Fuel_Price = df['Fuel_Price'].max()
    min_CPI = df['CPI'].min()
    max_CPI = df['CPI'].max()
    min_Unemployment= df['Unemployment'].min()
    max_Unemployment = df['Unemployment'].max()
    min_weekly_sales_date = df['week_of_number'].min()
    max_weekly_sales_date = df['week_of_number'].max()
    min_MarkDown = df['MarkDown'].min()
    max_MarkDown = df['MarkDown'].max()
    with column1:

        Store = st.selectbox("**Select a Store Id:**",options = df['Store'].unique())
        Temperature_fahr = st.number_input(f'**Enter Temperature_fahr: (Minimum : {min_Temperature}, Maximun : {max_Temperature})**')
        Fuel_Price = st.number_input(f'Enter Fuel_Price:')  #(Minimum : {min_Fuel_Price}, Maximun : {max_Fuel_Price})**
        CPI = st.number_input(f'**Enter CPI (Minimum : {min_CPI}, Maximun : {max_CPI})**')
        Unemployment = st.number_input(f'**Enter Unemployment  (Minimum : {min_Unemployment}, Maximun : {max_Unemployment})**')
        IsHoliday = st.selectbox("**Select a IsHoliday Id:**",options = df['IsHoliday'].unique())

    with column2:
        
        Dept = st.selectbox("**Select a Dept Id:**",options = df['Dept'].unique())
        Type = st.selectbox("Select a Type:",options = df['Type'].unique())
        MarkDown = st.number_input(f'Enter MarkDown:') # (Minimum : {min_MarkDown}, Maximun : {max_MarkDown})**
        week_of_number = st.number_input(f'**Enter week number:(Minimum : {min_weekly_sales_date}, Maximun : {max_weekly_sales_date})**')
        year = st.number_input('Enter the year:')
    lis.append(int(Store))
    lis.append(Temperature_fahr)
    lis.append(Fuel_Price)
    lis.append(CPI)
    lis.append(Unemployment)  
      
    a,b= 0.00,1.00
    if IsHoliday ==False:
        lis.append(a)
    if IsHoliday ==True:
        lis.append(b)
    lis.append(int(Dept))
    c,d,e = 0.0,1.0,2.0
    if Type == "A":
        lis.append(c)
    if Type =="B":
        lis.append(d)
    if Type == "C":
        lis.append(e)
    lis.append(MarkDown)     
    lis.append(year)
    lis.append(week_of_number)   
    
    # st.write(lis)
    
    if st.button("submit"): 
            y=np.array([lis])
            k=Result.predict(y)
            
            st.markdown(f"# :green[Prediction of weekly sales price is: :red['{k}']]")
            
            
if selected== "data_frame":
    # with st.form(key = 'form',clear_on_submit=False):
        st.markdown("## :green[Filter the Data]")
        @st.cache_data
        def df12():
            # df1=pd.read_csv(r"C:\Users\ADMIN\Videos\capstion_project\final_project\clean_dataset.csv").drop(columns=['Month',"week_of_number",'day','month'])
            df1=pd.read_csv(r"C:\Users\ADMIN\Videos\capstion_project\final_project\data_filtering.csv").drop(columns='date')
            return df1
        df7=df12()
        # st.dataframe(df7)
        
        create_data={"Store":"multiselect",
                    "CPI":"multiselect",
                    'Fuel_Price':"multiselect",
                    "Dept":"multiselect",
                    "Date":'multiselect',
                    "Type":'multiselect',
                    'date_name':"multiselect",
                    'year':'multiselect',
                    'IsHoliday':'multiselect'
                    }
        
        
        
        all_widgets=sp.create_widgets(df7,create_data)
        try:
            res=sp.filter_df(df7,all_widgets)
            if st.button("submit"):
                st.dataframe(res,use_container_width=True)
        except:
            st.warning("No Data in this filter")
           
           
           
           
           
           
           
           
   