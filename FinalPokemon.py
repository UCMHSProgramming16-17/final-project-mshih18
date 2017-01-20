# import requests and pandas module
import requests
import pandas as pd

# make endpoint for api
endpoint = "http://pokeapi.co/api/v2/pokemon/"

# make empty lists
namelist = []
heightlist = []
weightlist = []
type1list = []
type2list = []

# make a new url for each pokemon
for x in range(1, 722):
    pokemonnum = str(x)
    url = endpoint + pokemonnum + "/"
   
    # send request
    r = requests.get(url)

    # collects data on pokemon
    pokemon = r.json()
    name = pokemon['forms'][0]['name']
    height = pokemon['height']
    weight = pokemon['weight']
    
    # collect both types for dual-type pokeon, but only one for singe-type
    typeamount = len((pokemon['types']))
    if typeamount == 2:
        type1 = pokemon['types'][1]['type']['name']
        type2 = pokemon['types'][0]['type']['name']
    else:
        type1 = pokemon['types'][0]['type']['name']
        type2 = 'None'
        
    # add data to end of corresponding list
    namelist.append(name)
    heightlist.append(height)
    weightlist.append(weight)
    type1list.append(type1)
    type2list.append(type2)
    
    # update user on program, because it takes very long
    if x % 72 == 0:
        print(str((x/72)*10)+'%')


# make a dataframe from lists
df = pd.DataFrame({
    'name': namelist,
    'height' : heightlist,
    'weight' : weightlist,
    'type1' : type1list,
    'type2' : type2list
})

# print dataframe
print(df)

# import bar chart commands from bokeh
from bokeh.charts import Bar, Scatter, Chord, output_file, save

# make bar chart and save it to 'PokemonType.html'
BarChart = Bar(df, label = 'type1', values = 'name', agg = 'count', title = 'Frequency of Pokemon by Type', legend = False, bar_width = 0.5,
xlabel = 'Type', ylabel = 'Amount')
output_file('PokemonType.html')
save(BarChart)

# make scatter plot and save it to 'HeightWeight.html'
ScatterPlot = Scatter(df, x = "weight", y = "height", color = "type1", title = "Weight vs. Height (Sorted by Type)", legend = 'top_right',
xlabel = 'Weight', ylabel = 'Height')
output_file('HeightWeight.html')
save(ScatterPlot)

# make new data table without single-type pokemon
df2 = df[df['type2'] != 'None']

print(df2)

# make chord chart and save it to 'TypeRelation.html'
ChordChart = Chord(df2, source="type1", target="type2")
output_file('TypeRelation.html')
save(ChordChart)