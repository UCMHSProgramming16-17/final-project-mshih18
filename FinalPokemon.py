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

# make a new url for each type
for x in range(1,152):
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
        type1 = type2 = pokemon['types'][0]['type']['name']
        
    # add data to end of corresponding list
    namelist.append(name)
    heightlist.append(height)
    weightlist.append(weight)
    type1list.append(type1)
    type2list.append(type2)


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
from bokeh.charts import Bar, Scatter, output_file, save

# make bar chart and save it to 'PokemonType.html'
BarChart = Bar(df, 'type1', values = 'name', agg = 'count', title = 'Frequency of Pokemon by Type', bar_width = 0.5,
xlabel = 'Type', ylabel = 'Amount')
output_file('PokemonType.html')
save(BarChart)

# make scatter plot and save it to 'HeightWeight.html'
ScatterPlot = Scatter(df, x = "weight", y = "height", color = "type1", title = "Weight vs. Height (Sorted by Type)",
xlabel = 'Weight', ylabel = 'Height')
output_file('HeightWeight.html')
save(ScatterPlot)