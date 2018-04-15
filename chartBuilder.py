import pygal
from pygal.style import Style

#build chart using pygal, will convert to query from database in future

def build_language_chart(languages):

    # Reduce the array of languages to just the ones that the user has rated themselves
    languages = [(x[0], int(x[1])) for x in languages if x[0] is not 'N/A']

    # initializw the pie-chart object
    pie_chart = pygal.Pie(inner_radius = .4 )
    # Set table title
    pie_chart.title = 'Coder Break-down'
    # Find the total skill to take an average and weight the languages by that average
    totalskill = sum([x[1] for x in languages if type(x[1]) != None])

    # Case for skilled user
    if totalskill > 0:
        skillcents = [(x[0], x[1]/totalskill*100) for x in languages]

        for i in range(len(skillcents)):
            if skillcents[i][1] != 0.0: 
                # execute the following string as python code to set a pie chart value
                exec("pie_chart.add(skillcents[{}][0], skillcents[{}][1])".format(i, i))
        # create the piechart
        pie_chart = pie_chart.render_data_uri()
        return pie_chart
    # this case is only for skilless users, create empty pichart.
    else:
        custom_style = Style(colors = ('#A7ABB2', '#A7ABB2' ))
        pie_chart = pygal.Pie(inner_radius = .4, style =custom_style)
        pie_chart.title = 'Coder Break-down'
        pie_chart.add('None', 100)
        pie_chart = pie_chart.render_data_uri()
        return pie_chart

