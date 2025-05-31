import streamlit as st
from constants import currencies
from change_currency import  convert_currency , api_request

st.title(':dollar: Currency Converter')
st.markdown("""
This tool allows you to instantly convert amounts between defferent currencies:earth_asia:. 
            
Enter the amount and choose he currencies to see the result            
""")

base_currency = st.selectbox('From currency(Base):', currencies)
target_currency = st.selectbox('To currency(Target):', currencies)

amount= st.number_input('Enter amount:', min_value=0.0 , value= 100.0)
if amount>0 and base_currency and target_currency:
    exchange_rate = api_request(base_currency)['rates'][target_currency]
    
    if exchange_rate:
        converted_amount = convert_currency(amount , exchange_rate)
        st.success(f"✅ Exchange Rate:{exchange_rate: .2f}")
        col1 , col2 , col3 = st.columns(3)
        col1.metric(label= "Base Currency", value= f"{amount} {base_currency}")
        col2.markdown("<h1 style='text-align: center; margin: 0; color:green;'>&#8594;</h1>" , unsafe_allow_html=True)
        col3.metric(label = "Target Currency" , value=f"{converted_amount} {target_currency}")
    else:
        st.error('Error fetching exchange rate') 


st.markdown("___")
st.markdown("### ❕ About This Tool")
st.markdown("""
This currency converter uses real-time exchange rates provided by the ExchangeRate-API.
- The conversion update outomatically as you input the amount or change the currency.
- Enjoy seamless currency conversion without the need to press button!            
""")





