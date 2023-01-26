import app.helpers
from datetime import datetime, timedelta 

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

def test_pretty_date_with_one_day_ago():
    timestamp = int((datetime.utcnow() - timedelta(days=1)).timestamp())
    text = app.helpers.pretty_date(timestamp)
    assert text == "Yesterday"

def test_pretty_date_with_several_days_ago():
    timestamp = int((datetime.utcnow() - timedelta(days=3)).timestamp())
    text = app.helpers.pretty_date(timestamp)
    assert text == "3 days ago"

def test_pretty_date_with_several_week_ago():
    timestamp = int((datetime.utcnow() - timedelta(weeks=2)).timestamp())
    text = app.helpers.pretty_date(timestamp)
    assert text == "2 weeks ago"

def test_pretty_date_with_several_months_ago():
    timestamp = int((datetime.utcnow() - timedelta(days=60)).timestamp())
    text = app.helpers.pretty_date(timestamp)
    assert text == "2 months ago"

def test_pretty_date_with_several_years_ago():
    timestamp = int((datetime.utcnow() - timedelta(days=365 * 2)).timestamp())
    text = app.helpers.pretty_date(timestamp)
    assert text == "2 years ago"

def test_pretty_date_with_future_day():
    timestamp = int((datetime.utcnow() + timedelta(days=1)).timestamp())
    text = app.helpers.pretty_date(timestamp)
    assert text == "just about now"
