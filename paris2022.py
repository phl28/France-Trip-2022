from flask import Flask

# python library to create leaflet maps
import folium

app = Flask(__name__)


@app.route("/")
def index():
    start_coords = (46.9540700, 142.7360300)

    # create map object
    m = folium.Map(location=[49.451611, 0.931948], zoom_start=6)

    tooltip = "Click For More Info"

    # create custom marker icon
    departing_london = folium.features.CustomIcon(
        "deparing_airplane.png", icon_size=(50, 50)
    )
    landing_paris = folium.features.CustomIcon(
        "arriving_airplane.png", icon_size=(50, 50)
    )
    departing_paris = folium.features.CustomIcon(
        "deparing_airplane.png", icon_size=(50, 50)
    )
    landing_london = folium.features.CustomIcon(
        "arriving_airplane.png", icon_size=(50, 50)
    )
    restaurant_paris_1 = folium.features.CustomIcon(
        "restaurant.png", icon_size=(50, 50)
    )
    restaurant_lyon_1 = folium.features.CustomIcon("restaurant.png", icon_size=(50, 50))
    train_airport_paris = folium.features.CustomIcon("train.png", icon_size=(50, 50))
    train_paris_airport = folium.features.CustomIcon("train.png", icon_size=(50, 50))
    train_paris_lyon = folium.features.CustomIcon("train.png", icon_size=(50, 50))
    train_lyon_montpellier = folium.features.CustomIcon("train.png", icon_size=(50, 50))
    train_montpellier_toulouse = folium.features.CustomIcon(
        "train.png", icon_size=(50, 50)
    )
    train_toulouse_bordeaux = folium.features.CustomIcon(
        "train.png", icon_size=(50, 50)
    )
    train_bordeaux_paris = folium.features.CustomIcon("train.png", icon_size=(50, 50))
    train_lyon_paris = folium.features.CustomIcon("train.png", icon_size=(50, 50))
    train_toulouse_montpellier = folium.features.CustomIcon(
        "train.png", icon_size=(50, 50)
    )
    train_montpellier_lyon = folium.features.CustomIcon("train.png", icon_size=(50, 50))
    train_bordeaux_toulouse = folium.features.CustomIcon(
        "train.png", icon_size=(50, 50)
    )
    train_paris_bordeaux = folium.features.CustomIcon("train.png", icon_size=(50, 50))
    hotel_paris = folium.features.CustomIcon("hotel.png", icon_size=(50, 50))
    hotel_lyon = folium.features.CustomIcon("hotel.png", icon_size=(50, 50))
    hotel_montpellier = folium.features.CustomIcon("hotel.png", icon_size=(50, 50))
    hotel_toulouse = folium.features.CustomIcon("hotel.png", icon_size=(50, 50))
    hotel_bordeaux = folium.features.CustomIcon("hotel.png", icon_size=(50, 50))

    # create markers
    folium.Marker(
        [51.155898, -0.163376],
        popup=folium.Popup(
            "<h4>Departure<br>London Gatwick, Terminal S</h4><br><strong>Date: 08.25.2022<br>Time: 11:45(BST)<br>Flight: BA 8105<br>Seats: </strong>",
            max_width=450,
        ),
        tooltip=tooltip,
        icon=departing_london,
    ).add_to(m),

    folium.Marker(
        [49.004153, 2.571507],
        popup=folium.Popup(
            "<h4>Departure<br>Paris Charles De Gaulle, Terminal 2A</h4><br><strong>Date: 08.31.2022<br>Time: 20:25(CEST)<br>Flight: BA 327<br>Seats: 10E,10F</strong>",
            max_width=450,
        ),
        tooltip=tooltip,
        icon=departing_paris,
    ).add_to(m),

    folium.Marker(
        [48.729984, 2.367198],
        popup=folium.Popup(
            "<h4>Arrival<br>Paris Orly, Terminal 2</h4><br><strong>Date: 08.25.2022<br>Time: 14:05(CEST)<br>Flight: BA 8105<br>Seats: </strong>",
            max_width=450,
        ),
        tooltip=tooltip,
        icon=landing_paris,
    ).add_to(m),

    folium.Marker(
        [51.471306, -0.488158],
        popup=folium.Popup(
            "<h4>Arrival<br>London Heathrow, Terminal 5</h4><br><strong>Date: 08.31.2022<br>Time: 20:40(BST)<br>Flight: BA 327<br>Seats: 10E,10F</strong>",
            max_width=450,
        ),
        tooltip=tooltip,
        icon=landing_london,
    ).add_to(m),

    folium.Marker(
        [48.845884, 2.375537],
        popup=folium.Popup(
            "<h4>Hotel Prince Albert Concordia</h4><br><strong>Date: 08.25-26.2022<br>Our Rating: </strong>",
            max_width=450,
        ),
        tooltip=tooltip,
        icon=hotel_paris,
    ).add_to(m),

    folium.Marker(
        [48.844760, 2.373477],
        popup=folium.Popup(
            "<h4>Paris to Lyon<br>Gare De Lyon</h4><br><strong>Date: 08.26.2022<br>Time: 8:59(CEST)<br>Train: Train Frecciarossa 6651<br>Coach 7<br>Seats: 9C, 9D</strong>",
            max_width=450,
        ),
        tooltip=tooltip,
        icon=train_paris_lyon,
    ).add_to(m),

    folium.Marker(
        [48.864166, 2.346704],
        popup=folium.Popup(
            "<h4>L'Escargot Montorgueil</h4><br><strong>Date: 08.25.2022<br>Time: 19:00(CEST)<br>Our Rating: </strong>",
            max_width=450,
        ),
        tooltip=tooltip,
        icon=restaurant_paris_1,
    ).add_to(m),

    folium.Marker(
        [45.760940, 4.861024],
        popup=folium.Popup(
            "<h4>Lyon from Paris<br>Lyon Part Dieu</h4><br><strong>Date: 08.26.2022<br>Time: 10:56(CEST)<br>Train: Train Frecciarossa 6651<br>Coach 7<br>Seats: 9C,9D</strong>",
            max_width=450,
        ),
        tooltip=tooltip,
        icon=train_lyon_paris,
    ).add_to(m),

    folium.Marker(
        [45.755646, 4.859289],
        popup=folium.Popup(
            "<h4>ResidHotel Lyon Part Dieu</h4><br><strong>Date: 08.26-27.2022<br>Our Rating: </strong>",
            max_width=450,
        ),
        tooltip=tooltip,
        icon=hotel_lyon,
    ).add_to(m),

    folium.Marker(
        [45.754093, 4.825890],
        popup=folium.Popup(
            "<h4>Cafe Comptoir Abel</h4><br><strong>Date: 08.26.2022<br>Time: 12:00(CEST)<br>Our Rating: </strong>",
            max_width=450,
        ),
        tooltip=tooltip,
        icon=restaurant_lyon_1,
    ).add_to(m),

    folium.Marker(
        [45.760453, 4.859821],
        popup=folium.Popup(
            "<h4>Lyon to Montpellier<br>Lyon Part Dieu</h4><br><strong>Date: 08.27.2022<br>Time: 14:08(CEST)<br>Train: TGV INOUI 5026 - 2.Class<br>Coach 16<br>Seats: 107,108</strong>",
            max_width=450,
        ),
        tooltip=tooltip,
        icon=train_lyon_montpellier,
    ).add_to(m),

    folium.Marker(
        [43.595287, 3.923502],
        popup=folium.Popup(
            "<h4>Montepellier from Lyon<br>Montpellier Sud de France</h4><br><strong>Date: 08.27.2022<br>Time: 15:53(CEST)<br>Train: TGV INOUI 5026 - 2.Class<br>Coach 16<br>Seats: 107,108</strong>",
            max_width=450,
        ),
        tooltip=tooltip,
        icon=train_montpellier_lyon,
    ).add_to(m),

    folium.Marker(
        [43.604118, 3.880290],
        popup=folium.Popup(
            "<h4>Montepellier to Toulouse<br>Montpellier Saint-Roch</h4><br><strong>Date: 08.29.2022<br>Time: 7:06(CEST)<br>Train: TGV INOUI 5026 - 2.Class<br>Coach 8<br>Seats: 21,22</strong>",
            max_width=450,
        ),
        tooltip=tooltip,
        icon=train_montpellier_toulouse,
    ).add_to(m),

    # circle marker
    # folium.CircleMarker(location=[51.471, -0.47], radius=50, popup='Random place', color='#428bca'
    # ,fill=True, fill_color='#428bca').add_to(m)

    # generate map
    # m.save('paris2022.html')
    return m._repr_html_()


if __name__ == "__main__":
    app.run(debug=True)
