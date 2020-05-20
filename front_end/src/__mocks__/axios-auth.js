const mockAxios = jest.genMockFromModule('axios');

const data = {
    user_list: [
        {
            "username": "WAnderson",
            "email": "WAnderson@mail.com",
            "photo": null,
            "first_name": "William",
            "last_name": "Anderson",
            "followers": [],
            "photo_url": "/static/icons/no-picture.jpg",
            "get_absolute_url": "/account/people/WAnderson/"
        },
        {
            "username": "CGlover",
            "email": "CGlover@mail.com",
            "photo": null,
            "first_name": "Cynthia",
            "last_name": "Glover",
            "followers": [1],
            "photo_url": "/static/icons/no-picture.jpg",
            "get_absolute_url": "/account/people/CGlover/"
        },
        {
            "username": "JPatterson",
            "email": "JPatterson@mail.com",
            "photo": null,
            "first_name": "Jamie",
            "last_name": "Patterson",
            "followers": [1],
            "photo_url": "/static/icons/no-picture.jpg",
            "get_absolute_url": "/account/people/JPatterson/"
        },
        {
            "username": "SHansen",
            "email": "SHansen@mail.com",
            "photo": null,
            "first_name": "Sheila",
            "last_name": "Hansen",
            "followers": [],
            "photo_url": "/static/icons/no-picture.jpg",
            "get_absolute_url": "/account/people/SHansen/"
        },
        {
            "username": "JArias",
            "email": "JArias@mail.com",
            "photo": null,
            "first_name": "Jonathan",
            "last_name": "Arias",
            "followers": [],
            "photo_url": "/static/icons/no-picture.jpg",
            "get_absolute_url": "/account/people/JArias/"
        },
        {
            "username": "DTaylor",
            "email": "DTaylor@mail.com",
            "photo": null,
            "first_name": "Daniel",
            "last_name": "Taylor",
            "followers": [],
            "photo_url": "/static/icons/no-picture.jpg",
            "get_absolute_url": "/account/people/DTaylor/"
        },
        {
            "username": "LAcosta",
            "email": "LAcosta@mail.com",
            "photo": null,
            "first_name": "Lisa",
            "last_name": "Acosta",
            "followers": [],
            "photo_url": "/static/icons/no-picture.jpg",
            "get_absolute_url": "/account/people/LAcosta/"
        },
        {
            "username": "WFernandez",
            "email": "WFernandez@mail.com",
            "photo": null,
            "first_name": "William",
            "last_name": "Fernandez",
            "followers": [],
            "photo_url": "/static/icons/no-picture.jpg",
            "get_absolute_url": "/account/people/WFernandez/"
        },
        {
            "username": "JJuarez",
            "email": "JJuarez@mail.com",
            "photo": null,
            "first_name": "John",
            "last_name": "Juarez",
            "followers": [],
            "photo_url": "/static/icons/no-picture.jpg",
            "get_absolute_url": "/account/people/JJuarez/"
        },
        {
            "username": "SMeyer",
            "email": "SMeyer@mail.com",
            "photo": null,
            "first_name": "Sarah",
            "last_name": "Meyer",
            "followers": [],
            "photo_url": "/static/icons/no-picture.jpg",
            "get_absolute_url": "/account/people/SMeyer/"
        }
    ]
};

mockAxios.get = jest.fn(() => {
    return new Promise(resolve => resolve({data: data['user_list']}))
})

export default mockAxios;