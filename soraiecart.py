import streamlit as st
from datetime import datetime, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json



# アプリのタイトル
st.title("Soraie Monkey Cart")

# 宣伝文
st.header("Ride a gocart in real roads in Tokyo")

# 画像の表示
st.image("b4.jpg")
st.image("b6.jpg")

# YouTubeビデオの埋め込み
st.markdown("""
    <iframe width="560" height="315" 
    src="https://www.youtube.com/embed/tqQEjTG1Shw?autoplay=1&loop=1&playlist=tqQEjTG1Shw" 
    frameborder="0" allow="accelerometer; autoplay; 
    clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """, unsafe_allow_html=True)

# HIGHLIGHTSセクション
st.header("HIGHLIGHTS")
st.write("""
- Drive through some of Tokyo’s key attractions, such as Sensoji Temple, Tokyo Skytree, and Akihabara in custom go-karts with a guide.
- Cosplay as your favorite character and ride on real Tokyo roads with an in-built action camera to capture your thrilling moments.
- Click some Instagram-worthy pictures at Sensoji Temple, one of the oldest Buddhist temples in the capital, that takes you back to the Edo period.
- Drive past Tokyo Skytree, one of the most iconic landmarks in Tokyo and the tallest structure in Japan.
- Have your guide click pictures of you and your friends to always remember this experience.
""")
st.markdown("Price: ~~20000yen per person~~ Now 16500 per person with our discount")

st.subheader("Inclusions")
st.write("""
- English and Japanese-speaking expert guide
- Go-kart of your choice (Your vehicle)
- Photo
- Bluetooth speaker
""")

st.subheader("Exclusions")
st.write("""
- Optional insurance
- Personal expenses
- Micro SD card
""")

st.subheader("Where to meet us:")
st.write("Monkey kart Asakusa, Japan, 130-0003 Tokyo, Sumida City, Yokokawa, 4-chōme9-9, Monkey-kart Asakusa shop")

st.subheader("Cancellation Policy")
st.write("You can cancel these tickets up to 7 DAYS BEFORE before the experience begins and get a full refund. Please call 03-5309-2639 for cancellation.")


# Frequently Asked Questions
st.header("Frequently Asked Questions")

st.subheader("Q: Where does it start and what are the courses?")
st.write("A: Sensoji-temple -> Tokyo Skytree -> Akihabara -> Ryogoku Kokugikan Sumo Arena -> Sensoji-temple")
# 地図画像の表示
st.image("map1.jpg")


st.subheader("Q: How many people can ride in one cart?")
st.write("A: One person can fit in one kart but up to 10 people can apply for one time slot. If the time slot is full, our staff will contact you for more schedules.")

st.subheader("Q: How much is the ride?")
st.write("A: It is usually ¥20,000 per person, but when you apply from this page, it will be ¥16,500 (includes tax).")

st.subheader("Q: What time does the tour start?")
st.write("A: 10am, 12pm, 2pm, 4pm, or 6pm. Your tour takes about 1 hour.")

st.subheader("Q: What if I don't see my country in the country list?")
st.write("A: We are sorry but only those who are from the country in the list can receive an International Driver License that can be used in Japan.")

st.subheader("Q: Do I have to have an International Driver License?")
st.write("A: YES! Please note that you CANNOT DRIVE with a regular driver license from your country. You need to issue an INTERNATIONAL DRIVER LICENSE BEFORE YOU FLY TO JAPAN. We will NOT be able to refund the money if you don't have the INTERNATIONAL DRIVER LICENSE.")


# SELECT YOUR DATEセクション
st.header("SELECT YOUR DATE")

# 希望日
preferred_date = st.date_input("Preferred Date", min_value=datetime.today() + timedelta(days=1), value=datetime.today() + timedelta(days=1))

# 希望時間帯
preferred_timeslot = st.selectbox("Preferred Timeslot", ["10am", "12pm", "2pm", "4pm", "6pm"])

# 人数選択
how_many_people = st.selectbox("How many people", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Important Informationチェックボックス
st.markdown("### Important Information")
st.markdown("""
Before booking please kindly read the information below:
- We will need the hardcopy of your international driving permit (IDP) under geneva convention 1949.
- For cancellation and refund you have to at least inform us 7 days before your tour date.
- In case you reserve your spot 1-2 days before your tour, the cancellation policy will remain the same.
""")
important_info_checked = st.checkbox("I have read and agree to the Important Information", value=False)

# BOOK NOWセクション
st.header("BOOK NOW")

# ユーザー入力フォーム
col1, col2 = st.columns(2)
with col1:
    first_name_input = st.text_input("First Name", key="first_name")
with col2:
    last_name_input = st.text_input("Last Name", key="last_name")

address = st.text_input("Address as it appears in International Driver License", key="address")
license_number = st.text_input("International Driver License Number", key="license_number")  # この行を確認



# 国の選択
countries = [
    "Iceland", "Ireland", "Albania", "United Kingdom", "Italy", "Estonia", "Austria",
    "Netherlands", "Greece", "Kyrgyzstan", "Croatia", "San Marino", "Georgia", "Sweden", "Spain",
    "Slovakia", "Slovenia", "Serbia", "Czech Republic", "Denmark", "Norway", "Vatican City", "Hungary",
    "Finland", "France", "Bulgaria", "Belgium", "Poland", "Portugal", "Malta", "Monaco", "Montenegro",
    "Lithuania", "Liechtenstein", "Romania", "Luxembourg", "Russia", "Algeria", "Uganda", "Egypt", "Ghana",
    "Ivory Coast", "Congo", "Democratic Republic of the Congo", "Sierra Leone", "Zimbabwe", "Senegal",
    "Tunisia", "Togo", "Nigeria", "Namibia", "Niger", "Burkina Faso", "Benin", "Botswana", "Madagascar",
    "Malawi", "Mali", "Morocco", "Rwanda", "Lesotho", "Central African Republic", "South Africa",
    "United Arab Emirates", "Israel", "Cyprus", "Syria", "Turkey", "Jordan", "Lebanon", "India",
    "Cambodia", "Singapore", "Sri Lanka", "Thailand", "Bangladesh", "Philippines", "Brunei", "Malaysia",
    "Laos", "South Korea", "United States", "Argentina", "Ecuador", "Canada", "Cuba", "Guatemala",
    "Jamaica", "Chile", "Dominican Republic", "Trinidad and Tobago", "Haiti", "Paraguay", "Barbados",
    "Venezuela", "Peru", "Australia", "New Zealand", "Papua New Guinea", "Fiji", "Hong Kong", "Macao",
    "French Overseas Territories (including French Polynesia)", "Aruba", "Curaçao", "Sint Maarten",
    "Cayman Islands", "Isle of Man", "Guernsey", "Jersey", "Gibraltar", "United States Territories (including Guam, Puerto Rico)"
]

country = st.selectbox("Country", countries)
st.write("*If your country doesn't show up, I'm sorry but you cannot drive in Japan.")

# 連絡先情報
mobile_number = st.text_input("Mobile Number")
email_address = st.text_input("Email Address")

# Googleスプレッドシートの設定
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:\Users\ume27\my_app_monkeycart\soraiekart-f11049a5c177.json', scope)
gc = gspread.authorize(credentials)
worksheet = gc.open('soraiecart').sheet1

# Submitボタンとリダイレクトリンクの表示
submit = st.button('Submit', disabled=not (important_info_checked and first_name_input and last_name_input and address and license_number and mobile_number and email_address))

if submit:
    # スプレッドシートへの書き込み
    worksheet.append_row([str(datetime.now()), first_name_input, last_name_input, address, license_number, country, preferred_date.strftime('%Y-%m-%d'), preferred_timeslot, str(how_many_people), mobile_number, email_address])
    # ユーザーにクリック可能なリンクを表示
    st.markdown("Thank you for submitting! Please [click here to proceed](https://buy.stripe.com/aEU022aiw2wG7WUeV5).", unsafe_allow_html=True)