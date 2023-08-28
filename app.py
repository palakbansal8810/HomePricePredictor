import streamlit as st
import pickle
import pandas as pd
import numpy as np

lr=pickle.load(open('project1_data.pickle','rb'))
X=pickle.load(open('X.pickle','rb'))

locations=['other', 'Yeshwanthpur', 'Yelahanka New Town', 'Yelahanka','Whitefield', 'Vittasandra', 'Vijayanagar', 'Varthur','Uttarahalli', 'Tumkur Road', 'Thubarahalli', 'Thigalarapalya','Thanisandra', 'Talaghattapura', 'Subramanyapura', 'Sonnenahalli','Somasundara Palya', 'Seegehalli', 'Sarjapur  Road', 'Sarjapur','Sahakara Nagar', 'Ramamurthy Nagar', 'Ramagondanahalli','Rajiv Nagar', 'Rajaji Nagar', 'Raja Rajeshwari Nagar','Rachenahalli', 'Pattandur Agrahara', 'Parappana Agrahara','Panathur', 'Padmanabhanagar', 'Old Madras Road','Old Airport Road', 'Neeladri Nagar', 'Nagavarapalya','Nagarbhavi', 'Mysore Road', 'Munnekollal', 'Marsur','Marathahalli', 'Malleshwaram', 'Mahadevpura', 'Magadi Road','Lingadheeranahalli', 'Lakshminarayana Pura', 'Kundalahalli','Kudlu Gate', 'Kudlu', 'Kothanur', 'Koramangala', 'Kodihalli','Kodichikkanahalli', 'Kereguddadahalli', 'Kengeri Satellite Town','Kengeri', 'Kenchenahalli', 'Kasavanhalli', 'Karuna Nagar','Kannamangala', 'Kanakpura Road', 'Kanakapura', 'Kammasandra','Kambipura', 'Kalyan nagar', 'Kalena Agrahara', 'Kaggalipura','Kaggadasapura', 'Kadugodi', 'KR Puram', 'Jigani', 'Jalahalli','Jakkur', 'JP Nagar', 'Indira Nagar', 'Iblur Village', 'Hulimavu','Hosur Road', 'Hoskote', 'Hosakerehalli', 'Hosa Road', 'Hormavu','Horamavu Agara', 'Hoodi', 'Hennur Road', 'Hennur', 'Hegde Nagar','Hebbal Kempapura', 'Hebbal', 'Harlur', 'Haralur Road','HSR Layout', 'Gunjur', 'Gubbalala', 'Green Glen Layout','Gottigere', 'Gollarapalya Hosahalli', 'Frazer Town','Electronics City Phase 1', 'Electronic City Phase II','Electronic City', 'EPIP Zone', 'Domlur', 'Doddathoguru','Dodda Nekkundi', 'Devanahalli', 'Dasarahalli', 'Dasanapura','Choodasandra', 'Chikka Tirupathi', 'Channasandra', 'Chandapura','CV Raman Nagar', 'Budigere', 'Brookefield', 'Bommenahalli','Bommasandra', 'Bommanahalli', 'Bisuvanahalli', 'Binny Pete','Billekahalli', 'Bhoganhalli', 'Bharathi Nagar', 'Bellandur','Begur Road', 'Begur', 'Battarahalli', 'Bannerghatta Road','Banashankari', 'Balagere', 'Badavala Nagar', 'BTM 2nd Stage','Attibele', 'Ardendale', 'Anandapura', 'Ambedkar Nagar','Ambalipura', 'Akshaya Nagar', 'Abbigere', 'AECS Layout','9th Phase JP Nagar', '8th Phase JP Nagar', '7th Phase JP Nagar','5th Phase JP Nagar', '1st Phase JP Nagar']

sqft='total_sqft'

bath=[1-9]
# location,total_sqft,bath,size_bhk,balcony
st.title('_:green[Home Price Predictor]_')
location=st.selectbox('_:blue[Select The Location:]_',sorted(locations))

size_bhk=st.number_input('_:blue[BHK:]_')

total_sqft=st.number_input(':blue[Sqft Area:]')

col3,col4=st.columns(2)

with col4:
    bath=st.number_input(':blue[Number of bathrooms]',)
with col3:
    balcony=st.number_input('_:blue[Number of Balcony]_',)


def predict_price(location,total_sqft,bath,size_bhk,balcony):    
    loc_index = np.where(X.columns==location)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = size_bhk
    x[3] = balcony
    if loc_index >= 0:
        x[loc_index] = 1

    return lr.predict([x])[0]

if st.button('Predict Prices'):
    ans=int(np.round(predict_price(location,total_sqft,bath,size_bhk,balcony)*100000))
    if ans < 0:
        st.header('_:red[Fill appropriate values!!]_')
    else:
        st.header(f'₹{ans-100000} - ₹{ans+100000}')