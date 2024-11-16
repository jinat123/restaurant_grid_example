from flask import Flask, render_template

app = Flask(__name__)
restaurants = [
    {
        "id": 1,
        "location": "Makati",
        "restaurant_name": "Restaurant One",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.zYdByZPPNdRSg7XIzQubKwHaHa?rs=1&pid=ImgDetMain"
    },
    {
        "id": 2,
        "location": "Pasig",
        "restaurant_name": "Restaurant Two",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.8vh8Ag4nhzKu8nRnOdFDogAAAA?rs=1&pid=ImgDetMain"
   },
   {
        "id": 3,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Three",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.SqO3TAzw1HIoiQ-XLF1aTAHaHa?rs=1&pid=ImgDetMain"
    },
    {
        "id": 4,
        "location": "Quezon CIty",
        "restaurant_name": "Restaurant Four",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.K4_Sjr0pgvuliNYEvvATTgHaHa?rs=1&pid=ImgDetMain"
    },
    { 
         "id": 5,
        "location": "Alabang",
        "restaurant_name": "Restaurant Five",
        "status": "Clohttps://www.kkday.com/en/blog/wp-content/uploads/philippines_metro_manila_alabang_ramen_yushoken.jpgsed",
        "image_url": ""
    },
    {
         "id": 6,
        "location": "Pasig",
        "restaurant_name": "Restaurant Six",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/14646764/pexels-photo-14646764.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
    },
    {
          "id": 8,
        "location": "Davao",
        "restaurant_name": "Restaurant Eight",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.9yHI0qxR0taYfOdAIufbYwHaGK?rs=1&pid=ImgDetMain"
    },
    {
          "id": 9,
        "location": "Bohol",
        "restaurant_name": "Restaurant Nine",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.xEJu7Dzv4CYy7yBue_PwbwHaJ4?rs=1&pid=ImgDetMain"
    },
    {
          "id": 11,
        "location": "Las Piñas",
        "restaurant_name": "Restaurant Eleven",
        "status": "Closed",
        "image_url": "https://ph.phonebooky.com/webp?u=https:%2F%2Fcdn.phonebooky.com%2Fblog%2Fwp-content%2Fuploads%2F2018%2F02%2F13115532%2Fburgoo2-600x600.jpg&width=600"
    },
    {
         "id": 12,
        "location": "Muntinlupa",
        "restaurant_name": "Restaurant Twelve",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.8hLzmlHejkcZ6jw2OFXZVQHaJu?rs=1&pid=ImgDetMain"
    },
    {
        "id": 13,
        "location": "Valenzuela",
        "restaurant_name": "Restaurant Thirteen",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.zv4DbTggSiCFsU0lGs1n5wHaFA?rs=1&pid=ImgDetMain"
    },
    {
          "id": 14,
        "location": "Caloocan",
        "restaurant_name": "Restaurant Fourteen",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.soFOGJDZwc_735FoQC5u0wHaFj?rs=1&pid=ImgDetMain"
    },
    {
         "id": 15,
        "location": "Marikina",
        "restaurant_name": "Restaurant Fifteen",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.939VmOdYsYZjZGoEKP1wLwHaEK?rs=1&pid=ImgDetMain"
    },
    {
         "id": 16,
        "location": "Antipolo",
        "restaurant_name": "Restaurant Sixteen",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.wauWwPzrhybcW8TJ2DAFKAHaFT?rs=1&pid=ImgDetMain"
    },
    {
        "id": 17,
        "location": "Baguio",
        "restaurant_name": "Restaurant Seventeen",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.2LpHlonz2A5SHhxM2o3UwwHaEK?rs=1&pid=ImgDetMain"
    },
    {
       "id": 18,
        "location": "Bacolod",
        "restaurant_name": "Restaurant Eighteen",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.XdImgXgTo_qiPjFVuP7jQwHaEZ?rs=1&pid=ImgDetMain"
    },
    {
         "id": 18,
        "location": "Zambaonga City",
        "restaurant_name": "Restaurant Eighteen",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.m2pBRbGvWVT92tmxWyRAoQHaE4?rs=1&pid=ImgDetMain"
    },
    {
        "id": 19,
        "location": "Iloilo City",
        "restaurant_name": "Restaurant Nineteen",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.8Nw2SEnpw6dYWJbIcSxthwHaEo?rs=1&pid=ImgDetMain"
    },
    {
         "id": 20,
        "location": "Cagayan de Oro",
        "restaurant_name": "Restaurant Twenty",
        "status": "Open",
        "image_url": "https://www.lessandra.com.ph/assets/BlogImages/cdo-food-trip/chellys-far-resto-restaurant-in-cagayan-de-oro.png"
    },
    {
         "id": 21,
        "location": "General Santos",
        "restaurant_name": "Restaurant Twenty-One",
        "status": "Closed",
        "image_url": "https://lh5.googleusercontent.com/p/AF1QipM8cphNuzOjBXpdCan2roZ1Q8p8UpM-V5lrX2N9=w408-h306-k-no"
    },
    {
         "id": 22,
        "location": "Butuan",
        "restaurant_name": "Restaurant Twenty-Two",
        "status": "Open",
        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/0f/4f/45/47/photo2jpg.jpg"
    },
    {
         "id": 23,
        "location": "Pagadian City",
        "restaurant_name": "Restaurant Twenty-Three",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.x3gD4FZg6Na46JtM2EKTOAAAAA?rs=1&pid=ImgDetMain"
    },
    {
         "id": 24,
        "location": "Dagupan",
        "restaurant_name": "Restaurant Twenty-Four",
        "status": "Open",
        "image_url": "https://lh5.googleusercontent.com/p/AF1QipP8kIiDODY5wxZQ03hY30MadJb7hi_Fj_A0D4gw=w408-h306-k-no"
    },
    {
        "id": 25,
        "location": "Naga",
        "restaurant_name": "Restaurant Twenty-Five",
        "status": "Closed",
        "image_url": ""
    },
    {
         "id": 26,
        "location": "Batangas City",
        "restaurant_name": "Restaurant Twenty-Six",
        "status": "Open",
        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/09/05/71/b2/he-brews-cafe.jpg"
    },
    {
         "id": 27,
        "location": "Tacloban",
        "restaurant_name": "Restaurant Twenty-Seven",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.7kJZBXriGBl9KOTpkyavgAHaHa?rs=1&pid=ImgDetMain"
    },
    {
         "id": 28,
        "location": "Legazpi",
        "restaurant_name": "Restaurant Twenty-Eight",
        "status": "Open",
        "image_url": "https://lh5.googleusercontent.com/p/AF1QipMp_Jvg2abn0SbMl3q6vrxMaUxjtd6MtCyJ2lmw=w408-h306-k-no"
    },
    {
          "id": 29,
        "location": "Olongapo",
        "restaurant_name": "Restaurant Twenty-Nine",
        "status": "Closed",
        "image_url": "https://lh5.googleusercontent.com/p/AF1QipMaYcWETRdNssGUi7jJqjPyD-QI-hX_aAUvboHf=w408-h306-k-no"
    },
    {
        "id": 30,
        "location": "Lucena",
        "restaurant_name": "Restaurant Thirty",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.BVIELNJUSGTfNLL94p9fJwHaHa?rs=1&pid=ImgDetMain"
    },
    {
        "id": 31,
        "location": "Puerto Princesa",
        "restaurant_name": "Restaurant Thirty-One",
        "status": "Closed",
        "image_url": "https://d1k571r5p7i4n1.cloudfront.net/c.6976/large/5seafoodrestaurantsinpuertoprincesa.jpg"
    },
    {
         "id": 32,
        "location": "Tagaytay",
        "restaurant_name": "Restaurant Thirty-Two",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.E911aNe4Ee_K2-ukCvs-VQHaFj?rs=1&pid=ImgDetMain"
    },
    {
         "id": 33,
        "location": "Angeles City",
        "restaurant_name": "Restaurant Thirty-Three",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.Nev5PgzeiW0-oQPm94lcGgAAAA?rs=1&pid=ImgDetMain"
    },
    { 
         "id": 34,
        "location": "Tarlac City",
        "restaurant_name": "Restaurant Thirty-Four",
        "status": "Open",
        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/0a/f4/6a/29/20160402-121841-largejpg.jpg"
    },
    {
         "id": 35,
        "location": "Calamba",
        "restaurant_name": "Restaurant Thirty-Five",
        "status": "Closed",
        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/21/d2/5e/09/from-entrance-counter.jpg"
    },
    {
          "id": 36,
        "location": "Lipa City",
        "restaurant_name": "Restaurant Thirty-Six",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.a5kyIoRqgWX5XfJhpncgJgHaFj?rs=1&pid=ImgDetMain"
    },
    {
         "id": 37,
        "location": "San Fernando",
        "restaurant_name": "Restaurant Thirty-Seven",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.LZTZEtX6WDtGpPnicCFpgQHaFj?rs=1&pid=ImgDetMain"
    },
    {
          "id": 38,
        "location": "Ormoc",
        "restaurant_name": "Restaurant Thirty-Eight",
        "status": "Open",
        "image_url": "https://www.windowseat.ph/wp-content/uploads/2017/07/Best-Places-You-Should-Try-in-Ormoc-City-Jos-Milagrina-2.jpg"
    },
    {
        "d": 39,
        "location": "Sorsogon",
        "restaurant_name": "Restaurant Thirty-Nine",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.SY79Ig6TwMcIlnAL0g6mtAHaE7?rs=1&pid=ImgDetMain"
    },
    {
        "id": 40,
        "location": "Roxas City",
        "restaurant_name": "Restaurant Forty",
        "status": "Open",
        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/01/9f/e8/f3/the-mainhall-of-espacio.jpg"
    },
    {
        "id": 41,
        "location": "Dumaguete",
        "restaurant_name": "Restaurant Forty-One",
        "status": "Closed",
        "image_url": "https://www.marriedafilipina.com/wp-content/uploads/2019/08/img-9782-orig_orig.jpg"
    },
    {
        "id": 42,
        "location": "Koronadal",
        "restaurant_name": "Restaurant Forty-Two",
        "status": "Open",
        "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/0c/13/6d/74/sheila-s-park-restaurant.jpg"
    },
    {
        "id": 43,
        "location": "Cotabato City",
        "restaurant_name": "Restaurant Forty-Three",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.w2aGn-Shh_1YqA7yMgdsvAHaEJ?rs=1&pid=ImgDetMain"
    },
    {
         "id": 44,
        "location": "Santiago",
        "restaurant_name": "Restaurant Forty-Four",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.nAZsaPMq-kG7vK_QN8HCkwHaE8?rs=1&pid=ImgDetMain"
    },
    {
       "id": 45,
        "location": "Vigan",
        "restaurant_name": "Restaurant Forty-Five",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.woZiMNSAMQkyUpHYDJDmeAHaE8?rs=1&pid=ImgDetMain"
    },
    {
        "id": 46,
        "location": "Laoag",
        "restaurant_name": "Restaurant Forty-Six",
        "status": "Open",
        "image_url": "https://i2.wp.com/media-cdn.tripadvisor.com/media/photo-s/0f/08/17/5b/dining.jpg"
    },
    {
        "id": 47,
        "location": "Malaybalay",
        "restaurant_name": "Restaurant Forty-Seven",
        "status": "Closed",
        "image_url": "https://bukidnononline.com/wp-content/uploads/2017/09/yaka-malaybalay-restaurant-730x548.jpg"
    },
    {
       "id": 48,
        "location": "Baybay",
        "restaurant_name": "Restaurant Forty-Eight",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.4PjIK-TePqZ8foYsymSVswHaDm?rs=1&pid=ImgDetMain"
    },
    {
         "id": 49,
        "location": "Dumalinao",
        "restaurant_name": "Restaurant Forty-Nine",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.VvHfq3cZbFWXk5C9Ml_--QHaFj?rs=1&pid=ImgDetMain"
    },
    {
         "id": 50,
        "location": "Dipolog",
        "restaurant_name": "Restaurant Fifty",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.8Zy4kZ-DWiiTXZxNd4Eq_gAAAA?rs=1&pid=ImgDetMain"
    },
    ]
            
@app.route('/')
def hello_world():
    print(restaurants);
    return render_template('index.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run(debug=True)

