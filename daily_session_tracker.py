import datetime
import holidays
import pytz
from googletrans import Translator


class SessionTracker(object):
    def __init__(self):
        self.returned_items = {}
        self.open_markets = []



    def TellMarkets(self):
        
        # Grabs the Current time in two different formats, adjust in future
        today = datetime.date.today()
        currentTime = datetime.datetime.now()

        # standard holidays for United States, Great Britian, Japan, and Australia 
        us_holidays = holidays.US()
        britian_holidays = holidays.England()
        japan_holidays = holidays.Japan()
        australia_holidays = holidays.Australia()
        # Exchange Holiday is not included in the Standard Holiday's of Japan
        exchange_holiday = "{}-12-31".format(currentTime.year)
        japan_holidays.append({exchange_holiday:"Exchange Holiday"})
        # Translator needed because Japanese holiday's are returned in Japanese
        translator = Translator()
        

        # The Holidays that close Markets In the Given Countries, Unsure if all of Japan's Holiday's Close the Currency Markets
        us_market_holidays = [
            "New Year's Day",
            "Martin Luther King, Jr. Day",
            "Presidents Day or Washington's Birthday",
            "Good Friday",
            "Memorial Day",
            "Independence Day",
            "Labor Day",
            "Thanksgiving Day",
            "Christmas Day",
        ]

        britian_market_holidays = [
            "New Year's Day",
            "Good Friday",
            "Easter Monday",
            "May Day",
            "Spring Bank Holiday",
            "Summer Bank Holiday",
            "Christmas Day",
            "Boxing Day",
            "Exchange Holiday",
        ]

        japan_market_holidays = [
            "New Year's Day",
            "Adult Day",
            "Foundation Day",
            "Vernal Equinox Day",
            "Showa Day",
            "Constitution Memorial Day",
            "Greenery Day",
            "Children's Day",
            "Sea Day",
            "Respect for the Aged Day",
            "Autumnal Equinox Day",
            "Health and Sports Day",
            "Culture Day",
            "Labor Thanksgiving Day",
            "The birth of the Emperor",
            "Exchange Holiday",
        ]

        australian_market_holidays = [
            "New Year's Day",
            "Australia Day",
            "Good Friday",
            "Easter Monday",
            "Anzac Day",
            "Queen's Birthday",
            "Christmas Day",
            "Boxing Day",
        ]


        us_has_holiday = False
        japan_has_holiday = False
        britian_has_holiday = False
        australia_has_holiday = False

        
        
        if us_holidays.get(today) is not None:
            for i in us_market_holidays:
                if us_holidays.get(today) == i:
                    self.returned_items['US-Holiday'] = us_holidays.get(today)
                    us_has_holiday = True

                    
            
        if britian_holidays.get(today) is not None:
            for i in britian_market_holidays:
                if britian_holidays.get(today) == i:
                    self.returned_items['British-Holiday'] = britian_holidays.get(today)
                    britian_has_holiday = True
            

        if japan_holidays.get(today) is not None:
            holiday_in_english = translator.translate(japan_holidays.get(today))
            for i in japan_market_holidays:
                if holiday_in_english.text == i:
                    self.returned_items['Japanese-Holiday'] = holiday_in_english
                    japan_has_holiday = True


        if australia_holidays.get(today) is not None:
            for i in australian_market_holidays:
                if australia_holidays == i:
                    self.returned_items['Australian-Holiday'] = australia_holidays.get(today)
                    australia_has_holiday = True
            

        # checks to see if we are in daylight saving time
        #  need to make dynamic for what is being returned
        if bool(datetime.datetime.now(pytz.timezone("America/Los_Angeles")).dst()):
            if currentTime.hour >= 15 or currentTime.hour == 0:
                if not australia_has_holiday:
                    self.open_markets.append('Australia')

            if currentTime.hour >= 16 or currentTime.hour <= 1:
                if not japan_has_holiday:
                    self.open_markets.append('Japan')

            if currentTime.hour >= 0 and currentTime.hour <= 9:
                if not britian_has_holiday:
                    self.open_markets.append('Britian')

            if currentTime.hour >= 5 and currentTime.hour <= 14:
                if not us_has_holiday:
                    self.open_markets.append('US')
            

        else:
            if currentTime.hour >= 13 and currentTime.hour <= 22:
                if not australia_has_holiday:
                    self.open_markets.append('Australia')
            if currentTime.hour >= 15 or currentTime.hour == 0:
                if not japan_has_holiday:
                    self.open_markets.append('Japan')
            if currentTime.hour >= 0 and currentTime.hour <= 9:
                if not britian_has_holiday:
                    self.open_markets.append('Britian')
            if currentTime.hour >= 5 and currentTime.hour <= 14:
                if not us_has_holiday:
                    self.open_markets.append('US')
    
        return (self)