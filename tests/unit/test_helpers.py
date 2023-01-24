import app.helpers

def test_less_than_day_with_less_than_minute():
    text = app.helpers.less_than_day(30)
    assert text == "30 seconds ago" 

def test_less_than_day_with_one_minute():
    text = app.helpers.less_than_day(90)
    assert text == "a minute ago" 

def test_less_than_day_with_several_minutes():
    text = app.helpers.less_than_day(3500)
    assert text == str(3500 // 60) + " minutes ago"
