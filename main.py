import requests
from datetime import datetime
import smtplib


EMAIL = "hchapman1983@gmail.com"
PASSWORD = "ubqlirgkjmkiviwo"
MY_LAT = 33.942322  # Your latitude
MY_LONG = -84.316010  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

lat_pos = 31
long_pos = 86
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
currently_dark = {18, 19, 20, 21, 22, 23, 24, 1, 2, 3, 4, 5}
time_now = datetime.now()
time_hour = time_now.hour

if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LAT - 5 <= iss_longitude <= MY_LONG + 5 and
        time_hour in currently_dark):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="hchapman1983@yahoo.com",
            msg="Subject:ISS is over head\n\nLook up the ISS is above."
        )
else:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="hchapman1983@yahoo.com",
            msg="Subject:ISS Missing\n\nISS is not here Yet."
        )
