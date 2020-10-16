# flake8: noqa
test_movie_url = "https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6"
test_movie_url_second = "https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49"
test_people_url = "https://ghibliapi.herokuapp.com/people"

test_movie_resp = {
    "id": "0440483e-ca0e-4120-8c50-4c8cd9b965d6",
    "title": "Castle in the Sky",
    "description": "The orphan Sheeta inherited a mysterious crystal...",
    "release_date": "1986",
    "people": ["https://ghibliapi.herokuapp.com/people/"],
    "url": "https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6",
}

test_people_resp = [
    {
        "id": "ba924631-068e-4436-b6de-f3283fa848f0",
        "name": "Ashitaka",
        "films": [
            "https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6"
        ],
        "url": "https://ghibliapi.herokuapp.com/people/ba924631-068e-4436-b6de-f3283fa848f0",
    },
    {
        "id": "ebe40383-aad2-4208-90ab-698f00c581ab",
        "name": "San",
        "films": [
            "https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6"
        ],
        "url": "https://ghibliapi.herokuapp.com/people/ebe40383-aad2-4208-90ab-698f00c581ab",
    },
    {
        "id": "87b68b97-3774-495b-bf80-495a5f3e672d",
        "name": "Yasuko Kusakabe",
        "gender": "Female",
        "films": [
            "https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49"
        ],
        "url": "https://ghibliapi.herokuapp.com/people/87b68b97-3774-495b-bf80-495a5f3e672d",
    },
]


test_movies_resp = [
    {
        "id": "0440483e-ca0e-4120-8c50-4c8cd9b965d6",
        "title": "Castle in the Sky",
        "description": "The orphan Sheeta inherited a mysterious crystal...",
        "release_date": "1986",
        "people": [
            {
                "id": "ba924631-068e-4436-b6de-f3283fa848f0",
                "name": "Ashitaka",
                "films": [
                    "https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6"
                ],
                "url": "https://ghibliapi.herokuapp.com/people/ba924631-068e-4436-b6de-f3283fa848f0",
            },
            {
                "id": "ebe40383-aad2-4208-90ab-698f00c581ab",
                "name": "San",
                "films": [
                    "https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6"
                ],
                "url": "https://ghibliapi.herokuapp.com/people/ebe40383-aad2-4208-90ab-698f00c581ab",
            },
        ],
        "url": "https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6",
    },
    {
        "id": "58611129-2dbc-4a81-a72f-77ddfc1b1b49",
        "title": "Grave of the Fireflies",
        "description": "In the latter part of World War II,...",
        "release_date": "1988",
        "people": [
            {
                "id": "87b68b97-3774-495b-bf80-495a5f3e672d",
                "name": "Yasuko Kusakabe",
                "gender": "Female",
                "films": [
                    "https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49"
                ],
                "url": "https://ghibliapi.herokuapp.com/people/87b68b97-3774-495b-bf80-495a5f3e672d",
            }
        ],
        "url": "https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49",
    },
]
