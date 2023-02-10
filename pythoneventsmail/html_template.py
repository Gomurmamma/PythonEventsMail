"""
html Email template
"""

template = (
    """"
<html>
<head><title> Featured Events for {{ month0 }}, {{ day0 }} </title></head>
<body>
<h1>Tonight's Featured Events</h1>
<figure>
<img src={{ image_url0 }} alt="{{ title0 }}"/>
<figcaption>
<h2> {{ title0 }} </h2>
<p> {{ venue0 }}, {{ city0 }}, {{ state0 }}</p>
<p>{{ month0 }} {{ day0 }}</p>
<a href={{ ticket_url0 }}>Buy Tickets!</a>
</figcaption>
</figure>
<figure>
<img src={{ image_url1 }} alt="{{ title1 }}"/>
<figcaption>
<h2> {{ title1 }} </h2>
<p> {{ venue1 }}, {{ city1 }}, {{ state1 }}</p>
<p>{{ month1 }} {{ day1 }}</p>
<a href={{ ticket_url1 }}>Buy Tickets!</a>
</figcaption>
</figure>
<figure>
<img src={{ image_url2 }} alt="{{ title2 }}"/>
<figcaption>
<h2> {{ title2 }} </h2>
<p> {{ venue2 }}, {{ city2 }}, {{ state2 }}</p>
<p>{{ month2 }} {{ day2 }}</p>
<a href={{ ticket_url2 }}>Buy Tickets!</a>
</figcaption>
</figure>
<figure>
<img src={{ image_url3 }} alt="{{ title3 }}"/>
<figcaption>
<h2> {{ title3 }} </h2>
<p> {{ venue3 }}, {{ city3 }}, {{ state3 }}</p>
<p>{{ month3 }} {{ day3 }}</p>
<a href={{ ticket_url3 }}>Buy Tickets!</a>
</figcaption>
</figure>
<figure>
<img src={{ image_url4 }} alt="{{ title4 }}"/>
<figcaption>
<h2> {{ title4 }} </h2>
<p> {{ venue4 }}, {{ city4 }}, {{ state4 }}</p>
<p>{{ month4 }} {{ day4 }}</p>
<a href={{ ticket_url4 }}>Buy Tickets!</a>
</figcaption>
</figure>
<figure>
<img src={{ image_url5 }} alt="{{ title5 }}"/>
<figcaption>
<h2> {{ title5 }} </h2>
<p> {{ venue5 }}, {{ city5 }}, {{ state5 }}</p>
<p>{{ month5 }} {{ day5 }}</p>
<a href={{ ticket_url5 }}>Buy Tickets!</a>
</figcaption>
</figure>
<figure>
<img src={{ image_url6 }} alt="{{ title6 }}"/>
<figcaption>
<h2> {{ title6 }} </h2>
<p> {{ venue6 }}, {{ city6 }}, {{ state6 }}</p>
<p>{{ month6 }} {{ day6 }}</p>
<a href={{ ticket_url6 }}>Buy Tickets!</a>
</figcaption>
</figure>
<figure>
<img src={{ image_url7 }} alt="{{ title7 }}"/>
<figcaption>
<h2> {{ title7 }} </h2>
<p> {{ venue7 }}, {{ city7 }}, {{ state7 }}</p>
<p>{{ month7 }} {{ day7 }}</p>
<a href={{ ticket_url7 }}>Buy Tickets!</a>
</figcaption>
</figure>
<figure>
<img src={{ image_url8 }} alt="{{ title8 }}"/>
<figcaption>
<h2> {{ title8 }} </h2>
<p> {{ venue8 }}, {{ city8 }}, {{ state8 }}</p>
<p>{{ month8 }} {{ day8 }}</p>
<a href={{ ticket_url8 }}>Buy Tickets!</a>
</figcaption>
</figure>
<figure>
<img src={{ image_url9 }} alt="{{ title9 }}"/>
<figcaption>
<h2> {{ title9 }} </h2>
<p> {{ venue9 }}, {{ city9 }}, {{ state9 }}</p>
<p>{{ month9 }} {{ day9 }}</p>
<a href={{ ticket_url9 }}>Buy Tickets!</a>
</figcaption>
</figure>
</body>
</html>
"""
    ""
)
