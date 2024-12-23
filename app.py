import streamlit as st
from model.model import predict
from preprocessing.preprocess import preprocess

data = {}

st.title('Immo price prediction')

input = st.form('Input data')

TypeOfProperty = input.multiselect('Type of property', ['HOUSE', 'APARTMENT'], default='APARTMENT')
SubtypeOfProperty = input.multiselect('SubtypeOfProperty', ['APARTMENT', 'PENTHOUSE', 'GROUND_FLOOR', 'KOT', 'FLAT_STUDIO',
       'DUPLEX', 'LOFT', 'TRIPLEX', 'SERVICE_FLAT', 'APARTMENT_BLOCK',
       'HOUSE', 'MANSION', 'VILLA', 'MIXED_USE_BUILDING',
       'COUNTRY_COTTAGE', 'FARMHOUSE', 'BUNGALOW', 'TOWN_HOUSE',
       'OTHER_PROPERTY', 'EXCEPTIONAL_PROPERTY', 'MANOR_HOUSE', 'CHALET'], default='APARTMENT')
TypeOfSale = input.multiselect('Type of sale', ['residential_sale'], default='residential_sale')
StateOfTheBuilding = input.multiselect('State of the building', ['GOOD', 'AS_NEW', 'UNKNOWN', 'JUST_RENOVATED', 'TO_RENOVATE',
       'TO_BE_DONE_UP', 'TO_RESTORE'], default='GOOD') 
CompoundListing = input.multiselect('Compound Listing', ['single', 'compound'], default='single')

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
    data['Type of property'] = TypeOfProperty[0]
    data['Subtype of property'] = SubtypeOfProperty[0]
    data['Type of sale'] = TypeOfSale[0]
    data['State of the building'] = StateOfTheBuilding[0]
    data['Compound Listing'] = CompoundListing[0]

    data['Locality'] = Locality
    data['Garden area'] = GardenArea
    data['Surface of the land'] = SurfaceOfTheLand
    data['Surface area of the plot of land'] = SurfaceOfThePlot
    data['Number of rooms'] = NumberOfRooms
    data['Living Area'] = LivingArea
    data['Terrace area'] = TerraceArea
    data['Number of facades'] = NumberOfFacades
    row, data, preprocessed_data= preprocess(data)
    row
    data
    preprocessed_data
    pred = predict(preprocessed_data)
    pred
