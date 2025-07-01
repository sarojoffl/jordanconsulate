from django.shortcuts import render
from django.http import JsonResponse

# Static Pages
def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def useful_link(request):
    return render(request, 'main/useful_link.html')

def articles(request):
    return render(request, 'main/articles.html')

def contact(request):
    return render(request, 'main/contact.html')

def converters_view(request):
    return render(request, 'main/converters.html')


# News Page
def news_view(request):
    news = [
        {
            "title": "नेपाल र जोर्डनबिच निजी क्षेत्रको सहकार्य, व्यापार र आर्थिक सम्बन्ध विस्तार हुँदै",
            "url": "https://nayapatrikadaily.com/news-details/169444/2025-06-04",
            "source": "nayapatrikadaily.com",
            "date": "2025-06-04"
        },
        {
            "title": "सभामुख र जोर्डनका राजदूतबीच शिष्टाचार भेट | Nepal Khabar",
            "url": "https://nepalkhabar.com/politics/239084-2025-6-4-17-5-11",
            "source": "nepalkhabar.com",
            "date": "2025-06-04"
        },
        {
            "title": "Office of honorary consul of Jordan opens in Kathmandu",
            "url": "https://kathmandupost.com/national/2025/06/05/office-of-honorary-consul-of-jordan-opens-in-kathmandu",
            "source": "kathmandupost.com",
            "date": "2025-06-05"
        },
        {
            "title": "Nepal–Jordan private sector collaboration poised for trade and economic expansion",
            "url": "https://theannapurnaexpress.com/story/54924/",
            "source": "theannapurnaexpress.com",
            "date": None
        },
        {
            "title": "Nepal and Jordan set to boost trade and investment",
            "url": "https://en.nepalkhabar.com/news/detail/14100/",
            "source": "en.nepalkhabar.com",
            "date": None
        },
        {
            "title": "Jordan Opens Honorary Consulate in Nepal, Appoints Kunal Kayal as Honorary Consul - The Diplomat Nepal",
            "url": "https://diplomatnepal.com/news/jordan-opens-honorary-consulate-in-nepal-appoints-kunal-kayal-as-honorary-consul/",
            "source": "diplomatnepal.com",
            "date": None
        },
        {
            "title": "Jordan Ambassador Abdelghani Pays Courtesy Call on Speaker Ghimire - The Diplomat Nepal",
            "url": "https://diplomatnepal.com/news/jordan-ambassador-abdelghani-pays-courtesy-call-on-speaker-ghimire/",
            "source": "diplomatnepal.com",
            "date": None
        },
        {
            "title": "नेपाल-जोर्डन कूटनीतिक सम्बन्ध स्थापनाको ६०औं वार्षिकोत्सव मनाईयो, कसले के भने ? - Businesspana",
            "url": "https://businesspana.com/more/update/19395/",
            "source": "businesspana.com",
            "date": None
        },
        {
            "title": "Nepal–Jordan private sector collaboration poised for trade and economic expansion - The DMN News | Breaking News, Live Updates, Analysis from Nepal",
            "url": "https://thedmnnews.com/nepal-jordan-private-sector-collaboration-poised-for-trade-and-economic-expansion/",
            "source": "thedmnnews.com",
            "date": None
        }
    ]
    return render(request, 'main/news.html', {'news': news})


# Photo Album Page
def photo_album_view(request):
    albums = [
        {
            "title": "Bhaktapur Durbar Square Visit",
            "photos": [
                f"photos/bhaktapur ({i}).jpg" for i in range(1, 8)
            ]
        },
        {
            "title": "Courtesy Calls Paid of High-Profile Govt. Officials",
            "photos": (
                ["photos/courtesy (1).jpg", "photos/courtesy (1).jpeg",
                 "photos/courtesy (2).jpg", "photos/courtesy (2).jpeg"] +
                [f"photos/courtesy ({i}).jpg" for i in range(3, 9)]
            )
        },
        {
            "title": "Celebratory Dinner on 3rd June, 2025",
            "photos": (
                ["photos/dinner (1).jpg", "photos/dinner (1).jpeg",
                 "photos/dinner (2).jpg", "photos/dinner (2).jpeg",
                 "photos/dinner (3).jpg", "photos/dinner (3).jpeg",
                 "photos/dinner (4).jpg", "photos/dinner (4).jpeg",
                 "photos/dinner (5).jpg", "photos/dinner (5).jpeg",
                 "photos/dinner (6).jpg", "photos/dinner (6).jpeg",
                 "photos/dinner (7).jpg", "photos/dinner (7).jpeg",
                 "photos/dinner (8).jpg", "photos/dinner (8).jpeg"] +
                [f"photos/dinner ({i}).jpg" for i in range(9, 29)]
            )
        },
        {
            "title": "Formal Inauguration & Flag Hoisting Event",
            "photos": [
                f"photos/inauguration ({i}).jpg" for i in range(1, 7)
            ]
        }
    ]
    return render(request, 'main/photo_album.html', {'albums': albums})
