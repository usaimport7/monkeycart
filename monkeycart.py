import streamlit as st
from datetime import datetime, timedelta

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json

# 環境変数からクレデンシャルを読み込む
creds_json = os.getenv("google_credentials")
if creds_json is None:
    raise Exception("The google_credentials environment variable is not set.")

try:
    creds_dict = json.loads(creds_json)
except json.JSONDecodeError as e:
    raise Exception("Error decoding google_credentials JSON.") from e

creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

# 環境変数からサービスアカウントキーのパスを取得
creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("soraiekart-f11049a5c177.json", scope)
client = gspread.authorize(creds)

# スプレッドシートを開く（ここでは'Sheet1'を使用）
sheet = client.open("soraiemonkeycart").sheet1

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
- Go-kart of your choice (CAN-AM RYKER or Monkey-kart vehicle)
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
st.write("Monkey kart Asakusa, Japan, 130-0003 Tokyo, Sumida City, Yokokawa, 4-chōme9９ Monkey-kart Asakusa shop")

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

# 予約＆支払いボタン
#if st.button("Book & Pay by card"):
    # ここに支払い処理などのコードを追加することができます
    # 今回例では、単純にGoogleのホームページにリダイレクトします
  #  st.markdown("<a href='https://www.google.com' target='_blank'>Go to Google</a>", unsafe_allow_html=True)

# 予約＆支払いボタンがクリックされたときの処理
#if st.button("Book & Pay by card"):
    # 必須フィールドが適切に入力され、チェックボックスが選択されているかを確認
    #if not first_name or not last_name or not address or not license_number or not country or not mobile_number or not email_address or not important_info_checked:
        # 必須フィールドのいずれかが入力されていない、またはチェックボックスが選択されていない場合
   #     st.error("Please fill in all the required fields and agree to the Important Information before proceeding.")
   # else:
        # すべての条件が満たされている場合、支払い処理などの次のステップへ進む
        # ここに支払い処理などのコードを追加
        # 今回の例では、単純にGoogleのホームページにリダイレクトするリンクを表示
  #      st.markdown("<a href='https://www.google.com' target='_blank'>Go to Google</a>", unsafe_allow_html=True)

# 予約＆支払いボタンがクリックされたときの処理
if st.button("Book & Pay by card", key="book_and_pay"):
    # 不足しているフィールドを追跡するリスト
    missing_fields = []
    if not first_name_input: missing_fields.append("First Name")
    if not last_name_input: missing_fields.append("Last Name")
    if not address: missing_fields.append("Address")
    if not license_number: missing_fields.append("License Number")
    # 他の必須フィールドに対するチェックもここに追加
    if not important_info_checked: missing_fields.append("Important Information Agreement")

    if missing_fields:
        # 不足しているフィールドをユーザーに知らせる
        st.error(f"Please fill in all the required fields: {', '.join(missing_fields)}")
    else:
        # 全てのフィールドが適切に入力されている場合の処理
        # スプレッドシートにデータを追加し、成功メッセージを表示
        sheet.append_row([first_name_input, last_name_input, address, license_number, country, mobile_number, email_address, str(preferred_date), preferred_timeslot, str(how_many_people)])
        st.success("Your booking has been successfully submitted!")
        st.markdown("<a href='https://www.google.com' target='_blank'>Go to Google</a>", unsafe_allow_html=True)

print(f"Type of creds_json: {type(creds_json)}")
if creds_json:
    print(f"Length of creds_json: {len(creds_json)}")
    print("First 100 characters of creds_json:", creds_json[:100])
else:
    print("creds_json is None or empty.")

print(creds_dict)
