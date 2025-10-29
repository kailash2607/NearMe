# Ex04 Places Around Me
## Date: 29 - 10 - 2025

## AIM
To develop a website to display details about the places around my house.

## DESIGN STEPS

### STEP 1
Create a Django admin interface.

### STEP 2
Download your city map from Google.

### STEP 3
Using ```<map>``` tag name the map.

### STEP 4
Create clickable regions in the image using ```<area>``` tag.

### STEP 5
Write HTML programs for all the regions identified.

### STEP 6
Execute the programs and publish them.

## CODE
### Home.html
```
<!DOCTYPE html>
<html>
<head>
    <title>Nearby Places Map</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f9f9f9;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #333;
            margin-bottom: 20px;
        }
        .map-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        img {
            max-width: 80%;
            height: auto;
            border: 3px solid #ccc;
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <h1>Theni</h1>
    <h1>Kailash Prabhu S(212224240068)</h1>
    <div class="map-container">
        <img src="/static/images/map.png" usemap="#nearme">
    </div>

    <map name="nearme">
        <area shape="rect" coords="34,44,270,350" alt="Place1" href="/place1/">
        <area shape="rect" coords="290,172,333,250" alt="Place2" href="/place2/">
        <area shape="rect" coords="337,300,550,450" alt="Place3" href="/place3/">
        <area shape="rect" coords="100,400,250,500" alt="Place4" href="/place4/">
        <area shape="rect" coords="400,100,600,250" alt="Place5" href="/place5/">
    </map>
</body>
</html>

```

### Place1.html
```
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Theni</title>
<style>
body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(to bottom right, #f7f9fc, #d6e4f0);
    display: flex; justify-content: center; align-items: center;
    height: 100vh; margin: 0;
}
.container {
    background: white; padding: 40px; border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    max-width: 600px; text-align: center;
}
h1 { color: #1d3557; margin-bottom: 15px; }
p { color: #333; font-size: 16px; line-height: 1.6; }
a {
    display: inline-block; margin-top: 20px; padding: 10px 20px;
    background-color: #1d3557; color: white; text-decoration: none;
    border-radius: 8px; transition: 0.3s;
}
a:hover { background-color: #457b9d; transform: scale(1.05); }
</style>
</head>
<body>
<div class="container">
    <h1>Theni</h1>
    <p>Theni is a scenic town located near the Western Ghats, famous for its hills, waterfalls, and agricultural richness. It is surrounded by nature, rivers, and plantations. Known as the “Gateway to the Hills,” Theni offers travelers a refreshing mix of culture, trade, and natural beauty.</p>
    <p><strong>Location:</strong> Theni District, Tamil Nadu</p>
    <a href="MapApp.html">⬅ Back to Map</a>
</div>
</body>
</html>

```

### Place2.html
```
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Cumbum</title>
<style>
body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(to bottom right, #fff3e0, #ffe0b2);
    display: flex; justify-content: center; align-items: center;
    height: 100vh; margin: 0;
}
.container {
    background: white; padding: 40px; border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    max-width: 600px; text-align: center;
}
h1 { color: #e65100; margin-bottom: 15px; }
p { color: #333; font-size: 16px; line-height: 1.6; }
a {
    display: inline-block; margin-top: 20px; padding: 10px 20px;
    background-color: #e65100; color: white; text-decoration: none;
    border-radius: 8px; transition: 0.3s;
}
a:hover { background-color: #ef6c00; transform: scale(1.05); }
</style>
</head>
<body>
<div class="container">
    <h1>Cumbum</h1>
    <p>Cumbum is a fertile valley town known for its vineyards and lush green paddy fields. It lies close to the Tamil Nadu–Kerala border, surrounded by majestic hills. The scenic beauty, cool breeze, and nearby Suruli Falls make it an ideal destination for tourists and nature enthusiasts alike.</p>
    <p><strong>Location:</strong> Theni District, Tamil Nadu</p>
    <a href="MapApp.html">⬅ Back to Map</a>
</div>
</body>
</html>

```

### Place3.html
```
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Bodinayakanur</title>
<style>
body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(to bottom right, #e3f2fd, #bbdefb);
    display: flex; justify-content: center; align-items: center;
    height: 100vh; margin: 0;
}
.container {
    background: white; padding: 40px; border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    max-width: 600px; text-align: center;
}
h1 { color: #0d47a1; margin-bottom: 15px; }
p { color: #333; font-size: 16px; line-height: 1.6; }
a {
    display: inline-block; margin-top: 20px; padding: 10px 20px;
    background-color: #0d47a1; color: white; text-decoration: none;
    border-radius: 8px; transition: 0.3s;
}
a:hover { background-color: #1565c0; transform: scale(1.05); }
</style>
</head>
<body>
<div class="container">
    <h1>Bodinayakanur</h1>
    <p>Also known as Bodi, this beautiful town sits at the foothills of the Western Ghats. Famous for its cardamom plantations and cool weather, Bodi is a paradise for nature lovers. The scenic hills, lush greenery, and misty mornings make it a perfect getaway for those seeking peace and freshness.</p>
    <p><strong>Location:</strong> Theni District, Tamil Nadu</p>
    <a href="MapApp.html">⬅ Back to Map</a>
</div>
</body>
</html>

```

### Place4.html
```
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Chinnamanur</title>
<style>
body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(to bottom right, #e8f5e9, #c8e6c9);
    display: flex; justify-content: center; align-items: center;
    height: 100vh; margin: 0;
}
.container {
    background: white; padding: 40px; border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    max-width: 600px; text-align: center;
}
h1 { color: #2e7d32; margin-bottom: 15px; }
p { color: #333; font-size: 16px; line-height: 1.6; }
a {
    display: inline-block; margin-top: 20px; padding: 10px 20px;
    background-color: #2e7d32; color: white; text-decoration: none;
    border-radius: 8px; transition: 0.3s;
}
a:hover { background-color: #43a047; transform: scale(1.05); }
</style>
</head>
<body>
<div class="container">
    <h1>Chinnamanur</h1>
    <p>Chinnamanur is a beautiful town located along the Mullai River, rich in culture and agriculture. It is known for its ancient temples, lively markets, and warm hospitality. The town’s peaceful atmosphere and green surroundings make it a wonderful spot for visitors exploring the Theni district.</p>
    <p><strong>Location:</strong> Theni District, Tamil Nadu</p>
    <a href="MapApp.html">⬅ Back to Map</a>
</div>
</body>
</html>

```

### Place4.html
```
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Kumily</title>
<style>
body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(to bottom right, #ede7f6, #d1c4e9);
    display: flex; justify-content: center; align-items: center;
    height: 100vh; margin: 0;
}
.container {
    background: white; padding: 40px; border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    max-width: 600px; text-align: center;
}
h1 { color: #4a148c; margin-bottom: 15px; }
p { color: #333; font-size: 16px; line-height: 1.6; }
a {
    display: inline-block; margin-top: 20px; padding: 10px 20px;
    background-color: #4a148c; color: white; text-decoration: none;
    border-radius: 8px; transition: 0.3s;
}
a:hover { background-color: #6a1b9a; transform: scale(1.05); }
</style>
</head>
<body>
<div class="container">
    <h1>Kumily</h1>
    <p>Kumily, located on the Tamil Nadu–Kerala border, is famous for its spice plantations and eco-tourism. It is the gateway to Thekkady and the Periyar Wildlife Sanctuary. The town’s misty hills, aromatic air, and relaxed atmosphere attract travelers seeking a calm and refreshing mountain experience.</p>
    <p><strong>Location:</strong> Idukki District, Kerala (near Theni border)</p>
    <a href="MapApp.html">⬅ Back to Map</a>
</div>
</body>
</html>


```
## OUTPUT
Refer to the following screenshots to view the output or else watch the demonstration in  ```/OutputIllustration```
<img width="1919" height="1079" alt="Screenshot 2025-10-29 111201" src="https://github.com/user-attachments/assets/86d41406-5822-4c86-af04-1117227106b2" />
<img width="1916" height="982" alt="Screenshot 2025-10-29 112304" src="https://github.com/user-attachments/assets/39c469cd-919e-43a8-bc7a-56a880df947d" />
<img width="1914" height="983" alt="Screenshot 2025-10-29 112315" src="https://github.com/user-attachments/assets/8d84bde2-0f5d-4a0d-ab83-6c2d4f27faab" />
<img width="1915" height="991" alt="Screenshot 2025-10-29 112323" src="https://github.com/user-attachments/assets/d609578a-315b-49d0-800e-5f12ddad30c9" />
<img width="1916" height="989" alt="Screenshot 2025-10-29 112333" src="https://github.com/user-attachments/assets/ee5f73d2-8b69-4514-af58-d327963e36d7" />
<img width="1919" height="984" alt="Screenshot 2025-10-29 112346" src="https://github.com/user-attachments/assets/68d3a567-a22d-4604-991c-0b9a7f0e31f5" />


## RESULT
The program for implementing image maps using HTML is executed successfully.
