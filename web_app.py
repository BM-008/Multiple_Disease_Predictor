import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import pandas as pd

diabetes_model=pickle.load(open("trained_model.sav",'rb'))
heart_disease_model=pickle.load(open("heart_disease_trained_model.sav",'rb'))

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction','Heart Disease Prediction'],
                         icons=['activity','heart'],default_index=0)
    
if (selected=='Diabetes Prediction'):
    st.title('Diabetes Predictor')
    if 'default_pregnancies' not in st.session_state:
        st.session_state.default_pregnancies = 0
    if 'current_pregnancies' not in st.session_state:
        st.session_state.current_pregnancies = st.session_state.default_pregnancies
        
    if 'default_glucose' not in st.session_state:
       st.session_state.default_glucose = 100
    if 'current_glucose' not in st.session_state:
       st.session_state.current_glucose = st.session_state.default_glucose
       
    if 'default_bloodpressure' not in st.session_state:
        st.session_state.default_bloodpressure = 70
    if 'current_bloodpressure' not in st.session_state:
        st.session_state.current_bloodpressure = st.session_state.default_bloodpressure
        
    if 'default_skinthickness' not in st.session_state:
        st.session_state.default_skinthickness = 20
    if 'current_skinthickness' not in st.session_state:
        st.session_state.current_skinthickness = st.session_state.default_skinthickness
        
    if 'default_insulin' not in st.session_state:
        st.session_state.default_insulin = 100
    if 'current_insulin' not in st.session_state:
        st.session_state.current_insulin = st.session_state.default_insulin
        
    if 'default_bmi' not in st.session_state:
       st.session_state.default_bmi = 25.0
    if 'current_bmi' not in st.session_state:
       st.session_state.current_bmi = st.session_state.default_bmi
       
    if 'default_diabetespedigreefunction' not in st.session_state:
        st.session_state.default_diabetespedigreefunction = 0.5
    if 'current_diabetespedigreefunction' not in st.session_state:
        st.session_state.current_diabetespedigreefunction = st.session_state.default_diabetespedigreefunction
        
    if 'default_age' not in st.session_state:
        st.session_state.default_age = 30
    if 'current_age' not in st.session_state:
        st.session_state.current_age = st.session_state.default_age
        
    def reset_inputs_to_defaults():
        st.session_state.current_pregnancies = st.session_state.default_pregnancies
        st.session_state.current_glucose = st.session_state.default_glucose
        st.session_state.current_bloodpressure = st.session_state.default_bloodpressure
        st.session_state.current_skinthickness = st.session_state.default_skinthickness
        st.session_state.current_insulin = st.session_state.default_insulin
        st.session_state.current_bmi = st.session_state.default_bmi
        st.session_state.current_diabetespedigreefunction = st.session_state.default_diabetespedigreefunction
        st.session_state.current_age = st.session_state.default_age
        
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.number_input('Number of Pregnancies',min_value=0, max_value=20, value=st.session_state.current_pregnancies, key='pregnancies_input_widget', on_change=lambda: st.session_state.update(current_pregnancies=st.session_state.pregnancies_input_widget))
    with col2:
        Glucose=st.number_input('Glucose Level',min_value=0, max_value=300, value=st.session_state.current_glucose, key='glucose_input_widget', on_change=lambda: st.session_state.update(current_glucose=st.session_state.glucose_input_widget))
    with col3:
        BloodPressure=st.number_input('Blood Pressure Value',min_value=0, max_value=200, value=st.session_state.current_bloodpressure, key='bloodpressure_input_widget', on_change=lambda: st.session_state.update(current_bloodpressure=st.session_state.bloodpressure_input_widget))
    with col1:
        SkinThickness=st.number_input('Skin Thickness Value',min_value=0, max_value=100, value=st.session_state.current_skinthickness, key='skinthickness_input_widget', on_change=lambda: st.session_state.update(current_skinthickness=st.session_state.skinthickness_input_widget))
    with col2:
        Insulin=st.number_input('Insulin Level',min_value=0, max_value=900, value=st.session_state.current_insulin, key='insulin_input_widget', on_change=lambda: st.session_state.update(current_insulin=st.session_state.insulin_input_widget))
    with col3:
        BMI=st.number_input('BMI Value',min_value=0.0, max_value=70.0, value=st.session_state.current_bmi, key='bmi_input_widget', on_change=lambda: st.session_state.update(current_bmi=st.session_state.bmi_input_widget))
    with col1:
        DiabetesPedigreeFunction=st.number_input('Diabetes Pedigree Function Value',min_value=0.0, max_value=2.0, value=st.session_state.current_diabetespedigreefunction, format='%.2f',key='diabetespedigreefunction_input_widget', on_change=lambda: st.session_state.update(current_diabetespedigreefunction=st.session_state.diabetespedigreefunction_input_widget))
    with col2:
        Age=st.number_input('Age of the Person',min_value=0, max_value=120, value=st.session_state.current_age, key='age_input_widget', on_change=lambda: st.session_state.update(current_age=st.session_state.age_input_widget))
        
    st.markdown('---')
    col_pred, col_reset = st.columns(2)
    with col_pred:
        diabetes_test_button = st.button('Get Diabetes Prediction Result')
    with col_reset:
        st.button('Reset Inputs', on_click=reset_inputs_to_defaults)

    diab_dignosis=''
    if diabetes_test_button:
        diabetes_prediction=diabetes_model.predict([[Pregnancies,Glucose, BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
        if (diabetes_prediction==1):
            diab_dignosis='The Person is Diabetic'
            st.warning(diab_dignosis)
        else:
            diab_dignosis='The Person is Non Diabetic'
            st.success(diab_dignosis)
            
    st.markdown('---')
    
    st.subheader('Your Entered Values for Prediction:')
    input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
    input_data_summary = {
            'Feature': ['Number of Pregnancies', 'Glucose Level', 'Blood Pressure',
                        'Skin Thickness', 'Insulin Level', 'BMI',
                        'Diabetes Pedigree Function', 'Age'],
            'Value': input_data,
            'Units': ['count', 'mg/dL', 'mmHg', 'mm', 'µU/mL', 'kg/m²', 'score', 'years']
        }
    input_df = pd.DataFrame(input_data_summary)
    st.dataframe(
    input_df.set_index('Feature').style.format(precision=2)
    )


    st.markdown("---")

        
    st.markdown("#### Analysis of Key Indicators:")

    ranges = {
            'Glucose Level': {'healthy_max': 99, 'pre_diabetic_max': 125, 'unit': 'mg/dL'},
            'Blood Pressure': {'healthy_max': 80, 'elevated_max': 89, 'unit': 'mmHg (diastolic)'},
            'BMI': {'healthy_max': 24.9, 'overweight_max': 29.9, 'unit': 'kg/m²'},
            'Insulin (Fasting)': {'healthy_max':25, 'elevated_max':30, 'unit':'µU/mL'},
            'Skin Thickness':{'healthy_max':18, 'elevated_max':22, 'unit':'mm'},
            'Diabetes Pedigree Function':{'healthy_max':0.5, 'elevated_max':2, 'unit':'score'}
        }

    def get_status_info(feature_name_for_display, value, ranges_dict):

        try:
                unit = input_data_summary['Units'][input_data_summary['Feature'].index(feature_name_for_display)]
        except ValueError:
                unit = ""
            
        if feature_name_for_display not in ranges_dict:
            return f"Value: {value} {unit}", "black"

        r = ranges_dict[feature_name_for_display]
        actual_unit = r.get('unit', unit)
        status_text = f" {value} {actual_unit}"
        color = "black"

        if feature_name_for_display == 'Glucose Level':
            if value < r['healthy_max']:
                status_text += " (Healthy)"
                color = "green"
            elif value <= r['pre_diabetic_max']:
                status_text += " (Pre-diabetic Range)"
                color = "orange"
            else:
                status_text += " (Diabetic Range)"
                color = "red"
        elif feature_name_for_display == 'Blood Pressure':
            if value <= r['healthy_max']:
                status_text += " (Healthy)"
                color = "green"
            elif value <= r['elevated_max']:
                status_text += " (Elevated)"
                color = "orange"
            else:
                status_text += " (High BP)"
                color = "red"
        elif feature_name_for_display == 'BMI':
            if value <= r['healthy_max']:
                status_text += " (Healthy Weight)"
                color = "green"
            elif value <= r['overweight_max']:
                status_text += " (Overweight)"
                color = "orange"
            else:
                status_text += " (Obese)"
                color = "red"
        elif feature_name_for_display == 'Insulin (Fasting)':
            if value < r['healthy_max']:
                status_text += " (Healthy)"
                color = "green"
            elif value <= r['elevated_max']:
                status_text += " (Elevated Range)"
                color = "orange"
            else:
                status_text += " (High Level)"
                color = "red"
        elif feature_name_for_display == 'Skin Thickness':
            if value < r['healthy_max']:
                status_text += " (Healthy)"
                color = "green"
            elif value <= r['elevated_max']:
                status_text += " (Elevated Range)"
                color = "orange"
            else:
                status_text += " (High Value)"
                color = "red"
        if feature_name_for_display == 'Diabetes Pedigree Function':
            if value < r['healthy_max']:
                status_text += " (Healthy)"
                color = "green"
            elif value <= r['elevated_max']:
                status_text += " (Elevated Range)"
                color = "orange"
            else:
                status_text += " (High Value)"
                color = "red"
        return status_text, color

    col_analysis_1, col_analysis_2 = st.columns(2)

    with col_analysis_1:
            status_text, color = get_status_info('Glucose Level', Glucose, ranges)
            st.markdown(f"*Glucose Level:* <span style='color:{color}'>{status_text}</span>", unsafe_allow_html=True)
            status_text, color = get_status_info('Blood Pressure', BloodPressure, ranges)
            st.markdown(f"*Blood Pressure:* <span style='color:{color}'>{status_text}</span>", unsafe_allow_html=True)
            status_text, color = get_status_info('Skin Thickness', SkinThickness, ranges)
            st.markdown(f"*Skin Thickness Value:* <span style='color:{color}'>{status_text}</span>", unsafe_allow_html=True)

    with col_analysis_2:
            status_text, color = get_status_info('BMI', BMI, ranges)
            st.markdown(f"*BMI:* <span style='color:{color}'>{status_text}</span>", unsafe_allow_html=True)
            status_text, color = get_status_info('Insulin (Fasting)', Insulin, ranges)
            st.markdown(f"*Insulin Level (Fasting):* <span style='color:{color}'>{status_text}</span>", unsafe_allow_html=True)
            status_text, color = get_status_info('Diabetes Pedigree Function', DiabetesPedigreeFunction, ranges)
            st.markdown(f"*Diabetes Pedigree Function Value:* <span style='color:{color}'>{status_text}</span>", unsafe_allow_html=True)
    st.markdown("---")
    st.info("This tool is a basic predictor and should not be used as a substitute for professional medical advice.")
    st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            padding: 10px;
            font-size: 16px;
            color: #333;
            background-color: #f1f1f1;
        }
    </style>
    <div class="header">
        Made with ❤️ by Baibhav Malviya
    </div>
""", unsafe_allow_html=True)

    
if (selected=='Heart Disease Prediction'):
    st.title('Heart Disease Predictor')

    defaults = {
        'age': 30,
        'sex': 0,
        'cp': 0,
        'trestbps': 120,
        'chol': 200,
        'fbs': 0,
        'restecg': 0,
        'thalach': 150,
        'exang': 0,
        'oldpeak': 1.0,
        'slope': 1,
        'ca': 0,
        'thal': 1
    }

    for key, val in defaults.items():
        if f'default_{key}' not in st.session_state:
            st.session_state[f'default_{key}'] = val
        if f'current_{key}' not in st.session_state:
            st.session_state[f'current_{key}'] = val

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age of the Person', min_value=0, max_value=120, value=st.session_state.current_age, key='age_input_widget', on_change=lambda: st.session_state.update(current_age=st.session_state.age_input_widget))

    gender_options = {"Male": 0, "Female": 1}
    selected_gender = st.selectbox(
        "Gender", options=list(gender_options.keys()),
        index=list(gender_options.values()).index(st.session_state.get("current_sex", 0)),
        key='sex_input_widget',
        on_change=lambda: st.session_state.update(current_sex=gender_options[st.session_state.sex_input_widget])
    )
    sex = gender_options[selected_gender]

    cp_options = {
        "Typical Angina (0)": 0,
        "Atypical Angina (1)": 1,
        "Non-anginal Pain (2)": 2,
        "Asymptomatic (3)": 3
    }
    selected_cp = st.selectbox(
        "Chest Pain Type", options=list(cp_options.keys()),
        index=list(cp_options.values()).index(st.session_state.get("current_cp", 0)),
        key='cp_input_widget',
        on_change=lambda: st.session_state.update(current_cp=cp_options[st.session_state.cp_input_widget])
    )
    cp = cp_options[selected_cp]

    with col1:
        trestbps = st.number_input('Resting Blood Pressure (mmHg)', min_value=80, max_value=200, value=st.session_state.current_trestbps, key='trestbps_input_widget', on_change=lambda: st.session_state.update(current_trestbps=st.session_state.trestbps_input_widget))
    with col2:
        chol = st.number_input('Cholesterol Level (mg/dL)', min_value=100, max_value=600, value=st.session_state.current_chol, key='chol_input_widget', on_change=lambda: st.session_state.update(current_chol=st.session_state.chol_input_widget))

    fbs_options = {"<= 120 mg/dL (0)": 0, "> 120 mg/dL (1)": 1}
    selected_fbs = st.selectbox(
        "Fasting Blood Sugar", options=list(fbs_options.keys()),
        index=list(fbs_options.values()).index(st.session_state.get("current_fbs", 0)),
        key='fbs_input_widget',
        on_change=lambda: st.session_state.update(current_fbs=fbs_options[st.session_state.fbs_input_widget])
    )
    fbs = fbs_options[selected_fbs]

    restecg_options = {
        "Normal (0)": 0,
        "ST-T wave abnormality (1)": 1,
        "Left ventricular hypertrophy (2)": 2
    }
    selected_restecg = st.selectbox(
        "Resting ECG Results", options=list(restecg_options.keys()),
        index=list(restecg_options.values()).index(st.session_state.get("current_restecg", 0)),
        key='restecg_input_widget',
        on_change=lambda: st.session_state.update(current_restecg=restecg_options[st.session_state.restecg_input_widget])
    )
    restecg = restecg_options[selected_restecg]

    with col2:
        thalach = st.number_input('Max Heart Rate Achieved (bpm)', min_value=60, max_value=220, value=st.session_state.current_thalach, key='thalach_input_widget', on_change=lambda: st.session_state.update(current_thalach=st.session_state.thalach_input_widget))

    exang_options = {"No (0)": 0, "Yes (1)": 1}
    selected_exang = st.selectbox(
        "Exercise Induced Angina", options=list(exang_options.keys()),
        index=list(exang_options.values()).index(st.session_state.get("current_exang", 0)),
        key='exang_input_widget',
        on_change=lambda: st.session_state.update(current_exang=exang_options[st.session_state.exang_input_widget])
    )
    exang = exang_options[selected_exang]

    with col3:
        oldpeak = st.number_input('Oldpeak (ST depression)', min_value=0.0, max_value=6.5, value=float(st.session_state.current_oldpeak), step=0.1, key='oldpeak_input_widget', on_change=lambda: st.session_state.update(current_oldpeak=st.session_state.oldpeak_input_widget))

    slope_options = {
        "Upsloping (0)": 0,
        "Flat (1)": 1,
        "Downsloping (2)": 2
    }
    selected_slope = st.selectbox(
        "Slope of ST Segment", options=list(slope_options.keys()),
        index=list(slope_options.values()).index(st.session_state.get("current_slope", 1)),
        key='slope_input_widget',
        on_change=lambda: st.session_state.update(current_slope=slope_options[st.session_state.slope_input_widget])
    )
    slope = slope_options[selected_slope]

    ca = st.selectbox(
        "Number of Major Vessels Colored by Fluoroscopy (0–3)", options=[0, 1, 2, 3, 4],
        index=st.session_state.get("current_ca", 0),
        key='ca_input_widget',
        on_change=lambda: st.session_state.update(current_ca=st.session_state.ca_input_widget)
    )

    thal_options = {
        "Normal (1)": 1,
        "Fixed Defect (2)": 2,
        "Reversible Defect (3)": 3
    }
    selected_thal = st.selectbox(
        "Thalassemia Type", options=list(thal_options.keys()),
        index=list(thal_options.values()).index(st.session_state.get("current_thal", 1)),
        key='thal_input_widget',
        on_change=lambda: st.session_state.update(current_thal=thal_options[st.session_state.thal_input_widget])
    )
    thal = thal_options[selected_thal]

    def reset_input_to_default():
        for key in defaults.keys():
            st.session_state[f'current_{key}'] = st.session_state[f'default_{key}']

    st.markdown('---')
    col_pred, col_reset = st.columns(2)
    with col_pred:
        heart_disease_test_button = st.button('Get Heart Disease Prediction Result')
    with col_reset:
        st.button('Reset Inputs', on_click=reset_input_to_default)

    heart_disease_diagnosis = ''
    if heart_disease_test_button:
        heart_disease_prediction = heart_disease_model.predict([[
            age, sex, cp, trestbps, chol, fbs, restecg,
            thalach, exang, oldpeak, slope, ca, thal
        ]])

        if heart_disease_prediction == 1:
            heart_disease_diagnosis = 'The Person has Heart Disease'
            st.warning(heart_disease_diagnosis)
        else:
            heart_disease_diagnosis = 'The Person does not have Heart Disease'
            st.success(heart_disease_diagnosis)

    st.markdown("---")
    st.info("This tool is a basic predictor and should not be used as a substitute for professional medical advice.")
    st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            padding: 10px;
            font-size: 16px;
            color: #333;
            background-color: #f1f1f1;
        }
    </style>
    <div class="header">
        Made with ❤️ by Baibhav Malviya
    </div>
""", unsafe_allow_html=True)
