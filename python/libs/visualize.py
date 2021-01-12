from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.express as px

import plotly.io as pio
pio.templates.default = 'none'

def compare_both_by_year(dataframe, subset='deaths', start=1833, end=1849):

    dataframe = dataframe[dataframe['year'].between(start, end)]
    dataframe = dataframe.sum()
	
    if start == end:
    	year = start
    else:
    	year = f"{start} to {end}"
    title = f'Comparing total {subset} of both clinics ({year})'
    
    labels = ['First clinic', 'Second clinic']
    values = [dataframe['first_'+subset], dataframe['second_'+subset]]
    print()
    print(title)
    print('********************************************************************')
    print(f'Total {subset} cases in the "First clinic" \t: {values[0]}')
    print(f'Total {subset} cases in the "Second clinic" \t: {values[1]}')
    print(f'Difference \t\t\t\t\t: {values[0]-values[1]} ({round(values[0]/values[1], 1)} times)')
    # Subplots
    fig = make_subplots(
        rows=1, cols=2,
        specs=[[{"type":"xy"},{"type":"pie"}]]
    )
    # Bar plot 
    fig.add_trace(
        go.Bar(
            x=labels,
            y=values,
            name='Total ' + subset,
            showlegend=False
        ),
        row=1, col=1
    )
    # Pie chart
    fig.add_trace(
        go.Pie(
            labels=labels,
            values=values
        ),
        row=1, col=2
    )
    # Title
    fig.update_layout(
        title=title
    )
    # Show
    fig.show()

def compare_both_by_month(dataframe_1, dataframe_2):
    label_1 = dataframe_1.iloc[0, 1] + ' to ' + dataframe_1.iloc[-1, 1]
    dataframe_1 = dataframe_1.sum()
    label_2 = dataframe_2.iloc[0, 1] + ' to ' + dataframe_2.iloc[-1, 1]
    dataframe_2 = dataframe_2.sum()

    title = f'Comparing total deaths of between "{label_1}" and "{label_2}"'

    labels = [label_1, label_2]
    values = [dataframe_1["deaths"], dataframe_2["deaths"]]

    print()
    print(title)
    print('********************************************************************')
    print(f'Total deaths from {label_1}\t: {dataframe_1["deaths"]}')
    print(f'Total deaths from {label_2} \t: {dataframe_2["deaths"]}')
    print(f'Difference \t\t\t\t\t: {dataframe_1["deaths"] - dataframe_2["deaths"]} ({round(dataframe_1["deaths"] / dataframe_2["deaths"], 1)} times)')
    # Subplots
    fig = make_subplots(
        rows=1, cols=2,
        specs=[[{"type": "xy"}, {"type": "pie"}]]
    )
    # Bar plot
    fig.add_trace(
        go.Bar(
            x=labels,
            y=values,
            name='Total deaths',
            showlegend=False
        ),
        row=1, col=1
    )
    # Pie chart
    fig.add_trace(
        go.Pie(
            labels=labels,
            values=values
        ),
        row=1, col=2
    )
    # Title
    fig.update_layout(
        title=title
    )
    # Show
    fig.show()

def timeserie_plot(dataframe, start=1784, end=1846):
    
    df = dataframe[dataframe['year'].between(start, end)]
    fig = make_subplots(
        rows=1, cols=1
    )
    
    fig.add_trace(
        go.Scatter(
            x=df['year'], 
            y=df['first_clinic_deaths_perc'],
            name='First clinic'
        ), row=1, col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df['year'], 
            y=df['second_clinic_deaths_perc'],
            name='Second clinic'
        )
    )
    
    # Add vertical line to annotate important time-lines
    # Pathological anatomy begins
    if start < 1823:
        fig.add_shape(
            type='line',
            x0=1823, x1=1823,
            y0=0, y1=16,
            line=dict(
                color='grey',
                width=2,
                dash='dot'
            )
        )
        # Annotation
        fig.add_annotation(
           x=1823,
           y=6,
           text="Pathological anatomy begins",
           showarrow=True,
           arrowcolor='cyan',
           bgcolor='cyan'
        )
    # Second clinic initiated
    if start < 1833:
        fig.add_shape(
            type='line',
            x0=1833, x1=1833,
            y0=0, y1=16,
            line=dict(
                color='grey',
                width=2,
                dash='dot'
            )
        )
        # Annotation
        fig.add_annotation(
           x=1833,
           y=8,
           text="Second clinic initiated",
           showarrow=True,
           arrowcolor='yellowgreen',
           bgcolor='yellowgreen'
        )
        
    #Only mdwives worked in the second clinic
    if start < 1841:
        fig.add_shape(
            type='line',
            x0=1841, x1=1841,
            y0=0, y1=16,
            line=dict(
                color='grey',
                width=2,
                dash='dot'
            )
        )
    	# Annotation
        fig.add_annotation(
           x=1841,
           y=12,
           font=dict(
           	color='#FFFFFF'
           ),
           text="Only midwives were trained in the second clinic",
           showarrow=True,
           arrowcolor='orchid',
           bgcolor='orchid'
        )
    # Figure titles
    fig.update_layout(
    	title=f"Comparing total death percentage of both clinics between {start} and {end}",
    	xaxis_title='Year',
    	yaxis_title='Percentage'
    )
    fig.show()

def monthly_timeserie_plot(dataframe_1, dataframe_2):
    fig = make_subplots(
        rows=1, cols=1
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe_1['time'],
            y=dataframe_1['deaths_perc'],
            name='Before mandatory handwasing policy'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe_2['time'],
            y=dataframe_2['deaths_perc'],
            name='After mandatory handwasing policy'
        )
    )

    fig.add_shape(
        type='line',
        x0='1847-05-01',x1='1847-05-01',
        y0=0, y1=0.35,
        line=dict(
            color='grey',
            width=2,
            dash='dot'
        )
    )

    fig.add_annotation(
       x='1847-05-01',
       y=0.19,
       text="Mandatory hand washing policy started",
       showarrow=True,
       arrowcolor='lightgreen',
       bgcolor='lightgreen'
    )

    fig.show()
