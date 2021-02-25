import streamlit as st
import pandas as pd
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

def get_data():
    data = "https://github.com/alioh/Saudi-Districts-Dataset/raw/main/riyadh_districts.csv"
    df = pd.read_csv(data)
    return df

df = get_data()

st.title('Saudi Arabia Districts Dataset')
st.write("This dataset is a collection of files related to Saudi Arabia's districts. The data were collected manually from This data includes general information about districts of the Kingdom of Saudi Arabia, such as the number of residents, the proportion of Saudis and foreigners, the distribution of males and females, in addition to the average income. Data were collected manually from [Nine Tenths](https://map.910ths.sa/).")
st.write("## Credit")
st.write("[Ali Alohali](http://alioh.com), [Sara AlSiyat](http://linkedin.com/in/saraalsiyat), [Ibrahim AlHammad](http://linkedin.com/in/ibrahim-alhammad-7228b3178), [Nora AlAmri](https://www.linkedin.com/in/nora-alamri) and [Rawan AlMohimeed](https://www.linkedin.com/in/rawanmohimeed).")

st.write("## Thanks")
st.write("Thanks to the following contributors:")

st.markdown(
    """
    **Name**|**contribution**
:-----:|:-----:|
[Dr. Najwa Alghmadi](https://www.najwa-alghamdi.net/)|Providing most of Lat/Long data.
""")


st.write("## Data")
st.write("[GitHub link](https://github.com/alioh/Saudi-Districts-Dataset)")




agree = st.checkbox("Show all data")
if agree:
    st.write(df, value = True)

selectBox = st.selectbox(
        "Which district you want to know more about?",
        df["District_name_EN"].unique() ,
    )

district = df[df['District_name_EN'] == selectBox]

agree = st.checkbox("Show selected district data")
if agree:
    st.write(district, value = True)

googlemaps = f'https://www.google.com/maps/search/{district["latitude"].values[0]}+{district["longitude"].values[0]}'

# map
st.map(district, zoom=11)

st.markdown(f"<h6 style='text-align: right;'><a href={googlemaps}>View on Google maps</a></h6>", unsafe_allow_html=True)

# data stacked to graph
districtStacked = district.stack().reset_index()
districtStacked.columns=['index', 'Column', 'Value']
allExpectDistrict = df[df['District_name_EN'] != selectBox]
averageIncomeAll = pd.DataFrame([[0,"All_Districts_Average_Income", allExpectDistrict[['Average_Income']].mean().values[0]]], columns=['index','Column','Value'])
districtStacked = pd.concat([districtStacked, averageIncomeAll])

gender = districtStacked[districtStacked['Column'].isin(['Males', 'Females'])]
nationality = districtStacked[districtStacked['Column'].isin(['Saudis', 'Non_Saudis'])]
income = districtStacked[districtStacked['Column'].isin(['Average_Income', 'All_Districts_Average_Income'])]

# nationality graph
ax = sns.barplot(x="Column", y="Value", data=nationality)

for p in ax.patches:
    ax.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center', va='center', fontsize=11, color='white', xytext=(0, -10),
        textcoords='offset points')

ax.set_title('Nationality Distribution')
ax.set(xlabel='Nationality', ylabel='Total')
st.pyplot()

# gender graph
ax = sns.barplot(x="Column", y="Value", data=gender)

for p in ax.patches:
    ax.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center', va='center', fontsize=11, color='white', xytext=(0, -10),
        textcoords='offset points')

ax.set_title('Gender Distribution')
ax.set(xlabel='Gender', ylabel='Total')
st.pyplot()

# income graph

ax = sns.barplot(x="Column", y="Value", data=income)

for p in ax.patches:
    ax.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center', va='center', fontsize=11, color='white', xytext=(0, -10),
        textcoords='offset points')

ax.set_title('District Income VS All District Average Income')
ax.set(xlabel='Income', ylabel='Average')
st.pyplot()
