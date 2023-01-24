import app.helpers
from datetime import datetime 

def test_less_than_day_with_less_than_minute():
    text = app.helpers.less_than_day(30)
    assert text == "30 seconds ago" 

def test_less_than_day_with_one_minute():
    text = app.helpers.less_than_day(90)
    assert text == "a minute ago" 

def test_less_than_day_with_several_minutes():
    text = app.helpers.less_than_day(3500)
    assert text == str(3500 // 60) + " minutes ago"

def test_less_than_day_with_one_hour():
    text = app.helpers.less_than_day(7000)
    assert text == "an hour ago"

def test_less_than_day_with_several_hours():
    text = app.helpers.less_than_day(86000)
    assert text == str(86000 // 3600) + " hours ago"

def test_pretty_date_with_int_time():
    text = app.helpers.pretty_date(int(datetime.utcnow().timestamp()))
    assert text == "just now"

def test_pretty_date_with_empty_time():
    text = app.helpers.pretty_date(None)
    assert text == "just now"
