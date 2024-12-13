import streamlit as st
from preprocessing.preprocess import preprocess

data = {}

st.title('Immo price prediction')

input = st.form('Input data')

TypeOfProperty = input.multiselect('Type of property', ['Appartment', 'House'], default='Appartment')
SubtypeOfProperty = input.multiselect('SubtypeOfProperty', ['Option1', 'Option2'], default='Option1')
TypeOfSale = input.multiselect('Type of sale', ['Option1', 'Option2'], default='Option1')
StateOfTheBuilding = input.multiselect('State of the building', ['Option1', 'Option2'], default='Option1')
CompoundListing = input.multiselect('Compound Listing', ['True', 'False'], default='True')

Locality = input.number_input('Locality', value=1000)
GardenArea = input.number_input('Garden Area', value=0.0)
SurfaceOfTheLand = input.number_input('Surface of the land', value=0.0)
SurfaceOfThePlot = input.number_input('Surface of the plot of land', value=0.0)
NumberOfRooms  = input.number_input('Number of rooms:', value=0)
LivingArea = input.number_input('Living Area', value=0.0)
TerraceArea = input.number_input('Terrace Area', value=0.0)
NumberOfFacades = input.number_input('Number of facades', value=0)


submit = input.form_submit_button('Submit data')

if submit:
    data['Type of property'] = TypeOfProperty
    data['Subtype of property'] = SubtypeOfProperty
    data['Type of sale'] = TypeOfSale
    data['State of the building'] = StateOfTheBuilding
    data['Compound Listing'] = CompoundListing

    data['Locality'] = Locality
    data['Garden area'] = GardenArea
    data['Surface of the land'] = SurfaceOfTheLand
    data['Surface area of the plot of land'] = SurfaceOfThePlot
    data['Number of rooms'] = NumberOfRooms
    data['Living Area'] = LivingArea
    data['Terrace area'] = TerraceArea
    data['Number of facades'] = NumberOfFacades
    preprocess(data)
