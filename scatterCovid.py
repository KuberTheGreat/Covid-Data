import pandas as pd
import plotly.express as px

dataFrame = pd.read_csv('covid_data.csv')

figure = px.area(dataFrame, x = 'date', y = 'cases', title = 'Covid cases in Countries', color = 'country')

figure.show()