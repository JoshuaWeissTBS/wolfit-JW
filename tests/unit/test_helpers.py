import app.helpers

def test_less_than_day_with_less_than_minute():
    text = app.helpers.less_than_day(30)
    assert text == "30 seconds ago" 
