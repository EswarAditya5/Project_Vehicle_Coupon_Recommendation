import streamlit as st
import pandas as pd
import pickle

col1,col2,col3,col4,col5,col6,col7,col8=st.columns(8)

with col1:
    #destination
    destination_display=('No Urgent Place', 'Home', 'Work')
    destination_options=list(range(len(destination_display)))
    destination=st.selectbox('Destination',destination_options,format_func=lambda x:destination_display[x])
    
    #passanger
    passanger_display=('Alone', 'Friend(s)', 'Kid(s)', 'Partner')
    passanger_options=list(range(len(passanger_display)))
    passanger=st.selectbox('passanger',passanger_options,format_func=lambda x:passanger_display[x])
    
    #weather
    weather_display=('Sunny', 'Rainy', 'Snowy')
    weather_options=list(range(len(weather_display)))
    weather=st.selectbox('Weather',weather_options,format_func=lambda x:weather_display[x])

with col2:
    #temperature
    temperature_display=('55', '80', '30')
    temperature_options=list(range(len(temperature_display)))
    temperature=st.selectbox('temperature',temperature_options,format_func=lambda x:temperature_display[x])
    
    #time
    time_display=('2PM', '10AM', '6PM', '7AM', '10PM')
    time_options=list(range(len(time_display)))
    time=st.selectbox('time',time_options,format_func=lambda x:time_display[x])
    
    #coupon
    coupon_display=('Restaurant(<$20)', 'Coffee House', 'Carry out & Take away', 'Bar', 'Restaurant($20-$50)')
    coupon_options=list(range(len(coupon_display)))
    coupon=st.selectbox('coupon',coupon_options,format_func=lambda x:coupon_display[x])


with col3:
    #expiration
    expiration_display=('1d', '2h (the coupon expires in 1 day or in 2 hours)')
    expiration_options=list(range(len(expiration_display)))
    expiration=st.selectbox('expiration',expiration_options,format_func=lambda x:expiration_display[x])
    
    #gender
    gender_display=('Female', 'Male')
    gender_options=list(range(len(gender_display)))
    gender=st.selectbox('gender',gender_options,format_func=lambda x:gender_display[x])
    
    #age
    age_display=('21', '46', '26', '31', '41', '50plus', '36', 'below21')
    age_options=list(range(len(age_display)))
    age=st.selectbox('age',age_options,format_func=lambda x:age_display[x])


with col4:
    #maritalStatus
    maritalStatus_display=('Unmarried partner', 'Single', 'Married partner', 'Divorced', 'Widowed')
    maritalStatus_options=list(range(len(maritalStatus_display)))
    maritalStatus=st.selectbox('maritalStatus',maritalStatus_options,format_func=lambda x:maritalStatus_display[x])
    
    #has_Children
    has_Children_display=('1','0')
    has_Children_options=list(range(len(has_Children_display)))
    has_Children=st.selectbox('has_Children',has_Children_options,format_func=lambda x:has_Children_display[x])
    
    #education
    education_display=('Some college - no degree', 'Bachelors degree', 'Associates degree', 'High School Graduate', 
                       'Graduate degree (Masters or Doctorate)', 'Some High School')
    education_options=list(range(len(education_display)))
    education=st.selectbox('education',education_options,format_func=lambda x:education_display[x])


with col5:
    #occupation
    occupation_display=('Unemployed', 'Architecture & Engineering', 'Student', 'Education&Training&Library', 
                        'Healthcare Support', 'Healthcare Practitioners & Technical', 'Sales & Related, Management', 
                        'Arts Design Entertainment Sports & Media', 'Computer & Mathematical', 'Life Physical Social Science',
                        'Personal Care & Service', 'Community & Social Services', 'Office & Administrative Support', 
                        'Construction & Extraction', 'Legal', 'Retired', 'Installation Maintenance & Repair',
                        'Transportation & Material Moving', 'Business & Financial', 'Protective Service', 
                        'Food Preparation & Serving Related', 'Production Occupations', 'Building & Grounds Cleaning & Maintenance'
                        , 'Farming Fishing & Forestry')
    occupation_options=list(range(len(occupation_display)))
    occupation=st.selectbox('occupation',occupation_options,format_func=lambda x:occupation_display[x])
    
    #income
    income_display=('$37500 - $49999', '$62500 - $74999', '$12500 - $24999', '$75000 - $87499', '$50000 - $62499',
                    '$25000 - $37499', '$100000 or More', '$87500 - $99999', 'Less than $12500')
    income_options=list(range(len(income_display)))
    income=st.selectbox('income',income_options,format_func=lambda x:income_display[x])
    
    #Bar
    Bar_display=('never', 'less1', '1~3', 'gt8',  'nan4~8 ')
    Bar_options=list(range(len(Bar_display)))
    Bar=st.selectbox('Bar',Bar_options,format_func=lambda x:Bar_display[x])


with col6:
    #CoffeeHouse
    CoffeeHouse_display=('never', 'less1', '4~8', '1~3', 'gt8','nan')
    CoffeeHouse_options=list(range(len(CoffeeHouse_display)))
    CoffeeHouse=st.selectbox('CoffeeHouse',CoffeeHouse_options,format_func=lambda x:CoffeeHouse_display[x])
    
    #CarryAway
    CarryAway_display=('n4~8', '1~3', 'gt8', 'less1', 
                       'never')
    CarryAway_options=list(range(len(CarryAway_display)))
    CarryAway=st.selectbox('CarryAway',CarryAway_options,format_func=lambda x:CarryAway_display[x])
    
    #RestaurantLessThan20
    RestaurantLessThan20_display=( '4~8', '1~3', 'less1', 'gt8','never')
    RestaurantLessThan20_options=list(range(len(RestaurantLessThan20_display)))
    RestaurantLessThan20=st.selectbox('RestaurantLessThan20',RestaurantLessThan20_options,format_func=lambda x:RestaurantLessThan20_display[x])

with col7:
    #Restaurant20To50
    Restaurant20To50_display=('1~3', 'less1', 'never', 'gt8', '4~8',
                              'nan')
    Restaurant20To50_options=list(range(len(Restaurant20To50_display)))
    Restaurant20To50=st.selectbox('Restaurant20To50',Restaurant20To50_options,format_func=lambda x:Restaurant20To50_display[x])
    
    #toCoupon_GEQ15min
    toCoupon_GEQ15min_display=('0','1')
    toCoupon_GEQ15min_options=list(range(len(toCoupon_GEQ15min_display)))
    toCoupon_GEQ15min=st.selectbox('toCoupon_GEQ15min',toCoupon_GEQ15min_options,format_func=lambda x:toCoupon_GEQ15min_display[x])
    
    #toCoupon_GEQ25min
    toCoupon_GEQ25min_display=('0', '1 ')
    toCoupon_GEQ25min_options=list(range(len(toCoupon_GEQ25min_display)))
    toCoupon_GEQ25min=st.selectbox('toCoupon_GEQ25min',toCoupon_GEQ25min_options,format_func=lambda x:toCoupon_GEQ25min_display[x])


with col8:
   
    #direction_same
    direction_same_display=('0', '1')
    direction_same_options=list(range(len(direction_same_display)))
    direction_same=st.selectbox('direction_same',direction_same_options,format_func=lambda x:direction_same_display[x])
    
    #direction_opp
    direction_opp_display=('1', '0 ')
    direction_opp_options=list(range(len(direction_opp_display)))
    direction_opp=st.selectbox('direction_opp',direction_opp_options,format_func=lambda x:direction_opp_display[x])


model=pickle.load(open('gbmmodel.pkl','rb'))
my_dict={'destination':destination,'passanger':passanger,'weather':weather,'temperature':temperature,'time':time,
         'coupon':coupon,'expiration':expiration,'gender':gender,'age':age,'maritalStatus':maritalStatus,
         'has_Children':has_Children,'education':education,'occupation':occupation,'income':income,'Bar':Bar,
         'CoffeeHouse':CoffeeHouse,'CarryAway':CarryAway,'RestaurantLessThan20':RestaurantLessThan20,
         'Restaurant20To50':Restaurant20To50,'toCoupon_GEQ15min':toCoupon_GEQ15min,'toCoupon_GEQ25min':toCoupon_GEQ25min,
        'direction_same':direction_same,'direction_opp':direction_opp}

df= pd.DataFrame.from_dict([my_dict])
df= pd.get_dummies(df).reindex(columns=df.columns, fill_value=0)


if st.button("Predict") :
    result = model.predict(df)
    probability=model.predict_proba(df)
    st.text(result[0])
    st.text(probability[0])
